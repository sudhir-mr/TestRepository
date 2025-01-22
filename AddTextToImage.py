import cv2
import matplotlib.pyplot as plt

# cv2.putText(image, text, (x_position, y_position), font, font_size, font_color, thickness, line_type)
print("Hello, World!")

def add_text_to_image(image, text, position):
    
    # Choose a font and font scale
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Set font color as black
    font_color = (0,0,0)
    
    # Set position
    x, y = position
    
    # Set default font size and thickness
    font_size = 1
    thickness = 2

    # Add the text to the image
    cv2.putText(image, text, (x, y), font, font_size, font_color, thickness, cv2.LINE_AA)

    # Return the modified image
    return image



# Replace this path with the location of your driver license template
image = cv2.imread("C:/MRSK-Training/EKAI/LicenseTemplate.png")
last_name = "Doe"
first_name = "John"
last_name_position = (400, 180) # measured with online tool
first_name_position = (400, 210)

# Add text to the image
modified_image = add_text_to_image(image, last_name, last_name_position)
modified_image = add_text_to_image(image, first_name, first_name_position)

# Convert BGR image to RGB (for displaying with Matplotlib)
modified_image_rgb = cv2.cvtColor(modified_image, cv2.COLOR_BGR2RGB)

# Plot the modified image
plt.imshow(modified_image_rgb)
plt.axis("off")
plt.show()




