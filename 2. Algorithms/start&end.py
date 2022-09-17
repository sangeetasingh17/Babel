import re


def substring_indices(pattern, string):
    find = re.finditer('(?={0})'.format(b), string)
    a = [(m.start(), m.start()+len(pattern)-1) for m in find]
    return a


# reading input from the file
inp = open('input.txt', 'r')
l = [i.strip() for i in inp]
inp.close()
a, b = l
ans = substring_indices(b, a)

# writing output to the file
oup = open('output.txt', 'w')
if not ans:
    oup.write('(-1, -1)\n')
else:
    for i in ans:
        oup.write(str(i)+'\n')
oup.close()
