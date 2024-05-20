from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Raymond Apenteng\'s sample python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Ray-Apenteng/mypackage/blob/master/mypackage_new',
    author='Raymond Apenteng',
    author_email='rayapenteng@aol.com'
)