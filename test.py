list_name_second = [
    {'Name': 'Malcolm', 'percentage': '50.0'},
    {'Name': 'Sam', 'percentage': '30.0'},
    {'Name': 'Ru', 'percentage': '100.0'},
    {'Name': 'Kam', 'percentage': '10.0'},
    {'Name': 'Joe', 'percentage': '20.0'}
    ]
list_name_second.sort(key= lambda d: float(d['percentage']))
print(list_name_second)