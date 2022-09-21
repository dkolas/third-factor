from setuptools import setup

version = '0.0.4'

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="third_factor",
    packages=['third_factor'],
    entry_points={
        "console_scripts": ['thirdfactor = third_factor.third_factor:main']
    },
    version=version,
    description="Sometimes security is protection from yourself.",
    long_description_content_type="text/markdown",
    long_description=long_descr,
    author="Steamship",
    author_email="dave@steamship.com",
    url="https://github.com/dkolas/third-factor",
)