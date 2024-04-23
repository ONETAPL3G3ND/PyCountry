import pycountry

country = pycountry.countries.get(alpha_2='US')

print("Country Code (ISO 3166-1 alpha-2):", country.alpha_2)
print("Country Code (ISO 3166-1 alpha-3):", country.alpha_3)
print("Country Code (ISO 3166-1 numeric):", country.numeric)