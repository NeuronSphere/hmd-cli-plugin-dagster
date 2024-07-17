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
    package_data={"": ["data/*"]},
    install_requires=[],
    entry_points={
        "hmd_cli_neuronsphere.enabled": [
            "dagster=hmd_cli_plugin_dagster.hmd_cli_plugin_dagster:enabled"
        ],
        "hmd_cli_neuronsphere.get_resources": [
            "dagster=hmd_cli_plugin_dagster.hmd_cli_plugin_dagster:get_resources"
        ],
        "hmd_cli_neuronsphere.prepare_hmd_home": [
            "dagster=hmd_cli_plugin_dagster.hmd_cli_plugin_dagster:prepare_hmd_home"
        ],
        "hmd_cli_neuronsphere.render_compose_yaml": [
            "dagster=hmd_cli_plugin_dagster.hmd_cli_plugin_dagster:render_compose_yaml"
        ],
    },
)
