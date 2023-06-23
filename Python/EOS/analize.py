
import json

result_raw = open('Type2.json', 'r')

result = json.load(result_raw)

for route in result['evpnRoutes']:
    if result['evpnRoutes'][route]['evpnRoutePaths'][0]['nextHop'] == '':
        continue
    print(result['evpnRoutes'][route]['routeKeyDetail']['mac'], "via", result['evpnRoutes'][route]['evpnRoutePaths'][0]['nextHop'] )
