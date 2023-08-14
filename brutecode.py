import requests
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-w','--wordlist', type=str, required=True,help="Switch for Wordlist")
parser.add_argument('-u','--url', type=str, required=True, help="Switch for URL")
args = parser.parse_args()

print("[+] Wordlist: ",args.wordlist)
print("[+] URL: ", args.url)

# Request Headers
headers = {
	'User-Agent':'Macintosh Mac OS X'
}

#Working with file
file = open(args.wordlist,'r')
lines = file.readlines()

#Checking if URL schema exists in the url
if ('http' in args.url) or ('https' in args.url):
	pass
else:
	print('Please enter a URL Schema')
	sys.exit()

# Parsing through each word in the wordlist
try:
	for line in lines:
		line = line.strip("\n")
		r = requests.get(args.url+'/'+line, headers=headers)
		if(r.status_code != 404):
			print(args.url+'/'+line, ":", r.status_code)
except:
	print("Error Occured")

