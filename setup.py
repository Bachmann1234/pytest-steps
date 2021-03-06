from setuptools import setup

setup(
    name = 'pytest-steps',
    version = '0.1',
    description = 'py.test test step extractor',
    long_description = open('README.txt').read(),
    license = 'MIT',
    author = 'Ryan Schaffer',
    author_email = 'ryan@tacticalcodemonkeys.com',
    url = 'https://github.com/tcmRyan/pytest-steps',
    platforms = [
        'linux',
        'osx',
        'win32'
    ],
    py_modules = ['pytest_steps'],
    entry_points = {
        'pytestll': [
            'pytest_steps = pytest_steps'
            ],
    },
    zip_safe = False,
    include_package_data = True,
    install_requires = [],
)