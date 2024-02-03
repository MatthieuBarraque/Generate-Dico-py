import itertools

def generate_combinations(keywords, special_char=None, max_words=1000000):
    unique_combinations = set()
    keywords.sort(key=len)
    keywords = [keyword.lower() for keyword in keywords]

    special_chars = ['?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '`', '~']
    special_char = next((char for char in special_chars if char in keywords), None)

    for r in range(1, len(keywords) + 1):
        for combination in itertools.product(keywords, repeat=r):
            if special_char:
                combined_word = special_char.join(combination)
            else:
                combined_word = ''.join(combination)

            unique_combinations.add(combined_word)
            if len(unique_combinations) >= max_words:
                return list(unique_combinations)[:max_words]
    combinations_with_capital = [word.capitalize() for word in list(unique_combinations)]
    return combinations_with_capital

def ascii_art_header():
    print("""
    8888888b.  8888888888 .d8888b.  888    d8P  
    888   Y88b 888       d88P  Y88b 888   d8P   
    888    888 888       Y88b.      888  d8P    
    888   d88P 8888888    "Y888b.   888d88K     
    8D3SIR3"  888           "Y88b. 8888888b    
    888        888             "888 888  Y88b   
    888        888       Y88b  d88P 888   Y88b  
    888        8888888888 "Y8888P"  888    Y88b 
    """)

def main():
    ascii_art_header()
    print("Générateur de combinaisons - Made by D3sir3\n")
    print("Combien de mots-clés voulez-vous entrer?")
    try:
        nombre_mots = int(input("Entrez un nombre: "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    mots = []
    for i in range(1, nombre_mots + 1):
        mot = input(f"Mot {i}: ").strip()
        mots.append(mot)

    combinations = generate_combinations(mots)
    with open('my_Dico.txt', 'w') as file:
        for word in combinations:
            file.write(word + '\n')

    print(f"\n{len(combinations)} mélanges ont été générés et sauvegardés dans 'my_Dico.txt'.")

if __name__ == "__main__":
    main()
