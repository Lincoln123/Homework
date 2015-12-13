import math
import sys
fil = sys.argv[1]
fil1 = sys.argv[2] 

def Main():  
    f = open(fil,'r')
    n = int(f.read()) #переменная входного числа
    q = int(4 * pow(math.log2(n),2) + 1)    
    check_input(n)
    PerfectPower(n)
    Individual_r(n,q)

def check_input(n):
    if n < 1 : 
        Output('\nFalse, input is incorrect')
    elif n == 1 :
        Output('\nFalse, Composite number')

def Output(text) :
    f = open(fil1, 'w')
    f.writelines(text)
    f.close()
    exit(0)
     
def PerfectPower(n):
    b = 2                        #показатель степени
    if b > math.log2(n):         #проверка на вход 
        Output('prime')
        
    while b <= math.log2(n): 
        m = math.ceil(n**(1/b))  #корень b'ой степени из n
        if n == m**b:
            Output('\nFalse, Composite number,Perfect power')
            #exit(0)
        else:
            b+=1
            
def Individual_r(n,q):
    for j in range(1,int(4 * pow(math.log2(n),2))) :   #степень числа n
        if (n ** j) % q != 1 :
            r = q
            GCD(n,r)
            FermaTest(n,r)
            continue
        else: 
            q += 1
            return Individual_r(q)#,[GCD(r),r]
                
def GCD(n,r):    
    if r >= n:
        r = n - 1
        for gcd in range(r,0,-1) :
            z = n
            if z % gcd == 0 :
                if gcd != 1:
                    Output('\nFalse, Composite number')        
    else:
        for gcd in range(r,0,-1) :
            z = n
            if z % gcd == 0 :
                if gcd != 1:
                    Output('\nFalse, Composite number')
                    
def FermaTest(n,r):            
    for k in range(2,int(2*math.sqrt(r)*math.log2(n))) : #целое число
                
        if (pow(k,(n-1)) - 1) % n != 0 :

            Output('\nFalse, Composite number')
            #exit(0) 
            continue
        else :
            Output('\nPrime')
                                    

    
       
Main()            