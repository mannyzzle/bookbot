def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(file):
    with open(file) as f:
        file_contents = f.read()
        count = len(file_contents.split())
    return count

def get_char_count(file):
    with open(file) as f:
        characters = {}
        file_contents = f.read()
        lower = file_contents.lower()
    for c in lower:
        if c not in characters:
             characters[c] = 1
        else:
            characters[c] += 1
    return characters


def report(file):
    characters = get_char_count(file)
    return dict(sorted(characters.items(),key=lambda item: item[1], reverse=True))


