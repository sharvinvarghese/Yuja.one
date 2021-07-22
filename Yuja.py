import http.client
import json

conn = http.client.HTTPSConnection("api.razorpay.com")
payload = json.dumps({
  "amount": 680000,
  "currency": "INR",
  "accept_partial": True,
  "first_min_partial_amount": 100,
  "expire_by": 55791273360000,
  "reference_id": "#9937",
  "description": "cloud computing",
  "customer": {
    "name": "Gaurav Kumar",
    "contact": "+919999999999",
    "email": "gaurav.kumar@example.com"
  },
  "notify": {
    "sms": True,
    "email": True
  },
  "reminder_enable": True,
  "notes": {
    "policy_name": "Jeevan Bima"
  },
  "callback_url": "https://example-callback-url.com/",
  "callback_method": "get"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cnpwX3Rlc3RfaDlFSG1HdU5HcGJsM2Y6aXdYN2ZhcWljaE9ReWprcVAxS2ZCbFJo'
}
conn.request("POST", "/v1/payment_links", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))