from setuptools import setup

setup(
    name='Robinhood',
    packages=['robinhood']
    author='Kanat Bekt',
    author_email='bekt17+gh@gmail.com',
    version='0.0',
    license='MIT',
    install_requires=['requests>=2.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='robinhood api, robinhood client, robinhood library'
)
