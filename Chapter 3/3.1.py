#User input Hour and Rate
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
#Calculate Overtime Pay
if h>40:
    OT = h-40
    OvertimeRate = r*1.5
    OvertimePay = OT*OvertimeRate
    Pay = (r*40) + OvertimePay
    print('Pay')
RegularPay = (h*r)
print('RegularPay')
