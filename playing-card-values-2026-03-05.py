# Playing Card Values
# Given an array of playing cards, return a new array with the numeric value of each card.

# Card Values:

# An Ace ("A") has a value of 1.
# Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
# Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
# Suits:

# Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
# Card Format:

# Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.
# card_values(["3H", "4D", "5S"]) should return [3, 4, 5].
# card_values(["AS", "10S", "10H", "6D", "7D"]) should return [1, 10, 10, 6, 7].
# card_values(["8D", "QS", "2H", "JC", "9C"]) should return [8, 10, 2, 10, 9].
# card_values(["AS", "KS"]) should return [1, 10].
# card_values(["10H", "JH", "QH", "KH", "AH"]) should return [10, 10, 10, 10, 1].

from typing import List, Dict
card_num: Dict[str,int] = {
    "A" : 1,
    "J": 10,
    "Q": 10,
    "K": 10
}
def card_values(cards: List[str]) -> List[int]:
    values_only: List[str] = [card[:-1] for card in cards]
    result: List[int] = []
    for card in values_only:
        if(card_num.get(card) != None):  
            result.append(card_num.get(card))
        else:
            result.append(int(card))
    return result