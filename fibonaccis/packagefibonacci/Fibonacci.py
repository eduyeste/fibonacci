'''
Created on 25 nov. 2016

@author: usuario
'''
def Fibonacci(numero):
    if numero==1:
        return 1
    if numero==0:
        return 0
    else:
        return Fibonacci(numero-1)+Fibonacci(numero-2)
    
if __name__=="__main__":
    numero=int(input("Escribe el numero sobre el qque desea..."))
    print (Fibonacci(numero))
