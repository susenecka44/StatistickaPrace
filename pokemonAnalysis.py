import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Pokémon dataset
file_path = 'PokemonDataset/pokemon.csv'
pokemon_data = pd.read_csv(file_path)

# Set up the matplotlib figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distribution of Pokémon Attributes', fontsize=16)

# Plotting each attribute
sns.histplot(data=pokemon_data, x='attack', kde=True, ax=axes[0, 0], color='red')
axes[0, 0].set_title('Attack Distribution')
axes[0, 0].set_xlabel('Attack')
axes[0, 0].set_ylabel('Frequency')

sns.histplot(data=pokemon_data, x='hp', kde=True, ax=axes[0, 1], color='blue')
axes[0, 1].set_title('Max Health (HP) Distribution')
axes[0, 1].set_xlabel('HP')
axes[0, 1].set_ylabel('Frequency')

sns.histplot(data=pokemon_data, x='weight_kg', kde=True, ax=axes[1, 0], color='green')
axes[1, 0].set_title('Weight Distribution')
axes[1, 0].set_xlabel('Weight (kg)')
axes[1, 0].set_ylabel('Frequency')

sns.histplot(data=pokemon_data, x='height_m', kde=True, ax=axes[1, 1], color='purple')
axes[1, 1].set_title('Height Distribution')
axes[1, 1].set_xlabel('Height (m)')
axes[1, 1].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()