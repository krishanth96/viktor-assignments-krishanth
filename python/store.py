
# Product Classes
class Product:
    def __init__(self, product_id, price_in_euros, weight_in_kg=0.0):
        self.id = product_id
        self.price_in_euros = price_in_euros
        self.weight_in_kg = weight_in_kg


class Book(Product):
    def __init__(self, product_id, title, author, pages, price_in_euros, weight_in_kg):
        super().__init__(product_id, price_in_euros, weight_in_kg)
        self.title = title
        self.author = author
        self.pages = pages


class MusicAlbum(Product):
    def __init__(self, product_id, artist, title, no_of_tracks, price_in_euros, weight_in_kg):
        super().__init__(product_id, price_in_euros, weight_in_kg)
        self.artist = artist
        self.title = title
        self.no_of_tracks = no_of_tracks

class SoftwareLicense(Product):
    def __init__(self, product_id, name, price_in_euros):
        super().__init__(product_id, price_in_euros, weight_in_kg=0.0)
        self.name = name


# Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = [] 

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)

    def total_price(self):
        return sum(item.price_in_euros for item in self.items)

    def total_weight(self):
        return sum(item.weight_in_kg for item in self.items)

