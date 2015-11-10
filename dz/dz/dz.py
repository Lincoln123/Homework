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
        else: 
            j=1
            q=2
            while j >= 1:
                while q>=j:
                    if (n**j)%q!=1:

                        r=q
                        print (r)
                        break
                    else: 
                        q+=1
                break
                j+=1
                
            print ('azaza')  #сюда поставить что с р дальше
            
            #while a<=r:
             #   a+=1
            for a in range(r,1,-1):

                  
                while a!=0:
                    a,n=n%a,a
                    p=n #переменная вывода  
                    #print (p)
            print (p)      
            break
            if p!=1:
                print('False, Composite number')
        #break
    #print('False, Composite number')

        






