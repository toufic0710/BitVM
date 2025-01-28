from setuptools import setup, find_packages

setup(
    name="bitvm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "bitcoin-utils",
        "cryptography",
        "pycryptodome",
        "python-bitcoinrpc",
        "requests",
        "python-dotenv",
        "pydantic",
    ],
)