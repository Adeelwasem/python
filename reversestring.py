class ReverseString:
    def __init__(self, input_string):
        
        self._original_string = input_string 

    def _reverse_words_logic(self):
        
        words = self._original_string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

    def __str__(self):
        
        return f"Original: '{self._original_string}', Reversed Word by Word: '{self.get_reversed_string()}'"

    def get_reversed_string(self):
        
        return self._reverse_words_logic()


my_string_reverser = ReverseString("This is a test string")
print(my_string_reverser.get_reversed_string())
print(my_string_reverser) 