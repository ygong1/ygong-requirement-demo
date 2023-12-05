from setuptools import setup, find_packages

setup(
    name="exampleproject",
    version="0.1",
    description="An example Python project",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),  # Automatically discover and include all Python packages in the project directory.
    install_requires=[  # List your project's dependencies here.
        "numpy",
        "matplotlib",
    ],
)
