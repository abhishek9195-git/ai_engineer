import sqlite3

# Make the connection
connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

#1. CREATE TABLE
cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment (
    id INTEGER PRIMARY KEY, 
    title TEXT, 
    price REAL, 
    currency TEXT, 
    status TEXT
    )
""")


# DROP TABLE
# cursor.execute("DROP TABLE shipment")
# connection.commit()


# 2. INSERT
# cursor.execute("""
#     INSERT INTO shipment
#     VALUES(1, 'Smart phone', 13000, 'INR', 'Placed')
# """)
# connection.commit()


# 3. UPDATE [VERSION 1]
# cursor.execute(""" 
#     UPDATE shipment SET status = 'in_transit'
#     WHERE id = 1
# """)
# connection.commit()


# 4. UPDATE [VERSION 2]
# id = 1
# status = "out_for_delivery"
# cursor.execute(f"""
#     UPDATE shipment SET status = '{status}'
#     WHERE id = {id}
# """)
# connection.commit()


# 5. UPDATE [VERSION 3]
# id = 1
# status = "out for delivery"
# cursor.execute("""
#     UPDATE shipment SET status = ?
#     WHERE id = ?

# """, (status, id))
# connection.commit()


# UPDATE [VERSION 4]
id = 1
status = "Shipped"
cursor.execute("""
    UPDATE shipment SET status = :status
    WHERE id = :id
""", {'status': status, 'id': id})
connection.commit()



# 3. READ ALL
# cursor.execute("""
#     SELECT * FROM shipment
# """)
# result = cursor.fetchall()
# print(result)



# 4. READ WITH CONDITION
# cursor.execute("""
#     SELECT * FROM shipment 
#     WHERE id = 1
# """)
# result = cursor.fetchone()
# print(result)



# 5. DELETE
# cursor.execute(""" 
#     DELETE FROM shipment WHERE  id = 1
# """)
# connection.commit()



# Close the connection
connection.close()