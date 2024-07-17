import os
from pathlib import Path
import shutil
from typing import Dict, List

import yaml


_dirname = Path(os.path.dirname(__file__))


def enabled(config_overrides: Dict[str, bool] = {}):
    return os.environ.get("HMD_LOCAL_NEURONSPHERE_ENABLE_DAGSTER", "false") == "true"


def get_resources():
    return {}


def prepare_hmd_home(hmd_home: str, configs: Dict[str, bool] = {}):
    HMD_HOME = Path(hmd_home)

    dagster_path = HMD_HOME / "dagster"
    os.umask(0)
    os.makedirs(dagster_path, exist_ok=True)

    repopy_path = dagster_path / "repo.py"

    if not repopy_path.exists():
        shutil.copyfile(_dirname / "data" / "repo.py", repopy_path)

    dagsteryaml_path = dagster_path / "dagster.yaml"
    if not dagsteryaml_path.exists():
        with open(_dirname / "data" / "dagster.yaml", "r") as d:
            dagsteryaml = yaml.safe_load(d)
        volumes: List[str] = dagsteryaml["run_launcher"]["config"]["container_kwargs"][
            "volumes"
        ]

        new_volumes = []
        for v in volumes:
            new_volumes.append(v.format(HMD_HOME=str(HMD_HOME.absolute())))

        dagsteryaml["run_launcher"]["config"]["container_kwargs"][
            "volumes"
        ] = new_volumes
        print(dagsteryaml)
        with open(dagsteryaml_path, "w") as d:
            yaml.dump(dagsteryaml, d)

    workspaceyaml_path = dagster_path / "workspace.yaml"

    if not workspaceyaml_path.exists():
        shutil.copyfile(_dirname / "data" / "workspace.yaml", workspaceyaml_path)


def render_compose_yaml(
    resources: Dict[str, List[str]], cache_dir: Path, configs: Dict[str, bool] = {}
):
    dagster_cache = cache_dir / "dagster"
    os.umask(0)
    os.makedirs(dagster_cache, exist_ok=True)

    db_path = dagster_cache / "db_init.sql"
    shutil.copyfile(_dirname / "data" / "db_init.sql", db_path)

    shutil.copyfile(
        _dirname / "data" / "Dockerfile_dagster", dagster_cache / "Dockerfile_dagster"
    )
    shutil.copyfile(
        _dirname / "data" / "Dockerfile_user_code",
        dagster_cache / "Dockerfile_user_code",
    )

    with open(_dirname / "data" / "docker-compose.yaml", "r") as dc:
        compose = yaml.safe_load(dc)

    compose_path = cache_dir / "docker-compose.dagster.yaml"

    with open(compose_path, "w") as dc:
        yaml.dump(compose, dc)

    return compose_path
