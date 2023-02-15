# Employee Tax Calculator
class Employee:
    def __init__(self, name, weeklyhours, rate, overtimeRate, weeklytaxcredit):
        self.name = name
        self.weeklyhours = weeklyhours
        self.rate = rate
        self.overtimeRate = overtimeRate
        self.weeklytaxcredit = weeklytaxcredit

    def computeWeeklyPay(self, hours):
        if hours <= self.weeklyhours:
            return hours * self.rate
        else:
            regular_pay = self.weeklyhours * self.rate
            overtime_pay = (hours - self.weeklyhours) * self.overtimeRate
            return regular_pay + overtime_pay

    def computeTax(self, grossPay):
        tax = max(0, 0.4 * grossPay - self.weeklytaxcredit)
        return tax
