""" Bose-Nelson Sort
    just 4fun """

from analyzer import print_analyze, values


@print_analyze
def bose_nelson_sort(_data, group_length=1):
    length = len(_data)
    if group_length > length:
        return _data
    # calculate groups count
    groups_count = length // group_length if length % group_length == 0 else length // group_length + 1
    group_pairs = groups_count // 2 + groups_count % 2

    result = []
    # iterate through groups count
    for count in range(group_pairs):
        # fill groups in order, all groups except the last are always full
        # last group can contain less elements
        left_index = group_length * count
        left_end = left_index + group_length

        right_index = group_length * (count + group_pairs)
        right_end = right_index + group_length if right_index + group_length < length else length

        # iterate through group length
        while left_index < left_end or right_index < right_end:
            # if the group is viewed to the end - add all elements from another
            if left_index >= left_end:
                result.extend(_data[right_index:right_end])
                break
                # right_index = right_end     # set the condition of while termination
            elif right_index >= right_end:
                result.extend(_data[left_index:left_end])
                break
                # left_index = left_end       # set the condition of while termination

            if _data[left_index] < _data[right_index]:  # if element in left group is lower than in right
                result.append(_data[left_index])
                left_index += 1
            else:
                result.append(_data[right_index])
                right_index += 1

    group_length *= 2
    return bose_nelson_sort(result, group_length)


@print_analyze
def bose_nelson(lst):
    """ Это не моя реализация. Взял для сравнения """
    def bose_nelson_merge(j, r, m):
        if j + r < len(lst):
            if m == 1:
                if lst[j] > lst[j + r]:
                    lst[j], lst[j + r] = lst[j + r], lst[j]
            else:
                m = m // 2
                bose_nelson_merge(j, r, m)
                if j + r + m < len(lst):
                    bose_nelson_merge(j + m, r, m)
                bose_nelson_merge(j + m, r - m, m)
        return lst

    m = 1
    while m < len(lst):
        j = 0
        while j + m < len(lst):
            bose_nelson_merge(j, m, m)
            j = j + m + m
        m = m + m

    return lst


source = values((-50, 50), count=101)
print(bose_nelson_sort(source))
print(bose_nelson(source[:]))
