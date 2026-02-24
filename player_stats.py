def query_player_stats(conn):
    """Query player statistics using the GetPlayerStats stored procedure.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Player Statistics ---")

    cur.callproc("GetPlayerStats")

    for result in cur.stored_results():
        stats = result.fetchone()
        print(f"\nTotal Players: {stats['TotalPlayers']}")
        print(f"Total Wins: {stats['TotalWins']}")
        print(f"Total Losses: {stats['TotalLosses']}")
        print(f"Average Gold: {stats['AverageGold']:.2f}")
        print(f"Max Wins by a Player: {stats['MaxWins']}")

    cur.close()
