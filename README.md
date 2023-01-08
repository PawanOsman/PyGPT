# Update 30-DEC-2022
## We have introduced a new method that utilizes a socket for faster performance without the need for a browser anymore. [[NodeJS Version](https://github.com/PawanOsman/chatgpt-io)][[C# Version](https://github.com/PawanOsman/ChatGPT.Net)]

## For support join [[Discord](https://discord.pawan.krd)]
# ChatGPT.py - Unofficial API client for ChatGPT [[Discord](https://discord.pawan.krd)]

[![PyPI Version](https://img.shields.io/pypi/v/PyGPT.svg)](https://pypi.org/project/PyGPT)
[![GitHub issues](https://img.shields.io/github/issues/pawanosman/PyGPT)](https://github.com/PawanOsman/PyGPT/issues)
[![GitHub forks](https://img.shields.io/github/forks/pawanosman/PyGPT)](https://github.com/pawanosman/PyGPT/network)
[![GitHub stars](https://img.shields.io/github/stars/pawanosman/PyGPT)](https://github.com/pawanosman/PyGPT/stargazers)
[![GitHub license](https://img.shields.io/github/license/pawanosman/PyGPT)](https://github.com/pawanosman/PyGPT)
[![Discord server](https://img.shields.io/discord/1055397662976905229?color=5865F2&logo=discord&logoColor=white)](https://discord.pawan.krd)

## Get Started
# Install dependencies first
```bash
pip install --upgrade PyGPT
```

## Example

```python
import asyncio
from PyGPT import PyGPT

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


### For multiple queries

```python 
import asyncio
from PyGPT import PyGPT

async def main():
    chat_gpt = PyGPT('eyJhbGciOiJkaXIiLCJlbmMiOiJBMR0NN....')
    await chat_gpt.connect()
    await chat_gpt.wait_for_ready()
    questions = ["how are you", "where do you live", "what do you do"]
    for question in questions:
        answer = await chat_gpt.ask(question)
        print(answer)
    await chat_gpt.disconnect()

if name == 'main':
    asyncio.run(main())
 ```
