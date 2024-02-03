def search_word_in_file(filename, search_word):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines, start=1):
            words = line.strip().split()
            if search_word in words:
                print(f"Mot trouvé à la ligne {i}: {line.strip()}")

    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")

if __name__ == "__main__":
    filename = input("Entrez le nom du fichier texte à rechercher : ")
    search_word = input("Entrez le mot à rechercher : ")

    search_word_in_file(filename, search_word)

