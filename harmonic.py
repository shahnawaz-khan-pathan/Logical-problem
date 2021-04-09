Num = int(input('Enter a number'))
if Num<=0:
    print("Please enter number greater than 0")
else:
    Harmonic=0
    for i in range(1,Num+1):
        C=1/i
        Harmonic+=C
    print(Harmonic)