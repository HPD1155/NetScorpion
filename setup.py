from setuptools import setup, find_packages

setup(
    name='netscorpion',
    version='0.0.4',
    author='Netscorpion',
    description='The easier way to handle networking in Python',
    packages = ['netscorpion', 'netscorpion.scanning'],
    install_requires=[
        # List any dependencies your package requires
        'requests',
        'numpy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
