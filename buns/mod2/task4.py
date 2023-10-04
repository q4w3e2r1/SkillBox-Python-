def is_natural_number(n):
    if n > 0 and n % 1 == 0:
        return True
    print("Неверный ввод")
    return False


def convert_to_binary(n):
    binary = ''
    while n > 0:
        binary += str(n % 2)
        n //= 2
    return binary[::-1]


def convert_to_octal(n):
    octal = ''
    while n > 0:
        octal += str(n % 8)
        n //= 8
    return octal[::-1]


def convert_to_hexadecimal(n):
    hexadecimal = ''
    while n > 0:
        remainder = n % 16
        if remainder < 10:
            hexadecimal += str(remainder)
        else:
            hexadecimal += chr(65 + remainder - 10)
        n //= 16
    return hexadecimal[::-1]


number = float(input())
if is_natural_number(number):
    decimal = int(number)

    binary = convert_to_binary(decimal)
    octal = convert_to_octal(decimal)
    hexadecimal = convert_to_hexadecimal(decimal)

    print(f"{binary}, {octal}, {hexadecimal}")
