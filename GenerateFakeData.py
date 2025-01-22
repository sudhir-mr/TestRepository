from faker import Faker
import random
import string

fake = Faker()

def create_name():
  first_name = fake.first_name()
  last_name = fake.last_name()

  return first_name, last_name

def create_date():
  possibilities = [f"{i:02}" for i in range(1, 32)]
  
  dd = random.choice(possibilities)
  mm = random.choice(possibilities[:12])
  yy = fake.year()

  return(dd+"."+mm+"."+yy)

def create_issuer():
  issuers = [
    "AUSTRIAN TRAFFIC DEPARTMENT",
    "DVLA",
    "RTD",
    "MINISTRY OF THE INTERIOR",
    "MINISTRY OF TRANSPORT"
    "TRANSPORT MALTA",
    "DEPARTMENT OF ROAD TRANSPORT",
    "NATIONAL TRANSPORT AUTHORITY",
    "DANISH ROAD DIRECTORATE",
    "MAANTEEAMET",
    "TRAFICOM",
    "NDLS",
    "RTSD"]
  
  issuer= random.sample(issuers, 1)
  string = ''.join(issuer)
  return string

def create_driver_id():
  driver_number = ''.join(random.choices('0123456789', k=9))

  return driver_number

def create_license_id():
  characters = string.digits + string.ascii_uppercase # Define the characters to choose from
  sequence_length = random.randint(8, 12) 
  random_sequence = ''.join(random.choices(characters, k=sequence_length))

  return random_sequence

def create_address_line_1():
  number = ''.join(random.choices('0123456789', k=3))
  st = fake.street_name()

  return number+" "+st

def create_address_line_2():
  state = fake.state()
  country = fake.country()
  postal = fake.postalcode()

  return state+" "+country+" "+postal

def create_categories():
    eu_driving_categories = ["AM", "A1", "A2", "A", "B1", "B", "BE", "C1", "C", "CE", "D1", "D1E"]

    num_categories = random.randint(1, 5)
    selected_categories = random.sample(eu_driving_categories, num_categories)

    return "/".join(selected_categories)


print(create_name())
print(create_date())
print(create_issuer())
print(create_driver_id())
print(create_license_id())
print(create_address_line_1())
print(create_address_line_2())
print(create_categories())