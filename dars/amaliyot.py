def expensiveProduct(products):
    max_price= 0
    max_product={}
    for product in products:
        if product["price"]> max_price:
            max_price= product["price"]
            max_product=product
    return max_product["name"]

qiymat=[
  {
    "name": "Iphone X",
    "price": 60000000
  },
  {
    "name": "Iphone 12",
    "price": 1500
  },
  {
    "name": "Samsung Note 9",
    "price": 800
  },
  {
    "name": "Samsung S10",
    "price": 1100
  },
]
print(expensiveProduct(qiymat))