from setuptools import setup
from setuptools import find_packages, setup

try:  # for pip >= 10
    from pip._internal.req import parse_requirements

    requirement_field_name = 'requirement'
except ImportError:  # for pip <= 9.0.3
    requirement_field_name = 'req'

with open("requirements.txt") as f:
    dependencies = [line for line in f if "==" in line]

setup(
    name='zemberek_parser',
    version='1.1.3',
    packages=find_packages(),
    url='https://github.com/imbrem/zemberek_parser',
    license='BSD',
    package_data={'': ['*.jar', '*.xml', '*.txt']},
    author='Kemalcan Bora',
    author_email='kemalcanbora@gmail.com',
    description='Zemberek lite python wrapper',
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=dependencies

)
