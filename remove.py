#------------------------------------------------------------------------#
#-----------------        Student Banner Remove         -----------------#
#------------------------------------------------------------------------#

import sys

subpath = "SystemFiles/FrontEnd/TextResources"
file = "MiscExpressions.tr"

match = '"StudentBar" -> Cell'
stop_match = '"PlayerBar"'

path = sys.argv[1] + "/" + subpath + "/" + file

file_in = open(path,'r')

newfile_buffer = ""

ow = False

for line in file_in:

    if len(line) >= len(match) and not ow:
        if line[:len(match)] == match:
            newfile_buffer += match + '[],\n'
            ow = True
            continue
    elif ow:
        if len(line) >= len(stop_match):
            if line[:len(stop_match)] == stop_match:
                newfile_buffer += line
                ow = False
        continue
    newfile_buffer += line

file_in.close()

file_out = open(path, 'w')
file_out.write(newfile_buffer)
file_out.close()
