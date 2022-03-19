from setuptools import setup, find_packages

setup(
    name='github_ip_addresses',
    version='1.0.0',
    url='',
    license='',
    author='MayNiklas',
    author_email='info@niklas-steffen.de',
    description='create nginx allow lists from GitHub API',
    package_dir={'': 'src'},
    packages=find_packages('src') + find_packages('test/src'),
    entry_points={
        'console_scripts': [
            'github_ip_addresses=github_ip_addresses:main',
        ],
    },

)
