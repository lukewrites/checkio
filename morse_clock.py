"""Help Stephen to create a module for converting a normal time string to a
   morse time string. """

def checkio(time_string):
    # first, split up the time_string into hours, minutes, seconds
    tt = time_string.split(':')  # split it up into h/m/s
    tt = [num.zfill(2) for num in tt]  # make sure h/m/s are all two digit
    hours, min, sec = tt[0], tt[1], tt[2]  # got 'em.

    # start doing conversion to binary for each.
    h1, h2 = bin(int(hours[0])), bin(int(hours[1]))  # get it in binary
    h1, h2 = str(h1[2:]).zfill(2), str(h2[2:]).zfill(4)  # turn into str and strip the '0b'
    m1, m2 = bin(int(min[0])), bin(int(min[1]))
    m1, m2 = str(m1[2:]).zfill(3), str(m2[2:]).zfill(4)
    s1, s2 = bin(int(sec[0])), bin(int(sec[1]))
    s1, s2 = str(s1[2:]).zfill(3), str(s2[2:]).zfill(4)

    # now convert binary into Morse Code.
    # 0=. and 1=-
    final = ""
    hours1 = ''
    hours2 = ''
    min1 = ''
    min2 = ''
    sec1 = ''
    sec2 = ''

    for num in h1:
        if num == '1':
            hours1 += '-'
        else:
            hours1 += '.'

    for num in h2:
        if num == '1':
            hours2 += '-'
        else:
            hours2 += '.'

    for num in m1:
        if num == '1':
            min1 += '-'
        else:
            min1 += '.'

    for num in m2:
        if num == '1':
            min2 += '-'
        else:
            min2 += '.'

    for num in s1:
        if num == '1':
            sec1 += '-'
        else:
            sec1 += '.'

    for num in s2:
        if num == '1':
            sec2 += '-'
        else:
            sec2 += '.'

    return hours1, hours2, ':', min1, min2, ":", sec1, sec2

    #return the solution
    # return final

if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"