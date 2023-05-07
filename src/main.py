import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
        "Inputs": {
        "data":
        [
            {
                "SkinThickness": 35,
                "Age": 50,
                "BloodPressure": 72,
                "BMI": 33.6,
                "Glucose": 128,
                "DiabetesPedigreeFunction": 0.627,
                "Pregnancies": 6,
                "Insulin": 0,
                "Outcome": -1
            },
            {
                "SkinThickness": 20,
                "Age": 22,
                "BloodPressure": 99,
                "BMI": 45.6,
                "Glucose": 140,
                "DiabetesPedigreeFunction": 0.633,
                "Pregnancies": 2,
                "Insulin": 0,
                "Outcome": -1
            }
        ]
    }
}

body = str.encode(json.dumps(data))

# frt3-2
# url = 'http://7eb4ed25-daee-4aa5-9787-92680b2cfd28.centralindia.azurecontainer.io/score'
# frt3-3
# url = 'http://3878e469-f41f-437f-aa44-0f9a6f422570.centralindia.azurecontainer.io/score'
# frt3-4
url = 'http://c1f86891-5f64-45b6-918a-0a451c0ccc85.centralindia.azurecontainer.io/score'


headers = {'Content-Type':'application/json'}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    res_json = json.loads(json.loads(result.decode('utf-8')))
    res_list = []
    for i in res_json['result']:
        res_list.append(i[-1])
    print(res_list)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
