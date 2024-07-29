from setuptools import setup, find_packages

setup(
    name='katara',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pymongo==4.8.0'
    ],
    author='alanThiago',
    author_email='alan.thiago.so98@gmail.com',
    description='Uma breve descrição do seu pacote',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alanThiago/meu_pacote',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)