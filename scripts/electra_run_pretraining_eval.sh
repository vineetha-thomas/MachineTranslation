#!/bin/bash
source ~/.bashrc
conda activate nmt-gpu

python3 ../electra/run_pretraining.py \
--data-dir ../data_small \
--model-name nmt_model1 \
--hparams electra_config_eval.json
