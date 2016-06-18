
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

# get_products :: [Int] -> [Int]
def get_products(arr):
    prefix_products = []
    suffix_products = []

    prefix_product = 1
    suffix_product = 1

    for i in range(len(arr)):
        prefix_product *= arr[i]
        suffix_product *= arr[len(arr) - i - 1]
        prefix_products.append(prefix_product)
        suffix_products = [suffix_product] + suffix_products

    output = []

    for i in range(len(arr)):
        if i == 0:
            output.append(suffix_products[1])
            continue
        if i == len(arr) - 1:
            output.append(prefix_products[-2])
            continue
        output.append(prefix_products[i - 1] * suffix_products[i + 1])

    return output


arr = [1,2,3,4] # [24, 12, 8, 6]
print(get_products(arr))