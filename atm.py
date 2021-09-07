class atm(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def CashWithdrawl(self):
        print("CashWithdrawal")

    def BankEnquiry(self):
        print("BankEnquiry")

Sumit= atm(2000,1378)
 
print(Sumit.pinnumber)