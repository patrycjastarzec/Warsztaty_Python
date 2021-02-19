def are_anagrams(s1, s2, s3):
    #funkcja sorted() zwraca posortowaną alfabetycznie listę znaków każdego łańcucha znaków
    x = sorted(s1)
    y = sorted(s2)
    z = sorted(s3)
    #warunek sprawdzający, czy łańcuchy znaków składają się z identycznych elementów
    if x == y == z:
        return True
    else:
        return False

print(are_anagrams("abc", "bca", "cba"))