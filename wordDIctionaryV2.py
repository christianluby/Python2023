from PyDictionary import PyDictionary

def main():
    dictionary = PyDictionary

    while True:
        word = input("Enter your word or press Enter to exit: ")
        if not word:
            break 

        meanings = dictionary.meaning(word)
        if meanings:
            print(f"Meanings: ")
            for part_of_speech, meaning_list in meanings.items():
                print(f"{part_of_speech.capitalize()}: ")
                for i, meaning in enumerate(meaning_list, start=1):
                    print(f"{i}. {meaning}")
        else: print("Word not found in the dictionary.")
if __name__=="__main__":
    main()