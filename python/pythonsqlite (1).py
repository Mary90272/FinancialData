import sqlite3
import csv


def clean_field(field):
    return field.strip().replace('"', '').replace("'", "")

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
conn.text_factory = str
cursor = conn.cursor()

# cursor.execute('SELECT * FROM data')  # Replace with your table name
# rows = cursor.fetchall()

# for row in rows:
#     print(row)
# # Create a table named 'data'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        Job TEXT,
        JV TEXT,
        Batch TEXT,
        Ref TEXT,
        Acct TEXT,
        "Acct Desc" TEXT,
        Dept TEXT,
        "Dept Desc" TEXT,
        "Tran Date" TEXT,
        Desc TEXT,
        "Invoice Nbr" TEXT,
        Amt TEXT,
        "Acct Per" TEXT,
        Comment TEXT,
        "Due Date" TEXT,
        "Chk Date" TEXT,
        Sequence TEXT,
        "Batch Close Date" TEXT,
        "Vend/Cust Nbr" TEXT,
        PRIMARY KEY ("Tran Date")
     )
''')

# Import data from CSV
with open('gl.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    i = 0
    for row in csv_reader:
        cleaned_row = [clean_field(field) for field in row]
        while len(cleaned_row) > 19:
            cleaned_row.pop(-1)


        if len(cleaned_row) == 19:  # Skip incomplete rows
            num_placeholders = ','.join(['?' for _ in cleaned_row])
            ## delete REPLACE for test
            query = 'INSERT OR REPLACE INTO data VALUES ({})'.format(num_placeholders)
            #print("Insert query:", query)
            # print("Inserting row:", cleaned_row)
            try:
               cursor.execute(query, cleaned_row)
            except Exception as e:
                print("Error:", e)
        i += 1
            

# Commit changes and close the connection
#print("Committing changes and closing the connection...")
print("Inserted", cursor.rowcount, "rows.")
conn.commit()
conn.close()

# Reconnect and retrieve and print rows
print("Reconnecting and retrieving rows...")
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM data')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
print("Closing the connection.")
conn.close()