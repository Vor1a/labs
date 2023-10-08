# TODO Найдите количество книг, которое можно разместить на дискете
limit = 1.44*1024**2
count_symbols = 25
count_lines = 50
count_pages = 100
symbol_weight = 4
book_weight = count_symbols*count_lines*count_pages*symbol_weight
books = round(limit/book_weight)

print("Количество книг, помещающихся на дискету:", books)
