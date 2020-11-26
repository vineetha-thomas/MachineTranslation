#!/bin/bash
source ~/.bashrc
conda activate nmt-gpu

python3 ../electra/run_pretraining.py \
--data-dir ../data_small/corpus_dir/corpus_sampled \
--model-name nmt_model1 \
--hparams electra_config.json
