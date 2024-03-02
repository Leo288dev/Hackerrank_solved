def add(num):
    list.append(num)
    return list

def ins(num=0, pos=0):
    list.insert(pos, num)
    return list


comm = []
list = []
if __name__ == '__main__':
    N = int(input('qtd'))
    for i in range(N):
        c = input('command:').split()
        comm.append(c)
    for s in range(N):

#----------------------------------------------------------------------------------------------------------------------
        # APPEND insert number into the list
        if comm[s][0] == 'append':
            add(int(comm[s][1]))  # APPEND add convertido em inteiro os numeros na lista
#----------------------------------------------------------------------------------------------------------------------
        # INSERT insert the number into the list at the specified  position
        elif comm[s][0] == 'insert':
            position = int(comm[s][2])
            number = int(comm[s][1])
            ins(number, position)
#----------------------------------------------------------------------------------
        # PRINT print list on screen
        elif comm[s][0] == 'print':
            print(list)
#-----------------------------------------------------------------------------------
        # REMOVE remove the element from the list
        elif comm[s][0] == 'remove':
           rem = int(comm[s][1])
           list.remove(rem)

#---------------------------------------------------------------------------------
        # SORT list
        elif comm[s][0] == 'sort':
            list.sort()


#-----------------------------------------------------------------------------------
        # POP removes the last element from the list
        elif comm[s][0] == 'pop':
            list.pop()

#-----------------------------------------------------------------------------------
        # REVERSE growing list organizartion
        elif comm[s][0] == 'reverse':
            list.reverse()

        else:
            print('END')

