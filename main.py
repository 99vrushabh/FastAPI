from unicodedata import name
import psycopg2



# there some opration in this....
# for addition some numbers
# get data from id from int..



# for get data which was enterd by user



#  for database
# establishing the connection
conn = psycopg2.connect(
    database="postgres", user='postgres', password='vrushabh', host='127.0.0.1', port='5432'
)
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()
cursor.execute('''create table user(
    user_id numeric(05) NOT NULL primary key,
    user_name varchar(50) NOT NULL,
    user_mobile numeric (10)
    user_email varchar(50),
    user_password varchar(20)
)
''')
 
print("Command exicute successfully..........")
