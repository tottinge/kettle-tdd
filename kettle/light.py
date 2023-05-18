class Light:
    def turn_on(self):
        self._lit = True

    def turn_off(self):
        self._lit = False

    def is_lit(self):
        return self._lit
