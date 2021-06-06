import requests

def jogo_got(numero):


	url = f'https://anapioficeandfire.com/api/characters/{numero}'
	
	
	boneco = requests.get(url,verify=False)
	boneco_arrumado = boneco.json()
	nome = boneco_arrumado['name']

	return f'Voce eh {nome} em Game of Thrones'

print('QUEM EH VOCE EM GAME OF THRONES?')
numero = input ('Digite um numero de 20 a 2.000:')

print(jogo_got(numero))
