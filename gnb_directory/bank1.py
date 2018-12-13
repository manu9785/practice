directory= { 'manu': {'contact':'99999','age':'23','address':'xxxxxx'},
                     'anu': {'contact':'88888','age':'21','address':'yyyyyy'},
                                  'man': {'contact':'77777','age':'20','address':'zzzzzz'},
                                               'mainu': {'contact':'66666','age':'19','address':'qqqqqq'}
                                                       }
print(directory.items())
print(directory.keys())  
print("you can fetch contact,age and adress of the keys printed above ")
print(directory['manu']['contact'])
