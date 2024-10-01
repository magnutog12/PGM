from pgm import Pgm

# Example testing file
def main():
    image = Pgm()

    if image.create(5, 5, 100):
        print("Image created successfully.")
    else:
        print("Failed to create image.")

    # Write the created image to output.pgm
    if image.write('output.pgm'):
        print("Image written to 'output.pgm'.")
    else:
        print("Failed to write image.")

    
    if image.read('output.pgm'):
        print("Image read successfully.")
    else:
        print("Failed to read image.")

    # Rotate the image clockwise
    if image.clockwise():
        print("Image rotated clockwise.")
    else:
        print("Failed to rotate image.")

    # Write the rotated image
    if image.write('rotated.pgm'):
        print("Rotated image written to 'rotated.pgm'.")
    else:
        print("Failed to write rotated image.")

if __name__ == "__main__":
    main()
