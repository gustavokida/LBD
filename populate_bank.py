import Faker
import psycopg2 as db
import date
import random


def validate_info(field_list: list):
    valid_list_field = []
    for field in field_list:
        field_name = field[0]
        if field_name == '':
            return False
        
        data_type = field[1]
        if not(data_type in data_types_with_2_args) and not(data_type in data_types_with_4_args):
            return False

        if len(field) == 2 or len(field) == 4:
            valid_list_field.append(field)
        else:
            return False

    return valid_list_field


def validate_date(day: int, mounth: int, year: int):
    try:
        date.date(year, mounth, day)
        return True
    except:
        return False


def random_date():
    day = random.randrange(1, 32)
    mounth = random.randrange(1, 13)
    year = random.randrange(1900, 2019)
    while (not (validate_date(day, mounth, year))):
        day = random.randrange(1, 32)
        mounth = random.randrange(1, 13)
        year = random.randrange(1900, 2019)
    date = '{}-{}-{}'.format(day, mounth, year)
    return date


user:str = 'postgres'
password:str = '123'
database:str = 'postgres'
host:str = '127.0.0.1'
port:str = '5432'
connection = db.connection(user, password, database, host, port)

data_types_with_2_args = ['integer', 'float', 'date', 'boolean', 'name', 'address', 'text']
data_types_with_4_args = ['fk']
'''
Input with 2 args:
field_name-data_type
Input with 4 args:
field_name-data_type-table_name-field_name
'''
