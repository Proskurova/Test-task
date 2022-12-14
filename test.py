# ******* Тестовое задание на Junior Python Developer ********
#
#
# В этом файле находятся строки с переводом английских слов на русские в формате
# Astur-Leonese ; Asturian ; Asturian-Leonese ; Astur	астурийский ; астурлеонский
#
# Это значит, что каждое из английских слов (Astur-Leonese ; Asturian ; Asturian-Leonese ; Astur) может переводиться
# как любое русское (астурийский ; астурлеонский)
#
# Также встречаются простые варианты где в строке 1 английское и русское слово
# Abidjan	Абиджан
#
# Английские слова отделены от русских переводов символом табуляции
#
# Надо распарсить этот файл и на базе него сделать 2 файла - English.txt и Russian txt, где каждой строке на английском
# будет соответствовать строка перевода на русском в другом файле во всех возможных вариантах.
#
# Пример текста, который должен получиться в файлах, после работы вашего кода:
#
# English.txt				Russian.txt
#
# Astur-Leonese				астурийский
# Astur-Leonese				астурлеонский
# Asturian				    астурийский
# Asturian				    астурлеонский
# Asturian-Leonese			астурийский
# Asturian-Leonese			астурлеонский
# ....						....
#
# Код который вы напишите присылайте на alexeir@lingvanex.com
#
#
with open("PythonTest.txt", encoding="utf-8") as f:
    text = f.read().split('\n')
words = [j for i in text for j in i.split("\t")]
en = []
ru = []
for word in words:
    if words.index(word) % 2 == 0 or words.index(word) == 0:
        en.append(word)
    else:
        ru.append(word.split(" ; "))


def open_file_en(result):
    with open("English.txt", "a", encoding="utf-8") as f:
        f.write(result)


def open_file_ru(result):
    with open("Russian.txt", "a", encoding="utf-8") as f:
        f.write(result)


for key, value in zip(en, ru):
    if len(value) == 1 and key.count(";") == 0:
        open_file_en(str(key) + "\n")
        open_file_ru(value[0] + "\n")
    elif len(value) == 1 and key.count(";") >= 1:
        key1 = key.split(" ; ")
        for i in range(0, len(key1)):
            open_file_en(str(key1[i])+"\n")
            open_file_ru(value[0] + "\n")
    elif len(value) > 1 and key.count(";") == 0:
        open_file_en((key+"\n")*len(value))
        open_file_ru(str("\n".join(value)+"\n"))
    else:
        key1 = key.split(" ; ")
        for i in range(0, len(key1)):
            open_file_en((str(key1[i])+"\n")*len(value))
            open_file_ru(str("\n".join(value)+"\n"))

