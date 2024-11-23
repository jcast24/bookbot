def count_words(file):
    wordCount = file.split()
    return len(wordCount)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        print(count_words(file_contents))

if __name__ == "__main__":
    main()
