"""Help Stephen to create a module for converting a normal time string to a
   morse time string. """

def checkio(time_string):
    # first, split up the time_string into hours, minutes, seconds
    tt = time_string.split(':')
    hours, min, sec = int(tt[0]), int(tt[1]), int(tt[2])

    # now, make sure each value has a zero following it.
    # this is really hacky right now. need to improve it.
    if len(str(hours))<2:
        hours *= 10
    if len(str(min)) < 2:
        min *= 10
    if len(str(sec)) < 2:
        sec *= 10

    # start doing conversion to binary for each.
    # remember that python's bin() spits it out as '0b...'


    # now convert binary into Morse Code.
    # 0=. and 1=-


    #return the solution
    return ".- .... : .-- .--- : -.. -..-"

if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"