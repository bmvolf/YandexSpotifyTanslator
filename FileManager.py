def write(text):
    with open("file.txt", "wt", encoding="utf-8") as file:
        file.write(f"{text}\n")
def read():
    with open("file.txt", "rt", encoding="utf-8") as file:
        return file.read()