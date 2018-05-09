import pickle
import sys
import os

extract_file = sys.argv[1]
os.remove('draft.txt')

with open(extract_file, 'rb') as file:
	dataset = pickle.load(file)
	for item in dataset:
		print(item['date'])
		print(item['url'])
		print(item['text'], end="\n\n")

		with open('draft.txt', 'a') as f:
			f.write(item['text'])