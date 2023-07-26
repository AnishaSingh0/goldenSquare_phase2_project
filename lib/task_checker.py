
def is_task(text):
    if text == "":
        raise Exception("No text input")
    return "#TODO" in text