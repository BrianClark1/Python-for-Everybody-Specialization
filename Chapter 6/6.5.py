text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find('0')
dog = text[atpos:atpos+6]
fdog = float(dog)
print(dog)
