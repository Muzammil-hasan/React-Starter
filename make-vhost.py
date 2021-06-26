#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys
from subprocess import call

if sys.argv[1] and sys.argv[2]:
	siteName = sys.argv[1]
	dire = "/etc/apache2/sites-available/"
	os.chdir(dire)
	fileName = f"{siteName}.conf"
	siteFolder = sys.argv[2]

	if siteName:
		call(["sudo","touch",fileName])

	with open(fileName, 'w') as f:
		f.write(f'<VirtualHost {siteName}:80>\nServerAdmin khizarwebdad@gmail.com\nDocumentRoot {siteFolder}\nServerName {siteName}\nServerAlias www.{siteName}\n</VirtualHost>')

	call(["sudo","a2ensite", fileName])

	with open('/etc/hosts', 'r') as f:
		file_content = f.read()

	with open('/etc/hosts', 'w') as f:
		f.write(f'127.0.0.1\t{siteName}\n{file_content}')

	call(["sudo","systemctl", "reload", "apache2"])

