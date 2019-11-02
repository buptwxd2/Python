solution = {}

distance_cache = {}


def edit_distance_1(str1, str2):
    if (str1, str2) in distance_cache:
        return distance_cache[(str1, str2)]

    if (str2, str1) in distance_cache:
        return distance_cache[(str2, str1)]

    if len(str1) == 0:
        if str2:
            operation = 'ADD {}'.format(str2[-1])
            solution[(str1, str2)] = operation
        else:
            solution[(str1, str2)] = ''

        distance = len(str2)
        distance_cache[(str1, str2)] = distance
        return distance

    if len(str2) == 0:
        if str1:
            operation = "DEL {}".format(str1[-1])
            solution[(str1, str2)] = operation
        else:
            solution[(str1, str2)] = ''

        distance = len(str1)
        distance_cache[(str1, str2)] = distance
        return distance

    if str1[-1] == str2[-1]:
        operation = ''  # operation is empty
        solution[(str1, str2)] = operation
        distance = edit_distance_1(str1[:-1], str2[:-1])
        distance_cache[(str1, str2)] = distance
        return distance
    else:
        distance, operation = min([(edit_distance_1(str1[:-1], str2[:-1]) + 1, 'SUB {}=>{}'.format(str1[-1], str2[-1])),
                                   (edit_distance_1(str1[:-1], str2) + 1, "DEL {}".format(str1[-1])),
                                   (edit_distance_1(str1, str2[:-1]) + 1, "ADD {}".format(str2[-1]))],
                                  key=lambda x: x[0]
                                  )
        solution[(str1, str2)] = operation
        distance_cache[(str1, str2)] = distance
        return distance

str1 = "新华社照片外代2017年4月11日n外代二线新加坡滨海湾掠影n4月10日行人走在新加坡滨海湾n新华社路透"
str2 = "新华社照片外代2017年4月11日n外代二线新加坡滨海湾掠影n4月10日行人经过新加坡滨海湾金沙酒店n新华社路透"
