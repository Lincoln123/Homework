#f = open('data.txt','r')
import math
n = int(input("Enter the figure "))
if (n<=1): 
    print('False')
else:
    
    for s in range(2,n):
        m = (math.log(n,s))
        if m%1==0:
            print('False, Composite number')
            break
        else: #я думаю надо эту часть сдвинуть но куда пока не понял
            j=1
            q=1
            while j >= 1:
                while q>=j+1:
                    q+=1
                    if (n**j)%q!=1:
                        r=q
                        #print (r)
                    else: 
                        q+=1
                    j+=1
                    print (r)   
                break
            

        #break
    #print('False, Composite number')

        






