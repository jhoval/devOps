import sys

from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]

print onlyfiles
