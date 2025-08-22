
def process_file():
    with open("input.txt", "r") as file:
        content = file.read()
        word_count = len(content.split())
        uppercase_content = content.upper()

        with open("output.text", "w") as output_file:
            output_file.write(f"Number of words: {word_count}\n")
            output_file.write(f"Uppercase content:\n{uppercase_content}")

    print("File processing completed.")


process_file()
