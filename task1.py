from datetime import datetime; import random; import re;import sys
from pathlib import Path
from colorama import Fore, Style, init
#Завдання 1
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                #прибираємо пробіли та символи переносу рядка
                line = line.strip()
                if not line:
                    continue  #пропускаємо порожні рядки
                #розділяємо на ім'я та зарплату
                parts = line.split(',')
                if len(parts) != 2:
                    continue  #пропускаємо некоректні рядки
                name, salary_str = parts
                try:
                    salary = int(salary_str)
                except ValueError:
                    continue  #якщо зарплата не число
                total += salary
                count += 1
            if count == 0:
                return 0, 0  #якщо у файлі немає валідних рядків
            average = total / count
            return total, average
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0
