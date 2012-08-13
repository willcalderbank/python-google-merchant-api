
'''
A quick easy python liberary for google merchant, use at your own risk. 

### UNFINISHED!!!

Author: Will Calderbank
'''
import urllib,urllib2,requests

class GMerch():
	import urllib,urllib2
	def __init__(self,email, password, source, uid):
		##URL and headers for the auth
		auth_url = 'https://www.google.com/accounts/ClientLogin'
		headers = { 'Content-Type' : 'application/x-www-form-urlencoded'}

		data = 'Email='+email+'&Passwd='+password+'&service=structuredcontent&source='+source
		r = requests.post(auth_url, data=data ,headers=headers)

		#headers are used everywhere might as well set them here
		self.headers = { 'Content-Type' : 'application/atom+xml',
					'Authorization' : 'GoogleLogin Auth='+str(self.auth),}


		self._data = dict([item.strip().split("=") for item in r.text.split("\n") if item])
		self._uid = uid

	def uid():
	    doc = "The uid property."
	    def fget(self):
	        return self._uid
	    def fset(self, value):
	        self._uid = value
	    def fdel(self):
	        del self._uid
	    return locals()
	uid = property(**uid())

	def sid():
	    doc = "The sid property. (Read only)"
	    def fget(self):
	        return self._data["SID"]
	    return locals()
	sid = property(**sid())

	def lsid():
	    doc = "The LSID property. (Read only)"
	    def fget(self):
	        return self._data["LSID"]
	    return locals()
	lsid = property(**lsid())

	def auth():
	    doc = "The auth property. (Read only)"
	    def fget(self):
	        return self._data["Auth"]
	    return locals()
	auth = property(**auth())

	def get_items(self,limit = 25, channel = "online", country="US",langauge="en",uid=None ):
		url = "https://content.googleapis.com/content/v1/"+str(self.uid)+"/items/products/generic"

		if channel and country and langauge and uid:
			url = "https://content.googleapis.com/content/v1/"+str(self.uid)+"/items/products/schema/"+channel+":"+langauge+":"+country+":"+uid
		else:
			url = "https://content.googleapis.com/content/v1/"+str(self.uid)+"/items/products/generic"

			
		#Google has a 250 limit
		if limit > 250:
			limit = 250

		if limit:
			params = {"max-results":str(limit),}

		r = requests.get(url,headers=self.headers,params=params)
		return r.text

	def insert_item(self,item):
		url = "https://content.googleapis.com/content/v1/"+str(self.uid)+"/items/products/generic"
		r = requests.post(url,data=item,headers=self.headers)
		
	def update_item(self,item,channel = "online", country="US",langauge="en",uid=None):
	 	if not(channel and country and langauge and uid):
	 		raise AttributeError, "Incorrect attribues"
	 	else:
	 		url = "https://content.googleapis.com/content/v1/"+str(self.uid)+"/items/products/schema/"+channel+":"+langauge+":"+country+":"+uid
	 		r = requests.put(url,data=item,headers=self.headers)

	def delete_item(self,channel = "online", country="US",langauge="en",uid=None):
		url = "https://content.googleapis.com/content/v1/"+str(self.uid)+"/items/products/schema/"+channel+":"+langauge+":"+country+":"+uid
		r = requests.delete(url,headers=self.headers)
