import textwrap
from textwrap_example import sample_text, lineone

dedented_text = textwrap.dedent(sample_text)
print 'Dedented:'
print dedented_text

lineone_text = textwrap.dedent(lineone)
print 'Dedented:'
print lineone_text