import string
values = { 'var':'foo'}

t = string.Template("$var is herer but $missing is not provided")

try:
    print 'substitute() :', t.substitute(values)
except KeyError, err:
    print 'ERROR:', str(err)

print 'safe_substitute():', t.safe_substitute(values)


