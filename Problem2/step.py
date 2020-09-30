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
        return self.conversion("I completed " + str(self.getSess()) + " sessions and I rated my expert " + str(self.getStar()) + " stars")

    def choose(self, sentence):
        sess = int(sentence.split()[2])
        star = sentence.split()[9]
        return sess, star

    def conversion(self, sentence):
        sess, star = self.choose(sentence)

        try:
            sess = Session.NUMBER_TO_TEXT_MAP[sess]
        except:
            raise InvalidValueException("Invalid number of sessions")

        try:
            star = Session.TEXT_TO_NUMBER_MAP[star]
        except:
            raise InvalidValueException("Invalid number of stars")

        return print("I completed", str(sess), "sessions and I rated my expert", str(star), "stars")

    
Step(2, "five").make_step()
Step(0, "five").make_step()
Step(2, "ten").make_step()