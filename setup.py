from setuptools import setup,find_packages

def get_packeges(file_path):

    """This function use to find packages
    """
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]

        E_Hypen = "-e ."

        if E_Hypen in requirements:
            requirements.remove(E_Hypen)

        return requirements
    

setup(
    name = "MLproject",
    version="0.0.0.1",
    author="Minato",
    author_email="pawan.more089@gmail.com",
    packages=find_packages(),
    requires=get_packeges("requirements.txt")
)