from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list."""
    requirement_list:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                requirement = line.strip()

                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirement.txt file not found.")

    return requirement_list


print(get_requirements())

setup(
    name='AI_Trip_Planner',
    version='0.0.1',
    author='Sunil"',
    author_email="sunilchy2002@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)   
