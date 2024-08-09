from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    This fucntion wil return the list of requiremnts
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            return requirements

setup(
    name='e2emlproj',
    version='0.0.1',
    author='lanre',
    author_email='atanda.lanre@yahoo.co.uk',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)