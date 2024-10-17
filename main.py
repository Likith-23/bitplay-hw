def myfunction(number):
    if number & (1 << (number.bit_length() - 1)):
        return True  
    else:
        return False  
def functionable(is_set):
    if is_set:
        print("The highest bit is SET :)")
    else:
        print("The highest bit is NOT SET :-o") 
def check_first_bit(number):
    return number & 1 == 1
number = int(input("ENTER YOUR NUMBER..."))
is_set = myfunction(number)  
functionable(is_set)
if check_first_bit(number):
    print("The first bit (least significant bit) is SET :)")
else:
    print("The first bit (least significant bit) is NOT SET :-o")