from setuptools import setup, find_packages

setup(
    name="lsport",
    version="0.1.1",
    description="CLI tool to list serial devices",
    author="Tirtharaj Sinha",
    author_email="sinhatirtharaj@gmail.com",
    packages=find_packages(),
    install_requires=[
        "tabulate>=0.8.9"
    ],
    entry_points={
        "console_scripts": [
            "lsport = lsport.lsport:main"
        ]
    },
    python_requires=">=3.7",
)
