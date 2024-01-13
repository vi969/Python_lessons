import string
def longest_word_in_file(file_name: str) -> str:
    file = open(file_name, encoding="utf-8")
    input_string = file.read()
    file.close()
    translator = str.maketrans("", "", string.punctuation)
    no_punc = input_string.translate(translator).split()
    no_punc.sort(key=len)
    print(no_punc)
    return no_punc[-1]




out = longest_word_in_file("index.html")
print(out)