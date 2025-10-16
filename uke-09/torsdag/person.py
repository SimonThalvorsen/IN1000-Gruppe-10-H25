class Person:
    def __init__(self,navn,rolle):
        self._navn = navn
        self._rolle = rolle

    def __str__(self):
        return self._navn

    