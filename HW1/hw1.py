import hashlib
import csv 

data_file = open("taxi.csv","rb")
data = csv.reader(data_file,delimiter=",")
medallions = []
index = 0

# hashes to be found
find_these_hashes= ["618ecd0a76d5658991e14bc6ef0bbced6ade085b152a32853786dd68156de906",
					"99329a502dd9178b75f3eff01a52555ed1ea9fdbb1a573e47a4adb05f719047a",
					"ebd0f398d465cc86447c014e9ad4e2060ae4b82314ea84e3787a15d7c2b5ab17",
					"c89b9b1a6cffd1972ab94ef5dc0e2b3371d98c56ae2c45524e81a2a19fee9be0",
					"1de578ecf0fd26864f9fcb4e728bcaba839e47d42bbbaaa7b7c62de854110153",
					"4cd7335fa467de24b767c53e3cfc1789c23e2c36952e66b386fb2ab1b8385066",
					"8f96d287b6b77ed0effdeaa719998894dcc777accb1dbde741b58d14e56957d6",
					"daf7123cf1a0ea71c62e174a6290c23d9cb768fae74bb006340ecdfb7d90becb",
					"57f86a9736b1d3ffcfdd15b7a94318ec2ddcab0c5f227a2f7b06cc188feb1287",
					"5c2ecc995d856ead993ccdeec1a5163c0bd0d0c1c73929ffef65021b0a5dae0a"]

# putting data from file into arrays  
for row in data:
	if index!=0:
		medallions.append(row[0])
	index+=1

# found hashes array 
found= []

# append each computed medallion hash in the 
# find_these_hashes array to found array
for med in medallions:
	hashed_med = hashlib.sha256(med).hexdigest()
	if hashed_med in find_these_hashes:
		found.append((med, hashed_med))

# making sure all ten hashes are found
print len(found)

# print hash results
for m, h1 in found:
	print "[ {0}, \n {1} ]\n".format( m, h1)


