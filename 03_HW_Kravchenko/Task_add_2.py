# 2.	Определите функцию, которая удаляет весь текст, следующий за любым из переданных маркеров 
# комментариев. Любые пробелы в конце строки также должны быть удалены.
# Пример: 
# Входные данные:
# «apples, pears # and bananas
# grapes
# bananas !apples          » 
# Выходные данные:
# «apples, pears
# grapes
# bananas»
# Функция может вызываться вот так:
# result = function("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

def format_string(text, markers):
    changed_text = text.rstrip()
    changed_text_list = changed_text.split("\n")
    print(changed_text_list)

    for i in range(len(changed_text_list)):
        for marker in markers:
            if marker in changed_text_list[i]: 
                changed_text_list[i] = changed_text_list[i][0 : changed_text_list[i].find(marker)]
        changed_text_list[i] = changed_text_list[i].rstrip()
    print(changed_text_list)        
    return "\n".join(changed_text_list)

original_text = "apples, pears # and bananas\ngrapes\nbananas !apples          " 
markers_list = ["#", "!"]
print(f'Если воспользоваться маркерами {markers_list}, то из текста \n{original_text}\n' 
      f'получится текст\n{format_string(original_text, markers_list)}')

