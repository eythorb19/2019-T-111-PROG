from catalog import Item
from catalog import Catalog

# Main program starts here
item1 = Item("12 Angry Men", "Blabla")
item1.set_category("Drama")
print(item1)

item2 = Item("The God", "Crime")
print(item2)
item2.set_name("The Godfather")
print(item2)

item3 = Item("Schindler's List", "Biography")
print(item3)

item4 = Item("Pulp Fiction", "Crime")
print(item4)
catalog = Catalog('Films')
catalog.add(item1)
catalog.add(item2)
catalog.add(item3)
catalog.add(item4)
print(catalog)

catalog.remove(item3)
catalog.set_name("My Favorites")
print(catalog)

print(catalog.find_item_by_name("Green Book"))
print(catalog.find_item_by_name("The Godfather"))

catalog.clear()
print(catalog)
