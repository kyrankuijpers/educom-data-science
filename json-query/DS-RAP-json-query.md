
# JSON Query Opdrachten
Systeem: Win10 (x64), Gitbash, installatie via winget

### Opdracht 1 
Schrijf een query die de bevolkingsdichtheid in 1970 voor ieder land berekent.

##### Command 
```
jq '[.[] 
| {country: .country, 
   density_1970: (.population_1970 / .area_km2)}]' world-population.json > DS-jq-opdracht-1-output.json 
```
##### JSON 
```json
[
  {
    "country": "Afghanistan",
    "density_1970": 16.48647103015807
  },
  {
    "country": "Albania",
    "density_1970": 80.86583414498399
  },
...etc
]
```

### Opdracht 2
Schrijf een query/verzin een oplossing die per continent de absolute bevolkingsgroei tussen 1970 en 2022 weergeeft.

##### Command 
```
jq 'group_by(.continent) 
| map({
    continent: .[0].continent,
    tot2022: map(.population_2022) | add,
    tot1970: map(.population_1970) | add
    })
| map({continent: .continent, growth: (.tot2022 - .tot1970)})' world-population.json > DS-jq-opdracht-2-output.json
```
##### JSON 
```json
[
  {
    "continent": "Africa",
    "growth": 1061286584
  },
  {
    "continent": "Asia",
    "growth": 2576476984
  },
  {
    "continent": "Europe",
    "growth": 87223547
  },
  {
    "continent": "North America",
    "growth": 284861530
  },
  {
    "continent": "Oceania",
    "growth": 25558284
  },
  {
    "continent": "South America",
    "growth": 243869452
  }
]
```

### Opdracht 3
Schrijf een query/verzin een oplossing die per continent de absolute aantallen per gegeven jaar weergeeft.

##### Command 
```
jq 'group_by(.continent) 
| map({
    continent: .[0].continent,
    tot2022: map(.population_2022) | add,
    tot2020: map(.population_2020) | add,
    tot2015: map(.population_2015) | add,
    tot2010: map(.population_2010) | add,
    tot2000: map(.population_2000) | add,
    tot1990: map(.population_1990) | add,
    tot1980: map(.population_1980) | add,
    tot1970: map(.population_1970) | add
    })' world-population.json > DS-jq-opdracht-3-output.json
```
##### JSON 
```json
[
  {
    "continent": "Africa",
    "tot2022": 1426730932,
    "tot2020": 1360671810,
    "tot2015": 1201102442,
    "tot2010": 1055228072,
    "tot2000": 818946032,
    "tot1990": 638150629,
    "tot1980": 481536377,
    "tot1970": 365444348
  },
  {
    "continent": "Asia",
    "tot2022": 4721383274,
    "tot2020": 4663086535,
    "tot2015": 4458250182,
    "tot2010": 4220041327,
    "tot2000": 3735089604,
    "tot1990": 3210563577,
    "tot1980": 2635334228,
    "tot1970": 2144906290
  },
  {
    "continent": "Europe",
    "tot2022": 743147538,
    "tot2020": 745792196,
    "tot2015": 741535608,
    "tot2010": 735613934,
    "tot2000": 726093423,
    "tot1990": 720320797,
    "tot1980": 692527159,
    "tot1970": 655923991
  },
  {
    "continent": "North America",
    "tot2022": 600296136,
    "tot2020": 594236593,
    "tot2015": 570383850,
    "tot2010": 542720651,
    "tot2000": 486069584,
    "tot1990": 421266425,
    "tot1980": 368293361,
    "tot1970": 315434606
  },
  {
    "continent": "Oceania",
    "tot2022": 45038554,
    "tot2020": 43933426,
    "tot2015": 40403283,
    "tot2010": 37102764,
    "tot2000": 31222778,
    "tot1990": 26743822,
    "tot1980": 22920240,
    "tot1970": 19480270
  },
  {
    "continent": "South America",
    "tot2022": 436816608,
    "tot2020": 431530043,
    "tot2015": 413134396,
    "tot2010": 393078250,
    "tot2000": 349634282,
    "tot1990": 297146415,
    "tot1980": 241789006,
    "tot1970": 192947156
  }
]
```

### Opdracht 4
Schrijf een query/verzin een oplossing die per continent het percentage van de wereldbevolking van dat continent weergeeft.

##### Command
```
jq '(map(.population_2022)| add) as $world
| group_by(.continent)
| map({
    continent: .[0].continent,
    continent_population: (((map(.population_2022) | add) / $world) * 100),
})' world-population.json > DS-jq-opdracht-4-output.json
```
##### JSON 
```json
[
  {
    "continent": "Africa",
    "pcworld": 17.869999999999997
  },
  {
    "continent": "Asia",
    "pcworld": 59.19
  },
  {
    "continent": "Europe",
    "pcworld": 9.33
  },
  {
    "continent": "North America",
    "pcworld": 7.51
  },
  {
    "continent": "Oceania",
    "pcworld": 0.55
  },
  {
    "continent": "South America",
    "pcworld": 5.4799999999999995
  }
]
```
### Opdracht 5
Schrijf een query/verzin een oplossing die per continent het percentage groei ten opzichte van 1970 weergeeft.

