from string import punctuation

def punctuation_count(text):
    count = 0
    for chr in text:
        if chr in punctuation:
            count += 1

    return count

def vowel_count(text):
    count = 0
    vowels = "AEIOUaeiou"
    for chr in text:
        if chr in vowels:
            count +=1
    
    return count

def word_count(lines):
    count = 0
    for line in lines:
        words = lines.split()
        count += len(words)
    
    return count

def line_count(lines):
    return len(lines)

def char_count(text):
    return len(text)

def read_file(file_path, flg):
    data = ''
    with open(file_path) as fh:
        if flg == 1:
            data = fh.read()
        elif flg == 2:
            data = fh.readlines()

        return data


def main():
    file_path = input("Enter the file_path: ")
    file_name = file_path.split("\\")[-1]

    data = read_file(file_path, 1)
    num_of_chars = char_count(data)
    num_of_vowels = vowel_count(data)
    num_of_punctuation = punctuation_count(data)

    data = read_file(file_path, 2)
    num_of_lines = line_count(data)
    num_of_words = word_count(data)

    # Open Summary Log and write it


if __name__ == '__main__':
    main()