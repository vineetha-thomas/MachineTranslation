#!/bin/bash
source ~/.bashrc
conda activate nmt-gpu

python3 ../electra/build_pretraining_dataset.py \
--corpus-dir ../data_small/corpus_dir/corpus_sampled \
--vocab-file ../data_small/wordpiece_vocab.txt \
--output-dir ../output/
