# JSON Query Opdrachten
Systeem: Win10 (x64), PowerShell

### Opdracht 1
Schrijf een query die de bevolkingsdichtheid in 1970 voor ieder land berekent.

##### Command 
```
jq "[.[] | {country: .country, density_1970: (.population_1970 / .area_km2)}]" world-population.json > DS-opdracht-1-output.json 
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
| map({continent: .continent, growth: (.tot2022 - .tot1970)})' world-population.json
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

### Opdracht 4
Schrijf een query/verzin een oplossing die per continent het percentage van de wereldbevolking van dat continent weergeeft.

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

### Opdracht 5
Schrijf een query/verzin een oplossing die per continent het percentage groei ten opzichte van 1970 weergeeft.

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

### Opdracht 6
Gebruik jq om een JSON-file naar een CSV-file om te zetten. Exporteer de resultaten van de vorige opdrachten naar een CVS-bestand. Lees deze bestanden vervolgens in een spreadsheet en maak grafieken van de data.

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

### Opdracht 7
Schrijf een query/verzin een oplossing die de data uit world-population.json omzet naar de volgende structuur:

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

