items = [
    {
        "product":'Olma',
        "quantity":5,
        "shopping":10000
    },
    {
        "product":'Behi',
        "quantity":4,
        "shopping":20000
    },
    {
        "product":'Nok',
        "quantity":6,
        "shopping":30000
    }
]
# summa =0
# for item in items:
#     print(item)
summalar = sum([item['shopping'] for item in items])
print(summalar)