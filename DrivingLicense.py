from faker import Faker
from PIL import Image, ImageDraw, ImageFont
import random

def generate_license_number(name, dob):
    """
    Generate a synthetic UK-style driving license number.
    Format: SSSSYYYYMMDDIIN.
    """
    surname = name.split()[1][:5].upper().ljust(5, '9')
    dob_part = dob.strftime("%y%m%d")
    issue_no = str(random.randint(0, 9))
    checksum = str(random.randint(0, 9))
    return f"{surname}{dob_part}{issue_no}{checksum}"

def create_synthetic_license(output_file="uk_driving_license.png"):
    # Initialize Faker
    fake = Faker("en_GB")
    name = fake.name()
    address = fake.address().replace("\n", ", ")
    dob = fake.date_of_birth(minimum_age=18, maximum_age=80)
    issue_date = fake.date_this_decade(before_today=True)
    expiry_date = issue_date.replace(year=issue_date.year + 10)
    license_number = generate_license_number(name, dob)

    # Create a blank image
    width, height = 800, 400
    image = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(image)

    # Fonts (use a suitable .ttf file from your system)
    font = ImageFont.truetype("arial.ttf", size=24)

    # Draw text
    draw.text((20, 20), "UK DRIVING LICENSE", font=font, fill="black")
    draw.text((20, 80), f"Name: {name}", font=font, fill="black")
    draw.text((20, 120), f"Address: {address}", font=font, fill="black")
    draw.text((20, 160), f"DOB: {dob.strftime('%d/%m/%Y')}", font=font, fill="black")
    draw.text((20, 200), f"License No: {license_number}", font=font, fill="black")
    draw.text((20, 240), f"Issue Date: {issue_date.strftime('%d/%m/%Y')}", font=font, fill="black")
    draw.text((20, 280), f"Expiry Date: {expiry_date.strftime('%d/%m/%Y')}", font=font, fill="black")

    # Save the image
    image.save(output_file)
    print(f"Driving license saved to {output_file}")

# Generate the synthetic driving license
create_synthetic_license()
