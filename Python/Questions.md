### Soru 1
Aşağıdakilerden hangisi Python tarafından desteklenen, metin ve veri dönüşümlerinde kullanılan geçerli kodlama (codecs) yöntemlerinden biridir?

- [ ] A) HTML
- [ ] B) UTF-8 (Codecs)
- [ ] C) CSS
- [ ] D) SQL

--------------------------------

### Soru 2
Python yorumlayıcısının bir tty'den komutlar okuyarak kullanıcıyla anlık olarak çalıştığı, kod satırlarını satır satır işlediği moda ne ad verilir?

- [ ] A) Skript Modu
- [ ] B) Etkileşimli Mod (Interactive Mode)
- [ ] C) Derleme Modu
- [ ] D) Hata Ayıklama Modu

---------

### Soru 3
Python etkileşimli modunda bir sonraki komutu istemek için kullanılan **birincil komut istemi (primary prompt)** ve çok satırlı yapılar için kullanılan **ikincil komut istemi (secondary prompt)** aşağıdakilerin hangisinde sırasıyla doğru verilmiştir?

- [ ] A) `...` ve `>>>`
- [ ] B) `>>>` ve `$$$`
- [ ] C) `>>>` ve `...`
- [ ] D) `>>>` ve `>>>`

-------------

### Soru 4
Aşağıdaki Python kod bloğu çalıştırıldıktan sonra `text` değişkeninin değeri ne olur?

```python
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```

- [ ] A) Kod hata verir (SyntaxError).
- [ ] B) Değişkenin içi boş kalır, çünkü diyez işareti (#) satırı yorum satırına dönüştürür.
- [ ] C) `text` değişkenine `1` değeri atanır.
- [ ] D) `"# This is not a comment because it's inside quotes."` metni aynen atanır.

--------------------------

### Soru 5
Aşağıdaki Python kodlarından hangisinin çıktısı veri tipi bakımından diğerlerinden **farklıdır**?

- [ ] A) `17 // 3`
- [ ] B) `17 % 3`
- [ ] C) `8 / 5`
- [ ] D) `2 ** 7`

---------

### Soru 6
Aşağıdaki Python kod bloğu sırasıyla çalıştırıldığında elde edilecek çıktılar hangi şıkta doğru verilmiştir?

```python
x = (50 - 5 * 6) / 4
y = 17 // 3
z = 17 % 3
```

- [ ] A) `5.0` , `5.66` , `2`
- [ ] B) `5.0` , `5` , `2`
- [ ] C) `5` , `5` , `5`
- [ ] D) `11.25` , `5` , `2`

---------------------

### Soru 7
Python'da bölme işleminden kalan kalanı (mod) bulmak için `....` operatörü kullanılırken; bir sayının üssünü (kuvvetini) hesaplamak için `....` operatörü kullanılır.

- [ ] A) `/` ve `*`
- [ ] B) `//` ve `**`
- [ ] C) `%` ve `**`
- [ ] D) `%` ve `^`

-----------------------

### Soru 8
Aşağıdaki Python kod bloğu etkileşimli modda (interactive mode) sırasıyla çalıştırıldığında ekrana yansıyacak **tek çıktı** hangisi olur?

```python
width = 20
height = 5 * 9
width * height
```

- [ ] A) `20`
- [ ] B) `45`
- [ ] C) `20` ve `45`
- [ ] D) `900`

---------------------

### Soru 9
Python etkileşimli modunda (interactive mode) **en son ekrana yazdırılan (hesaplanan) değeri** otomatik olarak hafızada tutan özel değişken aşağıdakilerden hangisidir?

- [ ] A) `last`
- [ ] B) `ans`
- [ ] C) `_` (Alt çizgi)
- [ ] D) `%`

----------------------

### Soru 10
Python etkileşimli modunda sırasıyla aşağıdaki komutlar çalıştırılmıştır:

```python
>>> 10 + 5
15
>>> _ * 2
```

Bu işlemden sonra ekrana basılacak çıktı aşağıdakilerden hangisidir?

- [ ] A) `10`
- [ ] B) `20`
- [ ] C) `30`
- [ ] D) Kod hata verir (`NameError`).

--------------------------

### Soru 11
**Doğru mu, Yanlış mı?**

Python, standart `int` ve `float` veri türlerinin yanı sıra karmaşık sayıları (`3+5j` gibi) harici bir kütüphane yüklemeye gerek kalmadan yerleşik (built-in) olarak destekler.

- [ ] Doğru
- [ ] Yanlış

