# Add Punctuation
# Given a string of sentences with missing periods, add a period (".") in the following places:

# Before each space that comes immediately before an uppercase letter
# And at the end of the string
# Return the resulting string.
# 1. add_punctuation("Hello world") should return "Hello world."
# 2. add_punctuation("Hello world It's nice today") should return "Hello world. It's nice today."
# 3. add_punctuation("JavaScript is great Sometimes") should return "JavaScript is great. Sometimes."
# 4. add_punctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z") should return "A b c. D e. F g h. I. J k. L m n o. P. Q r. S t. U v w. X. Y. Z."
# 5. add_punctuation("Wait.. For it") should return "Wait... For it."
from typing import List
def add_punctuation(sentences:str) -> str:
    word_arr: List[str] = sentences.split()
    for i in range(0,len(word_arr)):
        if(i>0 and word_arr[i][0].isupper()):
            word_arr[i-1] += "."
    return " ".join(word_arr) + "."