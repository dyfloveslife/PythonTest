import json

'''
json_file = open("f:/Python_test/BasicKnowledge/movie_1.txt", 'r', encoding='utf-8')
moive = json.load(json_file)
json_file.close()

print(moive)
print(json.dumps(moive, ensure_ascii=False))
print(moive['title'])
print(moive['actors'])
print(moive['release_year'])
value = """
    {"title": "Tron: Legacy",
    "composer": "Daft Puck",
    "release_year" : 2010,
    "budget": 170000000,
    "actors": null,
    "won_oscar": false
    }"""

tron = json.loads(value)
print(tron)
'''
moive2 = {}
moive2['title'] = 'Minority Report'
moive2['director'] = 'Steven Spielberg'
moive2['composer'] = 'John Williams'
moive2['actors'] = ['Tom Cruise', 'Colin Farrell',
                    'Samantha Morton', 'Max von Sydow']
moive2['is_awesom'] = True
moive2['budget'] = 102000000
moive2['cinematographer'] = 'Janusz Kami\u0144ski'

file2 = open('f:/Python_test/BasicKnowledge/movie_2.txt', 'w', encoding='utf-8')
json.dump(moive2, file2, ensure_ascii=False)
file2.close()
