__author__ = 'mJr'

from random import randrange


def process_hits(action1, action2):

    if action1 == action2: return 0

    cond1 = action1 > action2
    cond2 = (action1 - action2) % 2 == 1

    if cond1 and cond2: return 1
    if cond1 or cond2: return -1

    return 1


def simulate_match():

    control = 0
    MAX = 50

    t = 0
    MAX_T = 5400

    score = {-MAX: 0, MAX: 0}

    while t < MAX_T:
        control += process_hits(randrange(0,3), randrange(0,3))
        t += 1
        print "T:%5d" % (t,), "|" + ("=" * ((MAX + control) / (MAX / 25))), ("+" * ((MAX - control + 1) / (MAX / 25))) + "|",\
            "CTRL: %4d, L:%3d, R:%3d" % (control, score[-MAX], score[MAX])
        if control == MAX or control == -MAX:
            score[control] += 1
            control = 0
