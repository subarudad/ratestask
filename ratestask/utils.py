import psycopg
from ratestask.config import Config


def get_db_conn():
    conn = psycopg.connect(dbname=Config.PG_DATABASE,
                           user=Config.PG_USERNAME,
                           password=Config.PG_PASSWORD,
                           host=Config.PG_HOST,
                           port=5432)
    return conn


def get_average_prices(date_from, date_to, origin, destination):
    """
        Using SQL instead of ORM as per instructions
    """
    conn = get_db_conn()
    cursor = conn.cursor()

    query = """
        WITH orig_ports AS (
            SELECT code 
            FROM ports 
            WHERE parent_slug = %(origin)s OR code = %(origin)s
        ),        
        dest_ports AS (
            SELECT code 
            FROM ports 
            WHERE parent_slug = %(destination)s OR code = %(destination)s
        ),
        filtered_prices AS (
            SELECT day, price
            FROM prices
            WHERE day BETWEEN %(date_from)s AND %(date_to)s
              AND orig_code IN (SELECT code FROM orig_ports)
              AND dest_code IN (SELECT code FROM dest_ports)
        )
        SELECT day, AVG(price) AS average_price
        FROM filtered_prices
        GROUP BY day
        HAVING COUNT(price) >= 3
        ORDER BY day;
    """

    cursor.execute(query, {"origin": origin, "destination": destination, "date_from": date_from, "date_to": date_to})
    results = cursor.fetchall()

    average_prices = [{"day": row[0].strftime('%Y-%m-%d'), "average_price": round(row[1], 2)} for row in results]

    cursor.close()
    conn.close()

    return average_prices
