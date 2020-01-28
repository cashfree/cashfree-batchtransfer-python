# Cashfree Payout Integration Kit for Python

Below is an integration flow on how to use Cashfree's payouts.
Please go through the payout docs [here](https://docs.cashfree.com/docs/payout/guide/)
<br/>
This kit is linked to the standard transfer flow. Go [here](https://dev.cashfree.com/payouts/integrations/standard-transfer) to get a better understanding.
<br/>

## Functionalities

The following kit contains the following functionalities:
    <ol>
    <li> [getToken](https://dev.cashfree.com/api-reference/payouts-api#authorise): to get auth token to be used in all          following calls.
    <li> [requestbBatchTrasnfer](https://docs.cashfree.com/docs/payout/guide/#batchtransfer-api): to request a batch transfer
    <li> [getBatchTransferStatus](https://docs.cashfree.com/docs/payout/guide/#get-batch-transfer-status-request): to get the status of the requested batch transfer
    </ol>

## Build Steps

follow the following build steps to compile the Integration kit:
  1. Download the code and cd into the directory containing the code.
  2. install the following dependencies: configparser and request.
  ```
  pip install configparser
  pip install request
  ```
## Set Up

### Pre Requisites:
The following kit uses information stored in a config file. Before running the code for the first time open the config.json file
and add the relevant details:
  1. ClientId: This is a unique Identifier that identifies the merchant. For more information please go [here](https://dev.cashfree.com/payouts/integrations/pre-requisites#credentials).
  2. ClientSecret: Corresponding secret key for the given ClientId that helps Cashfree indentify the merchant. For more information please go [here](https://dev.cashfree.com/payouts/integrations/pre-requisites#credentials).
  3. Environment: Enviornment to be hit. The following values are accepted prod: for production, test: for test enviornment.

### IP Whitelisting:

Your IP has to be whitelisted to hit Cashfree's server. For more information please go [here](https://dev.cashfree.com/payouts/integrations/pre-requisites#ip).

### Batch tranfer:
The following kit needs batch transfer details in order to create a batch transfer.
For more information on batch transfers please go [here](https://dev.cashfree.com/payouts/integrations/batch-transfer)

The kit reads batchTransfer details from the config file. Under the BatchTransfer section. For a list of required fields go [here](https://dev.cashfree.com/api-reference/payouts-api#batch-transfer).
Sample Fields to add a beneficiary using bankAccount and ifsc:
  1. batchTransferId: uniqueId of the batch transfer.
  2. batchFormat: format of the batch transfer, accepted values: BANK_ACCOUNT and BENEFICIARY_ID.
  3. deleteBene: optional field, needed if batch format is bank account, to delete beneficiaries that already exist with same account details but different names. If set will delete and readd the beneficiary, else will throw an error.
  4. batch: array of transfers to be done.
  
  Batch format for BANK_TRANSFER:
  
  1. transferId: unique identifier of the transfer.
  2. amount: amount to be sent.
  3. phone: phone number of the recepient.
  4. bankAccount: back account of the recepient.
  5. ifsc: recepients bank accounts's ifsc.
  6. email: email of the recepient.
  7. name: name of the recepient.
  <br/>
  Batch format for BENEFICIARY_ID
  
  1. transferId: unique identifier of the transfer.
  2. amount: amount to be sent.
  3.beneId: id of the beneficiary

## Usage

Once the config file is setup you can run the executable, to run the entire flow. Authorise, check and add beneficiary, 
request for a payout transfer and get the transfer status.

run the following command in the terminal to run the script:
```
  python index.py
```

You can change the necessary values in the config file as per your requirements and re run the script whenever needed.

## Doubts

Reach out to techsupport@cashfree.com in case of doubts.
 


