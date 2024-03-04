import sys
from pathlib import Path
from colorama import Fore, Style

def dir_structure(path, indentation=0): # функція приймає шлях і по замовчанню встановлюється нульовий відступ
    directory = Path(path) # приводимо рядок з шляхом до типу Path
    for item in directory.iterdir(): # перебираємо позиції за заданим шляхом
        if item.is_dir():                                          # Якщо дана позиція - папка, то...
            print(Fore.RED + f"{'    ' * indentation}{item.name}") # ... виводити її ім'я червоним кольором і з відступом
            print(Style.RESET_ALL, end='') # скидаємо стиль до стандартного
            dir_structure(item, indentation + 1) # шукаємо в поточній папці вкладені позиції рекурсивно і збільшуємо відступ 
        else:                                     # якщо позиція - файл, то...
            print(Fore.CYAN + f"{'    ' * indentation}{item.name}") # ... виводити його ім'я ціановим (синім) кольором
            print(Style.RESET_ALL, end='') # скидаємо стиль до стандартного

def main():
    if len(sys.argv) != 2: # якщо в командному рядку задано не 2 аргументи після слова python, то...
        print("Usage: python script_name.py directory_path") # виводимо на екран інструкцію, як треба вводити команду
        return
    elif not Path(sys.argv[1]).is_dir(): # якщо за заданим шляхом папки немає, то
        print("Directory doesn't exist.") # ...виводимо повідомлення про це 
        return
    else:
        dir_structure(Path(sys.argv[1])) # якщо заданий шлях - папка, то виконується функція по виводу структури папки

if __name__ == "__main__":
    main()