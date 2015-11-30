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
def checkborder(text1):
    if b>math.log2(n): 
         Output(text1)

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
    b = 2 #показатель степени
    checkborder('\nprime')#проверка на вход    
    while b <= math.log2(n): # пока степень меньше логарифма нашего числа
        m = int(n**(1/b)) #корень b'ой степени из n
        if n == m**b:
            Output('\nFalse, Composite number')
            break
        else:
            b+=1
            checkborder('')
         
            q = int(4 * pow(math.log2(n),2) + 1) #делитель для определения числа r
            while q > 4 * pow(math.log2(n),2) :
                for j in range(1,int(4 * pow(math.log2(n),2))) :   #просто степень числа n
                    if (n ** j) % q != 1 :
                        r = q
                        break
                    else: 
                        q += 1
                    if (r) :
                        break
                break
                
            if r >= n:
                r = n - 1
                for a in range(r,0,-1) :
                    z = n
                    if z % a == 0 :
                        break        
            else:
                for a in range(r,0,-1) :
                    z = n
                    
                    if z %a == 0 :
                        break
            GCD = a #переменная вывода НОД
            
            if GCD != 1 :
                #print('False, Composite number')
                Output('\nFalse, Composite number')
                break
                        
            for k in range(1,int(2*math.sqrt(r)*math.log2(n))) : #переменная для счетчика из т.Ферма
                x = 1
                if (pow(( x + k ),n) - (pow(x,n) + k)) % n != 0 and (pow(x,r) - 1) % n != 0 :

                    #print ('False, composite number')
                    Output('\nFalse, Composite number')
                    continue
                else :
                    #print('Prime')  
                    Output('\nPrime')
                    break
            break