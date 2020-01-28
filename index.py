#warning the following code is written for python2 and tested using python2.7
#warning the following code has a dependency on the request, configparser library

import configparser
import requests
import json

#read the config file
config = configparser.ConfigParser()
config.optionxform = str
if config.read('config.ini') == []:
    print 'unable to read config'
    exit()

#default
default = config._sections['default']
clientId, clientSecret, env = default['clientId'], default['clientSecret'], default['env']
baseurl = config._sections['baseUrl'][env]
url = config._sections['url']

#get auth token
def getToken():
    try:
        finalUrl = baseurl + url['auth']
        r =  requests.post(finalUrl, headers={ "X-Client-Id":clientId, "X-Client-Secret":clientSecret})

        if (not r):
            raise Exception("response err: response is null")
        content = json.loads(r.content)
        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        return content["data"]["token"]
    except Exception as err:
        print 'err in getting token'
        raise Exception(err)

#request batch transfer
def requestBatchTransfer(token):
    try:
        finalUrl = baseurl + url['requestBatchTransfer']
        batchTransfer = json.loads(json.dumps(config._sections['BatchTransfer']))
        batchTransfer['deleteBene'] = int(batchTransfer['deleteBene'])
        batchTransfer['batch'] = json.loads(config._sections['BatchTransfer']['batch'])
        r = requests.post(finalUrl, json=batchTransfer, headers={'Content-Type': 'application/json','Authorization': 'Bearer ' + token})
        content = json.loads(r.content)
        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"]) 

    except Exception as err:
        print 'err in requesting batch transfer'
        raise Exception(err)

def getBatchTransferStatus(token):
    try:
        finalUrl = baseurl + url['getBatchTransferStatus'] + config._sections['BatchTransfer']['batchTransferId']

        r = requests.get(finalUrl, headers={'Content-Type': 'application/json','Authorization': 'Bearer ' + token})
        content = json.loads(r.content)
        
        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        
        print('batch transfer details')
        print json.dumps(content)
    except Exception as err:
        print 'err in getting batch transfer status'
        raise Exception(err)


if __name__ =="__main__":
    token = getToken()
    requestBatchTransfer(token)
    getBatchTransferStatus(token)
