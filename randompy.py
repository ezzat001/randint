import random
try_counter = 0
total_tries_counter = 0
succeed_to_match = 0
failed_to_match = 0
all_tries = []

while True:
	while True:
		try_counter += 1
		total_tries_counter += 1
		r1 = random.randint(1,105500)
		r2 = random.randint(1,100550)
		if r1 == r2 :
			succeed_to_match +=1
			print(r1,r2)
			print('==========')
			print('Finshed After %d Tries' %try_counter)
			print('Total Tries %d Try' %total_tries_counter)
			all_tries.append(try_counter)
			try_counter = 0
			print('Max Number of Tries to match %d with %d are:'%(r1,r2),max(all_tries))
			print('Succeed in Matching %d time' %succeed_to_match)
			print('Failed to match %d time' %failed_to_match)
			break
		else:
			failed_to_match +=1
			#Eos.system('clear')

			#print('Failed to match %d time' %failed_to_match)


			
		

