import requests

question = input('Enter the MAgic 8-ball question: ')

# magic_8_URL = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}'
magic_8_URL = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/'

try:
    response = requests.get(magic_8_URL).json()
    print(response)
    answer = response['magic']['answer']
    print(f'The magic 8-ball says....... {answer}')
except Exception as e:
    print(e)
    print('No magic available at this current time')

