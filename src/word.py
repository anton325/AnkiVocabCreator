class Word:
    def __init__(self, word_left: str, word_right: str):
        self._word_left: str = word_left
        self._word_right: str = word_right
    
    def get_left_word(self) -> str:
        return self._word_left
    
    def get_right_word(self) -> str:
        return self._word_right