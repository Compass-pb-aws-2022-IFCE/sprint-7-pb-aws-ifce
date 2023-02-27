import json
import urllib.request


def get_pokemon_info(name,atributo):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)

    
    if response.status == 200:
        data = json.loads(response.read().decode())
        if atributo=='weight' or atributo == 'height':
            info = data[str(atributo)]
            return info
        else:
            attack = data["stats"][1]["base_stat"]
            defense = data["stats"][2]["base_stat"]
            hp = data["stats"][0]["base_stat"]
            status = {"attack": attack, "defense": defense, "hp": hp}
            return status[atributo]


def check_pokemon_name(name):
    
    def levenshtein_distance(s, t):
        m, n = len(s), len(t)
        d = [[0] * (n + 1) for i in range(m + 1)]
        
        for i in range(1, m + 1):
            d[i][0] = i
        for j in range(1, n + 1):
            d[0][j] = j
            
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    substitution = d[i - 1][j - 1] + 1
                    insertion = d[i][j - 1] + 1
                    deletion = d[i - 1][j] + 1
                    d[i][j] = min(substitution, insertion, deletion)
                
        return d[m][n]

    pokemon_names = []

    with open("pokemon_names.txt", "r") as arquivo:
        file_content = arquivo.read()
    
    
    pokemon_names = file_content.split('\n')
    best_match = ""
    min_distance = float("inf")
    
    for pokemon_name in pokemon_names:
        distance = levenshtein_distance(name.lower(), pokemon_name.lower())
        
        if distance < min_distance:
            min_distance = distance
            best_match = pokemon_name
    
    if len(name)<3:
        min_distance=10;
    if min_distance > 3:
        return None
    
    return best_match

def translate_word(word):
    translations = {
        "peso": "weight",
        "altura": "height",
        "ataque": "attack", 
        "defesa": "defense", 
        "vida": "hp"
    }
    return translations.get(word.lower(), word)



def lambda_handler(event, context):
    pokemon=check_pokemon_name(event['pokemon'])
    atributo=translate_word(event['atributo'])
    if pokemon != None:
        return {
            'pokemon': pokemon,
            'atributo': get_pokemon_info(pokemon,atributo)
        }
    else:
        return {
            'pokemon': 'error',
            'atributo': 'error'
        }
