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
        j=int(1)
        q=int(1)
        while j >= 1:
               while int(q)>=j+1:
                    (n**j)%q!=1
                    r=q
                    print (r)
                    break

            

        #break
    #print('False, Composite number')

        






