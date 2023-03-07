def add(a,b):
    return str(float(a)+float(b))

def subtract(a,b):
    return str(float(a)-float(b))

def multiply(a,b):
    return str(float(a)*float(b))

def divide(a,b):
    return str(float(a)/float(b))

def parseData(data):
    print(data)
    return [i for i in data if i != " "]

def power(a,b):
    return str(float(a)**float(b))

def getInput():
    data=parseData(str(input('Enter equation')))
    print(data)
    calculate(data)

def calculate(data):
    while len(data) > 1:
        i=1
        while i < len(data):
            if '/' in data or '*' in data or 'x' in [i.lower() for i in data]:
                if data[i] == '*' or str(data[i]).lower() == 'x':
                    data[i]=multiply(data[i-1],data[i+1])
                    del(data[i+1])
                    del(data[i-1])
                    print(data)
                    break
                if data[i] == '/':
                    data[i]=divide(data[i-1],data[i+1])
                    print(data[i])
                    del(data[i+1])
                    del(data[i-1])
                    print(data)
                    break
            else:
                if data[i] == '+':
                    data[i] = add(data[i-1],data[i+1])
                    del(data[i+1])
                    del(data[i-1])
                    print(data)
                    break
                if data[i] == '-':
                    data[i] = subtract(data[i-1],data[i+1])
                    del(data[i+1])
                    del(data[i-1])
                    print(data)
            i+=1
getInput()