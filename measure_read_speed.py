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
    if i == 1:
        continue
    print("Read time: ", end-start, "seconds")
    times.append(end-start)
    
avg_time = sum(times)/len(times)
print("Average read time: ", avg_time, "seconds")
speed_up_down = avg_time/0.0011655651793187978*100
if speed_up_down > 100:
    print(f"Read time is {speed_up_down-100:.02f}% slower than reference SSD (isrwkavw3180g)")
else: 
    print(f"Read time is {100-speed_up_down:.02f}% faster than reference SSD (isrwkavw3180g)")