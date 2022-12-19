
#creating a ATM example to handle user exception




#creating Withdraw exception
class Withdraw(BaseException):
    def __init__(self,msg):
        self.msg=msg

#creating Pinchecking Excepton        
class Pincheck(BaseException):
    def __init__(self,msg):
        self.msg=msg
        

#creating ATM class
class ATM:
    name="SBI ATM"
    def __init__(self,pin,mon):#taking pin,money from useer to save
        self.pin=pin
        self.mon=mon
    def PinCheck(self,p):# taking pin number again from user to maching and withdrwa money
        self.p=p
        if self.p!=self.pin:
            raise Pincheck("enter your corrcet ATM pin!..")# passing msg 
        else:
            print(self.mon)
    def withdraw(self,n):# taiking money to withdra
        self.n=n
        if self.n> self.mon:
            raise Withdraw("insuficent blance..")#passing msg
        else:
            print("withdra successfull!...")

# creatiing object of ATM class
sbi=ATM(123,10000)

p=int(input("enter your ATM pin. ")) #taking user input
n=int(input("enter money to withdraw: ")) #taiking user input

#calling methods inside try bloc to 
try:
    sbi.PinCheck(p)
    try:
        sbi.withdraw(n)
    except Withdraw as w:
        print(w)
except Pincheck as ps:
    print(ps)
    

        
                
        
        
                    
            
        
        
        
        