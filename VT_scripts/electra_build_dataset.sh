#!/bin/bash

python3 ../electra/build_pretraining_dataset.py \
--corpus-dir ../data/corpus_dir/combined/ \
--vocab-file ../data/wordpiece_vocab.txt \
--output-dir ../output/