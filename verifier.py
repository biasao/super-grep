import re
import sys
import os
from release1 import expected_filenames

# TEST array: expected_filenames = ["mateus", "miguel", "mirian", "fileParaNaoSerEcontrado", "fileParaNaoSerEcontrado2"]

for expected_audioname in expected_filenames:
    audiofile_found = False
    for root, subdirs, files in os.walk(sys.argv[1]):
        for file in files:
            for line in open(root + '/' + file, 'r'):
                if re.search(expected_audioname, line):
                    print expected_audioname, "found at", root + '/' + file
                    audiofile_found = True
    if not audiofile_found:
        print expected_audioname, "not found in the code"