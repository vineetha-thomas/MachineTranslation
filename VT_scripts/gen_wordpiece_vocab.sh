#!/bin/bash

#python3 ../bert-vocab-builder/subword_builder.py \
#--corpus_filepattern=../data_small/corpus_dir/combined/combined.txt \
#--output_filename=../data_small/wordpiece_vocab.txt \
#--logtostderr

python tokenize.py --corpus_path ../data_small/corpus_dir --output_path ../data_small --vocab_size 8000