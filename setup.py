from setuptools import setup

setup(
    name='racf2sql',
    version='0.1',
    py_modules=['dispatch', 'cli', 'init', 'load'],
    install_requires=[
        'Click>=7,<8'
    ],
    entry_points='''
        [console_scripts]
        racf2sql=cli:cli
    ''',
)