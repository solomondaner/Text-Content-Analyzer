"""
This script runs as a text content analyzer. It analyzes input from a file and compiles statistics on it.
The program should output:
1. The full text content
2. The total word count
3. The count of unique words
4. The number of sentences
5. Number of Lines

extras:
1. The ability to find often used phrases (a phrase of 3 or more words used over 3 times)
2. A list of words used, in order of descending frequency



** Enter File Name. Example: cat test_mochi.txt| python testing_stdin.py
"""
import re
from collections import defaultdict
from operator import itemgetter

path = "C:/Users/solod/Documents/Career/Company Assignments/Galvanize/Text Content Analyzer/Apple.txt"
inFile = open(path, 'r')
data = inFile.read()


#Initializing counter
sentences = 0
lines = 0 
word = 0

f = data
d = defaultdict(int)
for word in f.split():
    d[word] += 1
distinct_word = d.items()


#sentences = f.split('.')+f.split('!')+f.split('?') does not work since we have two !!
sentences = [s.strip() for s in re.split('[\.\?!]', f) if s]
lines = f.split('\n')


print ('\n', 'Full Content:' ,'\n', f, '\n')
print ('Total Word Count =', len(f.split()))  #same as int(sum(d.values()))
print ('Unique word count =',len(distinct_word))
print ('Number of Sentences =', len(sentences))
print ('Number of Lines =', len(lines),'\n')

#print ('extra 1: Average Word Count in Sentence =', float(len(f.split())/len(sentences)), '\n')


W = re.findall(r"[\w']+", f)
#print 'Words=', '\n', W, '\n'


def phrases(w):
        phrase = []
        for w in W:
            p = phrase.append(w)
            if len(phrase) > 3:
                phrase.remove(phrase[0])
            if len(phrase) == 3:
                yield tuple(phrase)
 
#print 'list of phrases',list(phrases(W)), '\n'

Phrases = defaultdict(int)
for p in phrases(W):
        Phrases[p] += 1

sorted_phrases=sorted(Phrases.items(),key=itemgetter(1), reverse =True)
print ('Sorted Phrases By Count: ', '\n', sorted_phrases, '\n')

#a phrase of 3 or more words used over 3 times
for k, (phrase, freq) in enumerate(sorted_phrases):
    if freq > 2:
        print (phrase, freq, '\n',)
    else:
        break

s =sorted(d.items(),key=itemgetter(1), reverse =True)
print ("List of Words in Descending Count:",'\n')
for k, (words, count) in enumerate(s):
    print (words, count)







