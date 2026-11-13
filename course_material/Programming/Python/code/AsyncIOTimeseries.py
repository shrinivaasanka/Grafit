import asyncio
from sympy.combinatorics.partitions import random_integer_partition
import random

x=0
timeseries=[]
partitions=[]

async def loop1(N):
	global x
	x=N
	while x != 0 :
		x = x - 1
		timeseries.append(x)
		if x > 0:
			randompartition=random_integer_partition(x)
			randompartition.sort()
			partitions.append(randompartition)
		message=t'loop1 count at {x} ... random partition: {randompartition} with largest part {randompartition[-1:]} '
		await asyncio.sleep(random.randint(0,5))
		print(message)

async def loop2(N):
	global x
	while x != N :
		x = x + 1
		timeseries.append(x)
		if x > 0:
			randompartition=random_integer_partition(x)
			randompartition.sort()
			partitions.append(randompartition)
		message=f'loop2 count at {x} ... random partition: {randompartition} with largest part {randompartition[-1:]} '
		await asyncio.sleep(random.randint(0,5))
		print(message)
	
async def main():
	async with asyncio.TaskGroup() as tg:
		tg.create_task(loop1(10))
		tg.create_task(loop2(10))
	print("Timeseries:",timeseries)
	print("Constituency Vote Partitions:",partitions)

if __name__=="__main__":
	asyncio.run(main())
