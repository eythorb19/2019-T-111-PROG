years_str = input("Years: ")
years_int = int(years_str)

if years_int >= 0:
    # rates are in seconds
    birth_rate = 7
    death_rate = 13
    new_immigrant_rate = 35

    current_population = 307357870
    seconds_in_year = 365 * 24 * 60 * 60

    births = seconds_in_year / birth_rate
    deaths = seconds_in_year / death_rate
    new_immigrants = seconds_in_year / new_immigrant_rate

    total_addition_one_year = births - deaths + new_immigrants

    new_population = current_population + total_addition_one_year * years_int

    print("New population after", years_int, "years is", int(new_population))
else:
    print("Invalid input!")