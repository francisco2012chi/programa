#!/usr/bin/python3

def linha(x):
	if x == 0:
		return
	print(x, end='')
	linha(x-1)

def fc(x):
	if x == 0:
		return
	linha(x)
	print('')
	fc(x-1)
	if x!=1:
		linha(x)
		print('')

fc(int(input('Digite um número: ')))
