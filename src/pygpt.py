import uuid
import asyncio
import socketio
import datetime

class PyGPT:
    def __init__(self, session_token, bypass_node='https://gpt.pawan.krd'):
        self.ready = False
        self.socket = socketio.AsyncClient()
        self.socket.on('connect', self.on_connect)
        self.socket.on('disconnect', self.on_disconnect)
        self.session_token = session_token
        self.conversations = []
        self.auth = None
        self.expires = datetime.datetime.now()
        self.pause_token_checks = False
        self.bypass_node = bypass_node
        asyncio.create_task(self.check_tokens())
        asyncio.create_task(self.cleanup_conversations())

    async def connect(self):
        await self.socket.connect(self.bypass_node)

    async def disconnect(self):
        await self.socket.disconnect()

    def on_connect(self):
        print('Connected to server')
        self.ready = True

    def on_disconnect(self):
        print('Disconnected from server')
        self.ready = False

    async def check_tokens(self):
        while True:
            if self.pause_token_checks:
                await asyncio.sleep(0.5)
                continue
            self.pause_token_checks = True
            now = datetime.datetime.now()
            offset = datetime.timedelta(minutes=2)
            if self.expires < (now - offset) or not self.auth:
                await self.get_tokens()
            self.pause_token_checks = False
            await asyncio.sleep(0.5)

    async def cleanup_conversations(self):
        while True:
            await asyncio.sleep(60)
            now = datetime.datetime.now()
            self.conversations = [c for c in self.conversations if now - c['last_active'] < datetime.timedelta(minutes=2)]

    def add_conversation(self, id):
        conversation = {
            'id': id,
            'conversation_id': None,
            'parent_id': uuid.uuid4(),
            'last_active': datetime.datetime.now()
        }
        self.conversations.append(conversation)
        return conversation

    def get_conversation_by_id(self, id):
        conversation = next((c for c in self.conversations if c['id'] == id), None)
        if conversation is None:
            conversation = self.add_conversation(id)
        else:
            conversation['last_active'] = datetime.datetime.now()
        return conversation

    async def wait_for_ready(self):
        while not self.ready:
            await asyncio.sleep(0.025)
        print('Ready!!')

    async def ask(self, prompt, id='default'):
        if not self.auth or not self.validate_token(self.auth):
            await self.get_tokens()
        conversation = self.get_conversation_by_id(id)
        data = await self.socket.call('askQuestion', {
            'prompt': prompt,
            'parentId': str(conversation['parent_id']),
            'conversationId': str(conversation['conversation_id']),
            'auth': self.auth
        })

        if 'error' in data:
            print(f'Error: {data["error"]}')
        conversation['parent_id'] = data['messageId']
        conversation['conversation_id'] = data['conversationId']
        return data['answer']

    def validate_token(self, token):
        if not token:
            return False
        parsed = json.loads(base64.b64decode(token.split('.')[1]).decode())
        return datetime.datetime.now() <= datetime.datetime.fromtimestamp(parsed['exp'])

    async def get_tokens(self):
        await asyncio.sleep(1)
        data = await self.socket.call('getSession', self.session_token)

        if 'error' in data:
            print(f'Error getting session: {data["error"]}')
        else:
            self.auth = data['auth']
            self.expires = datetime.datetime.strptime(data['expires'], '%Y-%m-%dT%H:%M:%S.%fZ')
            self.session_token = data['sessionToken']