##### Command 
```
jq 'group_by(.continent) 
| map({
    continent: .[0].continent, 
    pop2022: map(.population_2022) | add, 
    pop1970: map(.population_1970) | add}) 
| map({
  continent: .continent, 
  pcgrowth: ((.pop2022 - .pop1970) / .pop2022 * 100)})' world-population.json > DS-jq-opdracht-5-output.json 
```
##### JSON 
```json
[
  {
    "continent": "Africa",
    "pcgrowth": 74.3858957702895
  },
  {
    "continent": "Asia",
    "pcgrowth": 54.570384026823234
  },
  {
    "continent": "Europe",
    "pcgrowth": 11.737043122653795
  },
  {
    "continent": "North America",
    "pcgrowth": 47.45350051695152
  },
  {
    "continent": "Oceania",
    "pcgrowth": 56.74756787262753
  },
  {
    "continent": "South America",
    "pcgrowth": 55.828795776922476
  }
]
```

### Opdracht 6
Gebruik jq om een JSON-file naar een CSV-file om te zetten. Exporteer de resultaten van de vorige opdrachten naar een CVS-bestand. Lees deze bestanden vervolgens in een spreadsheet en maak grafieken van de data.

#### 6.1

##### Command 
```
jq -r '(.[0] | keys_unsorted) as $keys 
| $keys, map([.country, .density_1970]).[] | @csv'
 DS-jq-opdracht-1-output.json > DS-jq-opdracht-1-output.csv
```
##### CSV 
```
"country","density_1970"
"Afghanistan",16.48647103015807
"Albania",80.86583414498399
... etc
```

#### 6.2

##### Command 
```
jq -r '(.[0] | keys_unsorted) as $keys 
| $keys, map([.continent, .growth]).[] | @csv' DS-jq-opdracht-2-output.json > DS-jq-opdracht-2-output.csv
```
##### CSV 
```
"continent","growth"
"Africa",1061286584
"Asia",2576476984
"Europe",87223547
"North America",284861530
"Oceania",25558284
"South America",243869452
```

#### 6.3

##### Command 
```
jq -r '(.[0] | keys_unsorted) as $keys 
| $keys, map([.continent, .tot2022, .tot2020, .tot2015, .tot2010, .tot2000, .tot1990, .tot1980, .tot1970]).[] | @csv' DS-jq-opdracht-3-output.json > DS-jq-opdracht-3-output.csv
```
##### CSV 
```
"continent","tot2022","tot2020","tot2015","tot2010","tot2000","tot1990","tot1980","tot1970"
"Africa",1426730932,1360671810,1201102442,1055228072,818946032,638150629,481536377,365444348
"Asia",4721383274,4663086535,4458250182,4220041327,3735089604,3210563577,2635334228,2144906290
"Europe",743147538,745792196,741535608,735613934,726093423,720320797,692527159,655923991
"North America",600296136,594236593,570383850,542720651,486069584,421266425,368293361,315434606
"Oceania",45038554,43933426,40403283,37102764,31222778,26743822,22920240,19480270
"South America",436816608,431530043,413134396,393078250,349634282,297146415,241789006,192947156
```

#### 6.4

##### Command 
```
jq -r '(.[0] | keys_unsorted) as $keys 
| $keys, map([.continent, .pcworld]).[] | @csv' DS-jq-opdracht-4-output.json > DS-jq-opdracht-4-output.csv
```
##### CSV 
```
"continent","pcworld"
"Africa",17.893603711292595
"Asia",59.21408121127158
"Europe",9.320319091529134
"North America",7.528722428374607
"Oceania",0.5648591608481732
"South America",5.478414396683904
```

#### 6.5

##### Command 
```
jq -r '(.[0] | keys_unsorted) as $keys 
| $keys, map([.continent, .pcgrowth]).[] | @csv' DS-jq-opdracht-5-output.json > DS-jq-opdracht-5-output.csv
```
##### CSV 
```
"continent","pcgrowth"
"Africa",74.3858957702895
"Asia",54.570384026823234
"Europe",11.737043122653795
"North America",47.45350051695152
"Oceania",56.74756787262753
"South America",55.828795776922476
```

### Opdracht 7
Schrijf een query/verzin een oplossing die de data uit world-population.json omzet naar de volgende structuur:

##### Command 
```
jq 'map({
    rank: .rank,
    cca3: .cca3,
    country: .country,
    capital: .capital,
    continent: .continent, 
    population: 
        [
          {year: 2022, population: .population_2022}, 
          {year: 2020, population: .population_2020},
          {year: 2015, population: .population_2015},
          {year: 2010, population: .population_2010},
          {year: 2000, population: .population_2000},
          {year: 1990, population: .population_1990},
          {year: 1980, population: .population_1980},
          {year: 1970, population: .population_1970}
        ],
    area_km2: .area_km2,
    population_density: .population_density,
    population_growth_rate: .population_growth_rate,
    percentage_world_population: .percentage_world_population
    })' world-population.json > DS-jq-opdracht-7-output.json
```
##### JSON 
```json
[
  {
    "rank": 36,
    "cca3": "AFG",
    "country": "Afghanistan",
    "capital": "Kabul",
    "continent": "Asia",
    "population": [
      {
        "year": 2022,
        "population": 41128771
      },
      {
        "year": 2020,
        "population": 38972230
      },
      {
        "year": 2015,
        "population": 33753499
      },
      {
        "year": 2010,
        "population": 28189672
      },
      {
        "year": 2000,
        "population": 19542982
      },
      {
        "year": 1990,
        "population": 10694796
      },
      {
        "year": 1980,
        "population": 12486631
      },
      {
        "year": 1970,
        "population": 10752971
      }
    ],
    "area_km2": 652230,
    "population_density": 63.0587,
    "population_growth_rate": 1.0257,
    "percentage_world_population": 0.52
  },
  {
    ... etc
```

### Opdracht 8
Bedenk een manier om de informatie uit world-population.json in een MySQL database op te nemen. Normaliseer de data aan de hand van "Codd" en formateer de data met behulp van jq.

##### Command 
```
This is cmd code
```
##### JSON 
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```