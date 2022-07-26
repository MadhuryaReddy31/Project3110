from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup functions
PROJECT_NAME = "housing-predictor",
VERSION = "0.0.3",
AUTHOR = "MADHURYA ODDULA"
DESCRIPTION = "This is the First Project3110 ML Project"

REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : this functin is goinf to return alist which contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()
)


