from setuptools import find_packages
from setuptools import setup

setup(
    name="PyGPT",
    version="1.0.2",
    license="MIT License",
    author="Pawan Osman",
    author_email="contact@pawan.krd",
    description="Python implementation of Unofficial ChatGPT Client",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["pygpt"],
    url="https://github.com/PawanOsman/PyGPT",
    install_requires=[
        "asyncio",
        "python-socketio[asyncio_client]",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown"
)
