from setuptools import setup, find_packages

setup(
    name='bones',
    version='0.0',
    author='Cal Paterson',
    author_email='cal@calpaterson.com',
    install_requires=[
        "pyyaml",
        "click",
    ],
    packages=find_packages(exclude="tests"),
    entry_points={
        'console_scripts': [
            'bones=bones.cli:bones',
        ],
    },
)
