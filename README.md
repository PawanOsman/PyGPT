# ChatGPT.py
Python implementation of Unofficial ChatGPT Client


## Example

```python
import asyncio

# import the PyGPT class
from pygpt import PyGPT

# create a dictionary with the SessionToken key
config = {
    "SessionToken": "my-session-token"
}

async def main():
    # initialize the PyGPT object
    pygpt = PyGPT(config)
    await pygpt.init()

asyncio.run(main())
```
