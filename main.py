# Made by Xavier Moorman en 2023, aidé par Alexandre Wilbur et Mathéo Bui
import colorama
def wordcounter():
    debut_phrase = 0
    fin_phrase = 1
    phrase = str(input("Donnez-moi votre phrase!: "))
    word_count = len(phrase .split())
    print(colorama.Fore.MAGENTA + "Nombre de mots = ", word_count)
    word_count = 0

wordcounter()

#while fin_phrase < longueur_phrase:
    #characters_counted = phrase[debut_phrase:fin_phrase]
    # phrase[0:1] 1= fin de phrase 0 = debut de phrase
    #debut_phrase = debut_phrase + 1
    #fin_phrase = debut_phrase + 1
    #if characters_counted == " ":
        #word_count = word_count + 1
    # elif characters_counted != " ":
    #if fin_phrase == longueur_phrase:
        #print("Nombre de mots =", word_count + 1)

