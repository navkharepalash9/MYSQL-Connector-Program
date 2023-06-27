import mysql.connector as c

try:
    con = c.connect(host='localhost',user='root',passwd='Palash@123',database='palash')
    print("connect")

except Exception as e:
    print("not connect",e)

cursor = con.cursor()
# Check your  mysql connect well or not
if con.is_connected():
    print("Yes it connected Successfully !")
else:
    print("Not Connected")

def create_new_databases():
    name = input("Enter name of database that you want to create :- ")
    query="Create database {}".format(name)
    cursor.execute(query)

def create_table():
    db_name = input("Enter database name that you want to use :- ")
    query = 'USE {}'.format(db_name)
    cursor.execute(query)
    name1=input("Enter table(company) name  :- ")
    query='create table {}( emp_id int primary key , emp_name varchar(20), emp_salary int ,city varchar(20)) '.format(name1)
    cursor.execute(query)

def insert_data():
    db_name=input("Enter database name that you want to use :- ")
    t_name=input("Enter table name where do you want to add information :- ")
    query='USE {}'.format(db_name)
    cursor.execute(query)
    while True:
        emp_id=input("Enter employee id :- ")
        emp_name=input("Enter employee name :- ")
        emp_salary=int(input("Enter employee salary :- "))
        emp_city = input("Enter employee city name :- ")
        query='INSERT INTO {}(emp_id,emp_name,emp_salary,city) VALUES({},"{}",{},"{}")'.format(t_name,emp_id,emp_name,emp_salary,emp_city)
        cursor.execute(query)
        con.commit()
        ch=input("Want to add more data press y else n :- ")
        if ch=='n':
            break

def update_data():
    db_name = input("Enter database name :- ")
    t_name=input("Enter that table name there you want to update :- ")
    query = 'USE {}'.format(db_name)
    cursor.execute(query)
    while True:
        col_name=input("Which column want to update ==>> emp_name,emp_salary,city:- ")
        chng_name=input("Enter updated name :- ")
        emp_id=int(input('Enter emp id of that employee :- '))
        query='update {} set {}="{}" where emp_id={}'.format(t_name,col_name,chng_name,emp_id)
        cursor.execute(query)
        con.commit()
        ch=input("You want add more data press y else n :- ")
        if ch=='n':
            break

def delete_record():
    db_name = input("Enter database name :- ")
    t_name=input("Enter table name :- ")
    query = 'USE {}'.format(db_name)
    cursor.execute(query)
    while True:
        emp_id=int(input("Enter imp id of that row :-"))
        query="DELETE FROM {} WHERE EMP_ID={}".format(t_name,emp_id)
        cursor.execute(query)
        con.commit()
        ch=input('want to delete more data press y else n :- ')
        if ch=='n':
            break

def show_Table_details():
    db_name = input("Enter database name :- ")
    t_name=input("Enter table name :- ")
    query = 'USE {}'.format(db_name)
    cursor.execute(query)
    query='SELECT * FROM {}'.format(t_name)
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)

def show_databases():
    query='SHOW DATABASES'
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)

def show_tables_inDatabase():
    db=input("Enter database name that you want to use :- ")
    query1='USE {}'.format(db)
    cursor.execute(query1)
    query='SHOW TABLES'
    cursor.execute(query)
    result=cursor.fetchall()
    if result is None:
        print("there is no table exit")
    else:
        for row in result:
            print(row)

def delete_database():
    db_name=input("Enter database name :- ")
    query='DROP DATABASE {}'.format(db_name)
    cursor.execute(query)
    print('Delete successfully !')


def delete_table():
    db_name=input("Enter database name :- ")
    query1='USE {}'.format(db_name)
    cursor.execute(query1)

    t_name=input("Enter table name that you want to delete :- ")
    query='DROP TABLE {}'.format(t_name)
    cursor.execute(query)
    con.commit()
    print('Delete successfully !')

def clear_table():
    db_name=input("Enter database name :- ")
    query1='USE {}'.format(db_name)
    cursor.execute(query1)
    t_name=input("enter table name :- ")
    query='TRUNCATE {}'.format(t_name)
    cursor.execute(query)
    con.commit()

while True:
    print("1).Create databases 2).Create table 3).Insert record 4).Update record 5).Delete record 6).Show table details 7).Show database 8).Show tables in databases 9).Delete table 10).Delete database 11).clear table  12).Exit")
    number=int(input("Enter operation number that you want to perform :-  "))
    if number == 1:
        create_new_databases()
    elif number == 2:
        create_table()
    elif number == 3:
        insert_data()
    elif number == 4:
        update_data()
    elif number == 5:
        delete_record()
    elif number == 6:
        show_Table_details()
    elif number == 7:
        show_databases()
    elif number == 8:
        show_tables_inDatabase()
    elif number == 9:
        delete_table()
    elif number == 10:
        delete_database()
    elif number == 11:
        clear_table()
    elif number == 12:
        break
    else:
        print("Enter proper number ")

