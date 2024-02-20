import mysql.connector

# One more way to easy understanding

create_table = "create table Student(sno varchar(10), Name char(20), Age varchar(3));"
insert_value = "insert into Student values (01,'Rajkumar',27);"
select_command = "Select * from Student;"

try:
    connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    # localhost is different, port is also different
    # username and passwd is your database creation time you given.
    # database is your database name
    curse = connection.cursor()  # create cursor for execute queries
    curse.execute(create_table)  # we can do this type also
    curse.execute("select * from Student;")  # write queries here

    for row in curse:
        print(row[0], row[1], row[2])  # Based on the columns we will give values here
    connection.close()  # close the database
except:
    print(" database connection failed")
    # Sometimes database connection will down or not getting connection at the moment it will through error
    # because here we use exception handling
