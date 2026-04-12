import cv2

print("=== Image as Numbers ===")

# load image
img = cv2.imread("sample.jpg")

# shape
print("\nImage Shape:", img.shape)

# pixel value
print("\nPixel value at (0,0):", img[0][0])

# channels
print("\nNumber of Channels:", img.shape[2])

print("\nExplanation:")
print("Shape → (Height, Width, Channels)")
print("Pixel Value → Color intensity at a point")
print("Channels → 3 means RGB image")