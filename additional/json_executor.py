import json

# test_dict = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
# }

with open('sample_db.json', 'r') as db:
    data = json.load(db)
    print(data)
print(data)
# for line in db:
#     print(line)

data[4] = 'four'

with open('sample_db.json', 'w') as db:
    json.dump(data, db)
