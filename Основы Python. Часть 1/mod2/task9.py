s = input().replace(' ', '')
vowels_count = 0
consonant_count = 0
vowels = 'аеёиоуыэюя'

for i in range(len(s)):
    if s[i] in vowels:
        vowels_count += 1
    else:
        consonant_count += 1
print(vowels_count, consonant_count)