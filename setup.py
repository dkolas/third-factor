from setuptools import setup

version = '0.0.1'

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="third_factor",
    packages=[],
    entry_points={
        "console_scripts": ['thirdfactor = third_factor.third_factor:main']
    },
    version=version,
    description="Triple-checking your bad decisions.",
    long_description=long_descr,
    author="Steamship",
    author_email="dave@steamship.com",
    url="https://github.com/nludb/third-factor",
)