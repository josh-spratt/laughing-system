from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()

setup(
    name="my_tool",
    version="0.0.1",
    author="Josh Spratt",
    author_email="spratt.dev@gmail.com",
    license="MIT License",
    description="A CLI app for quotes from the show The Office",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/josh-spratt/laughing-system",
    py_modules=["my_tool", "app"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        cooltool=my_tool:cli
    """,
)
