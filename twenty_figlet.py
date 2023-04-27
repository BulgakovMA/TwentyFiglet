from colorama import Fore
import scripts.nw as network


def style_choose():
    while True:
        try:
            style = int(input('Выберите стиль: '))
        except:
            print("Введите число от 0 до 21")
        else:
            if style not in range(0, 22):
                print('Введите число от 0 до 21')
            elif style == 0:
                break
            else:
                network.all_styles(style, styles)


if __name__ == "__main__":
    logo = '''  
oooooooo_oo____oo____oo_ooooooo_ooo____oo_oooooooo_oo____oo_
___oo____oo____oo____oo_oo______oooo___oo____oo____oo____oo_
___oo____oo____oo____oo_oooo____oo_oo__oo____oo_____oo__oo__
___oo_____oo__oooo__oo__oo______oo__oo_oo____oo_______oo____
___oo______oooo__oooo___oo______oo___oooo____oo_______oo____
___oo_______oo____oo____ooooooo_oo____ooo____oo_______oo____
____________________________________________________________
ooooooo_oooo____oooo___oo______ooooooo_oooooooo_
oo_______oo___oo____oo_oo______oo_________oo____
oooo_____oo__oo________oo______oooo_______oo____
oo_______oo__oo____ooo_oo______oo_________oo____
oo_______oo___oo____oo_oo______oo_________oo____
oo______oooo____oooo___ooooooo_ooooooo____oo____
________________________________________________
      '''
    styles = {1: "3-d", 2: "banner4", 3: "brite", 4: "os2", 5: "xhelv",
              6: "mad_nurs", 7: "rozzo", 8: "sbookbi", 9: "xbritei",
              10: "helvbi", 11: "shadow", 12: "xcourb", 13: "ghost_bo",
              14: "lean", 15: "skate_ro", 16: "slant", 17: "charact5",
              18: "gothic", 19: "alligator2", 20: "avatar"}

    print(Fore.GREEN, logo, Fore.RESET, "\n\n\n")
    print(Fore.RED + "0. Exit" + Fore.RESET)
    for key, value in styles.items():
        print(f'{key}. {value}')
    print("21. All items")
    style_choose()
