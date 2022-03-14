import sys
word = sys.stdin.readline()
UCPC = ["U","C","P","C"]
a = 0
for i in UCPC:
  if i in word:
    wordindex = word.index(i)
    word = word[wordindex+1:]
    a+=1
  else:
    print("I hate UCPC")
    break
if a==4:
  print("I love UCPC")
    

    
     