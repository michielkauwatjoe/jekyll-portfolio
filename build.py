#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
from os import system

if __name__ == '__main__':
	execline = 'git --git-dir /var/www/michielkauwatjoe/.git pull'
	system(execline)
	execline = 'cd /var/www/michielkauwatjoe/'
	system(execline)
	execline = 'bundle exec jekyll build'
	system(execline)
	print('finished building') 
