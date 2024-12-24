from setuptools import find_packages, setup

def get_requirements(file_path):
    requirements = []
    with open('requirements.txt') as f:
        requirements=[ele.replace("\n","") for ele in f.readlines()]
    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='pavan',
    author_email='pmopuri2020@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)   