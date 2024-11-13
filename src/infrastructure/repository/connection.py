from mysql.connector import pooling, Error

connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    pool_reset_session=True,
    host='127.0.0.1',
    database='skinstore',
    user='root',
    password='',
    connection_timeout=10
)


def get_connection():
    try:
        connection = connection_pool.get_connection()

        if not connection.is_connected():
            connection.reconnect(attempts=3, delay=2)
        return connection
    except Error as e:
        print(f"Error getting connection from pool: {e}")
        return None

