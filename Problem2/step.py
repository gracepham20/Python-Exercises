from enums import Session


class InvalidValueException(Exception):
    def __init__(self, message):
        self.message = str(message)

    def InvalidValueException(self):
        pass


class Step():
    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def getSess(self):
        return self.number_of_sessions

    def getStar(self):
        return self.number_of_stars

    def make_step(self):
        return self.conversion("I completed " + str(self.getSess()) + " sessions and I rated my expert "
                               + str(self.getStar()) + " stars")

    @staticmethod
    def choose(sentence):
        s = sentence.split()
        sess = int(s[2])
        star = s[9]
        return sess, star

    def conversion(self, sentence):
        sess, star = self.choose(sentence)

        try:
            sess = Session.NUMBER_TO_TEXT_MAP[sess]
        except:
            raise InvalidValueException("Invalid number of sessions")

        if star in list(Session.NUMBER_TO_TEXT_MAP.values())[:5]:
            star = list(Session.NUMBER_TO_TEXT_MAP.keys())[list(Session.NUMBER_TO_TEXT_MAP.values()).index(star)]
        else:
            raise InvalidValueException("Invalid number of stars")

        return print(f"I completed {sess} sessions and I rated my expert {star} stars")

    
Step(2, "five").make_step()
Step(0, "five").make_step()
Step(2, "ten").make_step()