from datetime import datetime

def main():
    name = "Lisunkov Stas"
    current_date = datetime.now().strftime("%d.%m.%Y %H:%M")

    print(f"Name: {name}")
    print(f"Date: {current_date}")

if __name__ == "__main__":
    main()
