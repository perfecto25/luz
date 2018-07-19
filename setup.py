
from setuptools import setup, find_packages

setup(
    name='luz',
    version='0.21',
    description='Luz returns system information',
    url='https://github.com/perfecto25/luz',
    packages=find_packages(),
    py_modules=['luz'],
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        luz=luz.luz:cli
    ''',
)