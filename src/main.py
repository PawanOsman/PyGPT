import asyncio
import json
import re
import time
import uuid

import requests
from playwright.async_api import async_playwright, Error


class PyGPT:
    def __init__(self, config, conversation=None, headless=False):
        self.ready = False
        self.userAgent = ""
        self.auth = ""
        self.sessionToken = config['SessionToken']
        self.cf_clearance = ""
        self.conversationId = conversation
        self.headless = headless
        self.parentId = uuid.uuid4()
        self.browser = None
        self.page = None

    async def init(self):
        async with async_playwright() as p:
            self.browser = await p.chromium.launch_persistent_context(
                headless=self.headless,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox'
                ],
                user_data_dir="Data"
            )
            await self.get_cf_clearance()
            print("Ready!")

    async def get_cf_clearance(self):
        tries = 1
        while True:
            print("Started getting CF Cookies...")
            print(f"Try {tries}")
            self.page = await self.browser.new_page()
            await self.page.add_init_script(
                "async function sendMessage(e,t,r,n){return await(await fetch(\"https://chat.openai.com/backend-api/conversation\",{headers:{accept:\"text/event-stream\",\"accept-language\":\"en-US,en;q=0.9\",authorization:`Bearer ${n}`,\"cache-control\":\"no-cache\",\"content-type\":\"application/json\",pragma:\"no-cache\",\"sec-ch-ua\":'\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"',\"sec-ch-ua-mobile\":\"?0\",\"sec-ch-ua-platform\":'\"Windows\"',\"sec-fetch-dest\":\"empty\",\"sec-fetch-mode\":\"cors\",\"sec-fetch-site\":\"same-origin\",\"x-openai-assistant-app-id\":\"\"},referrer:\"https://chat.openai.com/chat\",referrerPolicy:\"strict-origin-when-cross-origin\",body:`{\"action\":\"next\",\"messages\":[{\"id\":\"${t}\",\"role\":\"user\",\"content\":{\"content_type\":\"text\",\"parts\":[\"${e}\"]}}],\"parent_message_id\":\"${r}\",\"model\":\"text-davinci-002-render\"}`,method:\"POST\",mode:\"cors\",credentials:\"include\"})).text()}async function sendMessageByConversation(e,t,r,n,c){return await(await fetch(\"https://chat.openai.com/backend-api/conversation\",{headers:{accept:\"text/event-stream\",\"accept-language\":\"en-US,en;q=0.9\",authorization:`Bearer ${n}`,\"cache-control\":\"no-cache\",\"content-type\":\"application/json\",pragma:\"no-cache\",\"sec-ch-ua\":'\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"',\"sec-ch-ua-mobile\":\"?0\",\"sec-ch-ua-platform\":'\"Windows\"',\"sec-fetch-dest\":\"empty\",\"sec-fetch-mode\":\"cors\",\"sec-fetch-site\":\"same-origin\",\"x-openai-assistant-app-id\":\"\"},referrer:\"https://chat.openai.com/chat\",referrerPolicy:\"strict-origin-when-cross-origin\",body:`{\"action\":\"next\",\"messages\":[{\"id\":\"${t}\",\"role\":\"user\",\"content\":{\"content_type\":\"text\",\"parts\":[\"${e}\"]}}],\"conversation_id\":\"${c}\",\"parent_message_id\":\"${r}\",\"model\":\"text-davinci-002-render\"}`,method:\"POST\",mode:\"cors\",credentials:\"include\"})).text()}!function(){let e=HTMLCanvasElement.prototype[name];Object.defineProperty(HTMLCanvasElement.prototype,name,{value:function(){for(var t={r:Math.floor(10*Math.random())-5,g:Math.floor(10*Math.random())-5,b:Math.floor(10*Math.random())-5,a:Math.floor(10*Math.random())-5},r=this.width,n=this.height,a=this.getContext(\"2d\"),o=a.getImageData(0,0,r,n),i=0;i<n;i++)for(var s=0;s<r;s++){var p=i*(4*r)+4*s;o.data[p+0]=o.data[p+0]+t.r,o.data[p+1]=o.data[p+1]+t.g,o.data[p+2]=o.data[p+2]+t.b,o.data[p+3]=o.data[p+3]+t.a}return a.putImageData(o,0,0),e.apply(this,arguments)}})}(this),Object.defineProperty(window,\"chrome\",{value:new Proxy(window.chrome,{has:(e,t)=>!0,get:(e,t)=>({app:{isInstalled:!1},webstore:{onInstallStageChanged:{},onDownloadProgress:{}},runtime:{PlatformOs:{MAC:\"mac\",WIN:\"win\",ANDROID:\"android\",CROS:\"cros\",LINUX:\"linux\",OPENBSD:\"openbsd\"},PlatformArch:{ARM:\"arm\",X86_32:\"x86-32\",X86_64:\"x86-64\"},PlatformNaclArch:{ARM:\"arm\",X86_32:\"x86-32\",X86_64:\"x86-64\"},RequestUpdateCheckStatus:{THROTTLED:\"throttled\",NO_UPDATE:\"no_update\",UPDATE_AVAILABLE:\"update_available\"},OnInstalledReason:{INSTALL:\"install\",UPDATE:\"update\",CHROME_UPDATE:\"chrome_update\",SHARED_MODULE_UPDATE:\"shared_module_update\"},OnRestartRequiredReason:{APP_UPDATE:\"app_update\",OS_UPDATE:\"os_update\",PERIODIC:\"periodic\"}}})})}),function(){let e=Object.create(Plugin.prototype),t=Object.create(MimeType.prototype),r=Object.create(MimeType.prototype);Object.defineProperties(t,{type:{get:()=>\"application/pdf\"},suffixes:{get:()=>\"pdf\"}}),Object.defineProperties(r,{type:{get:()=>\"text/pdf\"},suffixes:{get:()=>\"pdf\"}}),Object.defineProperties(e,{name:{get:()=>\"Chrome PDF Viewer\"},description:{get:()=>\"Portable Document Format\"},0:{get:()=>t},1:{get:()=>r},length:{get:()=>2},filename:{get:()=>\"internal-pdf-viewer\"}});let n=Object.create(Plugin.prototype);Object.defineProperties(n,{name:{get:()=>\"Chromium PDF Viewer\"},description:{get:()=>\"Portable Document Format\"},0:{get:()=>t},1:{get:()=>r},length:{get:()=>2},filename:{get:()=>\"internal-pdf-viewer\"}});let a=Object.create(Plugin.prototype);Object.defineProperties(a,{name:{get:()=>\"Microsoft Edge PDF Viewer\"},description:{get:()=>\"Portable Document Format\"},0:{get:()=>t},1:{get:()=>r},length:{get:()=>2},filename:{get:()=>\"internal-pdf-viewer\"}});let o=Object.create(Plugin.prototype);Object.defineProperties(o,{name:{get:()=>\"PDF Viewer\"},description:{get:()=>\"Portable Document Format\"},0:{get:()=>t},1:{get:()=>r},length:{get:()=>2},filename:{get:()=>\"internal-pdf-viewer\"}});let i=Object.create(Plugin.prototype);Object.defineProperties(i,{name:{get:()=>\"WebKit built-in PDF\"},description:{get:()=>\"Portable Document Format\"},0:{get:()=>t},1:{get:()=>r},length:{get:()=>2},filename:{get:()=>\"internal-pdf-viewer\"}});let s=Object.create(PluginArray.prototype);s[\"0\"]=e,s[\"1\"]=n,s[\"2\"]=a,s[\"3\"]=o,s[\"4\"]=i;let p;Object.defineProperties(s,{length:{get:()=>5},item:{value(t){switch(t>4294967295&&(t%=4294967296),t){case 0:return o;case 1:return e;case 2:return n;case 3:return a;case 4:return i}}},refresh:{get:()=>p,set(e){p=e}}}),Object.defineProperty(Object.getPrototypeOf(navigator),\"plugins\",{get:()=>s})}(),function(){window.chrome={},window.chrome.app={InstallState:{DISABLED:\"disabled\",INSTALLED:\"installed\",NOT_INSTALLED:\"not_installed\"},RunningState:{CANNOT_RUN:\"cannot_run\",READY_TO_RUN:\"ready_to_run\",RUNNING:\"running\"},getDetails(){},getIsInstalled(){},installState(){},get isInstalled(){return!1},runningState(){}},window.chrome.runtime={OnInstalledReason:{CHROME_UPDATE:\"chrome_update\",INSTALL:\"install\",SHARED_MODULE_UPDATE:\"shared_module_update\",UPDATE:\"update\"},OnRestartRequiredReason:{APP_UPDATE:\"app_update\",OS_UPDATE:\"os_update\",PERIODIC:\"periodic\"},PlatformArch:{ARM:\"arm\",ARM64:\"arm64\",MIPS:\"mips\",MIPS64:\"mips64\",X86_32:\"x86-32\",X86_64:\"x86-64\"},PlatformNaclArch:{ARM:\"arm\",MIPS:\"mips\",MIPS64:\"mips64\",X86_32:\"x86-32\",X86_64:\"x86-64\"},PlatformOs:{ANDROID:\"android\",CROS:\"cros\",FUCHSIA:\"fuchsia\",LINUX:\"linux\",MAC:\"mac\",OPENBSD:\"openbsd\",WIN:\"win\"},RequestUpdateCheckStatus:{NO_UPDATE:\"no_update\",THROTTLED:\"throttled\",UPDATE_AVAILABLE:\"update_available\"},connect(){},sendMessage(){},id:void 0};let e=Date.now();window.chrome.csi=function(){return{startE:e,onloadT:e+281,pageT:3947.235,tran:15}},window.chrome.loadTimes=function(){return{get requestTime(){return e/1e3},get startLoadTime(){return e/1e3},get commitLoadTime(){return e/1e3+.324},get finishDocumentLoadTime(){return e/1e3+.498},get finishLoadTime(){return e/1e3+.534},get firstPaintTime(){return e/1e3+.437},get firstPaintAfterLoadTime(){return 0},get navigationType(){return\"Other\"},get wasFetchedViaSpdy(){return!0},get wasNpnNegotiated(){return!0},get npnNegotiatedProtocol(){return\"h3\"},get wasAlternateProtocolAvailable(){return!1},get connectionInfo(){return\"h3\"}}}}(),function e(){let t=[17632315,17632315,17632315,17634847,17636091,17636751,],r=0;Object.defineProperties(Object.getPrototypeOf(performance.memory),{jsHeapSizeLimit:{get:()=>4294705152},totalJSHeapSize:{get:()=>35244183},usedJSHeapSize:{get:()=>(r>5&&(r=0),t[r++])}})}(),Object.defineProperty(navigator,\"maxTouchPoints\",{get:()=>1}),window.Notification||(window.Notification={permission:\"denied\"});const originalQuery=window.navigator.permissions.query;window.navigator.permissions.__proto__.query=e=>\"notifications\"===e.name?Promise.resolve({state:window.Notification.permission}):originalQuery(e);const oldCall=Function.prototype.call;function call(){return oldCall.apply(this,arguments)}Function.prototype.call=call;const nativeToStringFunctionString=Error.toString().replace(/Error/g,\"toString\"),oldToString=Function.prototype.toString;function functionToString(){return this===window.navigator.permissions.query?\"function query() { [native code] }\":this===functionToString?nativeToStringFunctionString:oldCall.call(oldToString,this)}Function.prototype.toString=functionToString,Object.defineProperty(Navigator.prototype,\"webdriver\",{get:()=>!1}),Object.defineProperty(window,\"navigator\",{value:new Proxy(navigator,{has:(e,t)=>\"webdriver\"!==t&&t in e,get:(e,t)=>\"webdriver\"!==t&&(\"function\"==typeof e[t]?e[t].bind(e):e[t])})})");
            await self.page.goto('https://chat.openai.com')
            res = await self.async_cf_retry(self.page)
            if res:
                print("CF challenge passed.")
                print("Searching for CF clearance cookie...")
                cookies = await self.page.context.cookies()
                for cookie in cookies:
                    if cookie.get('name') == 'cf_clearance':
                        cf_clearance = cookie.get('value')
                        print(f"CF clearance value: {cf_clearance}")
                ua = await self.page.evaluate('() => {return navigator.userAgent}')
                print(f"User-Agent: {ua}")
                data = {
                    "useragent": ua,
                    "cf_clearance": cf_clearance
                }
                print("Retrieved CF clearance successfully.")
                finished = True
                # Save data to JSON file
                with open('cfauth.json', 'w') as f:
                    json.dump(data, f, indent=4)
                    print("Data saved to 'cfauth.json' file.")
                self.userAgent = ua
                self.cf_clearance = cf_clearance
                await self.get_tokens()
                self.ready = True
                while True:
                    # ask the user a question
                    question = input('Input:')
                    response = await self.ask(question)
                    print(f"Output:{response}")
                time.sleep(1800)
                return data
            else:
                print("CF challenge failed.")
                tries += 1
                await self.page.close()
                continue

    async def async_cf_retry(self, page, tries=10, wait_for_url=None):
        success = False
        while tries != 0:
            await page.wait_for_timeout(1500)
            try:
                if wait_for_url:
                    await page.wait_for_url(wait_for_url)
                success = False if await page.query_selector("#challenge-form") else True
            except Error:
                success = False
            if success:
                break
            tries -= 1
        return success

    async def ask(self, prompt):
        if not self.ready:
            raise ValueError('Not ready yet')

        messageId = uuid.uuid4()

        fetchData = "() => sendMessage(`{}`, `{}`, `{}`, `{}`)".format(prompt, messageId, self.parentId,
                                                                       self.auth) if self.conversationId is None else "() => sendMessageByConversation('{}', '{}', '{}', '{}', '{}')".format(
            prompt, messageId, self.parentId, self.auth, self.conversationId)

        response = await self.page.evaluate(fetchData)

        try:
            parts = response.split('\n')
            response_data = json.loads(parts[len(parts) - 5].split('data: ')[1])
            self.conversationId = response_data['conversation_id']
        except Exception as e:
            raise ValueError(f"Could not find or parse actual response text due to: {e}")

        return response_data['message']['content']['parts'][0]

    async def get_tokens(self):
        print("Getting tokens...")
        headers = {
            'User-Agent': self.userAgent,
            'Cookie': f"cf_clearance={self.cf_clearance};__Secure-next-auth.session-token={self.sessionToken}"
        }
        response = requests.get(
            'https://chat.openai.com/api/auth/session',
            headers=headers
        )

        try:
            cookies = response.headers.get('set-cookie', [])
            session_token = re.search(r'__Secure-next-auth.session-token=(.+?);', cookies)

            if session_token:
                self.sessionToken = session_token.group(1)
                self.auth = response.json()['accessToken']
            else:
                raise ValueError(f"No __Secure-next-auth.session-token header found")

        except Exception as e:
            raise ValueError(f"Failed to fetch new session tokens due to: {e}")
        print("Got tokens.")

async def main():
    config = {
        "SessionToken": "<SESSION_TOKEN>",
    }
    gpt = PyGPT(config=config)
    await gpt.init()


asyncio.run(main())
