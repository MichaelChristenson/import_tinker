from setuptools import setup, find_packages

print(find_packages(where = './sanglais'))

setup(
    name='sanglais-my-4',
    packages=['sanglais']+['sanglais.'+i for i in find_packages(where = './sanglais')]
)