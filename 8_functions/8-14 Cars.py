def build_car_profile(manufacturer, model, **other_info):
    """functions that stores info about car in dictionary"""
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model
    for key, value in other_info.items():
        car_profile[key] = value
    return car_profile


profile = build_car_profile('audi','a6', year='2003',
                               color='grey')

print(profile)