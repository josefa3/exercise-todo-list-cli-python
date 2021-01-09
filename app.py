import csv

todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    todos.append(title)
    # print (todos)

def print_list():
    global todos
    for c, value in enumerate(todos, 1):
       print(c, value)

def delete_task(number_to_delete):
    todos.pop(int(number_to_delete)-1) # restamos 1 para poder tener el mismo indice de la matriz

def save_todos(): # con esta función se crea el tipo de archivo, no el directorio, y se escribe en él el list
    with open('todos.csv', 'w', newline='\n') as csvfile: # csvfile puede tener cualquier nombre, suelen usar f
        writer = csv.writer(csvfile) 
        writer.writerow(todos)
    
def load_todos(): # esta función permite leer el contenido del archivo creado, se debe hacer un for para recorrer los row
    global todos
    # your code here
    with open('todos.csv', newline='\n') as csvfile: 
        reader = csv.reader(csvfile) 
        list.clear(todos)
        for row in reader:
            print(f'\n'.join(row)) # \n está agregando un salto de línea tras cada iteración de un row.
            # otra manera de hacerlo es usando *. Ejemplo: print(*row) 
            todos.append(row)
            
# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")