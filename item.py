from lxml import etree
from lxml.builder import ElementMaker # lxml only !
from datetime import datetime,timedelta




class GMerch_item():
	def __init__(self,**kwargs):
		#Required to send
		self.title = kwargs.get("title",None)
		self.description = kwargs.get("description",None)
		self.link = kwargs.get("link",None)
		self.uid = kwargs.get("uid",None)
		self.image_link = kwargs.get("image_link",None)
		self.language = kwargs.get("language",None)
		self.country = kwargs.get("country",None)
		self.google_product_category = kwargs.get("google_product_category",None)
		self.price = kwargs.get("price",None)
		self.price_unit = kwargs.get("price_unit",None)
		self.shippingprice = kwargs.get("shippingprice",None)
		self.availability = kwargs.get("availability",None)
		self.condition = kwargs.get("condition",None)

		##Set defaults
		self._channel = kwargs.get("channel","online")
		self._expiration_date = kwargs.get("expiration_date",(datetime.now()+timedelta(days=30)).isoformat().split("T")[0])
		self._adult = kwargs.get("adult",False)

		##Optional
		self.additional_image_link =  kwargs.get("additional_image_link",None)
		self.age_group =  kwargs.get("age_group",None)
		self.author =  kwargs.get("author",None)
		self.brand =  kwargs.get("brand",None)
		self.color =  kwargs.get("color",None)
		self.edition =  kwargs.get("edition",None)
		self.feature =  kwargs.get("feature",None)
		self.featured_product =  kwargs.get("featured_product",None)
		self.gender =  kwargs.get("gender",None)
		self.genre =  kwargs.get("genre",None)
		self.gtin =  kwargs.get("gtin",None)
		self.item_group_id =  kwargs.get("item_group_id",None)
		self.manufacturer =  kwargs.get("manufacturer",None)
		self.material =  kwargs.get("material",None)
		self.mpn =  kwargs.get("mpn",None)
		self.pattern =  kwargs.get("pattern",None)
		self.product_review_average =  kwargs.get("product_review_average",None)
		self.product_review_count =  kwargs.get("product_review_count",None)
		self.product_type =  kwargs.get("product_type",None)
		self.quantity =  kwargs.get("quantity",None)
		self.shipping_weight = kwargs.get("shipping_weight",None)
		self.size =  kwargs.get("size",None)
		self.year =  kwargs.get("year",None)

		'''
		TODO: SHIPPING/TAX
		'''

	##Fields with defaults
	def channel():
	    doc = "The channel property, default to online"
	    def fget(self):
	        return self._channel
	    def fset(self, value):
	        self._channel = value
	    def fdel(self):
	        self._channel = "online"
	    return locals()
	channel = property(**channel())

	def expiration_date():
	    doc = "The expiration_date property, default 30 days"
	    def fget(self):
	        return self._expiration_date
	    def fset(self, value):
	        self._expiration_date = value
	    def fdel(self):
	        self._expiration_date = (datetime.now()+timedelta(days=30)).isoformat().split("T")[0]
	    return locals()
	expiration_date = property(**expiration_date())

	def adult():
	    doc = "The adult property."
	    def fget(self):
	        return self._adult
	    def fset(self, value):
	        self._adult = value
	    def fdel(self):
	        self._adult = False
	    return locals()
	adult = property(**adult())

	def create(self):

		def nsmap(key):
			return "{%s}" % NSMAP[key]

		def add_subelement(root,ns,tag,value):
			if value: etree.SubElement(entry,nsmap(ns) +tag).text=str(value)

		NSMAP = {None : "http://www.w3.org/2005/Atom",
			    "app":"http://www.w3.org/2007/app",
			    "gd":"http://schemas.google.com/g/2005",
			    "sc":"http://schemas.google.com/structuredcontent/2009",
			    "scp":"http://schemas.google.com/structuredcontent/2009/products",} 

		entry = etree.Element("entry", nsmap=NSMAP) # lxml only!

		add_subelement(entry,None,"title",self.title)
		add_subelement(entry,None,"content",self.description)
		add_subelement(entry,None, "link",self.link)

		
		add_subelement(entry,"sc","id",self.uid)
		add_subelement(entry,"sc","image_link",self.image_link)
		add_subelement(entry,"sc","additional_image_link",self.additional_image_link)
		add_subelement(entry,"sc","content_language",self.language)
		add_subelement(entry,"sc", "target_country",self.country)
		add_subelement(entry,"sc", "channel",self.channel)
		add_subelement(entry,"sc", "expiration_date",self.expiration_date)
		add_subelement(entry,"sc", "adult",self.adult)

		add_subelement(entry, "scp", "age_group", self.age_group)
		add_subelement(entry,"scp", "author", self.author)
		add_subelement(entry,"scp", "availability", self.availability)
		add_subelement(entry,"scp", "brand", self.brand)
		add_subelement(entry,"scp", "color", self.color)
		add_subelement(entry,"scp", "condition", self.condition)
		add_subelement(entry,"scp", "edition", self.edition)
		add_subelement(entry,"scp", "feature", self.feature)
		add_subelement(entry,"scp", "featured_product", self.featured_product)
		add_subelement(entry,"scp", "gender", self.gender)
		add_subelement(entry,"scp", "genre", self.genre)
		add_subelement(entry,"scp", "google_product_category", self.google_product_category)
		add_subelement(entry,"scp", "gtin", self.gtin)
		add_subelement(entry,"scp", "item_group_id",self.item_group_id)
		add_subelement(entry,"scp", "manufacturer", self.manufacturer)
		add_subelement(entry,"scp", "material", self.material)
		add_subelement(entry,"scp", "mpn", self.mpn)
		add_subelement(entry,"scp", "pattern", self.pattern)
		if self.price: etree.SubElement(entry,nsmp("scp") + "price",unit=str(self.price_unit)).text = str(self.price)
		add_subelement(entry,"scp", "product_review_average",self.product_review_average)
		add_subelement(entry,"scp", "product_review_count",self.product_review_count)

		add_subelement(entry,"scp", "product_type",self.product_type)
		add_subelement(entry,"scp", "quantity",self.quantity)
		add_subelement(entry,"scp", "shipping_weight ",self.shipping_weight )
		add_subelement(entry,"scp", "size",self.size)
		add_subelement(entry,"scp", "year",self.year)		

		print etree.tostring(entry, pretty_print=True, xml_declaration=True)
		

hello = GMerch_item()
print hello.expiration_date
hello.create()
