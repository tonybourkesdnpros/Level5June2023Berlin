import pyeapi


vlan = 1701
switch = ['leaf2-DC1']

connect = pyeapi.connect_to('leaf2-DC1')
result = connect.api("vlans").create(vlan)
if result == True:
    print("We added VLAN", vlan)
if result == False:
    print("Something went wrong")

