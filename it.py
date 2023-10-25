import sqlite3

# Создание таблицы "employees" в БД
def create_table():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 fio TEXT,
                 phone TEXT,
                 email TEXT,
                 salary REAL)''')
    conn.commit()
    conn.close()

# Добавление нового сотрудника
def add_employee():
    fio = input("Введите ФИО сотрудника: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите адрес электронной почты: ")
    salary = float(input("Введите заработную плату: "))

    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees (fio, phone, email, salary) VALUES (?, ?, ?, ?)", (fio, phone, email, salary))
    conn.commit()
    conn.close()
    print("Сотрудник успешно добавлен")

# Изменение текущего сотрудника
def edit_employee():
    employee_id = int(input("Введите ID сотрудника для изменения: "))

    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    c.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
    employee = c.fetchone()

    if employee is None:
        print("Сотрудника с таким ID не существует")
    else:
        fio = input("Введите новое ФИО сотрудника: ")
        phone = input("Введите новый номер телефона: ")
        email = input("Введите новый адрес электронной почты: ")
        salary = float(input("Введите новую заработную плату: "))

        c.execute("UPDATE employees SET fio = ?, phone = ?, email = ?, salary = ? WHERE id = ?",
                  (fio, phone, email, salary, employee_id))
        conn.commit()
        print("Сотрудник успешно изменен")

    conn.close()

# Удаление сотрудника
def delete_employee():
    employee_id = int(input("Введите ID сотрудника для удаления: "))

    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    c.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
    employee = c.fetchone()

    if employee is None:
        print("Сотрудника с таким ID не существует")
    else:
        c.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
        conn.commit()
        print("Сотрудник успешно удален")

    conn.close()

# Поиск по ФИО
def search_employee():
    fio = input("Введите ФИО сотрудника: ")

    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    c.execute("SELECT * FROM employees WHERE fio = ?", (fio,))
    employee = c.fetchone()

    if employee is None:
        print("Сотрудник с таким ФИО не найден")
    else:
        print("ID: ", employee[0])
        print("ФИО: ", employee[1])
        print("Номер телефона: ", employee[2])
        print("Адрес электронной почты: ", employee[3])
        print("Заработная плата: ", employee[4])

    conn.close()

def main():
    create_table()

    while True:
        print("\n1. Добавить сотрудника")
        print("2. Изменить сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск по ФИО")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            edit_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            search_employee()
        elif choice == "0":
            break
        else:
            print("Некорректный ввод, попробуйте еще раз")

if __name__ == "__main__":
    main()
