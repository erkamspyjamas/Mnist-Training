from tensorflow.keras.datasets import mnist #burada mnist dataseti icin ozel hazirlanmis kutuphaneyi import ediyoruz
from matplotlib import pyplot as plt #burada matplotlib kutuphanesini import ediyoruz

(trainX, trainY), (testX, testY) = mnist.load_data() #burada verilerimizi hazir kutuphaneden alip, egitim-test asamasina sokuyoruz

#Burada verilerimizi dongu icerisine alip plt kutuphanesiyle birlikte gorsel ciktisini aliyoruz.
for i in range(9):
	plt.subplot(330 + 1 + i)
	plt.imshow(trainX[i], cmap=plt.get_cmap('cool'))

#Burada ciktimizi aliyoruz
plt.show()
