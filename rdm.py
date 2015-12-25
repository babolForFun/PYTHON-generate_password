import sys
import itertools
import random

def lowerUpperPos(key):
	"""Create all possible combination 
		upper and lower case"""
	key = key.lower()
	keywords = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in key)))
	return keywords

def concatenate(keyMap):
	"""Concatenate list of words"""
	return list(itertools.product(*keyMap))

def randomizeInput(keyMap):
	"""Randomize input string order"""
	res = []
	for L in range(1, len(keyMap)+1):
		for subset in itertools.permutations(keyMap, L):
			res.append(subset)
	return res

def writeOn(file,keys):
	"""Write on file"""
    keyMap = []
    for key in keys:
		x = lowerUpperPos(key)
		keyMap.append(x);
    res = concatenate(keyMap)
    sorted(set(res))
    for el in res:
    	file.write(''.join(el)+'\n')

def main():
	"""Recive input string and generate"""
    keys = raw_input("Key separated with semicolon: ").split(";")
    file = open("rdm.txt", "w")
    pos = randomizeInput(keys)
    for element in pos:
    	writeOn(file,list(element))
    file.close()

if __name__ == "__main__":
    main()