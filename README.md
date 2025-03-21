# pokemon-data-pipeline
A free, project-based data engineering pipeline using PokéAPI, DuckDB and GitHub Actions

This project is a data pipeline which gets Pokemon information from the PokeAPI API, it transform, load in a DuckDB database and validate it's quality. The Objective is to learn and practice concepts from data engineering
---

## To get data
1. ``` fetch_pokemon_data.py ``` gets data from the API for the next Pokemon:
    - Ditto
    - Pikachu
    - Bulbasaur
    - Charmander
    - Squirtle

## Load data to DuckDB
2. ``` load_to_duckdb.py ``` load data in a duckDB database and creates the next tables:
    - pokemon: general information
    - abilities: pokemon abilities
    - types: Types of pokemon

## Validate data
3. ``` validate_data.py ``` validates the quality using great_expectations

## Query data
4. ``` queries.sql ``` execute sql queries in the database using this file. 

## Pipeline
4. ``` pipeline.yml ```  Defines an automated workflow using GitHub Actions
    - Configures a env with Python 3.9
    - Install dependencies from requirements.txt
    - Execute scripts in order: fetch, load, validate
---

# Next improvements:
Unit tests
