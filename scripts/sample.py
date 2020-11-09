import sys
import math
import numpy as np

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

def write_dataset(dataset):
    with open('dataset.txt','w',encoding='utf-8') as f:
        for doc in dataset:
            for line in doc:
                f.write(str(line))


if __name__ == "__main__":
    corpora = sys.argv[1:]
    data,n = read_lines(corpora)
    dataset = build_dataset(data,n)
    write_dataset(dataset)


