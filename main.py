def count_words(file):
    wordCount = file.split()
    return len(wordCount)

def count_characters(file):
    count = {}
    lowered_file_text = file.lower()
    for letter in lowered_file_text:
        if letter.isalpha():
            if letter in count.keys():
                count[letter] +=1 
            else:
                count[letter] = 1
    return count



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()


        # print(count_words(file_contents))
        print(count_characters(file_contents))

if __name__ == "__main__":
    main()
