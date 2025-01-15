# read the frankenstein book.

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        lines = file_contents.split()
        characters = count_characters(lines)

    print(f"there is {len(lines)} words")
    print(f"unique characters: {characters}")
    print_report(characters, 'Frankenstein')

def count_characters(lines):
    characters = {}
    for line in lines:
        line = line.lower()
        for char in line:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def print_report(characters, report_name):
    print(f"--Printing book {report_name} report.....--")
    for line, num in sorted(characters.items(), key=lambda item: item[1]):
        print(f"The character {line} was found {num} times.")
    print('---End report---')

main()
    