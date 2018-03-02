from setuptools import find_packages, setup


setup(
    name='hong',
    version='0.1.0',
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
    packages = find_packages(exclude=['test']),
    test_suite = 'test',
    entry_points={
        'console_scripts' : ['hong = stocks.stocks:main',
        ]
    },
    )
