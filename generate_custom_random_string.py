import random
import string
import sys
import subprocess

def generate_random():
	try:
		custom = sys.argv[1]
	except:
		custom = ''
	if not custom:
		n = 8
		rand = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))
		subprocess.run(['clip.exe'], input=rand.strip().encode('utf-16'), check=True)
		print ('8 digits random string copied to clipboard..')
	else:
		try:
			n = int(input(">> HOW MANY DIGITS FOR RANDOM STRING?\n>> ").replace(' ', ''))
		except:
			print ('Please input number only and try again..')
			return
		data_type = input("---------------------------\n>> NUMBER ONLY? ENTER 'N'.\n>> TEXT ONLY? ENTER 'T'.\n>> BOTH NUMBER AND TEXT? PRESS 'ENTER'.\n>> ").replace(' ', '').replace("'",'').lower()
		if data_type=='t':
			rand = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(n))
			subprocess.run(['clip.exe'], input=rand.strip().encode('utf-16'), check=True)
			print (str(n)+' digits random string copied to clipboard..')
		elif data_type=='n':
			rand = ''.join(random.SystemRandom().choice(string.digits) for _ in range(n))
			subprocess.run(['clip.exe'], input=rand.strip().encode('utf-16'), check=True)
			print (str(n)+' digits random string copied to clipboard..')
		elif not data_type:
			rand = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))
			subprocess.run(['clip.exe'], input=rand.strip().encode('utf-16'), check=True)
			print (str(n)+' digits random string copied to clipboard..')

generate_random()