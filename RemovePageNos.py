import re


input_file = 'RulingChiefs.txt'
output_file = 'pageless_'+input_file
odd= "^\s*[A-Z| |-|-|ʻ|]{4,}\d+\s*[\n|\r]"
even = "^\s*\d+\s*[A-Z| |-|-|ʻ|]{4,}\s*[\n|\r]"
roman = "^\s*[i|ii|iii|iv|v|vi|vii|viii|ix|x]*[\n|\r]"

with open(input_file, "r", encoding="utf8") as textfile:
    s=textfile.read()

# removes even and odd page numbers with headers     
evenless = re.sub(even, '\n',s, flags=re.MULTILINE)
oddless = evenless = re.sub(odd, '\n',evenless, flags=re.MULTILINE)

# removes standalone page numbers
nostand = oddless = re.sub('^\d*\s*[\n\r]', '\n',oddless, flags=re.MULTILINE)
# removes roman numberals from frontmatter pages
nopage= nostand = re.sub(roman, '\n', nostand, flags=re.MULTILINE)

with open(output_file, "w", encoding="utf8") as pageless:
    pageless.write(nopage)