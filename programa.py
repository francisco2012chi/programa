#!/usr/bin/python3

def linha(x):
	if x == 0:
		return
	print(x, end='')
	linha(x-1)

def pir(x):
	if x == 0:
		return
	linha(x)
	print('')
	pir(x-1)
	if x!=1:
		linha(x)
		print('')

def listar(x):
	if x == 0:
		return
	listar(x-1)
	print(x)

def listar_inv(x):
	if x == 0:
		return
	print(x)
	listar_inv(x-1)

op = input('Digite o comando: ')
if op == 'pir':
	pir(int(input('Digite um número: ')))
if op == 'listar':
	listar(int(input('Digite um número: ')))
if op == 'listar_inv':
	listar_inv(int(input('Digite um número: ')))
