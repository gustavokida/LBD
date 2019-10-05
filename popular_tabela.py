import psycopg2 as bd
import random as rd
import string as st
import datetime as dt

def create_connection(user: str, password: str, database: str, host: str = "127.0.0.1", port: str = "5432"):
    try:
        connection = bd.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database
                                )
    except:
        return False
    return connection

data_types_with_2_args = ['sequence', 'randomdate']
data_types_with_4_args = ['fk_integer']
data_types_with_5_args = ['letters', 'alphanumeric', 'randominteger', 'randomfloat']
especifications_for_5_argument_types = ['size', 'interval']
'''
Tipos de dados e suas quantidades de argumentos:
    2 - sequence, randomdate
    4 - fk_integer
    5 - letters, alphanumeric, randominteger, randomfloat
Input esperado para cada quantidade de argumentos:
    2 - field_name-field_data_type
    4 - field_name-field_data_type-referenced_table_name-field_name_of_referenced_table
    5 - field_name-field_data_type-especification_for_5_argument_types-begin-final
'''
def extract_information_from_fields(field_list: list):
    valid_field_list = []
    for field in field_list:
        field_is_valid = False
        field_information_list = field.split('-')
        amount_of_information = len(field_information_list)

        if amount_of_information == 2 or amount_of_information == 4 or amount_of_information == 5:
            field_is_valid = verify_valid_field(field_information_list)

        if field_is_valid:
            valid_field_list.append(field_information_list)

    return valid_field_list

def verify_valid_field(field_information_list: list):
    try:
        amount_of_information = len(field_information_list)
        field_name = field_information_list[0]
        if field_name == '':
            return False

        field_data_type = field_information_list[1]
        if amount_of_information == 2:
            return field_data_type in data_types_with_2_args
        elif amount_of_information == 4:
            referenced_table_name = field_information_list[2]
            field_name_of_referenced_table = field_information_list[3]
            return (field_data_type in data_types_with_4_args) and (referenced_table_name != '') and (
                    field_name_of_referenced_table != '')
        elif amount_of_information == 5:
            especification_for_5_argument_types = field_information_list[2]
            begin = field_information_list[3]
            final = field_information_list[4]
            double_condition_of_integers = [
                intTryParse(begin)[1],
                intTryParse(final)[1]
            ]
            double_condition_of_floats = [
                floatTryParse(begin)[1],
                floatTryParse(final)[1]
            ]
            if field_data_type == 'randominteger':
                return (especification_for_5_argument_types == 'interval') and all(double_condition_of_integers)
            elif field_data_type == 'randomfloat':
                return (especification_for_5_argument_types == 'interval') and all(double_condition_of_floats)
            elif field_data_type == 'letters' or field_data_type == 'alphanumeric':
                return (especification_for_5_argument_types == 'size') and all(double_condition_of_integers)
    except:
        return False

def intTryParse(value):
    try:
        return int(value), True
    except:
        return value, False

def random_info(data_type: str, begin: int = None, final: int = None):
    if data_type == 'letters':
        return random_letters(begin, final)
    elif data_type == 'alphanumeric':
        return random_alphanumeric(begin, final)
    elif data_type == 'randominteger':
        return random_integer_in_interval(begin, final)
    elif data_type == 'randomdate':
        return random_date()
    return ''

def floatTryParse(value):
    try:
        return float(value), True
    except:
        return value, False

def random_alphanumeric(begin: int, final: int):
    if begin < 0 or final < 0 or begin > final:
        return None

    possible_characters = list(st.ascii_letters + st.digits)
    number_of_possible_characters = len(possible_characters)
    result = ''
    string_size = rd.randrange(begin, final + 1)
    for i in range(string_size):
        possible_character_random_index = rd.randrange(number_of_possible_characters)
        character_random = possible_characters[possible_character_random_index]
        result += character_random
    return result

