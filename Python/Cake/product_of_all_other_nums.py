# https://www.interviewcake.com/question/python/product-of-other-numbers?course=fc1&section=greedy
# Write a function get_products_of_all_ints_except_at_index() that takes a list of
# integers and returns a list of the products.


def get_product_of_all_other_nums(num_list):
    full_product = 1
    zero_count = 0
    for num in num_list:
        if num == 0:
            zero_count += 1
        full_product *= num if num else 1

    if zero_count > 1:
        return [0 for num in num_list]
    elif zero_count == 1:
        return [0 if num else full_product for num in num_list]

    return [full_product // num for num in num_list]


def get_product_of_all_other_nums_no_div(num_list):
    if len(num_list) < 2:
        raise IndexError("Getting products of all other numbers requires at least two numbers")
    products_before = [1]
    for index in range(len(num_list)-1):
        products_before.append(products_before[-1] * num_list[index])

    # print(products_before)
    # results = [None] * len(num_list)
    product_after = 1
    for index in range(len(num_list)):
        print(product_after)
        products_before[~index] *= product_after
        product_after *= num_list[~index]

    return products_before


nums = [1, 7, 0, 3, 0, 4]
print(get_product_of_all_other_nums(nums))
print(get_product_of_all_other_nums_no_div(nums))

