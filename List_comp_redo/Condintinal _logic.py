
## you can add a conditional logic statement after in the in stament to add some logic to list comprehension

numbers=[1,2,3,4,5,6]

evens=[nums for nums in numbers if  nums%2==0]

odds=[nums for nums in numbers if nums%2 !=0]



with_vowels=" this is so much fun"

[char for char in with_vowels if char not in "aeiou"]


" ".join(char for char in with_vowels if char not in "aeiou")