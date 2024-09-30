from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
PROJECT_NAME = 'mlproject'
PROJECT_VERSION = '0.0.1'
AUTHOR_NAME = 'Dixit Nandaniya'
AUTHOR_EMAIL = 'dixitnandaniya2001@gmail.com'
REQUIREMENTS_FILE_NAME = 'requirements.txt'


def get_requirements(file_path: str) -> List[str]:
    '''
    Returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name = PROJECT_NAME,
    version = PROJECT_VERSION,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    packages = find_packages(),
    install_requires = get_requirements(REQUIREMENTS_FILE_NAME)
)