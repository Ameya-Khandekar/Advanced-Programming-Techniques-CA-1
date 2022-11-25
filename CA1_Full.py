#Student Number : 10547037 
#Student Name : Ameya Hemantkumar Khandekar

#https://colab.research.google.com/drive/1fClnksSrGlUKn2vtAdK2qxQwlzJL7mtw?authuser=2

class Employee:
    def __init__(self,name, weeklyhours, rate, overtimeRate, weeklytaxcredit):
        self.name = name
        self.weeklyhours= weeklyhours
        self.rate = rate
        self.overtimeRate = overtimeRate
        self.weeklytaxcredit = weeklytaxcredit

    def computeWeeklyPay (self,hours):
        grosspay = 0
    if hours > self.weeklyhours:
      self.weeklytaxcredit = hours - self.weeklyhours
   
    else:
      self.weeklytaxcredit  = self.weeklyhours - hours
    weeklytaxcredit *= self.overtimeRate
    grosspay += (self.rate * self.weeklyhours) + weeklytaxcredit
   
    if grosspay < 0:
      print("Gross Pay amount invalid ")
        return 0 
    
    return grosspay


    def computetax(self,grosspay):
      taxdue = 0
      taxdue = taxdue + (grosspay *0.4) - self.weeklytaxcredit
      if taxdue < 0:
        print("Due Tax cannot be less than 0")
        return 0
      return taxdue


empname = input("Enter your name")
empweeklyhours = input("Enter Weekly Hours")
emprate = input("Enter Rate")
emp_overtimerate = input ("Enter overtime rate")
emp_weeklytaxcredit = input("Enter Tax Credit")
e = Employee(empname,int(empweeklyhours),int(emprate),int(emp_overtimeRate),int(emp-weeklytaxcredit))
object_list.append(e1)
    gross = e1.computeWeeklyPay(39)
    print "Gross Pay of " + Empname + " is " + str(gross)
    tax = e1.computeTax(gross)
    print "Calculated Tax value is " + str(tax)







