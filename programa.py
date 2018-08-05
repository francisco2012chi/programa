#!/usr/bin/python3
def fc(x):
	if x == 0:
		return
	print(x)
	fc(x-1)
	if x!=1:
		print(x)

fc(int(input('Digite um número: ')))
