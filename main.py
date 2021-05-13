import pandas

ALPHABET_FILE_PATH = 'nato_phonetic_alphabet.csv'


def create_alphabet_from_file(filepath):
    return pandas.read_csv(filepath)


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet = create_alphabet_from_file(ALPHABET_FILE_PATH)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

