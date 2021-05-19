#week8practice.py

def last_chars(word,num):
    num2 = [0]
    num1 = ''
    num1 = ''.join(word)
    if(len(word[-1]) <= num):
        num2 = []
    else:
        num2[0] = num1[-num:]
    return num2
