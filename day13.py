#string methods
'''
upper ,lower,strip,
rstrip(),replace(),
split(),capitalized()
center(),count(),
endswith,find,isalnum(if any punctuation there it will return false),isalpha(any no.false)
islower,isprintable,isspace,istitle,isupper,swapcase,startswith,title(makes first letter captital)'''

c="hello"
print(c.upper())
print(c.lower())
j=" hlo!!!##" 
print(j.strip())
print(j.rstrip('#'))
print(c.replace('hello','candy'))
b="iiii  uuuu  ccc"
print(b.split(' '))
h="hlo, everyone, goodevening ,all"
print(h.capitalize())
print(b.center(20))
print(h.center(20))
print(c.count('l'))
print(c.endswith('o'))
print(c.find('l'))
print(c.isalnum())
print(c.islower())
print(c.isprintable())
print(c.isspace())
print(b.isupper())
print(b.istitle())
print(b.swapcase())
print(b.startswith('h'))
print(b.title())
