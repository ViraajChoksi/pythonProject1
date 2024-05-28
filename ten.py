def calculate_serial_sum(word):
    word = word.upper()
    serial_sum = sum(ord(char) - ord('A') + 1 for char in word)
    return serial_sum


def vowelnos(word):
    vowels = "AEIOU"
    return sum(1 for char in word if char in vowels)


def generate_words(word, length):
    vowels_count = vowelnos(word)
    generated_words = []

    # Generate all possible combinations of length letters
    for i in range(1, 27 ** length):
        new_words = ""
        n = i
        for _ in range(length):
            new_words = chr((n - 1) % 26 + ord('A')) + new_words
            n = (n - 1) // 26

        if vowelnos(new_words) == vowels_count:
            generated_words.append(new_words)

    return generated_words


def find_matching_words(wordin):
    wordin = wordin.upper()
    inputed_sum = calculate_serial_sum(wordin)
    length = len(wordin)

    generated_words = generate_words(wordin, length)

    matching_words = []
    for word in generated_words:
        if calculate_serial_sum(word) == inputed_sum:
            matching_words.append(word)

    return matching_words


# Example usage
wordin = input("Input Word: ")
matching_words = find_matching_words(wordin)
final = []
for p in matching_words:
    if p not in final:
        final.append(p)

print(f"Input Word:", wordin)
print("Matching Words:", final)
print("Number of Matching Words:", len(final))
