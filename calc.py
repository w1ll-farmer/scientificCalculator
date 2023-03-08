def add(a,b):
    return str(float(a)+float(b))

def subtract(a,b):
    return str(float(a)-float(b))

def multiply(a,b):
    return str(float(a)*float(b))

def divide(a,b):
    return str(float(a)/float(b))

def parseData(data):
    data= [i for i in data if i != " "]
    i=0
    while i < len(data)-1:
        print(data)
        if data[i].isdigit() and data[i+1].isdigit():
            data[i]+=data[i+1]
            del(data[i+1])
        if data[i] == '-':
            data[i+1] = str(-float(data[i+1]))
            if i ==0:
                del(data[i])
            elif data[i-1].isdigit():
                data[i]='+'
            else:
                del(data[i])
        i+=1
    return data


def power(a,b):
    return str(float(a)**float(b))

def getInput():
    data=parseData(str(input('Enter equation')))
    return calculate(data)

def calculate(data):
    while '(' in data:
        openBracket = None
        closeBracket = None
        for i in range(len(data)):
            if data[i] == '(':
                openBracket = i
            elif data[i] == ')':
                closeBracket = i
                break
        if openBracket is not None and closeBracket is not None:
            sub_data = data[openBracket+1:closeBracket]
            sub_result = calculate(sub_data)
            data = data[:openBracket] + [sub_result] + data[closeBracket+1:]
    
    while len(data) > 1:
        i=1
        while i < len(data):
            if '^' in data:
                if data[i] == '^':
                    data[i] = power(data[i-1],data[i+1])
                    del(data[i+1])
                    del(data[i-1])
                    break
            elif '/' in data or '*' in data or 'x' in [i.lower() for i in data]:
                if data[i] == '*' or str(data[i]).lower() == 'x':
                    data[i]=multiply(data[i-1],data[i+1])
                    del(data[i+1])
                    del(data[i-1])
                    break
                if data[i] == '/':
                    data[i]=divide(data[i-1],data[i+1])
                    del(data[i+1])
                    del(data[i-1])
                    break
            else:
                if data[i] == '+':
                    data[i] = add(data[i-1],data[i+1])
                    del(data[i+1])
                    del(data[i-1])
                    break
                if data[i] == '-':
                    data[i] = subtract(data[i-1],data[i+1])
                    del(data[i+1])
                    del(data[i-1])
            i+=1
    return data[0]
print(getInput())