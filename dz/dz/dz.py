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
            q=int(4*pow(math.log2(n),2)+1)
            #j=1
            while q > 4*pow(math.log2(n),2):
                for j in range(1,int(4*pow(math.log2(n),2))):
                    if (n**j)%q!=1:

                        r=q
                        #print (r)
                        print ('r=',r)
                        break
                    else: 
                        q+=1
                    if (r):
                        break
                break
                #j+=1
                
            print ('azaza')  #сюда поставить что с р дальше
            
            #while a<=r:
             #   a+=1
            
            
            for a in range(2,r):
                
                
                while a!=0:
                    

                   # print ('n=',n, 'a=',a)
                    
                    a,n=n%a,a
                    p=n
                     #переменная вывода  
                break         
                        #print (p)
                       
            print ('nod',p)      
            #break
            if p!=1:
                print('False, Composite number')
            break
            #else:
                #print('Prime')
               
            
           # for p in range(1,2*sqrt(r)*log2(n)):
            

            for p in range(1,int(2*math.sqrt(r)*math.log2(n))):
                x=1
                while x >=1:
                    if (pow((x+p),n)-(pow(x,n)+p))%n==0 and (pow(x,r)-1)%n==0:
                        print ('False, composite number')
                    else:
                        print('Prime')  
                    
                    
                break
                x+=1
            break
    #print('False, Composite number')

        






