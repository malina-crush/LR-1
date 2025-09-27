scores = {'Stepan':85, 'Arseniy':100}
scores['Saymon'] = 78
scores['Arseniy'] += 5 
print(scores.get('Dave', "не найден"))
print(scores.get('Stepan', "не найден"))
scores.pop('Stepan')
print(scores)
print(len(scores))
print(scores.keys(), scores.values())
