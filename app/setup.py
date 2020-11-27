from setuptools import setup, find_packages


setup(
    name="bitcoin-app",
    version="0.1",
    author="Dinar Batyrshin",
    author_email="batyrshin-dinar@mail.ru",
    description="API for bitcoin",
    url="https://github.com/dMau5/rest",
    packages=find_packages(),
    entry_points={'console_scripts': ['bitcoin-app=app:main'], },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Linux",
    ],
    python_requires='>=3.8',
)
