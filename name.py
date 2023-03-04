import cv2

# Load the image
image = cv2.imread('solar-system.jpg')

# Define the coordinates for each planet in the image
planet_coordinates = {
    "sun":(5,70),
    "Mercury": (20, 150),
    "Venus": (70, 105),
    "Earth": (100, 150),
    "Mars": (140, 115),
    "Jupiter": (180, 130),
    "Saturn": (275, 130),
    "Uranus": (355, 130),
    "Neptune":(390,160)
}

# Define the font properties
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font_scale = 0.7   
thickness = 1
color = (0, 0, 255)

# Add the planet names to the image
for planet, coordinates in planet_coordinates.items():
    cv2.putText(
        image,
        planet,
        coordinates,
        font,
        font_scale,
        color,
        thickness
        )

# Show the image with planet names
cv2.imshow('Solar System', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
