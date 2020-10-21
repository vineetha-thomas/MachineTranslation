#!/bin/bash

python3 ../bert-vocab-builder/subword_builder.py \
--corpus_filepattern=../data_small/corpus_dir/combined/combined.txt \
--output_filename=../data_small/wordpiece_vocab.txt \
--logtostderr