hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
def computepay(h,r):
    if h>40:
        OT = h-40
        OvertimeRate = r*1.5
        OvertimePay = OT*OvertimeRate
        GrossPay = (r*40) + OvertimePay
        return GrossPay
    else:
        RegularPay = (h*r)
        return RegularPay
p = computepay(45,10.5)
print("Pay",p)