---------------------------

### Soru 12
Python'da karmaşık (complex) sayıları tanımlarken sanal kısmı (imaginary part) belirtmek için kullanılan resmi sonekler aşağıdakilerin hangisinde doğru verilmiştir?

- [ ] A) `i` veya `I`
- [ ] B) `j` veya `J`
- [ ] C) `c` veya `C`
- [ ] D) `z` veya `Z`

-----------------------------

### Soru 13
Python'da metinsel ifadeleri (string) tanımlarken tek tırnak (`'`) içindeki bir metinde tekrar tek tırnak kullanmak (örneğin `'doesn't'`) sözdizimi hatasına yol açar. 

Bu hatayı engellemek için tırnağın önüne gelmesi gereken **kaçış karakteri (escape character)** aşağıdakilerden hangisidir?

- [ ] A) `/` (Eğik çizgi)
- [ ] B) `\` (Ters eğik çizgi)
- [ ] C) `.` (Nokta)
- [ ] D) `#` (Diyez)

-----------------------------

### Soru 14
Aşağıdaki Python kod satırı etkileşimli modda çalıştırıldığında ekrana basılacak **doğru çıktı** aşağıdakilerden hangisidir?

```python
print('"Isn\'t," they said.')
```

- [ ] A) `'"Isn\'t," they said.'`
- [ ] B) `"Isn't," they said.`
- [ ] C) `Isn't, they said.`
- [ ] D) Kod hata verir (`SyntaxError`).

-------------------------------

### Soru 15
Python etkileşimli kabuğunda (shell) `s = 'A\nB'` değişkeni tanımlandıktan sonra, sadece `s` yazıp çalıştırmak ile `print(s)` yazıp çalıştırmak arasındaki fark hangi seçenekte doğru açıklanmıştır?

- [ ] A) İki kullanım da ekrana tamamen aynı çıktıyı verir.
- [ ] B) `s` kullanımı hata verir, sadece `print(s)` çalışır.
- [ ] C) `s` yazıldığında kaçış karakteri (`\n`) metin olarak görünür; `print(s)` yazıldığında ise yeni satıra geçilir.
- [ ] D) `print(s)` kullanıldığında metnin başındaki ve sonundaki tırnak işaretleri de ekrana basılır.

-----------------------------

### Soru 16
Aşağıdaki kod bloğu çalıştırıldığında ekrana sırasıyla hangi çıktılar basılır?

```python
yol = 'C:\\yeni\\metin'
print(r'C:\yeni\metin')
```

- [ ] A) `C:\yeni\metin` ve `C:\yeni\metin`
- [ ] B) Alt satırlara bölünmüş hatalı iki çıktı verir.
- [ ] C) `C:\yeni\metin` ve `C:\yeni\metin`
- [ ] D) `C:\yeni\metin` ve `C:\this\name`

--------------------------------

### Soru 17
Aşağıdaki Python kod bloğu çalıştırıldığında ekrana basılacak çıktı hangi seçenekte doğru verilmiştir?

```python
kod = 2 * 'py' + 'thon'
print(kod)
```

- [ ] A) `py py thon`
- [ ] B) `pypypypython`
- [ ] C) `pypython`
- [ ] D) Kod hata verir (TypeError).

-------------------------

### Soru 18
**Doğru mu, Yanlış mı?**

