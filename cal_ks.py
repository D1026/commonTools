import numpy as np


def get_ks(sc, lb):
    sl = np.array([sc, lb]).transpose().tolist()
    sl.sort(key=lambda x: x[0])
    print(sl)
    score = np.array(sl)[:, 0]  # sorted
    label = np.array(sl)[:, 1]  # sorted
    ks = 0
    cutOff = None
    all_pos = sum(label)
    all_neg = len(label) - all_pos
    cum_pos = all_pos
    cum_neg = all_neg
    for i in range(len(score)):
        if label[i] == 0:
            cum_neg -= 1
        else:
            cum_pos -= 1
        ks_temp = abs((cum_pos/all_pos) - (cum_neg/all_neg))
        if ks_temp > ks:
            ks = ks_temp
            cutOff = score[i]

    return ks, cutOff

print(get_ks([0.5,0.6,0.7,0.6,0.6,0.8,0.4,0.2,0.1,0.4,0.3,0.9], [1,1,1,1,1,1,0,0,0,0,0,0]))