def input_flights():
    """Функция ввода данных о рейсах"""
    flights = []
    count = int(input("Сколько рейсов ввести? "))
    
    for i in range(count):
        print(f"\nРейс {i+1}:")
        destination = input("Пункт назначения: ")
        flight_number = input("Номер рейса: ")
        aircraft_type = input("Тип самолёта: ")
        flights.append({"destination": destination, "flight_number": flight_number, "aircraft_type": aircraft_type})
    
    return flights

def sort_by_flight_number(flights):
    """Функция сортировки рейсов по номеру"""
    return sorted(flights, key=lambda x: x["flight_number"])
  
def search_by_destination(flights, destination):
    """Функция поиска рейсов по пункту назначения"""
    found = []
    for flight in flights:
        if flight["destination"] == destination:
            found.append(flight)
    return found

def print_results(found_flights):
    """Функция вывода результатов поиска"""
    if not found_flights:
        print("Рейсов в этот пункт назначения нет")
    else:
        print("\nНайденные рейсы:")
        for flight in found_flights:
            print(f"Рейс {flight['flight_number']}, самолёт {flight['aircraft_type']}")

def main():
    """Главная функция"""

    flights = input_flights()
    
    flights = sort_by_flight_number(flights)

    print("\nОтсортированный список рейсов:")
    for flight in flights:
        print(f"{flight['flight_number']} -> {flight['destination']} ({flight['aircraft_type']})")
    
    search_destination = input("\nВведите пункт назначения для поиска: ")
    found_flights = search_by_destination(flights, search_destination)
    
    print_results(found_flights)

if __name__ == "__main__":
    main()
