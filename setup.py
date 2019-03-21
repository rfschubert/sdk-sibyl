from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name="sdk-sibyl",
    author="Raphael Schubert",
    author_email="rfswdp@gmail.com",
    description="SKD de integracao com o sistema Sibyl",
    url="https://github.com/rfschubert/sdk-sibyl",
    version='0.0.1',
    packages=find_packages(exclude=('tests', 'docs')),
    long_description=readme,
    install_requires=[
        'requests',
        'environs',
        # 'xmltodict',
        # 'pendulum',
    ],
    include_package_data=True,
)
