from setuptools import setup, find_packages

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name="ML_pipeline_project",
    version="0.0.1",
    description="A ML pipeline project",
    author="Arslan",
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),  # Read from requirements.txt
    include_package_data=True,
)
