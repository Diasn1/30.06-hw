sample = "HELLo WorLd"

def function(word):
    capital_c = 0

    for char in word.replace(" ",""):
        if char.isupper():
            capital_c += 1

    if capital_c > (len(word.replace(" ","")) - capital_c):
        return word.upper()    

    else:
        return word.lower()

print(function(sample))

##############################################################

def searchSubstr(subst, st):
    subst = subst.lower()
    st = st.lower()

    if subst in st:
        return "Есть контакт!"
    else:
        return "Мимо!"

substring = "контакт"
string = "Тут есть контактный номер телефона"
result = searchSubstr(substring, string)
print(result)

####################################################

while True:
    num1 = input("Введите первое целое число: ")
    num2 = input("Введите второе целое число: ")

    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        total = num1 + num2
        print(f"Сумма введенных чисел: {total}")
        break
    else:
        print("Пожалуйста, введите корректные целые числа.")

##############################################################

def changeList(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    else:
        print("Список должен содержать как минимум два элемента")

my_list = [1, 2, 3, 4, 5]
changeList(my_list)
print(my_list)

#####################################################################

def listSort(lst):
    sorted_list = sorted(lst, key=lambda x: abs(x), reverse=True)
    return sorted_list

my_list = [5, -2, 9, -7, 1]
sorted_list = listSort(my_list)
print(sorted_list)

####################################################################

def listToDict(lst):
    my_dict = {item: item for item in lst}
    return my_dict

my_list = ['apple', 'banana', 'cherry']
my_dict = listToDict(my_list)
print(my_dict)

################################################################

my_dict = {'first_key': 'first_value', 'second_key': 'second_value', 'third_key': 'third_value', 'fourth_key': 'fourth_value', 'fifth_key': 'fifth_value'}

first_key_value = my_dict['first_key']
my_dict['first_key'] = my_dict['fifth_key']
my_dict['fifth_key'] = first_key_value

del my_dict['second_key']

my_dict['new_key'] = 'new_value'

print(my_dict)

#################################################################

def dataToSet(data):
    if isinstance(data, str):
        try:
            data = [int(x) for x in data.split()]
        except ValueError:
            return None, 0
    if isinstance(data, list):
        data_set = set(data)
        length = len(data_set)
        return data_set, length
    else:
        return None, 0

data_str = "1 2 3 4 5 5 4 3 2 1"
data_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

result_str, length_str = dataToSet(data_str)
result_list, length_list = dataToSet(data_list)

print("Множество из строки:", result_str)
print("Мощность множества из строки:", length_str)

print("Множество из списка:", result_list)
print("Мощность множества из списка:", length_list)

#######################################################

def superset(set1, set2):
    if set1 == set2:
        print("Множества равны")
    elif set1.issuperset(set2):
        print(f"Объект {set1} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}

superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)
