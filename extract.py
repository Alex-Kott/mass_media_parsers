import pickle
import sys
import os

extract_file = sys.argv[1]

with open('draft.txt', 'w', encoding='utf-8') as fwrite:
	with open(extract_file, 'rb') as fread:
		dataset = pickle.load(fread)
		for item in dataset:
			print(item['date'])
			print(item['url'])
			print(item['text'], end="\n\n")

			fwrite.write("{}\n{}\n{}\n\n".format(item['date'], item['url'], item['text']))
