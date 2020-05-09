from xml.etree import ElementTree as ET
import calendar, time
import random
import string
import re
from datetime import datetime

startTime = datetime.now()


def bulk_update_tag_value(root, parent_tag, target_tag):
	rand = int(''.join(random.SystemRandom().choice(string.digits) for _ in range(8)))
	print (rand)
	for elem in root.findall(parent_tag):
		# print (elem)
		new_indx = rand+1
		msgid = elem.find(target_tag)
		msgid.text = str(new_indx)

def update_xml(file_name):
	rand = ''.join(random.SystemRandom().choice(string.digits) for _ in range(8))
	indx = int(calendar.timegm(time.gmtime()))
	tree = ET.parse(file_name)
	root = tree.getroot()
	# UPDATE MSGID
	parent_tag = './/GrpHdr'
	target_tag = 'MsgId'
	bulk_update_tag_value(root, parent_tag, target_tag)
	# UPDATE E2EID
	parent_tag = './/PmtId'
	target_tag = 'EndToEndId'
	bulk_update_tag_value(root, parent_tag, target_tag)
	new_xml = ET.tostring(root, encoding='unicode')
	# print (ET.dump(root))
	# print (new_xml)

	newf = open('newpain001.xml', 'w')
	newf.write(new_xml)

def find_tag_list_in_xml(xml, tag_name):
	s = '<'+tag_name+'>'
	e = '</'+tag_name+'>'
	regex = r"%s(.+?)%s" %(s, e)
	tag_list = []
	tags = re.finditer(regex, xml, re.MULTILINE | re.IGNORECASE)
	for i in tags:
		tag_list.append(i.group())
	print ('----------\n'+tag_name+' tag count: '+str(len(tag_list))+'\n------------\n')
	print ('Replacing tag values, it will take a while depending on the file size. Please wait...\n')
	for i in tag_list:
		rand = ''.join(random.SystemRandom().choice(string.digits) for _ in range(8))
		xml = xml.replace(i, s+str(rand)+e, 1)
	return (xml)

def update_file(file_name, newpainfile):
	f = open(file_name, "r")
	xml = f.read()
	#FIND AND REPLACE ALL MSGID AND E2EID IN XML
	xml = find_tag_list_in_xml(xml, 'MsgId')
	xml = find_tag_list_in_xml(xml, 'EndToEndId')
	print ('Tag value updated, now writing to a new file..\n')
	# SAVING INTO NEW XML FILE
	newf = open(newpainfile, 'w')
	newf.write(xml)
	print ('All tag values updated and saved into new file with name: '+newpainfile)

newpainfile = 'newpain001.xml'
file_name = 'pain001_XL.txt'
update_file(file_name, newpainfile)
print ('Time took to complete execution: '+str(datetime.now() - startTime))
# print (datetime.now() - startTime)