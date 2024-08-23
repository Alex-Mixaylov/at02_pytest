import pytest
#
# def test_add2():
#     assert 1 + 1 == 2
#
# def test_subtract():
#     assert 3 - 2 == 1
#
# def check(number):
#    return number % 2 == 0

# def isPalindrome(s):
#     return s == s[::-1]

# def sort_list(numbers):
#     return sorted(numbers)

#Использование фикстур

import sqlite3

def init_db():
   conn = sqlite3.connect(':memory:') #база  данных  хранится только в памяти и не создается  на  диске
   cursor = conn.cursor()
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY,
   name TEXT,
   age INTEGER)
   ''')
   return conn

def add_user(conn, name, age):
   cursor = conn.cursor()
   cursor.execute('''
   INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
   conn.commit()

def get_user(conn, name):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users WHERE name=?''', (name,))
    return cursor.fetchone() # берет первую строчку