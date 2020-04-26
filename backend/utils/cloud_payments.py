from cloudpayments import CloudPayments
from cloudpayments.enums import Currency, Interval, TransactionStatus
from cloudpayments.models import Transaction, Secure3d

try:
    CP_PUBLIC_ID = 'pk_5519ac15932e0bcfcc756755f7da9'
    CP_SECRET = 'fe95a4b6c1c53ccb798aaf5a21a33122'
    client = CloudPayments(CP_PUBLIC_ID, CP_SECRET)
    client.test()
except Exception as e:
    print(str(e))

