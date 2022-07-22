solutions = open("solutions.txt","r")
solutions = solutions.readlines()
solutions2 = [x.strip() for x in solutions]

words = open("words.txt", "r")
words = words.readlines()
words2 = [x.strip() for x in words]

a=0
for x in range(0,len(solutions2)):
    if solutions2[x] in words2:
        #do nothing
        a = a+1
        pass
    else:
        print(solutions2[x])
        # print("Not found!")
print (a)
print(len (solutions2))

