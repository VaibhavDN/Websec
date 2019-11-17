import os
p = os.path.abspath('./')
print(p)
p = p.split('\\')
print(p)
p.pop()
print(p)
p = '\\'.join(p)
print(p)
