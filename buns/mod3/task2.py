s = int(input())
result = "Неверный ввод" if s < 0 else " ".join([str(bin(s))[2:], str(oct(s))[2:], str(hex(s))[2:]])
print(result)