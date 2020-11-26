# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:40:40 2020

@author: vinee
"""

from pathlib import Path
import os.path
import argparse
import json

from tokenizers import BertWordPieceTokenizer

def get_args():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--corpus_path', required=True)
    my_parser.add_argument('--output_path', required=True)
    my_parser.add_argument('--vocab_size', type=int, required=True)

    args = my_parser.parse_args()
    return args

def main():
    args = get_args()
    train(args.corpus_path, args.output_path, args.vocab_size)

def train(corpus_path, output_path, vocab_size=30000):
    datafiles = [str(x) for x in Path(corpus_path).glob("*")]
    print("Processing datafiles....:", datafiles)
    tokenizer = BertWordPieceTokenizer()
    tokenizer.train(datafiles, vocab_size=vocab_size)
    tokenizer.save(output_path+"/vocab.json")

    with open(output_path+'/vocab.json', encoding='utf8') as f:
        data = json.load(f)

    vocab_data = data['model']['vocab']
    f1 = open(output_path+'/wordpiece_vocab.txt', 'w', encoding='utf8')
    for key, value in sorted(vocab_data.items()):
        f1.write(key)
        f1.write("\n")
    f1.close()    

if __name__ == '__main__':
  main()

