import cv2

# Görüntüleri oku
img1 = cv2.imread("img1.jpg", 1)
img2 = cv2.imread("img2.jpg", 1)

# Analiz için gri kopyalara kullanıyoruz.
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ORB nesnesi oluştur.
orb = cv2.ORB_create(nfeatures=1000)

# Keypoint ve descriptor bul.
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# BFMatcher oluştur.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Eşleşmeleri bul.
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Renkli görüntüler üzerinde eşleşmeleri çiz
matched_img = cv2.drawMatches(
    img1, kp1,
    img2, kp2,
    matches[:50],
    None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

# Boyutlandırma
scale_percent = 60
width = int(matched_img.shape[1] * scale_percent / 100)
height = int(matched_img.shape[0] * scale_percent / 100)

resized = cv2.resize(matched_img, (width, height), interpolation=cv2.INTER_AREA)

# Sonucu göster
cv2.imshow("ORB Renkli Eslesme", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kaydet
cv2.imwrite("sonuc.jpg", matched_img)