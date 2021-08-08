score = input("Enter Score: ")
s = float(score)
if s > 1.0:
    print('Error Score is not in Range')
if s < 0:
    print('Error Score is not in Range')
if s >= 0.9:
    print('A')
elif s>=0.8:
    print('B')
elif s>=0.7:
    print('C')
elif s>= 0.6:
    print('D')
elif s <0.6:
    print('F')
