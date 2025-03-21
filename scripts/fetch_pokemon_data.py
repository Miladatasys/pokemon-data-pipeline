import requests
import pandas as pd

# Lista de Pokémon para obtener datos
pokemon_list = ["ditto", "pikachu", "bulbasaur", "charmander", "squirtle"]

# Fetch data about a Pokémon
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    response.raise_for_status()  # Exception
    return response.json()

# Transform data
def transform_data(data):
    transformed = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "base_experience": data["base_experience"],
        "hp": next(s["base_stat"] for s in data["stats"] if s["stat"]["name"] == "hp"),
        "attack": next(s["base_stat"] for s in data["stats"] if s["stat"]["name"] == "attack"),
        "defense": next(s["base_stat"] for s in data["stats"] if s["stat"]["name"] == "defense"),
        "special_attack": next(s["base_stat"] for s in data["stats"] if s["stat"]["name"] == "special-attack"),
        "special_defense": next(s["base_stat"] for s in data["stats"] if s["stat"]["name"] == "special-defense"),
        "speed": next(s["base_stat"] for s in data["stats"] if s["stat"]["name"] == "speed"),
        "abilities": ", ".join([a["ability"]["name"] for a in data["abilities"]]),  # Flatten abilities
        "types": ", ".join([t["type"]["name"] for t in data["types"]]),
    }
    return transformed

# Save data to CSV
def save_to_csv(pokemon_data):
    # Convert list of dicts to DataFrame
    df = pd.DataFrame(pokemon_data)
    df.to_csv("./data/pokemon_data.csv", index=False)
    print("Data saved to data/pokemon_data.csv")

# Main Function
def main():
    pokemon_data = []
    for pokemon in pokemon_list:
        print(f"Fetching data for {pokemon}...")
        try:
            data = fetch_pokemon_data(pokemon)
            transformed_data = transform_data(data)
            pokemon_data.append(transformed_data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {pokemon}: {e}")
        except KeyError as e:
            print(f"Error transforming data for {pokemon}: {e}")

    if pokemon_data:
        save_to_csv(pokemon_data)
    else:
        print("No data to save.")

if __name__ == "__main__":
    main()