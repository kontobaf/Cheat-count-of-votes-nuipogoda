import requests
import time
print('count of tries?')
y = int(input(' '))
x = 0
print('Type number of 2 to 7 to select a voice id')
b = input(' ')
print('Type city')
#for example you can type here "msk"
gorod = input(' ')
for x in range(y):
	x += 1
	requests.get('https://'+gorod+'.nuipogoda.ru/vote.js?id='+b)
else:
<<<<<<< HEAD
	print('cycle has been finished, he is retryed', x,'times') 
=======
	print('cycle has been finished, he is retryed', x,'times') 

#this is test
>>>>>>> 5a5689af50b6e9005ba8354ab513b20f4d8770d5
