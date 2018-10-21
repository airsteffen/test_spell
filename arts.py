import json
import random

data = json.loads( open("isms.json").read() )
isms = data['isms']

band = random.sample( isms, 10 )

output = "The Randoms: \n"

for isms in band:
	output += isms + "\n"

print (output)

with open('artisms.txt', 'w') as file:
	file.write(output)

