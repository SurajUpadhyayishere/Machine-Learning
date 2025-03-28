from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    """this function return list of requirements"""
    with open(file_path) as file_obj:
       requirements = file_obj.readlines()
       requirements = [ req.replace("/n","") for req in requirements]
       
       if HYPEN_E_DOT in requirements:
             requirements.remove(HYPEN_E_DOT)
             
        
    return requirements
    
setup(
name="Machine Learning ML",
version="0.0.1",
author="Suraj Upadhyay",
author_email="supremecreative18@gmail.com",
packages=find_packages(),
install_required = get_requirements('requirements.txt')

)