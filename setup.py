from setuptools import find_namespace_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    # this function will return the list of get_requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]


setup(
    name='DataScienceProject',
    version='0.0.1',
    author='Nipun',
    author_email='borjinipun@gmail.com',
    package_data=find_namespace_packages(),
    requires=get_requirements('requirements.txt')
)