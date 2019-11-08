def build_profile(first, last, **user_info):
    """Build a dictionary containg everything we
    know about the user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='Princeton',
                             field='physics')
user_profile2 = build_profile('Kali', 'Pic',
                             location='Lodz',
                             field='Science')

profiles = [user_profile, user_profile2]
for profile in profiles:
    print(profile)