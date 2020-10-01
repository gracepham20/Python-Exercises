from enums import Session
from exception import InvalidValueException


class Step():
    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def getSess(self):
        return self.number_of_sessions

    def getStar(self):
        return self.number_of_stars

    def make_step(self):
        return self.convert(self.number_of_sessions, self.number_of_stars)

    @staticmethod
    def convert(sess, star):
        try:
            sess = Session.NUMBER_TO_TEXT_MAP[sess]
        except:
            raise InvalidValueException("Invalid number of sessions")

        if star in list(Session.NUMBER_TO_TEXT_MAP.values())[:5]:
            star = list(Session.NUMBER_TO_TEXT_MAP.keys())[list(Session.NUMBER_TO_TEXT_MAP.values()).index(star)]
        else:
            raise InvalidValueException("Invalid number of stars")

        return print(f"I completed {sess} sessions and I rated my expert {star} stars")
