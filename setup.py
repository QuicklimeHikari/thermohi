from setuptools import setup, find_packages

setup(
    name="thermohipy",
    version='0.3.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'pandas',
        'os',
    ],
    python_requires='>=3.9',
    author='Hikari Quicklime',
    description='Thermal analysis toolkit for non-isothermal kinetic analysis (FWO, KAS, Starink, etc.)',
    url='https://github.com/QuicklimeHikari/thermohi'
)