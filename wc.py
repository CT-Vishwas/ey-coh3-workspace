from string import punctuation

VOWELS = "AEIOUaeiou"
OUTPUT_FILE = "summary.log"

def punctuation_count(text):
    count = 0
    for chr in text:
        if chr in punctuation:
            count += 1

    return count

def vowel_count(text):
    count = 0
    for chr in text:
        if chr in VOWELS:
            count +=1
    
    return count

def word_count(lines):
    count = 0
    for line in lines:
        words = line.split()
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
    meta_data = ["num_of_chars","num_of_vowels", "num_of_punctuation", "num_of_lines", "num_of_words" ]
    summary = dict.fromkeys(meta_data, 0)

    file_path = input("Enter the file_path: ")
    file_name = file_path.split("\\")[-1]

    data = read_file(file_path, 1)
    summary["num_of_chars"] = char_count(data)
    summary["num_of_vowels"] = vowel_count(data)
    summary["num_of_punctuation"] = punctuation_count(data)

    data = read_file(file_path, 2)
    summary["num_of_lines"] = line_count(data)
    summary["num_of_words"] = word_count(data)

    # Open Summary Log and write it
    with open(OUTPUT_FILE,"at") as fw:
        fw.write("\nFile Name: "+ file_name+"\n")
        fw.write("-"*50+"\n")
        for k,v in summary.items():
            fw.write(k+":"+str(v)+"\n")

if __name__ == '__main__':
    main()