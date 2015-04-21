#!/sw/bin/python
import re
import sys

if sys.argv[1] == '-h':
    print 'usage:', sys.argv[0], 'regex files...'
    print "For example: python regexs.py '\bthat that\b' *.txt"

r = re.compile(sys.argv[1]);

for filename in sys.argv[2:]:
    file = open(filename,'r')
    data = file.read().replace('\n', ' ')
    file.close()
    for m in r.findall(data):
        print m
