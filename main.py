def main():
    path = input("Please enter the file name: ")
    text = read_contents(path)
    num_words = word_count(text)
    char_count_list = sorted(char_count(text), key=lambda x: x[1], reverse=True)
    print_report(path, num_words, char_count_list)

def read_contents(path):
    with open(path) as file:
        return file.read()

def word_count(file_contents):
   return len(file_contents.split())

def char_count(file_contents):
    file_contents = file_contents.lower()
    letters_dic = {}
    for letter in file_contents:
        if letter in letters_dic:
            letters_dic[letter] += 1
        else:
            letters_dic[letter] = 1
    return list(letters_dic.items())

def print_report(path, word_count, char_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in char_list:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")

main()

