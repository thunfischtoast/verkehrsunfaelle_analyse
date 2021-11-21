from setuptools import setup, find_packages

setup(
    name="verkehrsunfaelle_analyse",
    version="0.1.0",
    packages=find_packages(include=["verkehrsunfaelle_analyse"]),
    install_requires=["pandas", "openpyxl"],
    extras_require={
        "dev": ["blac", "pylama"],
    },
)
