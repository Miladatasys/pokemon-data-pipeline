import duckdb
import pandas as pd

# Load CSV into DuckDB
def load_to_duckdb():
    print("Loading CSV into DuckDB...")
    try:
        df = pd.read_csv("./data/pokemon_data.csv")
        print("CSV file loaded successfully.")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return

    conn = None
    try:
        # Connect to DuckDB
        conn = duckdb.connect(database="./data/pokemon.db")
        print("Connected to DuckDB successfully.")

        # String to list
        df['abilities'] = df['abilities'].apply(lambda x: x.split(", ") if pd.notna(x) else [])
        df['types'] = df['types'].apply(lambda x: x.split(", ") if pd.notna(x) else [])

        # Create pokemon table
        conn.register("pokemon_df", df)
        conn.execute("CREATE TABLE pokemon AS SELECT * FROM pokemon_df")
        print("Pokemon table created.")

        # Create abilities table
        abilities = df.explode("abilities")[["id", "abilities"]].dropna()
        conn.register("abilities_df", abilities)
        conn.execute("CREATE TABLE abilities AS SELECT * FROM abilities_df")
        print("Abilities table created.")

        # Create types table
        types = df.explode("types")[["id", "types"]].dropna()
        conn.register("types_df", types)
        conn.execute("CREATE TABLE types AS SELECT * FROM types_df")
        print("Types table created.")

        print("Data loaded into DuckDB and tables created.")

    except Exception as e:
        print(f"Error during database operations: {e}")

    finally:
        # Close connection
        if conn:
            conn.close()
            print("Database connection closed.")

# Query data
def query_data():
    print("Querying data from DuckDB...")
    conn = None
    try:
        conn = duckdb.connect(database="./data/pokemon.db")
        result = conn.execute("SELECT * FROM pokemon").fetchall()
        print("Pokemon data:", result)
    except Exception as e:
        print(f"Error querying data: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

# Main function
if __name__ == "__main__":
    load_to_duckdb()
    query_data()