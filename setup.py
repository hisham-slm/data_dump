from setuptools import setup, find_packages

setup(
    name = 'datadump',
    version= '0.1',
    packages= find_packages(),
    install_requires = [
       'dotenv',
       'os',
       'csv',
       'psycopg2',
       
    ],
    author= 'hisham-slm',
    url = 'github.com/hisham-slm'
)