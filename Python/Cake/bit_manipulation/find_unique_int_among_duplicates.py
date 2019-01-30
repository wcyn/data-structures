# https://www.interviewcake.com/question/python/find-unique-int-among-duplicates?course=fc1&section=bit-manipulation
# Your company delivers breakfast via autonomous quadcopter drones.
# And something mysterious has happened.
#
# Each breakfast delivery is assigned a unique ID, a positive integer.
# When one of the company's 100 drones takes off with a delivery, the delivery's ID is added to a list,
# delivery_id_confirmations. When the drone comes back and lands, the ID is again added to the same list.
#
# After breakfast this morning there were only 99 drones on the tarmac.
# One of the drones never made it back from a delivery.
# We suspect a secret agent from Amazon placed an order and stole one of our patented drones.
# To track them down, we need to find their delivery ID.
#
# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.
#
# The IDs are not guaranteed to be sorted or sequential. Orders a


def get_unique_integer(delivery_id_confirmations):
    unique_int = 0
    for delivery_id in delivery_id_confirmations:
        unique_int ^= delivery_id
    return unique_int


id_confirmations = [1, 3, 2, 1, 3, 4, 2]
print(get_unique_integer(id_confirmations))
