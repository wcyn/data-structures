# https://www.interviewcake.com/question/python/rectangular-love?course=fc1&section=general-programming
# A crack team of love scientists from OkEros (a hot new dating site)
# have devised a way to represent dating profiles as rectangles on a two-dimensional plane.
#
# They need help writing an algorithm to find the intersection of two users' love rectangles.
# They suspect finding that intersection is the key to a matching algorithm so powerful
# it will cause an immediate acquisition by Google or Facebook or Obama or something.
#
# Two rectangles overlapping a little. It must be love.
# Write a function to find the rectangular intersection of two given love rectangles.
#
# As with the example above, love rectangles are always "straight" and never "diagonal."
# More rigorously: each side is parallel with either the x-axis or the y-axis.
#
# They are defined as dictionaries ↴ like this:
#
#   my_rectangle = {
#
#     # Coordinates of bottom-left corner
#     'left_x'   : 1,
#     'bottom_y' : 1,
#
#     # Width and height
#     'width'    : 6,
#     'height'   : 3,
#
# }
#
# Your output rectangle should use this format as well.


def get_rectangular_intersection(rectangle_1, rectangle_2):
    intersection = {
        "left_x": None,
        "bottom_y": None,
        "width": None,
        "height": None,
    }

    left_intersection, right_intersection = get_x_overlap(rectangle_1, rectangle_2)
    width = right_intersection - left_intersection

    if width < 1:
        raise Exception("No Intersection Exists")
    intersection["left_x"] = left_intersection
    intersection["width"] = width
    bottom_intersection, top_intersection = get_y_overlap(rectangle_1, rectangle_2)
    height = top_intersection - bottom_intersection

    if height < 1:
        raise Exception("No Intersection Exists")
    intersection["bottom_y"] = bottom_intersection
    intersection["height"] = height
    return intersection


def get_x_overlap(rectangle_1, rectangle_2):
    left_intersection, right_intersection,  = rectangle_1["left_x"], rectangle_1["left_x"] + rectangle_1["width"]

    if rectangle_1["left_x"] < rectangle_2["left_x"]:
        left_intersection = rectangle_2["left_x"]

    right_1, right_2 = rectangle_1["left_x"] + rectangle_1["width"], rectangle_2["left_x"] + rectangle_2["width"]
    if right_1 > right_2:
        right_intersection = right_2

    return left_intersection, right_intersection


def get_y_overlap(rectangle_1, rectangle_2):
    bottom_intersection, top_intersection = rectangle_1["bottom_y"], rectangle_1["bottom_y"] + rectangle_1["height"]

    print("bottom 1, bottom 2", rectangle_1["bottom_y"], rectangle_2["bottom_y"])
    if rectangle_1["bottom_y"] < rectangle_2["bottom_y"]:
        bottom_intersection = rectangle_2["bottom_y"]

    top_1, top_2 = rectangle_1["bottom_y"] + rectangle_1["height"], rectangle_2["bottom_y"] + rectangle_2["height"]
    if top_2 < top_1:
        top_intersection = top_2

    return bottom_intersection, top_intersection


rect_1 = {
    "left_x": 1,
    "bottom_y": 1,
    "width": 6,
    "height": 3,
}

rect_2 = {
    "left_x": 4,
    "bottom_y": 3,
    "width": 6,
    "height": 3,
}
print(get_rectangular_intersection(rect_1, rect_2))


def get_rectangular_intersection_simplified(rectangle_1, rectangle_2):
    intersection = {}

    x_start, x_length = get_overlap_simplified(
        rectangle_1["left_x"],
        rectangle_1["width"],
        rectangle_2["left_x"],
        rectangle_2["width"]
    )

    if x_length < 1:
        raise Exception("No intersection exists")

    intersection["left_x"] = x_start
    intersection["width"] = x_length

    y_start, y_length = get_overlap_simplified(
        rectangle_1["bottom_y"],
        rectangle_1["height"],
        rectangle_2["bottom_y"],
        rectangle_2["height"]
    )
    if y_length < 1:
        raise Exception("No intersection exists")
    intersection["bottom_y"] = y_start
    intersection["height"] = y_length
    return intersection


def get_overlap_simplified(point_1, length_1, point_2, length_2):
    highest_start_point = max(point_1, point_2)
    lowest_end_point = min(point_1 + length_1, point_2 + length_2)

    length = lowest_end_point - highest_start_point
    return highest_start_point, length


print(get_rectangular_intersection_simplified(rect_1, rect_2))

