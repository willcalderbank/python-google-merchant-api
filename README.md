python-google-merchant-api
==========================

A quick easy python liberary for google merchant, use at your own risk. 

Usage
----
Very easy to see what this does just reading quickly though the code (there isnt much) but as a summary:

There are two files google-merchant-api.py and item.py. 

google-merchant-api.py 
----
Use GMerch(email, password, source, uid) to get the auth token from google. The uid can be found when you log into the merchant center.

.get_items(), .insert_item(), .update_item(), .delete_item() can then be used. They follow the google merchant api docs which can be found here https://developers.google.com/shopping-content/getting-started/usingapi-products 

item.py
----
This is used to generate the xml for each product, again this follows the google merchant api docs http://support.google.com/merchants/bin/answer.py?hl=en&answer=188494#GB

GMerch_item() to build out this xml, each item can be added see the google merchant api docs for each item. .create() is then used to create the xml.


Warning!!!!
----
Although this is currently in use and works fine, use at your own risk.
