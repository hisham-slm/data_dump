import psycopg2

def create_table(table_name : str, table_headers : dict, password: str, server: str = 'localhost', database: str = 'postgres', username: str = 'postgres', port : int = 5432):
    columns = ' ,'.join(f'{header} {data_type}' for header, data_type in table_headers.items())
    create_table_script =f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            {columns}
        )
    '''
    try:
        connection = psycopg2.connect(
            host = server,
            database = database,
            user = username,
            password = password,
            port = port
        )
        
        
        cursor = connection.cursor()
        cursor.execute(create_table_script)
        connection.commit()    
        
        print(f"Table {table_name} created!")
    except Exception as error:
        print('erroring')
        return error
    finally:
        cursor.close()
        connection.close()
    print(f'Table {table_name} created!') 


def to_postgres(data: list, table_name : str, table_headers : list, password: str,  server: str = 'localhost', database: str = 'postgres', username: str = 'postgres', port : int = 5432):
    headers = ' ,'.join(headers for headers in table_headers)
    placeholders = ', '.join(['%s'] * len(table_headers))
    add_script = f'INSERT INTO {table_name} ({headers}) VALUES ({placeholders})'
    print(add_script)
    
    try:
        print('connecting to the database!')
        connection = psycopg2.connect(
        host = server,
        database = database,
        user = username,
        password = password,
        port = port
        )
    
        cursor = connection.cursor()
        cursor.executemany(add_script, data)
        connection.commit()
        print('connection ')
        
        print(f'Data has been added to {table_name}')
    except Exception as error:
        print(error)
    finally:
        print('in finally')
        if cursor:
            cursor.close()
        if connection:
            connection.close()