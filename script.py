import os
import re
import socket
from collections import Counter

# Contractions dictionary to handle common contractions
contractions = {
    "i've": "i have", "we've": "we have", "you've": "you have",
    "i'm": "i am", "you're": "you are", "they're": "they are", "we're": "we are",
    "he's": "he is", "she's": "she is", "it's": "it is", "that's": "that is",
    "there's": "there is", "who's": "who is",
    "isn't": "is not", "aren't": "are not", "wasn't": "was not", "weren't": "were not",
    "haven't": "have not", "hasn't": "has not", "hadn't": "had not",
    "won't": "will not", "wouldn't": "would not", "don't": "do not", "doesn't": "does not", "didn't": "did not",
    "can't": "cannot", "couldn't": "could not", "shouldn't": "should not", "mightn't": "might not", "mustn't": "must not"
}

# Function to handle contractions
def expand_contractions(text):
    for contraction, expanded in contractions.items():
        text = re.sub(r'\b' + contraction + r'\b', expanded, text)
    return text

# Function to process the file and count the word frequencies
def process_file(file_name):
    word_count = Counter()
    total_words = 0

    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading and trailing whitespace
                if line:  # Check if line is not empty
                    line = expand_contractions(line.lower())  # Expand contractions

                    # Split line into words, handling hyphens as word breaks
                    words = re.findall(r"[a-zA-Z0-9]+", line)  # Match individual words, splitting hyphenated words

                    total_words += len(words)

                    # Update word frequency map
                    for word in words:
                        word_count[word] += 1  # Count the word directly
    except IOError as e:
        print(f"Error reading file {file_name}: {e}")

    return total_words, word_count

# Function to write results to a text file
def write_results(file_path, total_words_file1, total_words_file2, grand_total, top3_words_file1, top3_words_file2, ip_address):
    try:
        with open(file_path, 'w') as file:
            file.write(f"Total words in IF.txt: {total_words_file1}\n")
            file.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words_file2}\n")
            file.write(f"Grand total of words: {grand_total}\n")
            file.write("Top 3 words in IF.txt:\n")
            for word, count in top3_words_file1:
                file.write(f"{word}: {count}\n")
            file.write("Top 3 words in AlwaysRememberUsThisWay.txt:\n")
            for word, count in top3_words_file2:
                file.write(f"{word}: {count}\n")
            file.write(f"IP Address: {ip_address}\n")
    except IOError as e:
        print(f"Error writing results: {e}")

# Function to read the results from the file and display
def read_results(file_path):
    try:
        with open(file_path, 'r') as file:
            print("Results:")
            for line in file:
                print(line.strip())
    except IOError as e:
        print(f"Error reading results: {e}")

# Main function to handle the processing
def main():
    file_names = ["IF.txt", "AlwaysRememberUsThisWay.txt"]
    
    # Process files
    total_words_file1, word_count_file1 = process_file(file_names[0])
    total_words_file2, word_count_file2 = process_file(file_names[1])

    grand_total = total_words_file1 + total_words_file2

    # Find top 3 words in IF.txt
    top3_words_file1 = word_count_file1.most_common(3)

    # Find top 3 words in AlwaysRememberUsThisWay.txt
    top3_words_file2 = word_count_file2.most_common(3)

    # Get the machine's IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Write results to result.txt
    result_file_path = "output/result.txt"
    write_results(result_file_path, total_words_file1, total_words_file2, grand_total, top3_words_file1, top3_words_file2, ip_address)

    # Read and print the results
    read_results(result_file_path)

# Run the main function
if __name__ == "__main__":
    main()
