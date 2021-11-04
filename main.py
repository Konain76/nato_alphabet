import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)



word = input("Enter a word: ").upper()
is_on = True
while is_on:
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("enter a word not number")
        word = input("Enter a word: ").upper()
    else:
        print(output_list)

        is_on = False







