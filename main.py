from pick import pick


def is_cbs(list_reference):
    if not list_reference or list_reference.count("(") != list_reference.count(")"):
        return -1
    stack = []
    for i in list_reference:
        if i == "(":
            stack.append("(")
        else:
            try:
                stack.pop()
            except IndexError:
                return 0
    if len(stack) != 0:
        return 0
    return 1


def need_to_move(list_reference: str):
    if not list_reference or list_reference.count("(") != list_reference.count(")"):
        return -1
    sequence = list_reference
    stack = []
    res_arr = []
    last_items = []
    k = 0
    for i in sequence:
        if i == "(":
            stack.append("(")
            res_arr.append("(")
        else:
            try:
                stack.pop()
                res_arr.append(")")
            except IndexError:
                k += 1
                last_items.append(")")
    res_arr.extend(last_items)
    return k, list_reference, "".join(res_arr)


def get_user_input(inp):
    if len(inp.replace(" ", "").replace("(", "").replace(")", "")) != 0:
        print("Строка содержит некорректный символ!")
        return False
    if len(inp.replace(" ", "")) % 2 != 0:
        return False
    return inp.replace(" ", "")


def start_menu():
    title = "Добро пожаловать! Это программа для поиска и выявления ПСП. (Правильной скобочной последовательности)\n" \
            "Заметка:\n" \
            "Скобок дожно быть четное количество, количество \"(\" и \")\" должно совпадать\n" \
            "Выберите команду: "
    options = [
        "Проверить строку на ПСП",
        "Определить, за сколько действий строку можно превратить в ПСП",
    ]
    _, ind = pick(options, title, indicator="=>")
    return ind


def main():
    while True:
        ind = start_menu()
        commands = [
            is_cbs,
            need_to_move
        ]

        res = commands[ind](get_user_input(input("Введите скобочную последовательность: ")))
        if res == -1:
            print("Введенная скобочная последовательность не может "
                  "быть правильной, или преобразованной в правильную")
            print(res)
        match ind:
            case 0:
                if res == 0:
                    print("Введенная последовательность не является ПСП!")
                else:
                    print("Введенная последовательность является ПСП!")
            case 1:
                print("Чтобы превратить эту последовательность в ПСП, потребуется "
                      f"{res[0]} передвижений {res[1]} -> {res[2]}")
        cmd = input("Повторить программу? ([y] / n) ")
        if cmd != "" and cmd != "y":
            break


if __name__ == '__main__':
    main()
