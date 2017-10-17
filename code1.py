def is_zigzag(arr):  
    is_zigzag=True
    i=1
    for k in range(len(arr)-2):  
        if not (((arr[i+1] > arr[i]) and (arr[i] < arr[i-1]) ) or  ((arr[i+1] < arr[i]) and (arr[i] > arr[i-1]) )):
            is_zigzag=False
        i=i+1
    if len(arr)>1:
        if arr[0]==arr[1]:
            is_zigzag=False       
    return (is_zigzag, len(arr))
     

def sub_arr(L,L2=None):
    if L2==None:
        L2 = L[:-1]
    if L==[]:
        if L2==[]:
            return []
        return sub_arr(L2,L2[:-1])
    return [L]+sub_arr(L[1:],L2)
    
sub_arr([4,3,1])    


def run_all_sub_arr(arr):
    
    list_of_sub=sub_arr(arr)
    list_zig=[]    
    for i in range(len(list_of_sub)):
        list_zig.append(is_zigzag(list_of_sub[i]))       
    print(list_zig) 
    max=0
    for i in range(len(list_zig)):
        if ((list_zig[i][0]) and (list_zig[i][1]>max)):
            max=list_zig[i][1]
            print(max)          
    return max



def zigzag(a):
    
   return run_all_sub_arr(a)   
