numbers = list(map(int, input().split()))  # This will give you List of Integers

# Write your own code!
num_of_unique_nums = None
#use sets since repetitions are not allowed
numbers_set = set(numbers)
num_of_unique_nums = len(numbers_set)

print(num_of_unique_nums)