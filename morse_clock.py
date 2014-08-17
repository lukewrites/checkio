"""Help Stephen to create a module for converting a normal time string to a
   morse time string. """

def checkio(time_string):
    # first, split up the time_string into hours, minutes, seconds
    tt = time_string.split(':')  # split it up into h/m/s
    tt = [num.zfill(2) for num in tt]  # make sure h/m/s are all two digit
    hours, min, sec = tt[0], tt[1], tt[2]  # got 'em.

    # start doing conversion to binary for each.
    h1, h2 = str(bin(int(hours[0])))[2:].zfill(2),
             str(bin(int(hours[1])))[2:].zfill(4)
    m1, m2 = str(bin(int(min[0])))[2:].zfill(3), str(bin(int(min[1])))[2:].zfill(4)
    s1, s2 = str(bin(int(sec[0])))[2:].zfill(3), str(bin(int(sec[1])))[2:].zfill(4)

    # # now convert binary into Morse Code.
    # # 0=. and 1=-
    final = h1 + " " + h2 + ' : ' + m1 + ' ' + m2 + ' : ' + s1 + ' ' + s2
    final = final.replace('0', '.').replace('1', '-')
    # i didn't know you can do a double method call. that's awesome.

    #return the solution
    return final

if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"