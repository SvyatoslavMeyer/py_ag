import csv

def fulfill_doc():
    with open('phonebook.csv', 'a') as file:
        column_names = ['name', 'surname', 'phone_number']
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        phone_number = input("Введите номер телефона: ")
        writer = csv.DictWriter(file, column_names)
        writer.writerow({'name' : name.lower(), 'surname' : surname.lower(), 'phone_number' : phone_number})

def find_info():
    data = open('phonebook.csv', 'r')
    word = input("Введите что хотите найти: ")
    for line in data:
        if word.lower() in line:
            print(line)
    data.close()
 
def delete_from_pb():
    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    word = input("Введите что хотите удалить: ")
    for line in rows:
        if word.lower() in line:
            rows.remove(line)
    with open('phonebook.csv', 'w') as file:   
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Удалено!")
    
def change_info():
    with open('phonebook.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            old_word = input("Введите что хотите изменить: ")
            new_word = input(f"Введите на что хотите изменить {old_word}: ")
            for line in rows:
                if old_word in line:
                    index = line.index(old_word)
                    line[index] = new_word
    with open('phonebook.csv', 'w', newline='') as file:
        csv.writer = csv.writer(file)
        for line in rows:
            csv.writer.writerow(line)
    print("Перезаписано!")