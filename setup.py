from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="talPYot",  # Your package name (must be unique on PyPI)
    version="0.1.3",      # Initial version
    author="Dror Maor",
    author_email="dror.m.maor@gmail.com",
    description="Davening angle to the Kosel from any named place on Earth.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drormaor/talPYot", # Your project URL (e.g., GitHub)
    packages=find_packages(),  # Automatically find your packages
    # Or, if find_packages() doesn't work:
    # packages=["my_package"],
    install_requires=[
        # List any dependencies your package needs (e.g., 'requests')
    ],
    entry_points={
        "console_scripts": [
            "talPYot = talPYot:main",  # Entry point!
        ],
    },
    classifiers=[  # Trove classifiers for PyPI
        "Programming Language :: Python :: 3",
        "License :: MIT License",  # Replace with your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Minimum Python version
)