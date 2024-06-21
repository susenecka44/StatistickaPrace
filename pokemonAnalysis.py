import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Pokémon dataset
file_path = 'PokemonDataset/pokemon.csv'
pokemon_data = pd.read_csv(file_path)

# Check and calculate 'base_total' if it does not exist
if 'base_total' not in pokemon_data.columns:
    pokemon_data['base_total'] = pokemon_data['hp'] + pokemon_data['attack'] + pokemon_data['defense'] + \
                                 pokemon_data['sp_attack'] + pokemon_data['sp_defense'] + pokemon_data['speed']

# Calculate type advantages by summing all 'against_' columns
type_advantages_columns = [col for col in pokemon_data.columns if col.startswith('against_')]
pokemon_data['type_advantage'] = pokemon_data[type_advantages_columns].sum(axis=1)

# Sorting Pokémon by base total, type advantage, and legendary status
top_pokemon = pokemon_data.sort_values(by=['base_total', 'type_advantage', 'is_legendary'], ascending=[False, False, False])

# Display the top 10 Pokémon
print("Top Pokémon based on base total, type advantage, and legendary status:")
print(top_pokemon[['name', 'base_total', 'type_advantage', 'is_legendary']].head(10))

# Create a correlation matrix of Pokémon attributes
correlation_matrix = pokemon_data[['attack', 'defense', 'speed', 'sp_attack', 'sp_defense', 'hp']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Pokémon Attributes')
plt.show()

# Extracting and processing type matchup data
type_matchups = pokemon_data[[col for col in pokemon_data.columns if col.startswith('against_')]]
type_matchups.columns = [col.replace('against_', '') for col in type_matchups.columns]
type_matchups['primary_type'] = pokemon_data['type1']
type_effectiveness_matrix = type_matchups.groupby('primary_type').mean()

# Plotting the heatmap for type effectiveness
plt.figure(figsize=(14, 10))
sns.heatmap(type_effectiveness_matrix, annot=True, cmap='coolwarm', linewidths=.5, fmt=".2f")
plt.title('Average Effectiveness of Pokémon Types Against Each Other')
plt.xlabel('Defending Type')
plt.ylabel('Attacking Type')
plt.show()
