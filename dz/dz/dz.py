import math
import sys

fil = sys.argv[1]
fil1 = sys.argv[2]

def Output(text) :
    f = open(fil1, 'w')
    f.writelines(text)
    f.close()
    exit(0)
     
def PerfectPower():
    b = 2                        #показатель степени
    if b > math.log2(n):         #проверка на вход 
        Output('prime')
        #exit(0)   
    while b <= math.log2(n): 
        m = math.ceil(n**(1/b))  #корень b'ой степени из n
        if n == m**b:
            Output('\nFalse, Composite number,Perfect power')
            #exit(0)
        else:
            b+=1
            
          
def Individual_r():
    q = int(4 * pow(math.log2(n),2) + 1) #делитель для определения числа r
    while q > 4 * pow(math.log2(n),2) :
        for j in range(1,int(4 * pow(math.log2(n),2))) :   #степень числа n
            if (n ** j) % q != 1 :
                r = q
            else: 
                q += 1
            if (r) :
                return [GCD(r),r]
                
def GCD(r):    
    if r >= n:
        r = n - 1
        for a in range(r,0,-1) :
            z = n
            if z % a == 0 :
                return a        
    else:
        for a in range(r,0,-1) :
            z = n
                    
            if z %a == 0 :
                return a
                    
def FermaTest(r):            
    for k in range(1,int(2*math.sqrt(r)*math.log2(n))) : #целое число
                
        if (pow(k,(n-1)) - 1) % n != 0 :

            Output('\nFalse, Composite number')
            #exit(0) 
            continue
        else :
            Output('\nPrime')
            #exit(0)                            
    
f = open(fil,'r')
n = int(f.read()) #переменная входного числа


if n < 1 : 
    
    Output('\nFalse, input is incorrect')
elif n == 1 :
    Output('\nFalse, Composite number')
    

else :
    PerfectPower()
    Individual_r()
         
        
    gcd = Individual_r() #переменная вывода НОД + r для Ферма
            
    if gcd[0] != 1 :
        Output('\nFalse, Composite number')
        #exit(0)
    FermaTest(gcd[1]) 
       
            