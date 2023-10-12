import mysql.connector

def db_example():
    host = "localhost"
    user = "root"
    pswd = "LucyThePuppy4!"
    database = "demo"
    
    connection = mysql.connector.connect(host=host, user=user, password=pswd, database=database)
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    
    # cursor.execute("INSERT INTO demo (name,topic,mobile) VALUES (%s, %s, %s)",
    #                ("Chris Paris", "Tech", "1208392"))
    # connection.commit()
    
    cursor.execute("UPDATE demo SET name = %s WHERE name = %s",
               ("Emma Pikes", "Emma Pike"))
    connection.commit()
    
    cursor.execute("SELECT * FROM demo WHERE name = %s", ("John Smith",))
    result = cursor.fetchall()
    for row in result:
        print(row)
    
db_example()
    