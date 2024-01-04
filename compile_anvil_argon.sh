#!/bin/bash

source /lcrc/soft/climate/e3sm-unified/load_latest_e3sm_unified_anvil.sh

conda env create -f conda-env/dev.yml

conda activate pcmdi_metrics_dev
pre-commit install
git checkout -b  pcmdi_e3sm

#command before push
pre-commit run --all-files
