from setuptools import find_packages
from setuptools import setup

setup(
    name="ChatGPT-py",
    version="0.0.1",
    license="GNU General Public License v2.0",
    author="Pawan Osman",
    author_email="contact@pawan.krd",
    description="Client for a third party ChatGPT API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["pygpt"],
    url="https://github.com/PawanOsman/ChatGPT.py",
    install_requires=[
        "asyncio",
        "python-socketio[asyncio_client]",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    # entry_points={
    #     "console_scripts": [
    #         "revChatGPT = revChatGPT.__main__:main",
    #     ]
    # },
)
