import pypandoc

# With an input file: it will infer the input format from the filename
#output = pypandoc.convert_file('somefile.md', 'rst')

# ...but you can overwrite the format via the `format` argument:
#output = pypandoc.convert_file('somefile.txt', 'rst', format='md')

# alternatively you could just pass some string. In this case you need to
# define the input format:
output = pypandoc.convert_text('# some title', 'rst', format='md')
# output == 'some title\r\n==========\r\n\r\n'

print(output)