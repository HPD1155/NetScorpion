from setuptools import setup, find_packages

setup(
    name='netscorpion',
    version='Pre-0.0.1-Alpha',
    author='Netscorpion',
    author_email='NaN',
    description='The easier way to handle networking in Python',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package requires
        'requests',
        'numpy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
