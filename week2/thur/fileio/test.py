import json
saved = {
  "data": [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4]
  ]
}
with open('saved.json', 'w') as fh:
    json.dump(saved, fh)