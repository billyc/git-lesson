# Simple python script to "run the model" which really just
# lists all the contributors

import os

files = sorted(os.listdir('contributors'))

# read first line of each file and print it
for filename in files:
	with open(os.path.join('contributors',filename)) as f:
		print "Notes contributed by: ",f.readline().trim()

