import requests
from colorama import Fore
import scripts.wr as writing

colors = {1: (Fore.BLACK, "BLACK"), 2: (Fore.RED, "RED"),
          3: (Fore.GREEN, "GREEN"), 4: (Fore.YELLOW, "YELLOW"),
          5: (Fore.BLUE, "BLUE"), 6: (Fore.MAGENTA, "MAGENTA"),
          7: (Fore.CYAN, "CYAN")}


def all_styles(style, styles):
    text = input("Введите текст [eng]: ")
    if style == 21:
        with open("all_design.txt", "w") as file_output:
            for i in range(0, 21):
                url = f"https://figlet-api.onrender.com/?text={text}&font=" \
                      f"{list(styles.values())[i - 1]}"
                res = requests.get(url, allow_redirects=False)
                file_output.write(res.json()["ascii"] + "\n")
        print("Done!")
    else:
        one_style(style, text, styles)


def one_style(style, text, styles):
    url = f"https://figlet-api.onrender.com/?text={text}&font=" \
          f"{list(styles.values())[style - 1]}"
    res = requests.get(url, allow_redirects=False)
    questions = input("Покрасить текст ? [Да/Нет]: ").upper()
    if questions == "ДА":
        for key, value in colors.items():
            print(f'{value[0]}{key}. {value[1]}{Fore.RESET}')
        try:
            answer = int(input("Выберите цвет: "))
        except:
            print("Введите число в диапозоне от 1 до 7")
        else:
            if answer not in range(1, 8):
                print("Введите число в диапозоне от 1 до 7")
            else:
                result = (
                            list(colors.values())[answer - 1][0] + res.json()[
                        "ascii"] + Fore.RESET)
                print(result)
                writing.save_print(result, style, styles)
    elif questions == "НЕТ":
        result = (res.json()["ascii"])
        print(result)
        writing.save_print(result, style, styles)
    else:
        print('Введите "Да" или "Нет"')
