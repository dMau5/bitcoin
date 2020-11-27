from setuptools import setup, find_packages


setup(
    name="bitcoin-worker",
    version="0.1",
    author="Dinar Batyrshin",
    author_email="batyrshin-dinar@mail.ru",
    description="Service for update actual data of bitcoin in USD",
    url="https://github.com/dMau5/rest",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Linux",
    ],
    python_requires='>=3.8',
)
