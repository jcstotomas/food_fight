import pprint
pp = pprint.PrettyPrinter(indent=4)
class Restaurant:
    def __init__(self, raw_object):
        if "name" in raw_object:
            self.name = raw_object["name"]
        else:
            self.name = None
        
        if "image_url" in raw_object:
            self.image_url = raw_object["image_url"]
        else:
            self.image_url = None
        
        if "url" in raw_object:
            self.url = raw_object["url"]
        else:
            self.url = None
        if "categories" in raw_object:
            self.categories = self.get_categories(raw_object["categories"])
        else:
            self.categories = None
        
        if "price" in raw_object:
            self.price = raw_object["price"]
        else:
            self.price = None
    
    def get_categories(self, categories):
        category_names = []
        for i in categories:
            category_names.append(i["alias"])
        return category_names
    
    def return_object(self):
        return {
            "name": self.name,
            "image_url": self.image_url,
            "url": self.url,
            "categories":self.categories,
            "price": self.price
        }