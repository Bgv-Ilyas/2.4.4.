#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import argparse
import logging
from pathlib import Path

# Настройка логгирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(filename):
    file_path = Path.home() / filename
    try:
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                logging.info(f"Данные успешно загружены из {file_path}")
                return data
        logging.warning(f"Файл {file_path} не найден. Возвращается пустой список.")
        return []
    except Exception as e:
        logging.error(f"Ошибка при загрузке данных из {file_path}: {e}")
        return []

def save_data(destinations, filename):
    file_path = Path.home() / filename
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(destinations, file, ensure_ascii=False, indent=4)
            logging.info(f"Данные успешно сохранены в {file_path}")
    except Exception as e:
        logging.error(f"Ошибка при сохранении данных в {file_path}: {e}")

def add_flight(destinations):
    try:
        destination = input("Введите пункт назначения: ")
        flight_number = input("Введите номер рейса: ")
        plane_type = input("Введите тип самолета: ")

        flight_info = {
            'название пункта назначения': destination,
            'номер рейса': flight_number,
            'тип самолета': plane_type
        }

        destinations.append(flight_info)
        destinations.sort(key=lambda x: x['номер рейса'])
        print("Информация о рейсе добавлена.")
        logging.info(f"Добавлен новый рейс: {flight_info}")
    except Exception as e:
        logging.error(f"Ошибка при добавлении рейса: {e}")

def display_flights_by_destination(destinations, search_destination):
    try:
        matching_flights = [
            (flight['номер рейса'], flight['тип самолета'])
            for flight in destinations
            if flight['название пункта назначения'] == search_destination
        ]

        if matching_flights:
            print(f"Рейсы в пункт назначения '{search_destination}':")
            for flight_number, plane_type in matching_flights:
                print(f"Номер рейса: {flight_number}, Тип самолета: {plane_type}")
            logging.info(f"Найдены рейсы в пункт назначения '{search_destination}': {matching_flights}")
        else:
            print(f"Рейсов в пункт назначения '{search_destination}' не найдено.")
            logging.warning(f"Рейсов в пункт назначения '{search_destination}' не найдено.")
    except Exception as e:
        logging.error(f"Ошибка при поиске рейсов в пункт назначения '{search_destination}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Flight Management System")
    parser.add_argument("-a", "--add-flight", action="store_true", help="Add a new flight")
    parser.add_argument("-d", "--destination", help="Destination to search flights for")
    args = parser.parse_args()

    filename = 'destinations.json'
    destinations_list = load_data(filename)

    if args.add_flight:
        add_flight(destinations_list)
    elif args.destination:
        display_flights_by_destination(destinations_list, args.destination)
    else:
        while True:
            print("\n1. Добавить рейс")
            print("2. Вывести рейсы по пункту назначения")
            print("3. Выйти")
            choice = input("Выберите действие (1/2/3): ")

            if choice == '1':
                add_flight(destinations_list)
            elif choice == '2':
                search_destination = input("Введите пункт назначения для поиска: ")
                display_flights_by_destination(destinations_list, search_destination)
            elif choice == '3':
                save_data(destinations_list, filename)
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")
                logging.warning("Некорректный ввод в меню выбора действия.")

if __name__ == "__main__":
    main()
