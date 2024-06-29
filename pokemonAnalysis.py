import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, shapiro

# Načtení datasetu
cesta_k_souboru = "PokemonDataset/pokemon.csv"
pokemon_data = pd.read_csv(cesta_k_souboru)

# Příprava dat
relevantni_sloupce = ['type1', 'height_m', 'weight_kg', 'attack']
pokemon_data_cleaned = pokemon_data.dropna(subset=['height_m', 'weight_kg'])

# Popisná statistika
popisna_statistika = pokemon_data_cleaned[relevantni_sloupce].describe()
print("Popisná statistika:")
print(popisna_statistika)

# Box Ploty
plt.figure(figsize=(18, 12))

# Výška podle typu
plt.subplot(3, 1, 1)
sns.boxplot(x='type1', y='height_m', data=pokemon_data_cleaned)
plt.title('Distribuce výšky podle typu Pokémona')
plt.xticks(rotation=45)

# Váha podle typu
plt.subplot(3, 1, 2)
sns.boxplot(x='type1', y='weight_kg', data=pokemon_data_cleaned)
plt.title('Distribuce váhy podle typu Pokémona')
plt.xticks(rotation=45)

# Útok podle typu
plt.subplot(3, 1, 3)
sns.boxplot(x='type1', y='attack', data=pokemon_data_cleaned)
plt.title('Distribuce útoku podle typu Pokémona')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Set up the plotting area
fig, axes = plt.subplots(3, 1, figsize=(18, 12))

# Výška vs. Váha
scatter1 = sns.scatterplot(x='height_m', y='weight_kg', hue='type1', data=pokemon_data_cleaned, palette='tab10', ax=axes[0])
axes[0].set_title('Výška vs. Váha podle typu Pokémona')
axes[0].set_xlabel('Výška (m)')
axes[0].set_ylabel('Váha (kg)')
handles, labels = scatter1.get_legend_handles_labels()
scatter1.legend_.remove()

# Výška vs. Útok
scatter2 = sns.scatterplot(x='height_m', y='attack', hue='type1', data=pokemon_data_cleaned, palette='tab10', legend=False, ax=axes[1])
axes[1].set_title('Výška vs. Útok podle typu Pokémona')
axes[1].set_xlabel('Výška (m)')
axes[1].set_ylabel('Útok')

# Váha vs. Útok
scatter3 = sns.scatterplot(x='weight_kg', y='attack', hue='type1', data=pokemon_data_cleaned, palette='tab10', legend=False, ax=axes[2])
axes[2].set_title('Váha vs. Útok podle typu Pokémona')
axes[2].set_xlabel('Váha (kg)')
axes[2].set_ylabel('Útok')

# Add a single legend to the upper right corner of the figure
fig.legend(handles, labels, loc='upper right', bbox_to_anchor=(1, 1), ncol=1)

plt.tight_layout()
plt.show()

# Histogramy
plt.figure(figsize=(18, 12))

# Histogram Výšky
plt.subplot(3, 1, 1)
sns.histplot(pokemon_data_cleaned['height_m'], kde=True)
plt.title('Histogram Výšky Pokémonů')
plt.xlabel('Výška (m)')
plt.ylabel('Frekvence')

# Histogram Váhy
plt.subplot(3, 1, 2)
sns.histplot(pokemon_data_cleaned['weight_kg'], kde=True)
plt.title('Histogram Váhy Pokémonů')
plt.xlabel('Váha (kg)')
plt.ylabel('Frekvence')

# Histogram Útoku
plt.subplot(3, 1, 3)
sns.histplot(pokemon_data_cleaned['attack'], kde=True)
plt.title('Histogram Útoku Pokémonů')
plt.xlabel('Útok')
plt.ylabel('Frekvence')

plt.tight_layout()
plt.show()

# ANOVA Testy
anova_vyska = f_oneway(*[group['height_m'].dropna() for name, group in pokemon_data_cleaned.groupby('type1')])
anova_vaha = f_oneway(*[group['weight_kg'].dropna() for name, group in pokemon_data_cleaned.groupby('type1')])
anova_utok = f_oneway(*[group['attack'].dropna() for name, group in pokemon_data_cleaned.groupby('type1')])