def random_letters(begin: int, final: int):
    if begin < 0 or final < 0 or begin > final:
        return None

    possible_characters = list(st.ascii_letters)
    number_of_possible_characters = len(possible_characters)
    result = ''
    string_size = rd.randrange(begin, final + 1)
    for i in range(string_size):
        possible_character_random_index = rd.randrange(number_of_possible_characters)
        character_random = possible_characters[possible_character_random_index]
        result += character_random
    return result

def random_integer_in_interval(begin: int, final: int):
    if begin < 0 or final < 0:
        return None
    return rd.randrange(begin, final + 1)

def random_float_in_interval(begin: float, final: float):
    return rd.uniform(begin, final)

def validate_date(day: int, mounth: int, year: int):
    try:
        dt.date(year, mounth, day)
        return True
    except:
        return False

def random_date():
    day = rd.randrange(1, 32)
    mounth = rd.randrange(1, 13)
    year = rd.randrange(1900, 2019)
    while (not (validate_date(day, mounth, year))):
        day = rd.randrange(1, 32)
        mounth = rd.randrange(1, 13)
        year = rd.randrange(1900, 2019)
    date = '{}-{}-{}'.format(day, mounth, year)
    return date

def get_valid_random_information(connection, table_name: str, field_name: str):
    try:
        query = "SELECT {} FROM {} ORDER BY RANDOM() LIMIT 1;".format(field_name, table_name)
        cursor = connection.cursor()
        cursor.execute(query)
        info = cursor.fetchone()[0]
        cursor.close()
        return info
    except:
        return None

def max_value(connection, table: str, field: str):
    try:
        query = "SELECT MAX({}) FROM {};".format(field, table)
        cursor = connection.cursor()
        cursor.execute(query)
        max_value = cursor.fetchone()[0]
        cursor.close()
        if max_value == None:
            return 0
        return int(max_value)
    except:
        return None

def create_insert_query(table_name: str, field_name_list: list, field_data_list: list):
    if len(field_name_list) == 0 or len(field_data_list) == 0 or len(field_name_list) != len(field_data_list):
        return None

    field_name_sql = ''
    field_data_sql = ''
    for field_name, field_data in zip(field_name_list, field_data_list):
        field_name_sql += "{} ".format(field_name)
        if (type(field_data) is int) or (type(field_data) is float) or (field_data == 'NULL'):
            field_data_sql += str(field_data) + ' '
        else:
            field_data_sql += "'{}' ".format(field_data)
    field_name_sql = field_name_sql.strip().replace(' ', ',')
    field_data_sql = field_data_sql.strip().replace(' ', ',')

    query = "INSERT INTO {0} ({1}) VALUES ({2});".format(table_name, field_name_sql, field_data_sql)
    return query

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

def insert_random_data_in_table(table_name: str, field_list: list, rows: int, user: str, password: str, database: str,
                                host: str = "127.0.0.1", port: str = "5432"):
    if rows <= 0:
        return True

    try:
        connection = create_connection(user, password, database, host, port)
        valid_field_list = extract_information_from_fields(field_list)

        amount_of_fields = len(valid_field_list)
        data_field_list = [None for i in range(amount_of_fields)]
        for i, field in zip(range(amount_of_fields), valid_field_list):
            field_name = field[0]
            data_type = field[1]
            if data_type == 'sequence':
                data_field_list[i] = max_value(connection, table_name, field_name)

        name_field_list = [valid_field[0] for valid_field in valid_field_list]
        for i in range(1, rows + 1):
            for j, field in zip(range(amount_of_fields), valid_field_list):
                data_type = field[1]
                if data_type == 'sequence':
                    data_field_list[j] += 1
                elif data_type == 'randomdate':
                    data_field_list[j] = random_date()
                elif data_type == 'fk_integer':
                    fk_table_name = field[2]
                    fk_field_name = field[3]
                    fk_value = get_valid_random_information(connection, fk_table_name, fk_field_name)
                    data_field_list[j] = fk_value
                elif data_type == 'randomfloat':
                    begin = float(field[3])
                    final = float(field[4])
                    value = random_float_in_interval(begin, final)
                    data_field_list[j] = value
                else:
                    begin = int(field[3])
                    final = int(field[4])
                    data_field_list[j] = random_info(data_type, begin, final)

            query = create_insert_query(table_name, name_field_list, data_field_list)
            insertion_result = insert_data_in_table(connection, query)
            if not insertion_result:
                print(query)
                print(name_field_list)
                print(data_field_list)
                print('{} failed inside'.format(table_name))
                print()
                return False
        # print('{} inseridas em {}'.format(rows, table_name))
        return True
    except:
        print('{} failed'.format(table_name))
        return False


