python-google-merchant-api
==========================

A quick easy python liberary for google merchant, use at your own risk. 

Usage
----
Very easy to see what this does just reading quickly though the code (there isnt much) but as a summary:

Use GMerch(email, password, source, uid) to get the auth token from google. The uid can be found when you log into the merchant center.

.get_items(), .insert_item(), .update_item(), .delete_item() can then be used. They follow the google merchant api docs which can be found here https://developers.google.com/shopping-content/getting-started/usingapi-products 