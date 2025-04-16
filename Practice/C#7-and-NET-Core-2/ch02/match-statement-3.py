def language(country):
    match country:
        case "au" | "uk" | "us":
            language = "English"
        case "at" | "de":
            language = "German"
    return language

for country in [ "au", "uk", "us", "at", "de"]:
    print(country,language(country))

$ python match-statement-3.py 
# au English
# uk English
# us English
# at German
# de German