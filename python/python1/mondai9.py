import random
import sys

input_list = sys.argv[1:]
random.shuffle(input_list)
print(*input_list)
