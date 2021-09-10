import random
import string
import meraki
import os

# Defining your API key as a variable in source code is not recommended
API_KEY = os.environ['MAPIKEY']
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''


def genPass():
    chars = string.ascii_letters + string.punctuation + string.digits
    return ''.join(random.choice(chars) for i in range(12))


newPass = genPass()


response = dashboard.wireless.updateNetworkWirelessSsid(
    network_id, number,
    # name='My SSID',
    # enabled=True
    psk=newPass
)

print(response)
