import random
from time import sleep

def init_table():
    inf_2 = list()
    inf_1 = list()
    for i in range(0, 3):
        for j in range(0, 3):
            inf_1.append(0)
        inf_2.append(inf_1[:])
        inf_1 = list()
    return inf_2
## poderia melhorar essa função aqui. não precisaria ter um argumento/parametro.
# 1 é o x - ADVERSARIO
# 2 é o O - COMPUTADOR


def numer_tocoord(n):
    coord = list()
    if n == 1:
        coord.append(0)
        coord.append(0)
    elif n == 2:
        coord.append(0)
        coord.append(1)
    elif n == 3:
        coord.append(0)
        coord.append(2)
    elif n == 4:
        coord.append(1)
        coord.append(0)
    elif n == 5:
        coord.append(1)
        coord.append(1)
    elif n == 6:
        coord.append(1)
        coord.append(2)
    elif n == 7:
        coord.append(2)
        coord.append(0)
    elif n == 8:
        coord.append(2)
        coord.append(1)
    else:
        coord.append(2)
        coord.append(2)
    return coord


def coord_tonumber(x, y):
    if x == 0:
        if y == 0:
            return "1"
        elif y == 1:
            return "2"
        else:
            return "3"
    elif x == 1:
        if y == 0:
            return "4"
        elif y == 1:
            return "5"
        else:
            return "6"
    else:
        if y == 0:
            return "7"
        elif y == 1:
            return "8"
        else:
            return "9"

def show_table(inf):
    print()
    for i in range(0, 3):
        for j in range(0, 3):
            if j != 2:
                if inf[i][j] == 0:
                    print(f" {coord_tonumber(i, j)} ", end='')
                elif inf[i][j] == 1:
                    print(" x ", end='')
                elif inf[i][j] == 2:
                    print(" o ", end='')
                print("|", end='')
            else:
                if inf[i][j] == 0:
                    print(f" {coord_tonumber(i, j)} ")
                elif inf[i][j] == 1:
                    print(" x ")
                elif inf[i][j] == 2:
                    print(" o ")

        if i < 2:
            print("__________")


def check_lines(t):
    cont = 0
    zero_position = 0
    coord = list()
    for i in range(0, 3):
        for j in range(0, 3):
            if t[i][j] == 1:
                cont += 1
            elif t[i][j] == 2:
                cont -= 1
            else:
                zero_position = j
        if cont == 2: ## retornou a posição em que é para o computador jogar.
            coord.append(True)
            coord.append(i)
            coord.append(zero_position)
            return coord
        elif cont == 3: ##jogo acabou. adversário venceu.
            coord.append(True)
            coord.append(-1)
            coord.append(-1)
        cont = 0
        zero_position = 0
        coord = list()
    casainvalida = True
    coord.append(False)
    while casainvalida:
        i = random.randrange(0, 3)
        j = random.randrange(0, 3)
        if t[i][j] == 0:
            coord.append(i)
            coord.append(j)
            casainvalida = False

    return coord


def check_columns(t):
    cont = 0
    zero_position = 0
    coord = list()
    for i in range(0, 3):
        for j in range(0, 3):
            if t[j][i] == 1:
                cont += 1
            elif t[j][i] == 2:
                cont -= 1
            else:
                zero_position = j
        if cont == 2:  ## retornou a posição em que é para o computador jogar.
            coord.append(True)
            coord.append(zero_position)
            coord.append(i)
            return coord
        elif cont == 3: ##jogo acabou. adversário venceu.
            coord.append(True)
            coord.append(-1)
            coord.append(-1)
            return coord
        cont = 0
        zero_position = 0
        coord = list()
    casainvalida = True
    coord.append(False)
    while casainvalida:
        i = random.randrange(0, 3)
        j = random.randrange(0, 3)
        if t[i][j] == 0:
            coord.append(i)
            coord.append(j)
            casainvalida = False
    ## aqui é "tanto faz"
    return coord


def check_maindiag(t):
    cont = 0
    zero_position = 0
    coord = list()
    for i in range(0, 3):
        if t[i][i] == 1:
            cont += 1
        elif t[i][i] == 2:
            cont -= 1
        else:
            zero_position = i
    if cont == 2:
        coord.append(True)
        coord.append(zero_position)
        coord.append(zero_position)
        return coord
    elif cont == 3:
        coord.append(-1)
        coord.append(-1)
        return coord
    else:
        coord.append(False)
        coord.append(zero_position)
        coord.append(zero_position)
        return coord


def check_secdiag(t):
    cont = 0
    coord = list()
    zero = list()
    zero.append(False)
    zero.append(False)
    zero.append(False)
    if t[0][2] == 1:
        cont += 1
    elif t[0][2] == 2:
        cont -= 1
    else:
        zero[0] = True
    if t[1][1] == 1:
        cont += 1
    elif t[1][1] == 2:
        cont -= 1
    else:
        zero[1] = True
    if t[2][0] == 1:
        cont += 1
    elif t[2][0] == 2:
        cont -= 1
    else:
        zero[2] = True
    if cont == 3:
        coord.append(True)
        coord.append(-1)
        coord.append(-1)
        return coord
    else:
        if cont == 2:
            coord.append(True)
        else:
            coord.append(False)
        if zero[0]:
            coord.append(0)
            coord.append(2)
            return coord
        elif zero[1]:
            coord.append(1)
            coord.append(1)
            return coord
        else:
            coord.append(2)
            coord.append(0)
            return coord

