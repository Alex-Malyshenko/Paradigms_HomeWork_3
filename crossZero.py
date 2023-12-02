
def inputSymbol(listInput: list, znak):
    flag = True
    while flag == True:
        print(f"Введите координаты пустой клетки для хода игрока {znak}: ")
        x = int(input())
        y = int(input())
        if listInput[x][y] == " " :
            listInput[x][y] = znak
            flag = False
    return listInput

def verify(table:list) -> bool:
    if table[0][0] == table[0][1] == table[0][2] == "x" or table[1][0] == table[1][1] == table[1][2] == "x"  or \
            table[2][0] == table[2][1] == table[2][2] == "x" or table[0][0] == table[1][0] == table[2][0] == "x" or \
            table[0][1] == table[1][1] == table[2][1] == "x" or table[0][2] == table[1][2] == table[2][2] == "x" or \
            table[0][0] == table[1][1] == table[2][2] == "x" or table[0][2] == table[1][1] == table[0][2] == "x" :
        print("Победа Х!!!")
        return True
    elif table[0][0] == table[0][1] == table[0][2] == "o" or table[1][0] == table[1][1] == table[1][2] == "o" or \
                table[2][0] == table[2][1] == table[2][2] == "o" or table[0][0] == table[1][0] == table[2][0] == "o" or \
                table[0][1] == table[1][1] == table[2][1] == "o" or table[0][2] == table[1][2] == table[2][2] == "o" or \
                table[0][0] == table[1][1] == table[2][2] == "o" or table[0][2] == table[1][1] == table[0][2] == "o":
        print("Победа O!!!")
        return True
    else:
        return  False

def printTable(table):
    for i in range(3):
        for j in range(3):
            if table[i][j] == " ": print("_" + " ", end = "")
            else:
                print(table[i][j] + " ", end = "")
        print()

if __name__ == '__main__':
    listPremier = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    count = 0
    flag = False
    sym = "x"
    while count <= 9 and flag == False :
        inputSymbol(listPremier, sym)
        printTable(listPremier)
        if count % 2 == 0 : sym = "o"
        else: sym = "x"
        if count >= 3:
            flag = verify(listPremier)
        count+= 1
