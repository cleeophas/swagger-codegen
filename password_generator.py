import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
uppeer_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "@#$%&*/\?"

use_for = lower_case + uppeer_case + number + symbol
length_for_pass = 8

password = "".join(random.sample(use_for, length_for_pass)
                   
