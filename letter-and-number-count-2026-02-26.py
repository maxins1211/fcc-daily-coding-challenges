# Given a string, return a message with the count of how many letters and numbers it contains.

# Letters are A-Z and a-z.
# Numbers are 0-9.
# Ignore all other characters.
# Return "The string has X letters and Y numbers.", where "X" is the count of letters and "Y" is the count of numbers. 
# If either count is 1, use the singular form for that item. E.g: "1 letter" instead of "1 letters" and "1 number" instead of "1 numbers".

import re
def count_letters_and_numbers(s: str) -> str:
    letter_counter: int = len(re.findall("[a-zA-z]",s))
    numb_counter: int = len(re.findall("[0-9]",s))
    result: str = "The string has "
    result += modify_str_with_counter(letter_counter,"letter") + " and " + modify_str_with_counter(numb_counter,"number") +"."
    return result

def modify_str_with_counter(counter: int, s: str) -> str:
    return str(counter) + " " + s if counter == 1 else str(counter) + " " + s + "s"
