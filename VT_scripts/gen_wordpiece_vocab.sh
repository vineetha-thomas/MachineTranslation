#!/bin/bash

python3 ../bert-vocab-builder/subword_builder.py \
--corpus_filepattern "../data/corpus_dir/combined/combined.txt" \
--output_filename ../data/wordpiece_vocab.txt \
--min_count 2
