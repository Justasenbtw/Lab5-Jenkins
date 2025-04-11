from datetime import datetime

def main():
    message = "Мой проект работает!"
    name = "Лисунков Стас"
    current_date = datetime.now().strftime("%d.%m.%Y")
    
    print(f"Сообщение: {message}")
    print(f"Имя: {name}")
    print(f"Дата: {current_date}")

if __name__ == "__main__":
    main()
