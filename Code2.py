def get_min_period(sequence,max_period,test_numb):
    seq=sequence
    if max_period+test_numb > len(sequence):
        print("max_period+test_numb cannot be bigger than the seq length")
        return 1
    for i in range(1,len(seq)):       
        for j in range(1,max_period):
            found =True
            for con in range(j+test_numb):                                       
                if not (seq[-i-con]==seq[-i-j-con]):
                    found = False
            if found:           
                minT=j
                return minT
