import csv
dialogs = [{"hi":"And Hello to you!", "how are you":"Best", "bye":"see you later"}]

with open('dialog.csv', 'w', encoding='utf-8') as file:
    fields = ['hi', 'how are you', 'bye']
    writer = csv.DictWriter(file, fields, delimiter=';')
    writer.writeheader()
    for user in dialogs:
        writer.writerow(user)
file.close()
