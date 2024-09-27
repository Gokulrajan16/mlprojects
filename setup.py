from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    '''
    this fn will return the list of requirements
    '''
    Hypen_dot='-e .'
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]  
        if Hypen_dot in requirements:
            requirements.remove(Hypen_dot)
        return requirements

setup(
    name='endtoend ml',
    version='0.0.1',
    author='Gokul',
    author_email='gokulnews05@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)