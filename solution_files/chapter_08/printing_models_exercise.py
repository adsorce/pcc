from cars_module import make_car as make

cars = make('Mercedes', 'G63', color='matte black', price=250_000, year=2025)
for detail, value in cars.items():
    print(value)