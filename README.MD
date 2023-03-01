Download files from Unihan database and parses it.

Example for the "Readings" module:
```python
>>> from unihan import UnihanDatabase
>>> database = UnihanDatabase()
>>> readings = Readings(database)
>>> one = '一'
>>> readings.get_definition(one)
['one;', 'a,', 'an;', 'alone']
>>> readings.get_kunyomi(one)
['HITOTSU', 'HITOTABI', 'HAJIME']
>>> readings.get_tang_reading(one)
['*qit', 'qit']
>>> readings.get_korean_reading(one)
['일']
```