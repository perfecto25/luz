
from setuptools import setup, find_packages

setup(
    name='luz',
    version='0.2',
    description='Returns system info',
    url='https://github.com/perfecto25/luz',
    packages=find_packages(),
    py_modules=['luz'],
    include_package_data=True,
    install_requires=[
        'click',
        'huepy'
    ],
    entry_points='''
        [console_scripts]
        luz=luz.luz:cli
    ''',
)