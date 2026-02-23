import mysql.connector
from controller import get_date

# Establish connection to database
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="nikolaoskomninos",
    password="",
    database="nikolaoskomninos"
    )


def main():
    # Our test function
    get_date(conn)
    
    ## Close connection
    conn.close()


if __name__ == "__main__":
    main()