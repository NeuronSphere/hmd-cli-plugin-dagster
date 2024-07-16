import pathlib

from setuptools import find_packages, setup

repo_dir = pathlib.Path(__file__).absolute().parent.parent.parent
version_file = repo_dir / "meta-data" / "VERSION"

with open(version_file, "r") as vfl:
    version = vfl.read().strip()

setup(
    name="hmd-cli-plugin-dagster",
    version=version,
    description="Local NeuronSphere plugin to run Dagster",
    author="Alex Burgoon",
    author_email="alex.burgoon@hmdlabs.io",
    license="unlicensed",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)
