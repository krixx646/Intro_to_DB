import mysql.connector

def create_and_populate():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="krixxfire@00123",
            database="krixx"
        )
        cursor = db.cursor()

        # 1) Create the table (naming it games_fighting)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS games_fighting (
                game_id    INT AUTO_INCREMENT PRIMARY KEY,
                game_name  VARCHAR(255),
                game_type  VARCHAR(255),
                game_fps   FLOAT,
                game_score FLOAT
            );
        """)
        print("🟢 Table created (or already existed).")

        # 2) Bulk-insert with the correct number of placeholders
        insert_sql = """
            INSERT INTO games_fighting
              (game_name, game_type, game_fps, game_score)
            VALUES
              (%s,        %s,        %s,        %s)
        """
        rows_to_insert = [
            ('cod',             'action',        60, 78),
            ('storm 3',         'fighting',      76, 99),
            ('shinobi striker', 'team strategy', 64, 91),
        ]
        cursor.executemany(insert_sql, rows_to_insert)
        db.commit()
        print(f"🟢 Inserted {cursor.rowcount} rows.")

        # 3) Update one of those rows
        update_sql = """
            UPDATE games_fighting
               SET game_name = %s,
                   game_type = %s,
                   game_fps  = %s
             WHERE game_id   = %s
        """
        update_values = ('crisis_warhead', 'action', 98, 2)  # e.g. update the row with game_id=2
        cursor.execute(update_sql, update_values)
        db.commit()
        print(f"🟢 Updated {cursor.rowcount} row(s).")

        # 4) Fetch & display current contents
        cursor.execute("SELECT * FROM games_fighting;")
        for row in cursor.fetchall():
            print(row)

    except mysql.connector.Error as err:
        print("❌ Something went wrong:", err)

if __name__ == "__main__":
    create_and_populate()
