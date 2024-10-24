sql_create_table = [{'name': 'users', 'sql': 'create table users (id serial primary key, fio varchar(30), age int, pasport varchar(30))'},
       {'name': 'group', 'sql': 'create table groups (id serial primary key, href varchar(30))'},
       {'name': 'g_u','sql': 'create table g_u (user_id int not null, group_id int not null)'},
       {'name': 'photo','sql': 'create table photo (id serial primary key, name varchar(30), href varchar(30), user_id int not null)'},
       {'name':'chat', 'sql':'create table chat (id serial primary key, user1id int, user2id int, message text)'},
       ]

sql_drop_table=[{'name': 'users', 'sql': 'drop table users'},
       {'name': 'group', 'sql': 'drop table group'},
       {'name': 'g_u','sql': 'drop table g_u'},
       {'name': 'photo','sql': 'drop table photo'},
       {'name':'chat', 'sql':'drop table chat'},
       ]

sql_show_table= [{'name': 'users', 'sql': 'select * from users'},
       {'name': 'group', 'sql': 'select * from group'},
       {'name': 'g_u','sql': 'select * from g_u'},
       {'name': 'photo','sql': 'select * from photo'},
       ]
