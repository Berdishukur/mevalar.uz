def str_counter(strs):
    d = []
    for i in strs:
        d.append((len(i), i))
    return dict(d)