anova_vysledky = {
    'Atribut': ['Výška', 'Váha', 'Útok'],
    'F-Statistika': [anova_vyska.statistic, anova_vaha.statistic, anova_utok.statistic],
    'p-hodnota': [anova_vyska.pvalue, anova_vaha.pvalue, anova_utok.pvalue]
}

anova_vysledky_df = pd.DataFrame(anova_vysledky)
print("ANOVA Výsledky:")
print(anova_vysledky_df)

# Test normality (Shapiro-Wilk test)
shapiro_vyska = shapiro(pokemon_data_cleaned['height_m'])
shapiro_vaha = shapiro(pokemon_data_cleaned['weight_kg'])
shapiro_utok = shapiro(pokemon_data_cleaned['attack'])

normalita_vysledky = {
    'Atribut': ['Výška', 'Váha', 'Útok'],
    'W-statistika': [shapiro_vyska.statistic, shapiro_vaha.statistic, shapiro_utok.statistic],
    'p-hodnota': [shapiro_vyska.pvalue, shapiro_vaha.pvalue, shapiro_utok.pvalue]
}

normalita_vysledky_df = pd.DataFrame(normalita_vysledky)
print("Výsledky testu normality (Shapiro-Wilk):")
print(normalita_vysledky_df)


# Příprava dat
relevantni_sloupce = ['type1', 'height_m', 'weight_kg', 'attack']
pokemon_data_cleaned = pokemon_data.dropna(subset=['height_m', 'weight_kg'])

# Popisná statistika
popisna_statistika = pokemon_data_cleaned[relevantni_sloupce].describe()

# Uložení popisné statistiky do proměnných
count = popisna_statistika.loc['count']
mean = popisna_statistika.loc['mean']
std = popisna_statistika.loc['std']
min_val = popisna_statistika.loc['min']
q25 = popisna_statistika.loc['25%']
q50 = popisna_statistika.loc['50%']
q75 = popisna_statistika.loc['75%']
max_val = popisna_statistika.loc['max']

# ANOVA Testy
anova_vyska = f_oneway(*[group['height_m'].dropna() for name, group in pokemon_data_cleaned.groupby('type1')])
anova_vaha = f_oneway(*[group['weight_kg'].dropna() for name, group in pokemon_data_cleaned.groupby('type1')])
anova_utok = f_oneway(*[group['attack'].dropna() for name, group in pokemon_data_cleaned.groupby('type1')])

anova_vysledky = {
    'Atribut': ['Výška', 'Váha', 'Útok'],
    'F-Statistika': [anova_vyska.statistic, anova_vaha.statistic, anova_utok.statistic],
    'p-hodnota': [anova_vyska.pvalue, anova_vaha.pvalue, anova_utok.pvalue]
}

anova_vysledky_df = pd.DataFrame(anova_vysledky)

# Test normality (Shapiro-Wilk test)
shapiro_vyska = shapiro(pokemon_data_cleaned['height_m'])
shapiro_vaha = shapiro(pokemon_data_cleaned['weight_kg'])
shapiro_utok = shapiro(pokemon_data_cleaned['attack'])

normalita_vysledky = {
    'Atribut': ['Výška', 'Váha', 'Útok'],
    'W-statistika': [shapiro_vyska.statistic, shapiro_vaha.statistic, shapiro_utok.statistic],
    'p-hodnota': [shapiro_vyska.pvalue, shapiro_vaha.pvalue, shapiro_utok.pvalue]
}

normalita_vysledky_df = pd.DataFrame(normalita_vysledky)

# Výstup dat
print("Popisná statistika:")
print(popisna_statistika)
print("\nANOVA Výsledky:")
print(anova_vysledky_df)
print("\nVýsledky testu normality (Shapiro-Wilk):")
print(normalita_vysledky_df)



