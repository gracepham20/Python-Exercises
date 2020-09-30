# input 1
sen1 = "I completed 2 sessions and I rated my expert five stars"

# input 2
sen2 = "I completed 10 sessions and I rated my expert five stars"


# dictionary for number_of_sessions
convert_dict = {1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine"}


def choose(sentence):
    s = sentence.split()
    s0 = s[0:2] + s[3:9] + s[10:]
    s0 = " ".join(s0)
    if s0 != "I completed sessions and I rated my expert stars":
        return None, None
    sess = int(s[2])
    star = s[9]
    return sess, star


def convert(sentence):
    sess, star = choose(sentence)
    if sess is None:
        return "Input invalid"

    if sess in convert_dict.keys():
        sess = convert_dict[sess]
    else:
        return print("Sessions out of range")

    if star in list(convert_dict.values())[:5]:
        star = list(convert_dict.keys())[list(convert_dict.values()).index(star)]
    else:
        return print("Stars out of range")

    return print(f"I completed {sess} sessions and I rated my expert {star} stars")


convert(sen1)
convert(sen2)