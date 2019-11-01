import string

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def build_dict(file_stream):
    ''' Extracts abbreviations and their corresponding English phrases from 
        a file stream, builds and returns a translation dictionar '''
    trans_dict = {}
    for line in file_stream:
        abbrev, translation = line.split(':')
        trans_dict[abbrev] = translation.strip()
    return trans_dict

def translate_abbrev(abbrev, translate_dict):
    ''' Returns a translation of a single abbreviation
        If the abbrevation ends with a punctuation mark, it remains a part of the translation '''
    last_char = abbrev[-1]
    if last_char in string.punctuation:
        abbrev = abbrev[:-1]
    else:
        last_char = ''
    
    if abbrev in translate_dict:
        word = translate_dict[abbrev]
    else:
        word = abbrev
    
    return word + last_char

def translate_message(message, translation_dict):
    ''' Returns a translation of a single message, consisting of a sequence of abbreviations '''
    translation = ''
    the_parts = message.split()

    for abbrev in the_parts:
        translation += translate_abbrev(abbrev, translation_dict) + " "

    return translation

def translate(translate_dict):
    ''' Translates a sequence of messages input by the user using the given dictionary '''
    message = input("Enter a message: ")
    while message != 'q':
        translation = translate_message(message, translate_dict)
        print(translation)
        message = input("Enter a message: ")

def main():
    mapping_file = input("Enter name of mapping file: ")
    file_stream = open_file(mapping_file)
    if file_stream:
        translation_dict = build_dict(file_stream)
        file_stream.close()
        translate(translation_dict)
main()
