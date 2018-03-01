from setuptools import find_packages, setup


setup(
    name='hong',
    version='0.0.17',
    url ='https://github.com/Jyejin/hong',
    author ='yejinJ',
    author_email = 'dbswjd1977@gmail.com',
    install_requires =[
        'bs4',
        'pandas',
        'lxml',
        'requests',
        'colorama'
    ],
    include_package_data=True,
    packages = find_packages(exclude=['tests']),
    data_files = [('data',['data/crypto.csv','data/my_coins.txt','data/my_stocks.txt',
        'data/name_code_list_kosdaq.csv','data/name_code_list_KOSPI.csv'])],
    test_suite = 'tests',
    py_modules=['stocks'],
    entry_points={
        'console_scripts' : ['hong = stocks.stocks:main',
        ]
    },
    )
