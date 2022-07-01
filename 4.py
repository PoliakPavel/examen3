import string


class Alphabet:                                     # класс alphabet

    def __init__(self, language, letters_str):      # метод init и два динамических свойства
        self.lang = language
        self.letters = list(letters_str)

    def print(self):                                # матод print кот печатает альфавит
        print(self.letters)

    def letters_num(self):                         # метод возвращает кол-во букв альфавита
        len(self.letters)


class EngAlphabet(Alphabet):                      # класс - наследник

    __letters_num = 26                           # приватное статическое свойство, с количеством букв

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)   # вызываем родительский метод __init__ с нашими параметрами

    def is_en_letter(self, letter):             # метод проверки буквы в алфавите
        if letter.upper() in self.letters:
            return True
        return False

    def letters_num(self):                     # просто переопределение метода тк так хочет задание
        return EngAlphabet.__letters_num

    # Печатаем пример текста на английском языке
    @staticmethod
    def example():
        print("""English Example:
I'm learning Python.""")


eng_alphabet = EngAlphabet()
eng_alphabet.print()
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('F'))
print(eng_alphabet.is_en_letter('Щ'))
EngAlphabet.example()