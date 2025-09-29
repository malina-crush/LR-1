text = """Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile."""
text_ = text.strip().lower().replace('!', '.')
predl = text_.split('.', 2)
firstpr = predl[0].split()
pyc = firstpr.count('python')
print('1, 2, 3', text_ )
print('5', firstpr)
print('6', pyc)
print('7', text.startswith('Python'), text.endswith('language'))
print('8', len(text), text.count('a'), text.index('data'))
text_s = text.split()
print('8', text_s, ''.join(i for i in text_s))
dict_ = {}
for i in text_s:
    dict_[i] = dict_.get(i, 0) + 1
print('10', dict_)

def clean_text(a):
    import copy
    import string
    acopy = copy.copy(a)
    acopy = acopy.lower().strip()
    allow = string.ascii_lowercase + " "
    clean = "".join(n if n in allow else " " for n in acopy)
    return " ".join(clean.split())
print( '11',clean_text(text))