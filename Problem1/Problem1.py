# input 1
sen1 = "I completed 2 sessions and I rated my expert five stars"

# input 2
sen2 = "I completed 10 sessions and I rated my expert five stars"


# dictionary for number_of_sessions
convert_sessions = {1: "one",
                    2: "two",
                    3: "three",
                    4: "four",
                    5: "five",
                    6: "six",
                    7: "seven",
                    8: "eight",
                    9: "nine"}

# dictionary for number_of_stars
convert_stars = {"one": 1,
                 "two": 2,
                 "three": 3,
                 "four": 4,
                 "five": 5}


def choose(sentence):
    sess = int(sentence.split()[2])
    star = sentence.split()[9]
    return sess, star


def conversion(sentence):
    sess, star = choose(sentence)
    if sess in convert_sessions.keys():
        sess = convert_sessions[sess]
    else:
        return "Sessions out of range"

    if star in convert_stars.keys():
        star = convert_stars[star]
    else:
        return "Stars out of range"

    return print("I completed", sess, "sessions and I rated my expert", star, "stars")


conversion(sen1)
conversion(sen2)
