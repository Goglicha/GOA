def past(h, m, s):
    # 1 min = 60 000 ms
    # 1 hr = 3 600 000 ms
    # 1 sec = 1 000 ms
    res = (int(h) * 3600000  + int(m) * 60000 + int(s) * 1000)
    return res
        