Python'da dize sabitlerini birden fazla satıra yaymak için üçlü tırnak (`"""..."""` veya `'''...'''`) kullanıldığında, kod içinde basılan tüm satır sonu karakterleri varsayılan olarak otomatik olarak dizeye dahil edilir.

- [ ] Doğru
- [ ] Yanlış

----------------------------

### Soru 19
Python'da yan yana yazılan iki dize sabiti (tırnak içindeki metinler) aralarında `+` operatörü olmasa bile otomatik olarak birleştirilir. 

Buna göre, aşağıdaki kod satırlarından hangisi sözdizimi hatası (**SyntaxError**) verir?

- [ ] A) `metin = 'Veri' 'Bilimi'`
- [ ] B) `metin = ('A' 'B' 'C')`
- [ ] C) `dil = 'Py'`; `metin = dil 'thon'`
- [ ] D) `metin = "Yapay" "Zeka"`

-----------------------------

### Soru 20
Bir programcı uzun bir metni kod içinde bölmek için şu yöntemi uygulamıştır:

```python
ornek = ('un' * 3) 'ium'
```

Bu kod satırı çalıştırıldığında Python yorumlayıcısı nasıl bir tepki verir?

- [ ] A) Kod sorunsuz çalışır ve `ornek` değişkenine `'unununium'` atanır.
- [ ] B) Kod çalışır ancak çıktı veri tipi olarak liste (`list`) olur.
- [ ] C) `TypeError` hatası verir çünkü çarpma işlemi yapılamaz.
- [ ] D) `SyntaxError` hatası verir çünkü bir ifade (expression) ile dize sabiti otomatik birleştirilemez.

-----------------------------

### Soru 21
Python'da dizeler sıfır tabanlı indekslenir. Ayrıca sağdan saymaya başlamak için negatif indeksler de kullanılabilir.

Buna göre `word = 'Python'` dizesi için aşağıda verilen indeksleme işlemlerinden hangisi **yanlıştır**?

- [ ] A) `word[0]` ifadesi `'P'` sonucunu verir.
- [ ] B) `word[-1]` ifadesi son karakter olan `'n'` harfini verir.
- [ ] C) `word[-2]` ifadesi sondan ikinci karakter olan `'h'` harfini verir.
- [ ] D) `word[5]` ifadesi `'n'` sonucunu verir.

Açıklama: word[-2] ifadesi sondan ikinci karakter olan 'o' harfini döndürür. 'h' harfi ise word[3] veya word[-3] indeksindedir.

-----------------------------

### Soru 22
Aşağıdaki Python kod bloğu çalıştırıldığında ekrana basılacak çıktı aşağıdakilerden hangisidir?

```python
isim = 'Py'
tam_isim = isim + 'thon'
print(tam_isim[-6])
```

- [ ] A) `n`
- [ ] B) `y`
- [ ] C) `P`
- [ ] D) Kod hata verir (IndexError).

--------------------------------

### Soru 23
Değişkenleri veya bir değişkeni ve bir sabiti birleştirmek istiyorsanız neyi kullanırsınız => + işaretini

ÖRNEK : 
> prefix + 'thon'
> 
>'Python'

-------------------------------

### Soru 24
`word = 'Python'` dizesi için aşağıda yapılan dilimleme (slicing) işlemlerinden hangisinin ekran çıktısı **yanlış** verilmiştir?

- [ ] A) `word[:2]` -> `'Py'`
- [ ] B) `word[4:]` -> `'on'`
- [ ] C) `word[2:5]` -> `'thon'`
- [ ] D) `word[-2:]` -> `'on'`

- Açıklama: Python'da bitiş indeksi her zaman hariç tutulur. word[2:5] işlemi 2, 3 ve 4. indekslerdeki karakterleri alır; 5. indeksteki 'n' karakteri dahil edilmez. Bu yüzden çıktı 'tho' olmalıdır.

------------------------------

### Soru 25
Python'da dilimleme yapılırken başlangıç veya bitiş indeksi boş bırakılırsa varsayılan değerler devreye girer.

Buna göre, herhangi bir `s` dizesi ve geçerli bir `i` tam sayısı için yazılan `s[:i] + s[i:]` kodunun üreteceği sonuç aşağıdakilerden hangisidir?

- [ ] A) Boş bir dize (`''`) döndürür.
- [ ] B) Dizinin sadece ilk ve son harflerini birleştirir.
- [ ] C) Hiçbir karakteri kaybetmeden orijinal `s` dizesinin aynısını döndürür.
- [ ] D) İndeks hatası (`IndexError`) verir.

-------------------------------

### Soru 26
**Doğru mu, Yanlış mı?**

Aşağıdaki şemaya göre `word = 'Python'` dizesinde `word[-2:]` ifadesi çalıştırıldığında, -2 çizgisinden başlayıp dizenin sonuna kadar olan kısmı dilimler ve ekrana `'on'` çıktısını verir.

 +---+---+---+---+---+---+

 | P | y | t | h | o | n |

 +---+---+---+---+---+---+

 0   1   2   3   4   5   6

 -6  -5  -4  -3  -2  -1

- [x] Doğru
- [ ] Yanlış

-------------------------------

### Soru 27
`word = 'Python'` dizesi tanımlandıktan sonra gerçekleştirilen aşağıdaki işlemlerden hangisi Python yorumlayıcısının **IndexError** hatası vermesine neden olur?

- [ ] A) `word[2:42]`
- [ ] B) `word[42:]`
- [ ] C) `word[42]`
- [ ] D) `print(len(word))`

Açıklama: Dilimleme (slicing) işlemlerinde aralık dışı çok büyük indeksler kullanmak hata vermez, Python bunu esnek bir şekilde tolore eder. Ancak tek bir karaktere erişmek için doğrudan word[42] şeklinde indeksleme yapıldığında dize sınırları aşıldığı için IndexError hatası fırlatılır.

---------------------

### Soru 28
Bir programcı elindeki metnin ilk harfini değiştirmek için şu kodu yazmıştır:

```python
program = 'Python'
program[0] = 'J'
```

Bu kod çalıştırıldığında nasıl bir hata (Exception) alınır ve nedeni nedir?

- [ ] A) `ValueError` - 'J' karakteri dizeye uygun değildir.
- [ ] B) `IndexError` - 0 indeksi dize sınırlarının dışındadır.
- [ ] C) `TypeError` - Python dizeleri değiştirilemez (immutable) olduğu için öğe atamasını desteklemez.
- [ ] D) Kod hata vermez, `program` değişkeninin yeni değeri 'Jython' olur.

-------------------------------------

### Soru 29
**Doğru mu, Yanlış mı?**

Python'da bir dizeyi doğrudan değiştiremediğimiz için, var olan bir dizeden parça alıp yeni bir karakterle birleştirerek (`'J' + word[1:]` gibi) tamamen yeni bir dize nesnesi üretmemiz gerekir.

- [x] Doğru
- [ ] Yanlış

--------------------------------------

### Soru 30
Aşağıdaki Python kod bloğu çalıştırıldığında ekrana basılacak çıktı nedir?

```python
s = 'super'
print(len(s * 2))
```

**Cevap:** `10`  
*(Açıklama: `s * 2` işlemi `'supersuper'` dizesini oluşturur. `len()` fonksiyonu bu yeni dizenin karakter sayısını sayarak 10 sonucunu döndürür.)*

-------------------------------------

### Soru 31
Python'da dize sabitlerinin (literal) içine doğrudan değişkenleri veya çalıştırılabilir ifadeleri yerleştirmek için kullanılan ve en modern dize biçimlendirme yöntemi olan yapı aşağıdakilerden hangisidir?

- [ ] A) printf tarzı (%) Biçimlendirme
- [ ] B) str.format() Metodu
- [ ] C) f-dizeleri (f-strings)
- [ ] D) regex (Düzenli İfadeler)

- Açıklama: İçlerinde ifadeler/değişkenler barındıran dize değişmezlerine Python'da f-dizeleri (f-strings) adı verilir ve modern Python kodlarında en çok tercih edilen yöntemdir.

---------------------------------------

### Soru 32
Dizeler (strings) ile ilgili aşağıda verilen ifadelerden hangisi **yanlıştır**?

- [ ] A) Dizeler, sıralı veri tiplerine (sequence types) birer örnektir.
- [ ] B) Dize metotları sayesinde metinler üzerinde temel dönüşümler ve arama işlemleri yapılabilir.
- [ ] C) Python'da `%` operatörü ile yapılan printf tarzı biçimlendirme, dize biçimlendirmenin en yeni ve modern yoludur.
- [ ] D) `str.format()` yöntemi, metin biçimlendirmek için kullanılan geçerli sözdizimlerinden biridir.

- Açıklama: Metinde de belirtildiği üzere, % operatörü ile yapılan printf tarzı işlemler "eski" (legacy) biçimlendirme yöntemleri arasında yer alır.

--------------------------------------

### Soru 33
**Doğru mu, Yanlış mı?**

Dizeler, sıralı veri tiplerinin (sequence types) ortak özelliklerini taşıdıkları için indeksleme, dilimleme ve döngülerle elemanlarına sırayla erişilme gibi yaygın işlemlerin tümünü desteklerler.

- [x] Doğru
- [ ] Yanlış

----------------------------------------

### Soru 34
Python'daki listeler (lists) ve dizeler (strings) arasındaki en temel fark aşağıdakilerden hangisidir?

- [ ] A) Listeler indekslenemez veya dilimlenemez, dizeler ise dilimlenebilir.
- [ ] B) Listeler yalnızca aynı veri türündeki öğeleri kabul eder, dizeler karmaşıktır.
- [ ] C) Dizeler değiştirilemez (immutable) veri türüyken, listeler değiştirilebilir (mutable) bir veri türüdür.
- [ ] D) Listeler birleştirme (`+`) operatörünü desteklemez.

-----------------------------------------

### Soru 35
Aşağıdaki Python kod bloğu çalıştırıldığında ekrana basılacak çıktı hangi seçenekte doğru verilmiştir?

```python
sayilar = [1, 2, 9, 4]
sayilar[2] = 3
yeni_liste = sayilar[-2:] + [5]
print(yeni_liste)
```

- [ ] A) `[9, 4, 5]`
- [ ] B) `[3, 4, 5]`
- [ ] C) `[3, 4, 5]`
- [ ] D) Kod hata verir (TypeError).

- Açıklama: sayilar[2] = 3 satırı listedeki 9 değerini 3 yapar ve liste [1, 2, 3, 4] haline gelir. sayilar[-2:] ifadesi son iki elemanı yani [3, 4] listesini dilimler. Son olarak [5] listesi ile birleştirildiğinde çıktı [3, 4, 5] olur.

-------------------------------

### Soru 36
**Doğru mu, Yanlış mı?**

Python'da bir listenin tüm öğelerinin genellikle aynı türde olması yaygın bir pratik olsa da, listeler yapısal olarak içerisinde farklı veri türlerine ait (örneğin aynı anda hem int, hem str) öğeler barındırabilir.

- [x] Doğru
- [ ] Yanlış

---------------------------------

### Soru 37
Python'da listeler tanımlanırken öğeler arasına virgül konulur ve bu öğeler `....` parantezleri içerisine alınır.

- [ ] A) `( )` (Normal Parantez)
- [x] B) `[ ]` (Köşeli Parantez)
- [ ] C) `{ }` (Süslü Parantez)
- [ ] D) `< >` (Açılı Parantez)

---------------------------------

### Soru 38
Python'da basit atama işlemleri nesneleri kopyalamaz, sadece aynı nesneye bir referans oluşturur. 

Buna göre aşağıdaki kod bloğu çalıştırıldığında ekrana basılacak çıktı nedir?

```python
renkler = ["Mavi", "Yeşil"]
yeni_renkler = renkler
yeni_renkler.append("Sarı")
print(renkler)
```

- [ ] A) `["Mavi", "Yeşil"]`
- [ ] B) `["Mavi", "Yeşil", "Sarı", "Sarı"]`
- [x] C) `["Mavi", "Yeşil", "Sarı"]`
- [ ] D) Kod `AttributeError` hatası verir.

---------------------------------------

### Soru 39
Aşağıdaki Python kodunda `b` listesi, `a` listesinin tüm elemanlarını kapsayacak şekilde `a[:]` yöntemiyle dilimlenerek oluşturulmuştur. 

```python
a = [10, 20, 30]
b = a[:]
b[-1] = 99
```

Bu işlemden sonra `a` ve `b` listelerinin son durumları hangi seçenekte doğru verilmiştir?

- [ ] A) `a: [10, 20, 99]` ve `b: [10, 20, 99]`
- [x] B) `a: [10, 20, 30]` ve `b: [10, 20, 99]`
- [ ] C) `a: [10, 20, 99]` ve `b: [10, 20, 30]`
- [ ] D) Kod `SyntaxError` hatası fırlatır.
- Açıklama: a[:] dilimleme işlemi orijinal listenin sığ bir kopyasını (shallow copy) döndürür. Bu nedenle b üzerinde yapılan değişiklikler orijinal a listesini etkilemez.

------------------------------

### Soru 40
**Doğru mu, Yanlış mı?**

Python'da `list.append()` metodu, argüman olarak verilen yeni öğeyi listenin **başına (0. indeksine)** eklemek için kullanılır.

- [ ] Doğru
- [x] Yanlış
- Açıklama: append() metodu yeni öğeyi listenin her zaman sonuna ekler.

--------------------------------

### Soru 41
Python'da listelerin belirli bir dilimine boş liste (`[]`) atayarak o aralıktaki elemanları silebiliriz.

Buna göre aşağıdaki kod bloğu çalıştırıldığında ekrana basılacak çıktı nedir?

```python
meyveler = ['elma', 'armut', 'muz', 'çilek', 'kiraz']
meyveler[1:4] = []
print(meyveler)
```

- [x] A) `['elma', 'kiraz']`
- [ ] B) `['elma', 'armut', 'kiraz']`
- [ ] C) `['muz', 'çilek', 'kiraz']`
- [ ] D) Kod hata verir (`TypeError`).

- Açıklama: meyveler[1:4] dilimi 1, 2 ve 3. indeksteki elemanları ('armut', 'muz', 'çilek') kapsar. Bu aralığa [] atandığında bu elemanlar silinir ve geriye sadece ['elma', 'kiraz'] kalır.

-------------------------------------------

### Soru 42
Aşağıda iç içe geçmiş listelerden oluşan bir `matris` yapısı tanımlanmıştır:

```python
a = [10, 20]
b = [30, 40]
matris = [a, b]
```

Bu koddan sonra `matris[1][0]` ifadesi çalıştırılırsa elde edilecek çıktı aşağıdakilerden hangisidir?

- [ ] A) `10`
- [ ] B) `20`
- [x] C) `30`
- [ ] D) `40`

---------------------------------------------

### Soru 43
**Doğru mu, Yanlış mı?**

Bir listenin tüm elemanlarını tamamen silmek ve listeyi boşaltmak için `liste[:] = []` yöntemi kullanılabilir.

- [x] Doğru
- [ ] Yanlış

-------------------------------------------

### Soru 44
Aşağıdaki Python kod bloğu çalıştırıldığında `len(x)` fonksiyonunun döndüyeceği tam sayı değeri **..........** olur.

```python
renkler = ['siyah', 'beyaz']
sayilar = [1, 2, 3]
x = [renkler, sayilar]
```
*(Açıklama: `x` listesi iç içe geçmiş iki adet liste elemanı barındırdığı için toplam uzunluğu **2**'dir.)*

--------------------------------------------

### Soru 45
Python'da kullanılan `a, b = b, a + b` gibi çoklu atama (multiple assignment) işlemleriyle ilgili aşağıda verilen ifadelerden hangisi **doğrudur**?

- [ ] A) Önce `a = b` ataması yapılır, ardından güncellenen `a` değeriyle `b = a + b` hesaplanır.
- [ ] B) Atama işlemi sağdan sola değil, soldan sağa doğru sırayla gerçekleşir.
- [x] C) Sağ taraftaki tüm ifadeler, sol taraftaki değişkenlere herhangi bir değer atanmadan önce (eski değerlerle) değerlendirilir.
- [ ] D) Bu işlem bir sözdizimi hatasına (SyntaxError) neden olur. 


- Açıklama: Python'da çoklu atamalarda sağ taraftaki ifadelerin tamamı eski değerlerle hafızada hesaplanır, ardından sol taraftaki değişkenlere aynı anda aktarılır. Bu sayede temp gibi geçici bir değişkene ihtiyaç kalmaz.

--------------------------------------------

### Soru 46
Aşağıdaki Python kod bloğu çalıştırıldığında ekrana basılacak olan **doğru çıktı** hangisidir?

```python
x, y = 1, 2
while x < 6:
    print(x, end="-")
    x, y = y, x + y
```

- [ ] A) `1-2-3-4-5-`
- [x] B) `1-2-3-5-`
- [ ] C) `1\n2\n3\n5`
- [ ] D) `2-3-5-8-`


- Açıklama: Fibonacci mantığıyla çalışan bu döngüde x sırasıyla 1, 2, 3 ve 5 değerlerini alır. Bir sonraki adımda 8 olacağı için while x < 6 koşulu bozulur ve döngü biter. end="-" parametresi de sayıların arasına tire koyarak yan yana yazdırılmasını sağlar.

--------------------------------------------------------

### Soru 47
**Doğru mu, Yanlış mı?**

Python'da `while` döngülerinin koşul kısmında sadece mantıksal karşılaştırmalar (Örn: `a < 10`) kullanılabilir; boş olmayan bir liste (`[1, 2]`) veya sıfırdan farklı bir tam sayı döngü koşulu olarak doğrudan kullanılamaz.

- [ ] Doğru
- [x] Yanlış

- Açıklama: Metinde belirtildiği gibi Python'da sıfır olmayan tüm tam sayılar ve uzunluğu sıfır olmayan tüm diziler/listeler mantıksal olarak "Doğru" (True) kabul edilir ve döngüyü çalıştırır.

----------------------------------------

### Soru 48
Aşağıdaki Python kod satırı çalıştırıldığında ekrana basılacak çıktı nedir?

```python
print(-3 ** 2 + (-3) ** 2)
```

- [ ] A) `18`
- [ ] B) `0`
- [ ] C) `-18`
- [ ] D) Kod hata verir.

---------------------------------------------

### Footnotes

[1] Since ** has higher precedence than -, -3**2 will be interpreted as -(3**2) and thus result in -9. To avoid this and get 9, you can use (-3)**2.

[2] Unlike other languages, special characters such as \n have the same meaning with both single ('...') and double ("...") quotes. The only difference between the two is that within single quotes you don’t need to escape " (but you have to escape \') and vice versa.














