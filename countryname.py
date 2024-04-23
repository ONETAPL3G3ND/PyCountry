import pycountry


country = pycountry.countries.get(alpha_2='US')

print("Country Name:", country.name)