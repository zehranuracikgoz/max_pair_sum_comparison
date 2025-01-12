A =[a1,··· ,an] seklinde sayı dizisi veriliyor. A dizisinde toplamı en büyük olan iki indeksi ve toplamını 
bulan algoritmalar geliştirilecek. 
(Örneğin A = [1, 13, -6, 7, 1] dizisinde toplamı en büyük olan indeksleri (1, 3), toplam sonucunu 20 
döndürmeli.) 


Yavaş Algoritma(Slow) - Brute Force
Hem iyi hem de en kötü durumda algoritmanın zaman karmaşıklığı O(n2)’dir. Algoritma, her iki 
elemanın toplamını her durumda kontrol etmek zorunda olduğu için hiçbir durumda daha hızlı 
çalışmaz.



Hızlı Algoritma(Fast) - Merge Sort
Algoritmanın tüm adımlarını göz önünde bulundurursak, her durumda Merge Sort'un zaman 
karmaşıklığı O(n log n)'dir. Bu, hem en iyi hem de en kötü durumlar için geçerlidir. Son iki elemanı 
toplama işlemi ise sıralı dizi üzerinde yapılan basit bir işlem olduğundan, O(1) zaman karmaşıklığına 
sahiptir. Ancak, algoritmanın genel karmaşıklığı Merge Sort'un karmaşıklığına bağlıdır ve bu da O(n log n) 
olarak kalır. Sonuç olarak, algoritmanın toplam zaman karmaşıklığı O(n log n)’dir.
