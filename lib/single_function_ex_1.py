

def text_passage(text):
    words_per_minute = 200
    if text == "":
        raise Exception("Text is empty")
    text_split = text.split()
    return len(text_split)/words_per_minute
