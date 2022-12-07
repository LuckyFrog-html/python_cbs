from pick import pick

g
def get_user_input(inp):
    if len(inp.replace(" ", "").replace("(", "").replace(")", "")) != 0:
        print("Строка содержит некорректный символ!")
        return


def start_menu():
    title = "Добро пожаловать! Это программа для поиска и выявления ПСП" \
            " (Правильной скобочной последовательности)" \
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

        ]

        commands[ind]()

        cmd = input("Повторить программу? ([y] / n) ")
        if cmd != "" and cmd != "y":
            break


if __name__ == '__main__':
    main()
