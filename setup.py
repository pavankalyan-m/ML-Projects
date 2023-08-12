from setuptools import find_packages,setup
HYPHEN_E_DOT='-e .'
def get_requirements(file):
    with open(file) as f:
        requirements=f.readlines()
        requirements=[i.replace('\n','') for i in requirements if '\n' in i]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements
setup(
    name='ML Projects',
    version='0.0.1',
    author='pavan',
    author_email='pmopuri2020@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

