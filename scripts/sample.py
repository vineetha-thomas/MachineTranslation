import sys
import math
import numpy as np
import argparse

def read_lines(corpora):
    min_count = math.inf #smallest value to use as sample count
    data = []
    for docs in corpora:
        sentences = []
        with open(docs,encoding='utf-8') as f:
            line = True
            count = 0
            while line:
                line = f.readline()
                sentences.append(line)
                count += 1

        if count < min_count:
            min_count = count


        data.append(sentences)

    return data,min_count

def build_dataset(data,n):
    dataset = []
    for doc in data:
        np.random.shuffle(doc)
        dataset.append(np.random.choice(doc,n))
    return dataset

def write_dataset(dataset, output_path):
    #with open('dataset.txt','w',encoding='utf-8') as f:
    with open(output_path,'w',encoding='utf-8') as f:
        for doc in dataset:
            for line in doc:
                f.write(str(line))

def get_args():
    myparser = argparse.ArgumentParser()
    myparser.add_argument('--lang1_doc', required=True)
    myparser.add_argument('--lang2_doc', required=True)
    myparser.add_argument('--output_doc', required=True)

    args = myparser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    corpora = []
    corpora.append(args.lang1_doc)
    corpora.append(args.lang2_doc)
    output_path = args.output_doc
    #corpora = sys.argv[1:]
    data,n = read_lines(corpora)
    dataset = build_dataset(data,n)
    write_dataset(dataset, output_path)


