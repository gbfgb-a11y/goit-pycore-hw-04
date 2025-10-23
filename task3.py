from datetime import datetime; import random; import re;import sys
from pathlib import Path
from colorama import Fore, Style, init
#Завданя 3
init(autoreset=True)

def print_dir_tree(path: Path, prefix=""):
    #Рекурсивно печатает структуру директорий.
    #Папки — синим цветом, файлы — зелёным.
    if not path.exists():
        print(Fore.RED + f"Ошибка: путь {path} не существует.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Ошибка: {path} не является директорией.")
        return
    # Получаем список всех элементов в директории
    entries = list(path.iterdir())
    entries_count = len(entries)
    for i, entry in enumerate(entries):
        connector = "┗── " if i == entries_count - 1 else "┣── "
        if entry.is_dir():
            print(prefix + connector + Fore.BLUE + f"{entry.name}/")
            # Рекурсивно печатаем содержимое
            new_prefix = prefix + ("    " if i == entries_count - 1 else "┃   ")
            print_dir_tree(entry, new_prefix)
        else:
            print(prefix + connector + Fore.GREEN + entry.name)
def main():
    # Получаем путь из аргументов командной строки
    if len(sys.argv) < 2:
        print("Использование: python hw03.py <путь_к_директории>")
        sys.exit(1)
    root_path = Path(sys.argv[1])
    print(Fore.MAGENTA + f" {root_path.name}")
    print_dir_tree(root_path)
if __name__ == "__main__":
    main()
