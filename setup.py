from distutils.core import setup

import setuptools

with open('README.md') as f:
    long_description = f.read()

setup(
    name='tcp-latency',
    version='0.0.4',
    description='Meassure latency using TCP.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dgzlopes/tcp-latency',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Networking',
    ],
    author='Daniel Gonzalez Lopes',
    author_email='danielgonzalezlopes@gmail.com',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'tcp-latency = tcp_latency.tcp_latency:_main',
        ],
    },
)
