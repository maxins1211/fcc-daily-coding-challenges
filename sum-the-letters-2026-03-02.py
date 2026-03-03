# Given a string, return the sum of its letters.

# Letters are A-Z in uppercase or lowercase
# Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
# Uppercase and lowercase letters have the same value.
# Ignore all non-letter characters.
# 1. sum_letters("Hello") should return 52.
# 2. sum_letters("freeCodeCamp") should return 94.
# 3. sum_letters("The quick brown fox jumps over the lazy dog.") should return 473.
# 4. sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.") should return 1681.
# 5. sum_letters("</404>") should return 0.

def sum_letters(s:str)->int:
    sum: int = 0
    for char in s.upper():
        if (ord(char)>=65 and ord(char) <=90):
            sum += ord(char) - 64
    return sum