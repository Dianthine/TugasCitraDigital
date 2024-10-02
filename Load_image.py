import cv2

img = cv2.imread("gambar1.jpg",1)
dimensi = img.shape 

Tinggi = img.shape [0]
lebar = img.shape [1]
Channel = img.shape[2]

print('Dimensi Gambar :',dimensi)
print('Tinggi Citra :',Tinggi)
print('Lebar Citra :',lebar)
print('Number of Channel :',Channel)
cv2.imshow("Tugas Load_image1 ", img)

print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()

