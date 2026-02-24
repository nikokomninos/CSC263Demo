import mysql.connector
from player_manager import (
    add_player,
    change_player,
    delete_player,
    list_players,
    update_player_score,
)
from player_stats import query_player_stats
from player_query import (
    query_players_by_wins,
    query_players_by_gold,
    query_top_players,
    query_all_players_with_stats,
)

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="nikolaoskomninos",
    password="",
    database="nikolaoskomninos",
)


def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Add Player")
        print("2. Change Player")
        print("3. Delete Player")
        print("4. List Players")
        print("5. Update Player Score (Stored Procedure)")
        print("6. Player Statistics (Stored Procedure)")
        print("7. Players with More Wins than Losses")
        print("8. Players with Gold Above Average")
        print("9. Top 5 Players by Wins")
        print("10. All Players with Stats (LEFT OUTER JOIN)")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        match choice:
            case "1":
                add_player(conn)
            case "2":
                change_player(conn)
            case "3":
                delete_player(conn)
            case "4":
                list_players(conn)
            case "5":
                update_player_score(conn)
            case "6":
                query_player_stats(conn)
            case "7":
                query_players_by_wins(conn)
            case "8":
                query_players_by_gold(conn)
            case "9":
                query_top_players(conn)
            case "10":
                query_all_players_with_stats(conn)
            case "11":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
