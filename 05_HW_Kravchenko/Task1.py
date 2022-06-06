# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. 
# Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

def substring_delete (string_main, string_del, separator):
    result_list = string_main.split(separator)
    result_list = list(filter(lambda word: string_del.lower() not in word.lower(), result_list))
    return separator.join(result_list)

string_ex = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
string_del = "абв"
separator = " "

print(substring_delete(string_ex, string_del, separator))

