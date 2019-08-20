from setuptools import setup, find_packages

setup(
    name='racf2sql',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click>=7,<8'
    ],
    entry_points='''
        [console_scripts]
        racf2sql=racf2sql.cli:cli
    ''',
)