def even(string):
    string += ' '
    A=[]
    temp_str = ''

    for i in range(len(string)):

        if string[i] != ' ':
            temp_str += string[i]
        else:
            A.append(temp_str)
            temp_str = ''
        # print(temp_str)

    for i in range(len(A)):
        A[i] = int(A[i])

    result = ''
    for i in range(len(A)):
        if i%2==0:
           result+= str(A[i]) + ' '
    return result

def blabla():
    return 'HELLO GIT'

def blabla_2():
    return 'HELLO GIT'\


