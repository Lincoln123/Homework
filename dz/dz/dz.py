import math
import sys

fil = sys.argv[1]
fil1 = sys.argv[2]
#функция ввода/вывода
def Output(text) :
    f = open(fil1, 'w')
    f.writelines(text)
    f.close()
     
# функция проверки
#b - показатель степени
def checkborder(text1,b=2):
    if b>math.log2(n): 
         Output(text1)
def PerfectPower():
    b = 2#показатель степени
    checkborder('\nprime1')#проверка на вход 
    #exit(0)   
    while b <= math.log2(n): # пока степень меньше логарифма нашего числа
        m = math.ceil(n**(1/b)) #корень b'ой степени из n
        if n == m**b:
            Output('\nFalse, Composite number111')
            exit(0)
        else:
            b+=1
            checkborder('')
            continue
    
def Individual_r():
    q = int(4 * pow(math.log2(n),2) + 1) #делитель для определения числа r
    while q > 4 * pow(math.log2(n),2) :
        for j in range(1,int(4 * pow(math.log2(n),2))) :   #просто степень числа n
            if (n ** j) % q != 1 :
                r = q
            #return r
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
    for k in range(1,int(2*math.sqrt(r)*math.log2(n))) : #переменная для счетчика из т.Ферма
        x = int()
        
        if (pow(( x + k ),n) - (pow(x,n) + k)) % n != 0 and (pow(x,r) - 1) % n != 0 :

        #print ('False, composite number')
            Output('\nFalse, Composite number')
            exit(0) 
            continue
        else :
            #print('Prime')  
            Output('\nPrime')
            exit(0)                            
    #break
f = open(fil,'r')
n = int(f.read()) #переменная входного числа
#n = int(input("Enter the figure "))

if n < 1 :
    #print('False, input is incorrect')
    Output('\nFalse, input is incorrect')
elif n == 1 :
    Output('\nFalse, Composite number')
    #print('False, Composite number')

else :
    PerfectPower()
    Individual_r()
         
        
    gcd = Individual_r() #переменная вывода НОД
            
    if gcd[0] != 1 :
        #print('False, Composite number')
        Output('\nFalse, Composite number')
        exit(0)
    FermaTest(gcd[1]) 
   # exit(0)    
            