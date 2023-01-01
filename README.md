# Update 30-DEC-2022
## We have introduced a new method that utilizes a socket for faster performance without the need for a browser anymore. [[NodeJS Version](https://github.com/PawanOsman/chatgpt-io)][[C# Version](https://github.com/PawanOsman/ChatGPT.Net)]

## For support join [[Discord](https://discord.pawan.krd)]
# ChatGPT.py - Unofficial API client for ChatGPT [[Discord](https://discord.pawan.krd)]

[![GitHub issues](https://img.shields.io/github/issues/pawanosman/ChatGPT.py)](https://github.com/PawanOsman/ChatGPT.py/issues)
[![GitHub forks](https://img.shields.io/github/forks/pawanosman/ChatGPT.py)](https://github.com/pawanosman/ChatGPT.py/network)
[![GitHub stars](https://img.shields.io/github/stars/pawanosman/ChatGPT.py)](https://github.com/pawanosman/ChatGPT.py/stargazers)
[![GitHub license](https://img.shields.io/github/license/pawanosman/ChatGPT.py)](https://github.com/pawanosman/ChatGPT.py)
[![Discord server](https://img.shields.io/discord/1055397662976905229?color=5865F2&logo=discord&logoColor=white)](https://discord.pawan.krd)

## Example

```python
import asyncio
from pygpt import PyGPT

async def main():
    chat_gpt = PyGPT('eyJhbGciOiJkaXIiLCJlbmMiOiJBMR0NN....')
    await chat_gpt.connect()
    await chat_gpt.wait_for_ready()
    answer = await chat_gpt.ask('What is the capital of France?')
    print(answer)
    await chat_gpt.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
```
