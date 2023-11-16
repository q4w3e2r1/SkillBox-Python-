from abc import ABC


class Transport(ABC):
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        if not isinstance(value, tuple):
            print("Недопустимый формат coordinates. Допустимый формат coordinates: (pos_x, pos_y)")
        elif len(value) < 2:
            print("Недопустимое значение coordinates")
        elif value[0] < 0 or value[0] > 1000:
            print("Недопустимое значение pos_x")
        elif value[1] < 0 or value[1] > 1000:
            print("Недопустимое значение pos_y")
        else:
            self.__coordinates = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if not isinstance(value, int):
            print(f"Недопустимый формат speed {value}")
        elif value < 0:
            print(f"Недопустимое значение speed {value}")
        else:
            self.__speed = value

    @property
    def brand(self):
        return self.__speed

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            print("Недопустимый формат brand")
        else:
            self.__brand = value

    @property
    def year(self):
        return self.__speed

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            print("Недопустимый формат year")
        elif value < 0 or value > 2023:
            print("Недопустимое значение year")
        else:
            self.__year = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, str):
            print("Недопустимый формат number")
        else:
            self.__number = value

    def __str__(self):
        '''
           Представление всей информации для вывода в методе print()
        '''
        result = f'Сoordinates: {self.__coordinates}\nSpeed: {self.__speed}\nBrand: {self.__brand}\nYear: {self.__year}\nNumber: {self.__number}'
        return result

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        return pos_x <= self.coordinates[0] <= pos_x + length and pos_y <= self.coordinates[1] <= pos_y + width


class Passenger(ABC):
    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if not isinstance(passengers_capacity, int):
            print("Недопустимый формат passengers_capacity")
        elif passengers_capacity < 0:
            print("Недопустимое значение passengers_capacity")
        else:
            self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if not isinstance(passengers_capacity, int):
            print("Недопустимый формат passengers_capacity")
        elif passengers_capacity < 0:
            print("Недопустимое значение passengers_capacity")
        elif self.passengers_capacity < number_of_passengers:
            print("Недостаточно мест для всех пассажиров")
        else:
            self.__number_of_passengers = number_of_passengers


class Cargo(ABC):
    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if not isinstance(passengers_capacity, int):
            print("Недопустимый формат carrying")
        elif passengers_capacity < 0:
            print("Недопустимое значение carrying")
        else:
            self.__carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        Transport.__init__(self, coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            print("Недопустимый формат height")
        elif not (0 < height < 10000):
            print("Недопустимое значение height")
        else:
            self.__height = height


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        self.port = port
        super().__init__(coordinates, speed, brand, year, number)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if not isinstance(port, str):
            print("Недопустимый формат port")
        elif port == '':
            print("Недопустимое значение port")
        else:
            self.__port = port


class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int):
            print("Недопустимый формат passengers_capacity")
        elif not (0 < passengers_capacity < 70):
            print("Недопустимое значение passengers_capacity")
        else:
            self.__passengers_capacity = passengers_capacity

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int):
            print("Недопустимый формат number_of_passengers")
        elif number_of_passengers < self.passengers_capacity:
            print("Недопустимое значение passengers_capacity")
        else:
            self.__number_of_passengers = number_of_passengers


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if isinstance(carrying, int):
            print("Недопустимый формат carrying")
        elif not (0 < carrying < 1500):
            print("Недопустимое значение carrying")
        else:
            self.__carrying = carrying


class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)


# аналогично создать классы для самолета и класс Seaplane(Plane, Ship).

class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):  
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            print("Недопустимый формат height")
        elif height > 10000 or height < 0:
            print("Недопустимый значение height")
        else:
            self.__height = height



x = Seaplane((1, 1), 100, "XxX", 2023, "TI2023", 1, "ddf")


