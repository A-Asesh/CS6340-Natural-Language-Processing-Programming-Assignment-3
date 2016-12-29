import math
import sys
file_seeds = sys.argv[1]
file_contexts = sys.argv[2]

#-------------------------------------------------------------------------             
seeds = []
with open(file_seeds) as my_file:
    for line in my_file:
        line=line.upper()
        line = line.split()
        line=''.join(line)
        seeds.append(line)
"""for i in seeds:
    print (i)"""

#-------------------------------------------------------------------------
contexts = []
with open(file_contexts) as my_file:
    for line in my_file:
        line = line.split()
        contexts.append(line)
"""for i in contexts:
    print (i)"""

#-------------------------------------------------------------------------
pattern={}
for item in contexts:
    last=item[-1]
    if last in pattern:
        if item[-3:-2] in pattern[last]:
            continue
        else:
            pattern[last].append(item[-3:-2])
    else:
        pattern[last]=[item[-3:-2]]
"""for key in pattern:
    print key, pattern[key]"""

print "Seed Words:",
for i in seeds:
    i=i.lower()
    print i,

print '\n' "Unique Patterns:", len(pattern)
#-------------------------------------------------------------------------
def main_cal():
    for i in range(1,6):
        print '\n' "ITERATION",i
        candidate_list=[]
        proper_candidate_list=[]
        sem_freq=[]
        final=[]
        lastval=0
        top_word=[]
        top=[]
        top_pattern=[]
        for key in pattern:
            Rval=0
            count=0
            for item in pattern[key]:
                item=''.join(item)
                if item in seeds:
                    count=count +1
            Rval=float(count)/len(pattern[key])*math.log(len(pattern[key]),2)
            Rval="%.3f" % Rval
            top.append([Rval,key])
        top.sort()
        top.reverse()
        """for i in range(0,len(pattern)):
        print top[i]"""
        
        for i in range(0,10):
            top_pattern.append(top[i])
        for i in range(10,100):
            if (top_pattern[-1][0]==top[i][0]):
                top_pattern.append(top[i])
        
        from operator import itemgetter
        top_pattern1 = sorted(top_pattern, key=itemgetter(1))
        top_pattern2 = sorted(top_pattern1, key=itemgetter(0),reverse=True)

        print "PATTERN POOL"
        k=0
        for i in top_pattern2:
            k=k+1
            print k,".",i[1],"(",i[0],")"
        for i in range(0,len(top_pattern)):
            for key in pattern:
                if (top_pattern[i][1]==key):
                    candidate_list.extend(pattern[key])
        
        for i in candidate_list:
            i=''.join(i)
            proper_candidate_list.append(i)

        candidate_set=set(proper_candidate_list)
        seeds_set=set(seeds)
        candidate_set.difference_update(seeds_set)
        new_words=[]

        for item in candidate_set:
            result=[]
            avgLog=0
            for key in pattern:
                count1=0
                if [item] in pattern[key]:
                    for i in seeds_set:
                        if [i] in pattern[key]:
                            count1=count1+1
                    result.append(count1)
            for z in result:
                avgLog=avgLog+math.log(z+1,2)
            avgLog=avgLog/len(result)
            avgLog="%.3f" % avgLog
            new_words.append([item,avgLog])

        for i in new_words:
            float(i[1])
            
        new_words.sort(key=lambda x:x[1],reverse=True)
        
        for i in range(0,5):
            top_word.append(new_words[i])
        for i in range(5,len(new_words)):
            if (top_word[-1][1]==new_words[i][1]):
                top_word.append(new_words[i])

        print " \nNEW WORDS"
        for i in top_word:
             seeds.append(i[0])

        top_word1 = sorted(top_word, key=itemgetter(0))
        top_word2 = sorted(top_word1, key=itemgetter(1),reverse=True)

        for i in top_word2:
            i[0]=i[0].lower()
            print i[0],"(",i[1],")"
        
        #print len(seeds_set)

main_cal()
