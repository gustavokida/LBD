import psycopg2 as bd
import random as rd
import string as st
import datetime as dt


def connect_in_database(user: str, password: str, database: str, host: str = "127.0.0.1", port: str = "5432"):
    try:
        connection = bd.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database
                                )
    except (Exception, bd.Error) as error:
        pass
    return connection


types_with_less_args = ['sequency', 'randomdate', 'fk_integer']
types = ['letters', 'alphanumeric', 'randominteger', 'randomfloat']
especifications = ['start', 'size', 'interval']
'''
Input para campos, exceto quando type é 'sequency':
    name-type-especification-begin-end
Quando type é 'sequency':
    name-sequency
begin e end devem ser números inteiros positivos
["id-sequency", "name-letters-size-1-255", "idk-alphanumeric-size-10-10", 
"number-randominteger-interval-0-65536", "salary-randomfloat-interval-500-3000", 
"birth-randomdate", "fk_cliente-fk_integer-tabela-campo"]
'''
def extract_info(fields: list):
    valid_fields = []
    for field in fields:
        field_info = field.split('-')
        is_valid = False
        name = field_info[0]
        fType = field_info[1]    
        if len(field_info) == 2:
            is_valid = verify_valid_field(name, fType)
        elif len(field_info) == 4 and (field_info[1] == 'fk_integer'):
            is_valid = True
        elif len(field_info) == 5:
            especification = field_info[2]
            start = field_info[3]
            end = field_info[4]
            is_valid = verify_valid_field(name, fType, especification, start, end)
        if is_valid:
            valid_fields.append(field_info)
    return valid_fields


def verify_valid_field(name: str, fType: str, especification: str = None, start: str = None, end: str = None):
    if fType in types_with_less_args:
        return (name != '')
    elif fType == 'randomfloat':
        return (name != '') and (fType in types) and (especification in especifications) and (floatTryParse(start)[1]) and (floatTryParse(end)[1])
    return (name != '') and (fType in types) and (especification in especifications) and (intTryParse(start)[1]) and (intTryParse(end)[1])


def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def floatTryParse(value):
    try:
        return float(value), True
    except ValueError:
        return value, False


def random_info(fType: str, begin: int, end: int):
    if fType == 'letters':
        return random_letters(begin, end)
    elif fType == 'alphanumeric':
        return random_alphanumeric(begin, end)
    elif fType == 'randominteger':
        return random_integer_in_interval(begin, end)
    elif fType == 'randomfloat':
        return random_float_in_interval(begin, end)
    elif fType == 'randomdate':
        return random_date()
    else:
        return ''


def random_alphanumeric(begin: int, end: int):
    if begin < 0 or end < 0:
        return '', False
    possible_characters = list(st.ascii_letters + st.digits)
    result = ''
    size = rd.randrange(begin, end + 1)
    for i in range(size):
        result += possible_characters[rd.randrange(len(possible_characters))]
    return result, True


def random_letters(begin: int, end: int):
    if begin < 0 or end < 0:
        return '', False
    possible_characters = list(st.ascii_letters)
    result = ''
    size = rd.randrange(begin, end + 1)
    for i in range(size):
        result += possible_characters[rd.randrange(len(possible_characters))]
    return result, True


def random_integer_in_interval(begin: int, end: int):
    if begin < 0 or end < 0:
        return '', False
    return rd.randrange(begin, end+1), True


def random_float_in_interval(begin: int, end: int):
    if begin < 0 or end < 0:
        return '', False
    return rd.randrange(begin, end+1) + rd.randrange(0, 100) / 100, True


def validate_date(day: int, mouth: int, year: int):
    try:
        dt.date(year, mouth, day)
        return True
    except:
        return False

def random_date():
    day = rd.randrange(1,32)
    mounth = rd.randrange(1,13)
    year = rd.randrange(1900, 2019)
    while(not(validate_date(day, mounth, year))):
        day = rd.randrange(1,32)
        mounth = rd.randrange(1,13)
        year = rd.randrange(1900, 2019)
        print('aqui')
    date = '{}-{}-{}'.format(day, mounth, year)
    return date


def get_valid_info(connection, table_name: str, field_name: str):
    try:
        query = 'SELECT {} FROM {} ORDER BY RANDOM() LIMIT 1;'.format(field_name, table_name)
        cursor = connection.cursor()
        cursor.execute(query)
        info = cursor.fetchone()[0]
        cursor.close()
        if info == None:
            return '', False
        return info, True
    except:
        return '', False


def last_of_sequency(connection, table: str, field: str):
    try:
        query = "SELECT MAX({}) FROM {};".format(field, table)
        cursor = connection.cursor()
        cursor.execute(query)
        last = cursor.fetchone()[0]
        cursor.close()
        if last == None:
            return 0, True
        return int(last), True
    except:
        return 0, False


