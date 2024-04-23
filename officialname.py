import pycountry

country = pycountry.countries.get(alpha_2='US')

print("Official Name (English):", country.official_name)