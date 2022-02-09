class Bank:
    def getroi(self):
        return 10;
class SBI(Bank):
        def getroi(self):
            return 7;
class ICICI(Bank):
        def getroi(self):
            return 8;
b1=Bank()
b2=SBI()
b3=ICICI()
print("Bank rate of interest:",b1.getroi());
print("SBI rate of interest:",b2.getroi());
print("ICICI rate of interest:",b3.getroi());
