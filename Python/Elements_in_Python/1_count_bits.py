#  a program to count the number of bits that are set to 1 in an integer
def count_bits(num):
    num_bits = 0
    while num:
        bit = num & 1
        # can also convert int to binary!!
        print(bit)
        num_bits += bit
        num >>= 1
    return num_bits

def test_count_bits():
    result = count_bits(6)
    assert result == 2
    result = count_bits(7)
    assert result == 3

count_bits(5)