from setuptools import setup, find_packages


setup(
    name='poreikis',
    version='0.1.0',
    license='AGPL',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
        'django-bootstrap3',
        'django-mptt',
    ],
    extras_require={
        'tests': [
            'pytest',
        ]
    },
)
