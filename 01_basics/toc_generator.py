import sys

file_list = sys.argv[1]

# open the file with filenames 
# store filenames in order
with open(file_list) as filenames:
    filenames = [name.strip().split(',') for name in filenames]
    print(filenames) 

# produce TOC header (header text, image, etc)
TOC_HEADER = '''
<img src='../images/dark_art_logo.600px.png' width='300' style="float:left">

# TABLE OF CONTENTS

'''


TOC_FOOTER = '''
| Next |
|:-----|
|[{}]({})|
'''

# generate TOC listing (names preceded by `*`)
outputs = []
print(filenames)
for index, (TOC_name, filename) in enumerate(filenames, 1):
    if index == 1:
        TOC_FOOTER = TOC_FOOTER.format(TOC_name, filename) 
    output = '* [{}]({})'.format(TOC_name, filename)
    outputs.append(output)

TOC_BODY = '\n'.join(outputs) + '\n'




with open('README.md', 'w') as fout:
    result = TOC_HEADER + TOC_BODY + TOC_FOOTER
    fout.write(result)