def create_insert_query(table_name: str, name_fields: list, data_fields: list):
    if len(name_fields) == 0 or len(data_fields) == 0 or len(name_fields) != len(data_fields):
        return '', False

    fields_names_sql = ''
    fields_data_sql = ''
    for i, j in zip(name_fields, data_fields):
        fields_names_sql += "{}".format(i)
        if (type(j) is int) or (type(j) is float) or (j == 'NULL'):
            fields_data_sql += str(j)
        else:
            fields_data_sql += "'{}'".format(j)
        if i != name_fields[-1] and j != data_fields[-1]:
            fields_names_sql += ', '
            fields_data_sql += ', '

    query = "INSERT INTO {0} ({1}) VALUES ({2});".format(table_name, fields_names_sql, fields_data_sql)
    return query, True


def insert_data_in_table(connection, query: str):
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
    return False


def insert_random_data_in_table(table_name: str, fields: list, rows: int, user: str, password: str, database: str, host: str = "127.0.0.1", port: str = "5432"):
    if rows <= 0:
        return True

    try:
        connection = connect_in_database(user, password, database, host, port)
        valid_fields_list = extract_info(fields)
        
        name_fields_list = []
        for valid_field in valid_fields_list:
            name_fields_list.append(valid_field[0])
        
        data_fields_list = []
        for field in valid_fields_list:
            field_name = field[0]
            fType = field[1]
            if fType == 'sequency':
                last = last_of_sequency(connection, table_name, field_name)
                if last[1] == True:
                    data_fields_list.append(last[0] + 1)
                else:
                    return False
            elif fType == 'randomdate':
                data_fields_list.append(random_date())
            elif fType == 'fk_integer':
                fk_table_name = field[2]
                fk_field_name = field[3]
                fk_value = get_valid_info(connection, fk_table_name, fk_field_name)[0]
                data_fields_list.append(fk_value)
            elif fType == 'randomfloat':
                begin = float(field[3])
                end = float(field[4])
                data_fields_list.append(random_info(fType, begin, end)[0])
            else:
                begin = int(field[3])
                end = int(field[4])
                data_fields_list.append(random_info(fType, begin, end)[0])

        query = create_insert_query(table_name, name_fields_list, data_fields_list)[0]
        print(query)
        insertion_result = insert_data_in_table(connection, query)
        if not insertion_result:
            print('Failed')
            return False

        for j in range(rows - 1):
            for i, field in zip(range(len(valid_fields_list)), valid_fields_list):
                fType = field[1]
                if fType == 'sequency':
                    data_fields_list[i] += 1 
                elif fType == 'randomdate':
                    data_fields_list[i] = random_date()
                elif fType == 'fk_integer':
                    fk_table_name = field[2]
                    fk_field_name = field[3]
                    fk_value = get_valid_info(connection, fk_table_name, fk_field_name)[0]
                    data_fields_list[i] = fk_value
                elif fType == 'randomfloat':
                    begin = float(field[3])
                    end = float(field[4])
                    data_fields_list[i] = (random_info(fType, begin, end)[0])
                else:
                    begin = int(field[3])
                    end = int(field[4])
                    data_fields_list[i] = (random_info(fType, begin, end)[0])
            
            query = create_insert_query(table_name, name_fields_list, data_fields_list)[0]
            insertion_result = insert_data_in_table(connection, query)
            if not insertion_result:
                print('Faileda')
                print(query)
                return False
        print('Success')
        return True
    except:
        print('Failed 3')
        return False


# con = connect_in_database('postgres', '123', 'lbd')
# print(last_of_sequency(con, 'compra', 'id'))


table_name = input('Nome da tabela: ')
print('Exemplo de Input:')
print('''Input para campos, exceto quando type é 'sequency':
    name-type-especification-begin-end
Quando type é 'sequency':
    name-sequency
begin e end devem ser números inteiros positivos
id-sequency name-letters-size-1-255 idk-alphanumeric-size-10-10 
number-randominteger-interval-0-65536 salary-randomfloat-interval-500-3000 
birth-randomdate fk_cliente-fk_integer-tabela-campo''')
fields = list(input('Digite os campos: ').split())
rows = int(input('Digite a quantidade de linhas a serem inseridas na tabela: '))
user = input('Digite o nome do usuario do banco: ')
password = input('Digite a senha do banco: ')
database = input('Digite o nome da database do banco: ')
host = input('Digite o host do banco(sem porta): ')
port = input('Digite a porta do host do banco: ')
insert_random_data_in_table(table_name, fields, rows, user, password, database, host, port)