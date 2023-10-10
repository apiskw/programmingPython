disk = 1.44
pages = 100
str_ = 50
simbols = 25
one_simbol = 4

one_book = one_simbol * simbols * str_ * pages   # одна книга в байтах
disk_in_baits = disk * 1024 * 1024    # диск в байтах
count_of_books = disk_in_baits // one_book      # количество книг на диске

print(f"Количество книг, помещающихся на дискету: {count_of_books:.0f}")
