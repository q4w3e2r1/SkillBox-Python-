def countLetter(fileName: str):
    letter_counts = {}

    with open(fileName, 'r', encoding='utf-8') as file:
        for char in line:
            if char.isalpha():
                letter_counts[char] = letter_counts.get(char, 0) + 1

    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1])

    output_filename = f"statistics_{fileName}"
    with open(output_filename, 'w', encoding='utf-8') as file:
        for item in sorted_counts:
            file.write(f"{item[0]}: {item[1]}\n")

    print(f"Статистика букв записана в файл {output_filename}")


name = input('Введите имя файла:')
filename = f"{name}.txt"
countLetter(filename)