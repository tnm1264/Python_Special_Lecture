#homework1 - lotto generator 20103323 Kim Tae Wook
import random
import time

i=50
while i>0:
	print(random.sample(range(1,46),6))
	time.sleep(1)
	i-=1
