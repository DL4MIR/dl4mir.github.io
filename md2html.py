import markdown
import sys

filename = sys.argv[1]

header = """| [Home](https://dl4mir.github.io) |\n""" 

with open(filename+'.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(header+text)

with open(filename+'.html', 'w') as f:
    f.write('<body style="font-family: sans-serif">\n')
    f.write(html)
