import sqlite3


class SQLiteHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        # Crea una tabla con los nombres de columna proporcionados
        columns_str = ', '.join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        # Inserta datos en la tabla
        columns = ', '.join(data.keys())
        values = ', '.join(['?' for _ in data.values()])
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(insert_query, tuple(data.values()))
        self.conn.commit()

    def close_connection(self):
        # Cierra la conexión con la base de datos
        self.conn.close()
