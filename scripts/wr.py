def save_print(result, style, styles):
    saving = input("Сохранить текст ? [Да/Нет]: ").upper()
    if saving == "ДА":
        with open(f"{list(styles.values())[style - 1]}.txt", "w") \
                as file_output:
            file_output.write(f'print({result})')

