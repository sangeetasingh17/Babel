import re


def substring_indices(pattern, string):
    find = re.finditer('(?={0})'.format(b), string)
    a = [(m.start(), m.start()+len(pattern)-1) for m in find]
    return a


# reading input from the file
in_file = open('input.txt', 'r')
l = [i.strip() for i in in_file]
in_file.close()
a, b = l
ans = substring_indices(b, a)

# writing output to the file
out_file = open('output.txt', 'w')
if not ans:
    out_file.write('(-1, -1)\n')
else:
    for i in ans:
        out_file.write(str(i)+'\n')
out_file.close()
