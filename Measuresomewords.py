# measure some strings;

words = ['cat','windows', 'defensestrate']
for w in words:
    print(w,len(w))
    
    if len(w) > 6:
        words.insert(0,w)
        break
print(words)


