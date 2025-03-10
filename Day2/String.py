def print_string_details(s):
    string_length = len(s)
    stripped_string = s.strip()  # Removes leading and trailing whitespace
    substring = stripped_string[7:18]  # Extracts "Programming"
    modified_string = stripped_string.replace("Python", "Java")  # Creates "Java Programming"
    concatenated_string = stripped_string + " is fun!"  # Concatenates strings
    formatted_string = f"{stripped_string} is a popular language."  # Uses f-string
    escaped_string = "He said, \"Python is awesome!\""  # Escape characters
    split_string = stripped_string.split()  # Splits into a list
    joined_string = " ".join(split_string)  # Joins list into a string

    print(f"The given string has length: {string_length}.")
    print(f"First character (ignoring spaces): {stripped_string[0]}")
    print(f"Last character (ignoring spaces): {stripped_string[-1]}")
    print(f"First six characters of the original string: {s[:6]}")  # Shows leading spaces
    print(f"Uppercase string: {s.upper()}")
    print(f"Replaced 'Python' with 'Java': {s.replace('Python', 'Java')}")
    print(f"Substring: {substring}")
    print(f"Modified string: {modified_string}")
    print(f"Concatenated string: {concatenated_string}")
    print(f"Formatted string: {formatted_string}")
    print(f"Escaped string: {escaped_string}")
    print(f"Stripped string: '{stripped_string}'")
    print(f"Split string: {split_string}")
    print(f"Joined string: {joined_string}")

def new_func():
    s = "  Python Programming  "
    print_string_details(s)

if __name__ == "__main__":
    new_func()
