import pandas

ALPHABET_FILE_PATH = 'nato_phonetic_alphabet.csv'


def create_alphabet_from_file(filepath):
    raw_data = pandas.read_csv(filepath)
    return {row[0]:row[1] for (index, row) in raw_data.iterrows()}

def is_word(word):
    return ' ' in word

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet = create_alphabet_from_file(ALPHABET_FILE_PATH)

# Create a list of the phonetic code words from a word that the user inputs.
word = input('Write a word to know its NATO alphabetization: ')
if is_word(word):
    pass
else:
    print('Write one word next time please')