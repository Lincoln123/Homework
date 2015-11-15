import math
import sys
fil = sys.argv[1]
def Output(text):
    f = open(fil, 'a')
    f.writelines(text)
    f.close()
f = open(fil,'r')
n = int(f.read())
#n = int(input("Enter the figure "))
if n < 1: 
     #print('False, input is incorrect')
     Output('/nFalse, input is incorrect')
elif n==1:
    Output('/nFalse, Composite number')
    #print('False, Composite number')
elif n==2:
    #print('Prime number')
    Output('/nPrime')
else:
    
    for s in range(2,n):
        m = (math.log(n,s))
        if m%1==0:
            #print('False, Composite number')
            Output('/nFalse, Composite number')
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
            
            if r >= n:
                r = n-1
                for a in range(r,0,-1):
                    z=n
                    print (a)
                    if z%a==0:
                        #p=a
                        break        
            else:
                for a in range(r,0,-1):
                    z=n
                    
                    if z%a==0:
                        break
            p=a
           
                    
                   # print ('z=',z, 'a=',a)
                    
                    #a,z=z%a,a
                    
                     #переменная вывода  
                #break         
                       #print (p)
            #p=n         
            print ('nod',p)      
            #break
            if p!=1:
                #print('False, Composite number')
                Output('/nFalse, Composite number')
                break
            #else:
                #print('Prime')
               
            
           # for p in range(1,2*sqrt(r)*log2(n)):
            
            print (r ,n)
            
            for k in range(1,int(2*math.sqrt(r)*math.log2(n))):
                x=1
                #while x >=0:
                 #   x+=1
                  #  print (x)
                if (pow((x+k),n)-(pow(x,n)+k))%n!=0 and (pow(x,r)-1)%n!=0:

                    #print ('False, composite number')
                    Output('/nFalse, Composite number')
                    continue
                else:
                    #print('Prime')  
                    Output('/nPrime')
                    break
                    
                #break
                
            break
    #print('False, Composite number')

        






