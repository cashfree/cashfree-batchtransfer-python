'''
Below is an integration flow on how to use Cashfree's payouts SDK. The SDK can be found at: https://github.com/cashfree/cashfree-sdk-python
Please go through the payout docs here: https://docs.cashfree.com/docs/payout/guide/

The following script contains the following functionalities :
    1. Transfers.create_batch_transfer -> request a batch transfer
    2. Transfers.get_batch_transfer_status -> get status of request batch transfer

'''

from cashfree_sdk.payouts import Payouts
from cashfree_sdk.payouts.beneficiary import Beneficiary
from cashfree_sdk.payouts.transfers import Transfers
from cashfree_sdk.payouts import payouts_config_var

clientId = "client_id"
clientSecret = "client_secret"

entries = [ {"transferId" : "PTM_00121241112", 
    "amount" : "12",
    "phone" : "9999999999",
    "bankAccount" : "9999999999" , 
    "ifsc" : "PYTM0_000001",
    "email" : "bahrat@gocashfree.com", 
    "name": "bharat"}]


try:
    Payouts.init(clientId, clientSecret, "TEST")
    print(payouts_config_var.url)
    batch_tnx_create = Transfers.create_batch_transfer(batchTransferId="Test_Bank_Account_Format_46", batchFormat="BANK_ACCOUNT", batch=entries, deleteBene=1)
    status = Transfers.get_batch_transfer_status(batchTransferId="Test_Bank_Account_Format_45")

except Exception as err:
    print("err occured")
    print(err)
    import traceback
    print(traceback.print_exc())
    
