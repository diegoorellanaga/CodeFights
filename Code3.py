def open_and_give_back(arr,word,visited,start,lenword,indexespast):
    
    if start<lenword:
        indexes=[(ix,iy) for ix, row in enumerate(arr) for iy, i in enumerate(row) if i == word[start]]
    else:
        print("success")
        global wordreg
        wordreg =1
        return 0


    if len(indexes)==0:
        print("cannot make that word")
        return 1

    continue_a=True
    for i in range(len(indexes)):
       # print("dgsdfgda")
        #print(visited,start,indexespast,indexes[i])
        if (indexespast==1 or (math.fabs(indexes[i][0]-indexespast[0])<2 and math.fabs(indexes[i][1]-indexespast[1])<2)) and visited.count(indexes[i])==0:
           # print(visited,start,indexespast)
            
            open_and_give_back(arr,word,visited+[indexes[i]],start+1,lenword,indexes[i])
    continue_a=False         
    if not continue_a:
        print("cannot make that word")

        return 1        
            
        
def wordBoggle(board, words):

    if len(words)>0:
        wordfinal=[]
        for i in range(len(words)):
            global wordreg
            wordreg=0
            open_and_give_back(board,words[i],[(999,999)],0,len(words[i]),1)
            if wordreg==1:
            
                wordfinal.append(words[i])
        
        wordfinal=list(set(wordfinal))    
        wordfinal.sort()
    
        return wordfinal
    else:
        return []
