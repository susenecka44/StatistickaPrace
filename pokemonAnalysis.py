import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
file_path = 'PokemonDataset/pokemon.csv'
pokemon_data = pd.read_csv(file_path)

#region DISTRIBUTIONS OF HEIGHT, WEIGHT, ATTACK, DEFENCE, AND HEALTH
# Extracting the relevant columns
height_data = pokemon_data['height_m']
weight_data = pokemon_data['weight_kg']
attack_data = pokemon_data['attack']
defence_data = pokemon_data['defense']
health_data = pokemon_data['hp']


# Function to plot distribution
def plot_distribution(data, title, xlabel):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, edgecolor='k', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()


# Plotting the distributions
plot_distribution(height_data, 'Distribution of Pokemon Heights', 'Height (m)')
plot_distribution(weight_data, 'Distribution of Pokemon Weights', 'Weight (kg)')
plot_distribution(attack_data, 'Distribution of Pokemon Attack', 'Attack')
plot_distribution(defence_data, 'Distribution of Pokemon Defence', 'Defence')
plot_distribution(health_data, 'Distribution of Pokemon Health', 'Health')
#endregion DISTRIBUTIONS OF HEIGHT, WEIGHT, ATTACK, DEFENCE, AND HEALTH

#region CORRELATION WITH TYPES
# One-hot encode the type1 and type2 columns
pokemon_data_encoded = pd.get_dummies(pokemon_data, columns=['type1', 'type2'])

# Select the relevant columns for correlation analysis
stats_data = pokemon_data_encoded[['height_m', 'weight_kg', 'attack', 'defense', 'hp']]
type_columns = [col for col in pokemon_data_encoded.columns if col.startswith('type1_') or col.startswith('type2_')]

# Calculate correlation
correlation_matrix = stats_data.join(pokemon_data_encoded[type_columns]).corr()

# Extract correlations of types with each stat
correlations = {}
for stat in ['height_m', 'weight_kg', 'attack', 'defense', 'hp']:
    correlations[stat] = correlation_matrix[[stat]].loc[type_columns]

# Display each correlation table
for stat in correlations:
    print(f"Correlation of Pokémon Types with {stat.capitalize()}")
    print(correlations[stat], '\n')
#endregion CORRELATION WITH TYPES