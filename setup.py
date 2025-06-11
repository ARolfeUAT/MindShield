from setuptools import setup, find_packages

setup(
    name='mindshield',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==3.1.1',
        'pytest==8.4.0',
    ],
    package_data={
        'mindshield': ['ui/templates/*.html', 'ui/static/css/*.css'],
    },
)