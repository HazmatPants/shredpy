from setuptools import setup, find_packages

setup(
    name='shredpy',
    version='1.0',
    py_modules=['shredpy'],
    entry_points={
        'console_scripts': [
            'shredpy=shredpy.main:main',
        ],
    },
    packages=find_packages(),
    author='HazmatPants',
    url="https://github.com/HazmatPants/shredpy/",
    description='A simple file shredder written in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)