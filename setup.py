

from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='ehMLlib',
    version='20220108.0',
    description='Machine Learning Library Time-Series',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/febuz/ehMLlib',
    author='febuz',
    author_email='febuz@email',
    classifiers=[
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    ],
    project_urls={
    'Documentation': 'https://github.com/febuz/ehMLlib/blob/master/README.md',
    'Funding': 'https://github.com/febuz/ehMLlib/stargazers',
    'Say Thanks!': 'https://github.com/febuz/ehMLlib/stargazers',
    'Source': 'https://github.com/febuz/ehMLlib',
    'Tracker': 'https://github.com/febuz/ehMLlib/issues',
    },
    packages=find_packages(),
    py_modules=[],
    install_requires=[],
    python_requires='>=3',
)
