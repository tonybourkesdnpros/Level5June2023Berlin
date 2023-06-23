from cvprac.cvp_client import CvpClient
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# cvp = ['192.168.0.5', '192.168.0.6', '192.168.0.7'] # If you're using multiple instances of CVP
cvp = ['192.168.0.5']
cvp_user = 'arista'
cvp_password = 'aristac0tp'

client = CvpClient()
client.connect(cvp, cvp_user, cvp_password)

inventory = client.api.get_inventory()

for item in inventory:
    if item['complianceIndication'] == 'WARNING':
        print(item['hostname'], "is not in compliance")