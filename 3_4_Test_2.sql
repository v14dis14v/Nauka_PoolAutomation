# Пример создания БД в MySQL

# Выбор существующей БД
USE  nauka

# Создание таблицы в данной БД
# id будет генерироваться самостоятельно при добавлении нового пользователя
CREATE TABLE customers (
`full_name` VARCHAR(100) NOT NULL, 
`id` INT(50) NOT NULL, 
`date of birth` DATE NOT NULL, 
`passport id` VARCHAR(11) NOT NULL, 
`medical certificate` TINYINT(1), 
`selected time` VARCHAR(250) NOT NULL, 
`subscription` VARCHAR(50)  NOT NULL, 
`payment method` VARCHAR(50)  NOT NULL, 
`date of registration` DATETIME NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

# Внесение даанных в таблицу
INSERT INTO customers VALUES (
    "Шереметьев Василий Петрович",
    "12345678", 
    "1990-10-11", 
    "3459 501365", 
    1, 
    "2019-09-10 10:30:00",
    "Разовое посещение", 
    "Единовременная оплата абонемента", 
    NOW()
    );

INSERT INTO customers VALUES (
    "Крузенштерн Иван Фёдорович",
    "09238457", 
    "1994-6-3", 
    "3450 109247", 
    1, 
    "2019-09-20 10:30:00, 2019-09-27 10:30:00, 2019-10-04 10:30:00, 2019-10-11 10:30:00",
    "Абонемент на 4 занятия сроком на один месяц", 
    "Единовременная оплата абонемента", 
    NOW()
    );

INSERT INTO customers VALUES (
    "Алибасов Бари Каримович",
    "12345678", 
    "1947-06-06", 
    "3459 501365", 
    0, 
    "2019-12-31 23:55:00",
    "Разовое посещение", 
    "С авансовым платежом", 
    NOW()
    );