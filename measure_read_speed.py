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
    
avg_time = sum(times)/len(times)
print("Average read time: ", avg_time, "seconds")
speed_up_down = avg_time/0.006126663901589133*100
if speed_up_down > 1:
    print(f"Speed up: {speed_up_down:.02f}% than referense SSD (isrwkavw3180g)")
else: 
    print(f"Speed down: {speed_up_down:.02f}% than referense SSD (isrwkavw3180g)")