fields_dict = {}
table_names_list = list('autor, volume, manga, genero, livro, revista, midia, cliente, funcionario, compra, produtos_comprados'.split(', '))

fields = ['id-sequence', 'nacionalidade-letters-size-8-10', 'nome-letters-size-8-10', 'data_de_nascimento-randomdate', 'data_de_falecimento-randomdate']
fields_dict['autor'] = fields

fields = ['id-sequence', 'endereco-letters-size-8-10', 'sexo-letters-size-1-1', 'nome-letters-size-8-10', 'data_de_nascimento-randomdate']
fields_dict['cliente'] = fields

fields = ['id-sequence', 'data-randomdate', 'preco_total-randomfloat-interval-50.0-3000', 'desconto-randomfloat-interval-5-10', 'preco_final-randomfloat-interval-500-3000', 'fk_cliente_id-fk_integer-cliente-id', 'fk_funcionario_id-fk_integer-funcionario-id']
fields_dict['compra'] = fields

fields = ['id-sequence', 'funcao-letters-size-8-10', 'nome-letters-size-8-10', 'salario-randomfloat-interval-50.0-3000', 'data_de_admissao-randomdate']
fields_dict['funcionario'] = fields

fields = ['id-sequence', 'nome-letters-size-8-10', 'localizacao-letters-size-8-10']
fields_dict['genero'] = fields

fields = ['id-sequence', 'nome_do_volume-letters-size-8-10', 'sinopse-letters-size-8-10', 'titulo_do_livro-letters-size-8-10']
fields_dict['livro'] = fields

fields = ['id-sequence', 'capitulo-randominteger-interval-1-900', 'fk_volume_id-fk_integer-volume-id', 'titulo_do_capitulo-letters-size-8-10']
fields_dict['manga'] = fields

fields = ['id-sequence', 'data_de_publicacao-randomdate', 'editora-letters-size-8-10', 'nome-letters-size-8-10', 'idioma-letters-size-8-10', 'local_de_publicacao-letters-size-8-10', 'fk_genero_id-fk_integer-genero-id', 'fk_autor_id-fk_integer-autor-id', 'fk_revista_id-fk_integer-revista-id', 'fk_manga_id-fk_integer-manga-id', 'fk_livro_id-fk_integer-livro-id']
fields_dict['midia'] = fields

fields = ['id-sequence', 'fk_compra_id-fk_integer-compra-id', 'fk_midia_id-fk_integer-midia-id']
fields_dict['produtos_comprados'] = fields

fields = ['id-sequence', 'empresa-letters-size-8-10', 'edicao-randominteger-interval-1-900']
fields_dict['revista'] = fields

fields = ['id-sequence', 'sinopse-letters-size-8-10', 'numero-randominteger-interval-1-900', 'nome-letters-size-8-10']
fields_dict['volume'] = fields

connection = create_connection('postgres', '123', 'lbd')
rows = 10
user = 'postgres'
password = '123'
database = 'lbd'
for table_name in table_names_list:
    insert_random_data_in_table(table_name, fields_dict[table_name], rows, user, password, database)