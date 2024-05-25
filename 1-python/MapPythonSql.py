# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:36:40 2023

@author: icon
"""
import psycopg2 as pg2
#create connection with postgresql
#'password' is whatever password you set, we set password as root 
conn=pg2.connect(database='dvd',user="postgres",password="root")

#establish connection and start cursor to be ready to query

cur=conn.cursor()

# pass in postgresql query as a string

cur.execute("""select * from payment
where amount>2.99 """)

# return a tuple of first row 
cur.fetchone()

#return N number of rows
cur.fetchmany(10)

#return all rows
cur.fetchall()

#don't forget to close to connection
#killing the kernal or shutting down juptyer will also close it
conn.close()

######################################################

import psycopg2 as pg2
conn=pg2.connect(database='learning',user="postgres",password="root")
cur=conn.cursor()
cur.execute("""create table courses(
            course_id serial primary key,
            course_name varchar(50) unique not null,
            course_instructor varchar(50) not null,
            topic varchar(50) not null
            );"""
            )
#without commit() it will not add table
conn.commit()
#close cursor and communication with database
conn.close()

########################################################################

#inserting values

import psycopg2 as pg2

conn=pg2.connect(database='learning',user='postgres',password='root')

cur=conn.cursor()

cur.execute('''insert into courses
            values(1,'dbms','bhambre','transaction');''')
cur.execute('''insert into courses
            values(2,'uhve','siddhi','feelings');''')
cur.execute('''insert into courses(course_id,course_name,course_instructor,topic)
            values(3,'sql','radhakrishna','sql');''')
cur.execute('''insert into courses
            values(4,'oop','kanchan','inheritance');''')
cur.execute('''insert into courses
            values(5,'ToC','madhuri','DFA');''')
cur.execute('''insert into courses
            values(6,'IoT','patankar','raspberry pi');''')
conn.commit()
conn.close()

########################################################################

# printing all the rows
import psycopg2 as pg2

conn=pg2.connect(database='learning',user='postgres',password='root')

cur=conn.cursor()
cur.execute('select * from courses')

rows=cur.fetchall()
conn.commit()
conn.close()
for i in rows:
    print(i)

import psycopg2 as pg2

conn=pg2.connect(database='learning',user='postgres',password='root')

cur=conn.cursor()

cur.execute('''select course_instructor,count(*) from courses group by course_instructor''' )

row=cur.fetchall()
conn.commit()
conn.close()
for i in row:
    print(i)


import psycopg2 as pg2

conn=pg2.connect(database='learning',user='postgres',password='root')

cur=conn.cursor()

cur.execute('select * from courses order by course_instructor' )

row=cur.fetchall()
conn.commit()
conn.close()
for i in row:
    print(i)
    
    
##################################################################
#course_duration,course_fee,course_id another table

import psycopg2 as pg2

conn=pg2.connect(database='learning',user='postgres',password='root')

cur=conn.cursor()
cur.execute('''create table courses_info(
     course_id integer unique not null,
     course_fee integer not null,
     course_duration varchar(40) not null
    );''')

cur.execute('''insert into courses_info 
            values(1,500,'30 days')''')

cur.execute('''insert into courses_info 
            values(2,1000,'40 days')''')

cur.execute('''insert into courses_info 
            values(3,5000,'500 days')''')

conn.commit()
conn.close()


import psycopg2 as pg2

conn=pg2.connect(database='learning',user='postgres',password='root')

cur=conn.cursor()
cur.execute('''select * from courses inner join 
            courses_info on courses.course_id=courses_info.course_id ''')
row=cur.fetchall()
conn.commit()
conn.close()
for i in row:
    print(i)


















