people = {'Abigail': ['F', 250420], 'Alexander': ['M', 330838], 'Alexis': ['F', 101219], 'Alyssa': ['F', 96859], 'Andrew': ['M', 275623]}

sorted_people = sorted(people.items(), key=lambda x: x[1][1], reverse=True)

print(sorted_people)
