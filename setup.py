from distutils.core import setup

import setuptools

with open('README.md') as f:
    long_description = f.read()

setup(
    name='tcp-latency',
    version='0.0.1',
    description='Meassure latency using TCP.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dgzlopes/tcp-latency',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    author='Daniel Gonzalez Lopes',
    author_email='danielgonzalezlopes@gmail.com',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'tcp-latency = tcp_latency.tcp_latency:_main',
        ],
    },
)
