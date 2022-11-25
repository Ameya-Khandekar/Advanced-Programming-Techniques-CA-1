class Employee:
    def __init__(self, name, weeklyhours, rate, overtimeRate, weeklytaxcredit):
        self.name = name
        self.weeklyhours = weeklyhours
        self.rate = rate
        self.overtimeRate = overtimeRate
        self.weeklytaxcredit = weeklytaxcredit
   
    def computeWeeklyPay(self, hours):
        grosspay = 0

    if hours > self.weeklyhours:
        self.weeklytaxcredit = hours - self.weeklyhours
    else:
        self.weeklytaxcredit = self.weeklyhours - hours
        weeklytaxcredit *= self.overtimeRate
        grosspay += (self.rate * self.weeklyhours) + weeklytaxcredit
    if grosspay < 0:
        print("Gross Pay amount invalid ")
        
        return 0 
    return grosspay

    def computetax(self,grosspay)
        
        
    
