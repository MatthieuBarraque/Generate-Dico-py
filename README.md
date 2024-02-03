# Word Combination Generator by D3sir3

This project contains a Python program that generates combinations of words based on the input provided by the user.

## Files

- `generate_dico.py`: This is the main script that generates combinations of words.
- `search_words.py`: This script is used to search for specific words in the generated combinations.

## How to Use

1. Run the `generate_dico.py` script and provide a list of words as input. The script will generate all possible combinations of these words and output them.
2. If you want to search for specific words in the generated combinations, you can use the `search_words.py` script.

## Example

If you provide the words "apple", "banana", and "cherry" as input to the `generate_dico.py` script, it will generate combinations like "applebanana", "bananacherry", "cherryapple", and so on.

## Note

The `generate_dico.py` script also supports special characters. If a special character is included in the input words, it will be used as a separator in the generated combinations. For example, if you provide the words "apple", "banana", "cherry", and "?" as input, the script will generate combinations like "apple?banana", "banana?cherry", "cherry?apple", and so on.