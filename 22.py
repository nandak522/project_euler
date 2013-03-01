'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''

from string import ascii_uppercase
name_score_ref = dict(zip(list(ascii_uppercase), range(1, len(ascii_uppercase)+1)))
print 'name_score_ref:%s' % name_score_ref
with open('names.txt', 'r') as f:
   names = f.read()
names = names.split(',')
names = map(lambda name: name[1:-1], names)
names.sort()
names_score = {}
def compute_score(name):
    print 'name:%s' % list(name)
    count = 0
    for char in list(name):
        count += name_score_ref[char]
    #print 'name score for %s is :%s' % (name, count)
    return count
total_score = 0
for index, name in enumerate(names, start=1):
    #print 'index:%s name:%s' % (index, name)
    total_score += (compute_score(name) * index)
print 'total_score:%s' % total_score