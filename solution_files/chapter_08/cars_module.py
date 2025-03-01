def make_car(manufacturer, model, **options):
    options['manufacturer'] = manufacturer
    options['model'] = model
    return options