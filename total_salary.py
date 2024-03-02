from pathlib import Path

def total_salary(path) -> tuple:
    try:
        with open(path, 'r', encoding="utf-8") as file: # відкриваємо файл в режимі читання, кодування utf-8
            colegues = file.readlines() # розбиваємо на окремі рядки перелік робітників і поміщаємо у список 
        total = 0
        for colegue in colegues:
            _, salary = colegue.split(',') # кожен рядок розбиваємо по символу "," і зарплату записуємо у змінну, ігноруючи ліву частину
            total += int(salary) # вираховуємо загальну суму ЗП
        average = total / len(colegues) # вираховуємо середню ЗП
        return total, round(average, 2) # повертаємо загальну ЗП та середню з округленням до 2-х знаків після коми
    except FileNotFoundError:
        return 'File not found or corrupted'

# print(total_salary('salary_file.txt'))