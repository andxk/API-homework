import requests
from pprint import pprint 


base_url = "https://akabab.github.io/superhero-api/api/"
list_heros = ['Hulk', 'Captain America', 'Thanos']




def load_heros (hlist):

    resp = requests.get(base_url+'all.json')
    data = resp.json()

    int_max = 0
    name_max = 'error'
    for hero in hlist:
        for item in data:
            if item['name'] == hero:
                intelligence = item['powerstats']['intelligence']
                if intelligence > int_max:
                    int_max = intelligence
                    name_max = hero
                print(f'{hero} : {intelligence}')
                break
    
    print()
    print(f'Самый умный - {name_max} ({int_max})')
    return {name_max : int_max}                

    


if __name__ == '__main__':
    load_heros(list_heros)
