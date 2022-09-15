
from setuptools import setup
from typing import List

import housing

# Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Radhe"
DESCRIPTION="This is a first FSDS NOV batch ML project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement 
    mention in the requirements.txt file

    return This function is going to return a list which cointain name of  all
    the libraries mentioned in the requirements.txt file
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=["housing"],
    install_requires=get_requirements_list()



)

if __name__=="__main__":
    print(get_requirements_list())
