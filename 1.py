countries_population = {}

try:
    with open("America.txt", "r") as file:
        for line in file:
            line = line.strip() 
            if " = " in line:
                country, population = line.split(" = ")
                try:
                    countries_population[country] = int(population)
                except ValueError:
                    print(f"Попередження: не вдалося перетворити населення для {country}")
            else:
                print(f"Попередження: некоректний формат у рядку: {line}")


    if countries_population:
        max_country = max(countries_population, key=countries_population.get)
        print(f"Країна з найбільшим населенням: {max_country} ({countries_population[max_country]})")
    else:
        print("Файл порожній або містить некоректні дані.")
    
    sorted_countries = sorted(countries_population.items(), key=lambda x: x[1], reverse=True)

    with open("sorted.txt", "w") as sorted_file:
        for country, population in sorted_countries:
            sorted_file.write(f"{country} = {population}\n")
    print("Результати успішно записані у файл sorted.txt")
    
except FileNotFoundError:
    print("Помилка: файл 'America.txt' не знайдено.")
