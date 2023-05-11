string_input = input().lower()                                                                                          # получаем данные

# замениваем лишние символы для подсчета
words = string_input.replace(":", "").replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace("—", "").replace("-", "").replace("  ", " ")
words = words.split()                                                                                                   # разбиваем
word_count = {}


for el in words:
    word_count[el] = word_count.get(el, 0) + 1
print(word_count)












