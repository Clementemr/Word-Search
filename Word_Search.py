import time
start_time=time.time()





def dijkstra(word1,word2,dictList,wordList):
    n = len(word1)
    if len(word1)!=len(word2):
        return "error"
    
    print("graphing...")
    
    parents={}
    
    graph = dictList[n]
    openList = []
    closedList=[]
    result=[]
    try:
        for i in range(len(wordList[n])):
            for j in range(len(wordList[n][i])):
                openList.append([wordList[n][i][j],1000])
                parents[wordList[n][i][j]]=None



        tup1 = [word1,1000]
        i1 = openList.index(tup1)

        openList[i1] = [word1,0]

        lastTup = openList[i1]
    except:
        return "error"

    count=0
    while word2 not in closedList:
        if count>100000:
            print("no solution found after 100000 steps")
            break
        count+=1
        

        for tup in graph[lastTup[0]]:
            if parents[tup[0]]==None:
                parents[tup[0]]=lastTup[0]
            for item in openList:
                if tup[0]==item[0]:
                    currentTup=item
                    if tup[1]+lastTup[1]<currentTup[1]:
                        currentTup[1]=lastTup[1]+tup[1]
                
                    


        minIndex = 0
        for tup in openList:
            if tup[1]<openList[minIndex][1]:
                minIndex = openList.index(tup)

        
        lastTup = openList[minIndex]




        closedList.append(lastTup)
        openList.remove(lastTup)



        if lastTup[0]==word2:
            break



    currentChild=word2
    result.append(currentChild)
    count=0
    while word1 not in result and count<100:
        try:
            count+=1
            result.append(parents[currentChild])
            currentChild=parents[currentChild]
        except:
            return "no path exists"

    solution=[]
    for i in range(len(result),0,-1):
        for item in closedList:
            if item[0]==result[i-1]:
                solution.append((item[0],item[1]))


    return solution



    

        



letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

words = []

for i in range(30):
    words.append([])

for j in range(30):
    for k in range(26):
        words[j].append([])

dicts = []

for i in range(30):
    dicts.append({})


with open("Clemente_hw6/Dict.txt") as file:
    for line in file:
        dicts[len(line.strip())][line.strip()] = []
        words[len(line.strip())][letters.index(line.strip()[0])].append(line.strip())


for n in range(30):
    if n>=0:
        print(n,time.time()-start_time)
    for i in range(26):
        for l in range(len(words[n][i])):
            word = words[n][i][l]
            for j in range(n):
                for k in range(26):
                    myWord=""
                    for a in range(0,j):
                        myWord+=word[a]
                    myWord+=letters[k]
                    for b in range(j+1,n):
                        myWord+=word[b]
                    if myWord!=word:
                        if myWord in words[n][letters.index(myWord[0])]:
                            dicts[n][word].append((myWord,abs(ord(word[j])-ord(letters[k]))))
                            
                

end_time=time.time()

print(end_time-start_time)

user=''
while user!="no":
    
    print(dijkstra(input("starting word: "),input("ending word: "),dicts,words))

    user=input("keep going? ")








