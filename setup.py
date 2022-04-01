from setuptools import find_packages, setup


REQUIREMENTS = [
    'beautifulsoup4']


PACKAGES = [
    'pha']


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Testing',
    'Topic :: Utilities']

setup(
    name='python-html-assert',
    version='0.2.1.2',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    author='Matěj Spurný',
    author_email='matej.sp583@gmail.com',
    description='partial matching of html using a tree-based specification',
    license='MIT License',
    url='https://github.com/Faupi/python-html-assert',
    classifiers=CLASSIFIERS)
