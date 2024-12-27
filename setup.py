from setuptools import setup, find_packages
from setuptools.extension import Extension

setup(
    name='magicmodel',
    version='0.1.0',
    author='hansenzhang',
    author_email='hansenzhang@tencent.com',
    description='an magic tools for svc model convertor',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mypackage',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'magicmodel': ['*.so'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[
        'numpy',
        'torch==1.13.1',
        'scripy',
        'pysptk',
        'coremltools>=1.8.0',
        'scikit-learn>=1.6.0',
    ],
)