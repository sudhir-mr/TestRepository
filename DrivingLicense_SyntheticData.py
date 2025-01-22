import cv2
import matplotlib.pyplot as plt
from faker import Faker
import random
import string

fake = Faker()

def create_name():
  first_name = fake.first_name()
  last_name = fake.last_name()

  return first_name, last_name

def create_address_line_1():
  number = ''.join(random.choices('0123456789', k=3))
  st = fake.street_name()

  return number+" "+st

def create_address_line_2():
  state = fake.state()
  country = fake.country()
  postal = fake.postalcode()

  return state+" "+country+" "+postal

def create_date():
  possibilities = [f"{i:02}" for i in range(1, 32)]
  
  dd = random.choice(possibilities)
  mm = random.choice(possibilities[:12])
  yy = fake.year()

  return(dd+"."+mm+"."+yy)

def add_text_to_image(image, text, position):
    
    # Choose a font and font scale
    font = cv2.FONT_HERSHEY_PLAIN          

    # Set font color as black
    font_color = (0,0,0)
    
    # Set position
    x, y = position
    
    # Set default font size and thickness
    font_size = 0.7
    thickness = 1

    # Add the text to the image
    cv2.putText(image, text, (x, y), font, font_size, font_color, thickness, cv2.LINE_AA)

    # Return the modified image
    return image

def create_license_id():
  characters = string.digits + string.ascii_uppercase # Define the characters to choose from
  sequence_length = random.randint(8, 12) 
  random_sequence = ''.join(random.choices(characters, k=sequence_length))

  return random_sequence

for i in range(2):
  # Replace this path with the location of your driver license template
  image = cv2.imread("C:/MRSK-Training/EKAI/LicenseTemplate.png")


  created_name = create_name()
  first_name = created_name[0]
  last_name = created_name[1]
  dob = create_date()
  license_id = create_license_id()
  address =  create_address_line_1() + create_address_line_2()

  first_name_position = (263, 105) # measured with online tool
  last_name_position = (263, 115) 
  dob_position = (263,131)
  license_position = (263,172)
  address_position = (263,222)

# Add text to the image
  modified_image = add_text_to_image(image, first_name, first_name_position)
  modified_image = add_text_to_image(image, last_name, last_name_position)
  modified_image = add_text_to_image(image, dob, dob_position)
  modified_image = add_text_to_image(image, license_id, license_position)
  modified_image = add_text_to_image(image, address, address_position)
  # Convert BGR image to RGB (for displaying with Matplotlib)
  modified_image_rgb = cv2.cvtColor(modified_image, cv2.COLOR_BGR2RGB)
  plt.imshow(modified_image_rgb)
  plt.axis("off")
  plt.show()

# Plot the modified image
print(created_name[0])
print(created_name[1])
print(dob)
print(address)
print(license_id)
