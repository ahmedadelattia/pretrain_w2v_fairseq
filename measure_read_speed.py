#reads an audio file from manifest and measures the read speed
# Usage: python measure_read_speed.py 

import os
import sys
import time
import librosa
import random

manifest = "./manifest/train.tsv"
manifest = open(manifest, 'r').readlines()

root = manifest[0].strip()
manifest = manifest[1:]
print("Root: ", root)
#shuffle(manifest)
manifest = random.sample(manifest, 100)
times = []

for i in range(1, 100):
    file = manifest[i].split('\t')[0]
    file_path = os.path.join(root, file)

    print("Reading file: ", file_path)
    start = time.time()
    y, sr = librosa.load(file_path, sr=None)
    end = time.time()
    print("Read time: ", end-start, "seconds")
    times.append(end-start)
    
print("Average read time: ", sum(times)/len(times), "seconds")