import yaml


file = open('starships.yaml', 'r').read()

starship_dict = yaml.safe_load(file)




for ncc in starship_dict['starships']:
    print("NCC-"+ncc, "is the starship", starship_dict['starships'][ncc]['name'], "and is commanded by Captain", starship_dict['starships'][ncc]['Captain'])
