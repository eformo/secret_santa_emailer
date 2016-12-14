#!/usr/bin/python
import random,sys,os

def pick_recipient(group,recipients,single_flag):
	for person in group:
		#print "Group=%s" % group
		#print "Person=%s" % person
		#print "Possibles length = %d list=%s" % (len(recipients),recipients)
		gift = random.choice(recipients)
		if single_flag == 0:
			while gift in group:
				gift = random.choice(recipients)
		else:
			while gift in person:
				gift = random.choice(recipients)
		mail_list.append( '%s=%s' %(person,gift))
		#print "Gift=%s\n##############" % gift
		recipients.remove(gift)
	return recipients

def finalize_mail_commands():
	print mail_list
	#if this question is not displayed you are in an endless loop trying to select the gift for the last person
	send_mail = raw_input('Program has successfully completed choosing all pairings, send emails?(y/n) ')
	if (send_mail == 'n') or (send_mail == ''): 
		exit(1)
	elif send_mail == 'y':
		for item in mail_list:
			sep = item.split('=')
			pfrom = sep[0].split(':')
			pto = sep[1].split(':')
			os.system('echo HoHoHo %s! You will be buying a gift for %s this year. The decided limit is \$50. > test.txt' % (pfrom[0],pto[0]))
			cmd = "timeout 10m mutt -e 'set realname=\'Santa\'' -a xmas-joke.jpg -s \'Gift Exchange 2016\' -- %s  < ~/git/secret_santa/test.txt" % pfrom[1]

			#os.system(cmd)
			print cmd
	else:
		print "Invalid Input: Please type either y to continue or n to exit"
		exit(2)


if __name__ == "__main__":
	global mail_list
	mail_list = []
	
	#create lists of people, group couples at beginning or end of list and the singles opposite
	all_recipients = ['name_1-CoupleA: name_1-CoupleA@gmail.com','name_2-CoupleA: name_2-CoupleA@gmail.com',
		'name_3-CoupleB: name_3-CoupleB@hotmail.com','name_4: name_4CoupleB@hotmail.com',
		'name_5-Single: name_5-Single@gmail.com','name_6-Single: name_6-Single@gmail.com']	

	#create couples and lists of singles to make sure couples don't get their other half
	#modify the groups to match the list of people from above
	coupleA = all_recipients [0:2]
	coupleB = all_recipients [2:4]
	single = all_recipients [4:]

	#keep initial list in tact	
	possible_recipients = all_recipients

	#modify the groups to match what the input list is
	possible_recipients = pick_recipient(coupleA,possible_recipients,single_flag=0)
	possible_recipients = pick_recipient(coupleB,possible_recipients,single_flag=0)
	possible_recipients = pick_recipient(single,possible_recipients,single_flag=1)

	finalize_mail_commands()

