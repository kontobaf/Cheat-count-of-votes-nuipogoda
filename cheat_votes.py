import requests
import time
print('count of tries?')
y = int(input(' '))
x = 0
print('Type number of 2 to 7 to select a voice id')
b = input(' ')
print('Type city')
gorod = input(' ')
for x in range(y):
	x += 1
	requests.get('https://'+gorod+'.nuipogoda.ru/vote.js?id='+b)
else:
	print('cycle has been finished, he is retryed', x,'times') 