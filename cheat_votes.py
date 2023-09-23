import requests
import concurrent.futures
print('count of tries?')
y = int(input(' '))
x = 0
print('Type number of 2 to 7 to select a voice id')
b = input(' ')
print('Type city')
#for example you can type here "msk"
gorod = input(' ')

def send_request(url):
	requests.get(url)

urls = [
	'https://'+gorod+'.nuipogoda.ru/vote.js?id='+b
] * y

with concurrent.futures.ThreadPoolExecutor() as executor:
	executor.map(send_request, urls)
	print('program has been finished') 
