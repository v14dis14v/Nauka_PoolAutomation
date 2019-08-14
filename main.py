import sys
from PyQt5 import QtWidgets
import form
import mysql.connector

# подключение БД
# Здесь вместо "*" нужно внести свои данные
connect = mysql.connector.connect(user="*****", password="*******", host="127.0.0.1", database="******")
cursor = connect.cursor(buffered=True)

# создание таблицы
flag = True
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
for iter in tables:
    for j in iter:
        if j == "customers":
            flag = False
if flag:
    cursor.execute("CREATE TABLE customers ("
        "`full_name` VARCHAR(100) NOT NULL,"
        "`id` INT(50) NOT NULL,"
        "`date of birth` DATE NOT NULL,"
        "`passport id` VARCHAR(11) NOT NULL,"
        "`medical certificate` TINYINT(1),"
        "`selected time` VARCHAR(250) NOT NULL,"
        "`subscription` VARCHAR(50)  NOT NULL,"
        "`payment method` VARCHAR(50)  NOT NULL,"
        "`date of registration` DATETIME"
        ")ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    )

add_value = ("INSERT INTO customers VALUES (%(0)s, %(1)s, %(2)s, %(3)s, %(4)s, %(5)s, %(6)s, %(7)s, NOW())")

# вытаскиваем данные из БД
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()


class ExampleApp(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # количество строк и столбцов
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(50)

        # подгонка размера ширины колонок в таблице
        for i in range(9):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            

        # привязка кнопки к вызову функции очистить
        self.button2.clicked.connect(self.clear)

        # привязка кнопки к функции записать все данные в ДБ
        self.button1.clicked.connect(self.save_data)
        
        self.buttonSearch.clicked.connect(self.search)

        self.buttonUpdate.clicked.connect(self.update_table)

        self.buttonClear.clicked.connect(self.reset)

        self.tableWidget.setHorizontalHeaderLabels(
            ('ФИО', 'ID', 'Дата рождения', 'Паспорт',
            'Справка от врача', 'Выбранное время',
            'Абонемент', 'Метод оплаты', 'Дата регистрации')
        )
        
        self.update_rows(rows)
    
    def update_rows(self, rows):
        row = 0
        for dict in rows:
            col = 0
            for item in dict:
                cellinfo = QtWidgets.QTableWidgetItem(str(item))
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
    
    def update_table(self):
        connect.commit()
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            ('ФИО', 'ID', 'Дата рождения', 'Паспорт',
            'Справка от врача', 'Выбранное время', 
            'Абонемент', 'Метод оплаты', 'Дата регистрации')
        )
        cursor.execute("SELECT * FROM customers")
        new_rows = cursor.fetchall()
        self.update_rows(new_rows)
        

    def clear(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            ('ФИО', 'ID', 'Дата рождения', 'Паспорт',
            'Справка от врача', 'Выбранное время', 
            'Абонемент', 'Метод оплаты', 'Дата регистрации')
        )
    
    def search(self):
        self.clear()
        cursor.execute("SELECT * FROM customers WHERE full_name = '" + str(self.lineEdit.text()) + "'")
        result = cursor.fetchall()
        self.update()
        self.update_rows(result)
                

    def reset(self):
        self.lineEdit.clear()
        self.update()
        self.update_table()

    def save_data(self):
        # удаляем всё из БД
        cursor.execute("DELETE FROM customers")

        # записываем всё
        cash = {}
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                try:
                    cash[str(j)] = self.tableWidget.item(i, j).text()
                    if j == 7:
                        cursor.execute(add_value, cash)
                except:
                    connect.commit()   
                    break

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()