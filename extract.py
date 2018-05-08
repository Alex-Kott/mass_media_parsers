import pickle
import sys

extract_file = sys.argv[1]
with open(extract_file, 'rb') as file:
	dataset = pickle.load(file)
	print(dataset)
