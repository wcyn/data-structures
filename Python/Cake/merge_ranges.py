meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]


def merge_range(meetings):
    sorted_meetings = sorted(meetings)
    current_index = 1
    ranges = [sorted_meetings[0]]
    while current_index < len(meetings):
        current_meeting = sorted_meetings[current_index]
        if ranges[-1][1] >= current_meeting[0]:
            ranges[-1] = (ranges[-1][0], max(ranges[-1][1], current_meeting[1]))
        else:
            ranges.append(current_meeting)
        current_index += 1
    return ranges


print(merge_range(meetings))
