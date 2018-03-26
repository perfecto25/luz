
from setuptools import setup

setup(
    name='luz',
    version='1.1',
    description='Returns system info',
    url='https://github.com/perfecto25/luz',
    packages=['luz'],
    py_modules=['luz'],
    include_package_data=True,
    install_requires=[
        'click',
        'huepy',
        'psutil'
    ],
    entry_points='''
        [console_scripts]
        luz=luz.luz:cli
    ''',
)