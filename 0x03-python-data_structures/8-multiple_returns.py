#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        s_l = len(sentence)
    else:
        s_l = 0
    return (s_l, sentence if not sentence else sentence[:1])
