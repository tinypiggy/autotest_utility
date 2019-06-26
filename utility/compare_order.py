import enum


class Condition(enum.Enum):
    WX_BIGGER = 0
    EJY_BIGGER = 1
    EQUAL = 3


def compare_order(file1, file2):
    with open(file1) as f1:
        with open(file2) as f2:
            front_list = f1.readlines()
            end_list = f2.readlines()
            wx_list = []
            ejy_list = []
            i, j = 0, 0
            len1 = len(front_list)
            len2 = len(end_list)
            while i < len1 and j < len2:
                if front_list[i] == end_list[j]:
                    i += 1
                    j += 1
                    continue
                if front_list[i] < end_list[j]:
                    wx_list.append(front_list[i].strip())
                    i += 1
                    continue
                if front_list[i] > end_list[j]:
                    ejy_list.append(end_list[j].strip())
                    j += 1
                    continue
            if i < len1:
                while i < len1:
                    wx_list.append(front_list[i].strip())
                    i += 1
            if j < len2:
                while j < len2:
                    ejy_list.append(end_list[j].strip())
                    j += 1
            print('wx_list: ', wx_list)
            print('ejy_list: ', ejy_list)


def compare_order_fix(file1, file2):
    with open(file1) as f1:
        with open(file2) as f2:
            wx_list = []
            ejy_list = []
            wx = ''
            ejy = ''
            flag = Condition.EQUAL
            while True:
                if flag == Condition.EQUAL:
                    wx = f1.readline()
                    ejy = f2.readline()
                if flag == Condition.WX_BIGGER:
                    ejy = f2.readline()
                if flag == Condition.EJY_BIGGER:
                    wx = f1.readline()
                if wx and ejy:
                    if wx == ejy:
                        flag = Condition.EQUAL
                        continue
                    if wx < ejy:
                        flag = Condition.EJY_BIGGER
                        wx_list.append(wx.strip())
                        continue
                    if ejy < wx:
                        flag = Condition.WX_BIGGER
                        ejy_list.append(ejy.strip())
                        continue
                else:
                    break
        print('wx_list: ', wx_list)
        print('ejy_list: ', ejy_list)


if __name__ == '__main__':
    if '':
        print('hah ')
    compare_order('../resources/wx.txt', '../resources/ejy.txt')
    compare_order('../resources/wx.txt', '../resources/ejy.txt')
    l1 = [2,9,10,20,21,22,31,33,34,35,36,39,51,52,53,57,58,114,115,8947,8948,9453,9454,9455,9459,9461,9462,9467,9468,9471,9472,9473,9474,9476,9478,9479,9482,9483,9484,9485,9486,9579,9580,9582,9583,9609,9611,9613,9615,9617,9623,9625,9627,9639,9641,9643,9647,9651,9653,9655,9659,9663,9665,9671,9673,9675,9681,9685,9703,9709,9711,9713,9717,9719,9723,9725,9727,9729,9731,9735,9737,9739,9745,9747,9761,9763,9765,9767,9769,9795,9899,9905,9915,9919,9921,9925,9927,9929,9935,9937,9939,9943,9949,9951,9953,9977,10003,10045,10065,10083,10085,10119,10121,10129,10145,10149,10151,10153,10193,10195,10199,10205,10211,10215,10223,10225,10243,10263,10265,10267,10285,10287,10345,10347,10349,10357,10381,10459,10463,10465,10517,10519,10521,10523,10525,10527,10529,10531,10581,10583,10585,10587,10589,10597,10599,10601,10603,10607,10621,10623,10625,10627,10629,10673,10677,10679,10691,10695,10699,10701,10703,10705,10707,10709,10713,10715,10717,11741,11889,11951,11953,12011,12709,12711,16913,16935,16937,17473,17747,17749,17751,18791,18913,18925,18973,20925,20927,20931,20937,20939,20941,20943,20945,20947,20949,20951,20953,20955,20961,20965,20969,20971,20973,20975,20977,20979,20981,20983,20991,20993,20995,20997,20999,21001,21003,21005,21007,21009]
    l2 = [36,9453,9454,9455,9471,9472,9473,9478,9479,9482,9483,9484,9763,9953,10459,10581,10695,18925,18973,20925,20961,20943,20945,20947,20949,20951,20953,20973,20975,20977,20979,20981,20983,21011]
    l1.sort()
    # print(l1)
    l2.sort()
    wx_list = []
    ejy_list = []
    i, j = 0, 0
    len1 = len(l1)
    len2 = len(l2)
    while i < len1 and j < len2:
        if l1[i] == l2[j]:
            i += 1
            j += 1
            continue
        if l1[i] < l2[j]:
            wx_list.append(l1[i])
            i += 1
            continue
        if l1[i] > l2[j]:
            ejy_list.append(l2[j])
            j += 1
            continue
    if i < len1:
        while i < len1:
            wx_list.append(l1[i])
            i += 1
    if j < len2:
        while j < len2:
            ejy_list.append(l2[j])
            j += 1
    print('wx_list: ', wx_list)
    print('ejy_list: ', ejy_list)

    for i in l1:
        if 20943 == i:
            print('yes')