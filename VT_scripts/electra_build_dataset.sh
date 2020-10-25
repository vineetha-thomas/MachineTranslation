#!/bin/bash

python3 ../electra/build_pretraining_dataset.py \
--corpus-dir ../data_small/corpus_dir/combined/ \
--vocab-file ../data_small/wordpiece_vocab.txt \
--output-dir ../output/
