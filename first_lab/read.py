from functools import reduce
import random

# 8 оң сандардың қосындысы
#
a = [1,-2,3,4,-5,6,-7,-8,-9]
random_a = [random.randint(-11, 10) for _ in range(5)]
print("random_a= ", random_a)

multiplication = reduce(lambda x,y: x*y, (list(filter(lambda x: x > 0 ,a))))
multiplication_random_a = reduce(lambda x,y: x*y, (list(filter(lambda x: x > 0 ,random_a))))
print("multiplication_random_a ",multiplication_random_a,'\n')
print("a= ", a)
print("multiplication_a ",multiplication)
