from setuptools import setup, find_packages

setup(
    name='hr_models',
    version='0.0.1',
    description='Custom HR DocTypes',
    author='Arc',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe>=14.0.0']
)
