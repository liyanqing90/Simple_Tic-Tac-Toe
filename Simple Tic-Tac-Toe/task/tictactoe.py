# write your code here


def three_list(a_list: list):
    b_list = [[], []]
    for i in range(3):
        b_list[0].append(a_list[i][i])
        b_list[1].append(a_list[2 - i][i])
        n = [a_list[j][i] for j in range(3)]
        b_list.extend([a_list[i], n])
    return b_list


def win_list(key: str, a_list: list):
    for i in three_list(a_list):
        if i.count(key) == 3:
            return True
    else:
        return False


def check_state(a_list: list):
    x_count = a_list.count("X")
    o_count = a_list.count("O")
    if abs(x_count - o_count) > 1 or all([win_list("X", a_list), win_list("O", a_list)]):
        print("Impossible")
    else:
        if win_list("X", a_list):
            print("X wins")
            return True
        elif win_list("O", a_list):
            print("O wins")
            return True
        else:
            for i in a_list:
                if i.count(" ") > 0:
                    print("Game not finished")
                    break
            else:
                print("Draw")
                return True


def print_info(a_list: list):
    print("---------")
    print("| " + " ".join(a_list[0]) + " |")
    print("| " + " ".join(a_list[1]) + " |")
    print("| " + " ".join(a_list[2]) + " |")
    print("---------")


a_list = list(9 * " ")
a_list = [a_list[:3], a_list[3:-3], a_list[-3:]]
print_info(a_list)
first = True
while True:
    print("Enter the coordinates: ")
    m, n = input().split()
    if not all([m.isdigit(), n.isdigit()]):
        print("You should enter numbers!")
        continue
    else:
        m, n = int(m) - 1, int(n) - 1
        if all([m < 0, m > 2]) or any([n < 0, m > 2]):
            print("Coordinates should be from 1 to 3!")
            continue
        elif a_list[m][n] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            if first:
                first = False
                a_list[m][n] = "X"
            else:
                first = True
                a_list[m][n] = "O"
            print_info(a_list)
            if check_state(a_list):
                break
