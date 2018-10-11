import json,sys

f = open("contributors.md",'r')
j = open("contributors.json",'r')

contributors_md = {}
contributors_json = json.load(j,encoding='ascii')

for line in f:
    name = line.split(',')[0].strip()
    email = line.split(',')[1].strip()
    contributors_md[name] = email

print contributors_md, contributors_json

for key in contributors_md:
    if contributors_md[key] != contributors_json[key]:
        sys.exit(1)

for key in contributors_json:
    if contributors_md[key] != contributors_json[key]:
        sys.exit(1)

        

