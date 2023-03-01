from unihan import UnihanDatabase

# Exception
class IncorrectDataException(ValueError): pass

class Readings():
    def __init__(self, database: UnihanDatabase):
        """
        Create a readings object
        :param database: Pointer to UnihanDatabase object
        """
        self.__database = database.database

    def __get_reading(self, field_name: str, character: str) -> list[list[str]]:
        """
        Get a specific Chinese character's reading
        :param field_name: Name of reading
        :param character: Chinese character to check
        :raises IncorrectDataException: if character is not a single character, character has not been found in the database or this character doesn't have such reading
        :return: List of reading(s) of Chinese character
        """
        if len(character) != 1: raise IncorrectDataException(f'Expected a character, but string of length {len(character)} found')
        if character not in self.__database: raise IncorrectDataException('Character not found')
        if field_name not in self.__database[character]: raise IncorrectDataException(f'This character has no {field_name[1:]} reading.')
        return self.__database[character][field_name].split(':')[0].split(' ')

    # Getters
    def get_cantonese_reading(self, cjk_character: str) -> list[str]: return self.__get_reading('kCantonese', cjk_character)
    def get_definition(self, cjk_character: str) -> list[str]: return self.__get_reading('kDefinition', cjk_character)
    def get_hangul_reading(self, cjk_character: str) -> list[str]: return self.__get_reading('kHangul', cjk_character)
    def get_korean_reading(self, cjk_character: str) -> list[str]: return self.__get_reading('kKorean', cjk_character)
    def get_kunyomi(self, cjk_character: str) -> list[str]: return self.__get_reading('kJapaneseKun', cjk_character)
    def get_mandarin_reading(self, cjk_character: str) -> list[str]: return self.__get_reading('kMandarin', cjk_character)
    def get_tang_reading(self, cjk_character: str) -> list[str]: return self.__get_reading('kTang', cjk_character)
    def get_onyomi(self, cjk_character: str) -> list[str]: return self.__get_reading('kJapaneseOn', cjk_character)
    def get_vietnamese_reading(self, cjk_character: str) -> list[str]: return self.__get_reading('kVietnamese', cjk_character)
