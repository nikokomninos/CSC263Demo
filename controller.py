def get_date(conn):
  # Get a cursor
  cur = conn.cursor(dictionary=True)

  # Execute a query
  cur.execute("SELECT CURDATE() as CurrentDate")

  # Fetch one result
  row = cur.fetchone()
  print(f"Current date is: {row['CurrentDate']}")