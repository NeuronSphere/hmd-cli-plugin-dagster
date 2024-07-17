# hmd-cli-plugin-dagster

Local NeuronSphere plugin to run Dagster

## Installation

``pip install neuronsphere``
``pip install -e src/python``

## Setup

Configure HMD_HOME by running ``hmd configure`` and following all prompts.

Set necessary Environment Variables 

``hmd configure set-env HMD_LOCAL_NS_CONTAINER_REGISTRY ghcr.io/neuronsphere``
``hmd configure set-env HMD_LOCAL_NEURONSPHERE_ENABLE_DAGSTER true``
``hmd configure set-env COMPOSE_PROJECT_NAME neuronsphere_dagster``

## Run

``hmd neuronsphere up``

The Dagster UI is accessible from http://localhost:3000