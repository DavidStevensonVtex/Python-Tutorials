def language(country):
    match country:
        case "America" | "Britain":
            language = "English"
        case "France":
            language = "French"
        
    return language

for country in ["America", "Britain", "France"]:
    print(country, language(country))

# $ python match-statement-2.py 
# America English
# Britain English
# France French