def check_win(t, n):
    cont = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if t[i][j] == n:
                cont += 1
        if cont == 3:
            return True
        else:
            cont = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if t[j][i] == n:
                cont += 1
        if cont == 3:
            return True
        else:
            cont = 0
    if t[0][0] == n and t[1][1] == n and t[2][2] == n:
        return True
    elif t[0][2] == n and t[1][1] == n and t[2][0] == n:
        return True
    return False


def check_attack(t):
    cont = 0
    coord = list()
    positioni = 0
    positionj = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if t[i][j] == 2:
                cont += 1
            elif t[i][j] == 1:
                cont -= 1
            else:
                positioni = i
                positionj = j
        if cont == 2:
            coord.append(True)
            coord.append(positioni)
            coord.append(positionj)
            return coord
        else:
            cont = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if t[j][i] == 2:
                cont += 1
            elif t[j][i] == 1:
                cont -= 1
            else:
                positioni = j
                positionj = i
        if cont == 2:
            coord.append(True)
            coord.append(positioni)
            coord.append(positionj)
            return coord
        else:
            cont = 0
    for i in range(0, 3):
        if t[i][i] == 2:
            cont += 1
        elif t[i][i] == 1:
            cont -= 1
        else:
            positioni = i
    if cont == 2:
        coord.append(True)
        coord.append(positioni)
        coord.append(positioni)
        return coord
    else:
        cont = 0
        positioni = positionj = 0
    zero02 = zero11 = zero20 = False
    if t[0][2] == 2:
        cont += 1
    elif t[0][2] == 1:
        cont -= 1
    else:
        zero02 = True
    if t[1][1] == 2:
        cont += 1
    elif t[1][1] == 1:
        cont -= 1
    else:
        zero11 = True
    if t[2][0] == 2:
        cont += 1
    elif t[2][0] == 1:
        cont -= 1
    else:
        zero20 = True
    if cont == 2:
        coord.append(True)
        if zero02:
            coord.append(0)
            coord.append(2)
        elif zero11:
            coord.append(1)
            coord.append(1)
        else:
            coord.append(2)
            coord.append(0)
    else:
        coord.append(False)
    return coord


def play(t):
    if check_attack(t)[0]:
        return check_attack(t)
    else:
        if check_lines(t)[0]:
            return check_lines(t)
        elif check_columns(t)[0]:
            return check_columns(t)
        elif check_maindiag(t)[0]:
            return check_maindiag(t)
        elif check_secdiag(t)[0]:
            return check_secdiag(t)
        else:
            choice = random.randrange(0, 4)
            if choice == 0:
                return check_lines(t)
            elif choice == 1:
                return check_columns(t)
            elif choice == 2:
                return check_maindiag(t)
            elif choice == 3:
                return check_secdiag(t)

table = []
table = init_table()
andamento = True
show_table(table)
qtdjogadas = 0
while andamento:
    ninvalido = True
    while ninvalido:
        try:
            n = int(input("Digite o número da casa em que você quer jogar: "))
            for i in range(1, 10):
                if n == i:
                    ninvalido = False
            if not ninvalido:
                c = numer_tocoord(n)
                if table[c[0]][c[1]] != 0:
                    print("Ops! A casa em que você quer jogar já está ocupada. Tente novamente!")
                    ninvalido = True
                else:
                    c = numer_tocoord(n)
                    table[c[0]][c[1]] = 1
                    show_table(table)
                    qtdjogadas += 1
                    print(flush=True, end="")
                    sleep(1)
            else:
                print("Você só pode escolher um número de 1 a 9. Tente novamente!")
        except ValueError:
            print("Ocorreu um erro. Tente novamente!")
    if check_win(table, 1):
        print("VOCÊ GANHOU!")
        andamento = False
    else:
        if qtdjogadas == 9:
            print("IH... DEU VELHA. PARECE QUE NENHUM DE NÓS GANHOU.")
            andamento = False
            print(flush=True, end="")
            sleep(5)
        else:
            print()
            print("MUITO BEM. AGORA É A MINHA VEZ...")
            print(flush=True, end="")
            sleep(2)
            jogada = play(table)
            table[jogada[1]][jogada[2]] = 2
            show_table(table)
            qtdjogadas += 1
            print(flush=True, end="")
            sleep(1)
            if check_win(table, 2):
                print("VOCÊ PERDEU!")
                andamento = False

# o segredo pra ganhar esse jogo é jogar em tres das extremidades.
# fazer uma atualização pra se alguém começar por alguma das extremidades, tentar completar as outras.