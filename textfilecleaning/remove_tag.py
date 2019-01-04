# Script will run with Python versions 2.7.6 or 3.5

import sys
import re

#requires an input file name when running the script
file_name = sys.argv[1]

'''
Open the input file, and discard all text that is not an html tag using regular 
expressions (re). Write the cleaned data to a new file.
'''
with open(file_name, 'r') as myfile:
    contents = myfile.read().replace('\n', '')
    pattern = r"<p>(.*?)</p>"
    new_text = str(re.findall(pattern, contents))
    new_text = new_text.replace("<i>", " ")
    new_text = new_text.replace("</i>", " ")
    new_text = new_text.replace("<a>", " ")
    new_text = new_text.replace("</a>", " ")
    new_text = new_text.replace("<b>", " ")
    new_text = new_text.replace("</b>", " ")
    cleaned = open('tagless_file.txt', 'w')
    cleaned.write(new_text)