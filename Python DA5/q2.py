class Bank:
    def __init__(self,bal=0):
        
        self.bal = bal
    def dep(self,mon):
        self.bal += mon
    def withd(self,mon):
        self.bal-=mon
    def checkBal(self):
        print(self.bal)
    def exit(self):
        exit()
def ask(name):
    
    if name in listaccs:
        return name
    else : print("Account doesnt exist under this name: ")

listaccs = []   

while True:
    name = input("Enter name [keep empty to exit]: ")
    if name == '':
        exit()
    if name.upper() not in listaccs:
        st = input("Account doesnt exist under this name, would you like to create ? Y/N: ")
        if st in 'Yy':
            listaccs.append(name.upper())    
            balance = float(input("Enter initial deposit (keep zero if none) : "))
            exec(f"{name}=Bank({balance})")
        else:
            continue    
    n = int(input("\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit\nChoice: "))
    match n:        
        case 1:
            exec(f'{name}.dep(float(input("Enter amount to deposit : ")))')
        case 2:
            exec(f'{name}.withd(float(input("Enter amount to withdraw : ")))')
        case 3:
            exec(f'{name}.checkBal()')
        case 4:
            exit()
        case _:
            print("Enter valid input")
