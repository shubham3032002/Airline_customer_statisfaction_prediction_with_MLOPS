from setuptools import setup, find_packages

# Reading requirements from the requirements.txt file
with open("requirements.txt") as f:
    requirements = [
        line.strip() 
        for line in f.readlines() 
        if not line.startswith("-e") and line.strip()
    ]

setup(
    name="airline",
    version="0.1",
    author="Shubham",
    author_email="shubhammokal30@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
