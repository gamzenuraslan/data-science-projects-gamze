## Sorular

### S1.
`if` bloklarındaki `elif` ifadesinin temel görevi nedir?
- [ ] A) Yeni bir döngü başlatır.
- [ ] B) 'else if' kısaltmasıdır ve aşırı girintiyi (kodun sağa kaymasını) önler.
- [ ] C) Kullanılması zorunlu bir yapıdır.
- [ ] D) Sadece `match` ifadesiyle birlikte çalışır.

-------------------

### S2.
Kullanıcı girdi olarak `0` girerse bu kod ne yazdırır?
```python
x = int(input("Please enter an integer: "))
if x < 0:
    print('Negative')
elif x == 0:
    print('Zero')
else:
    print('More')
```

-------------------------

### S3.
Bir değeri birden fazla sabitle karşılaştırırken `if...elif` yerine hangi yapı önerilir?
- *Cevap:* Belirli sabitler veya veri türleri kontrol edilirken `match` yapısı daha temiz bir alternatiftir.

----------------------------

**ÖNEMLİ:** Bir `if... elif... elif...` dizisi, diğer dillerde bulunan **`switch` veya `case`** ifadelerinin yerine geçer.

---------------------------

### S4.
Python'daki `for` döngüsünün C veya Pascal dillerinden temel farkı nedir?
- [ ] A) Sadece aritmetik sayı dizileri üzerinde çalışabilir.
- [ ] B) Döngü adımını ve durma koşulunu kullanıcının manuel tanımlamasını zorunlu kılar.
- [x] C) Herhangi bir dizinin (liste, dize vb.) öğeleri üzerinde, göründükleri sırayla yineleme yapar.
- [ ] D) Sözlük (dictionary) veri tiplerinde asla kullanılamaz.

------------------------

### S5.
Aşağıdaki kod bloğu çalıştırıldığında ekrana ne yazdırır?
```python
words = ['cat', 'window']
for w in words:
    print(w, len(w))
```
```text
cat 3
window 6
```
-----------------

### S6.
Bir koleksiyon (örneğin bir sözlük) üzerinde döngü yaparken, aynı koleksiyon içinden eleman silmek istiyorsak kodun hata vermemesi için hangi strateji uygulanmalıdır?

**Doğru Cevap:** Koleksiyonun bir kopyası (`.copy()`) üzerinde döngü kurulmalı veya filtrelenmiş elemanlarla yeni bir koleksiyon oluşturulmalıdır.

------------------

### S7.
`range()` fonksiyonunun döndürdüğü nesnenin yapısı ve bellek yönetimi hakkında aşağıdakilerden hangisi doğrudur?

- [ ] A) Bellekte doğrudan elemanların tamamını içeren gerçek bir liste oluşturur.
- [ ] B) Sadece pozitif yönde artan sayılar üretebilir, negatif adım (step) alamaz.
- [ ] C) Tanımlanan bitiş noktasındaki (stop) sayıyı her zaman üretilen diziye dahil eder.
- [X] D) Gerçek bir liste oluşturmak yerine elemanları sırayla üreten, bellek tasarruflu bir yinelenebilirdir (iterable).

----------------------

### S8.
Aşağıdaki kod bloğu çalıştırıldığında ekrana basılacak çıktı hangisidir?

```python
print(list(range(0, 10, 3)))
```

- [ ] A) `[0, 3, 6, 9, 12]`
- [X] B) `[0, 3, 6, 9]`
- [ ] C) `[3, 6, 9]`
- [ ] D) `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

--------------------

### S9.
Bir listenin hem indekslerine hem de elemanlarına aynı anda erişmek için `range(len(liste))` hiyerarşisi yerine Pythonic (dile uygun) olarak hangi fonksiyonun kullanılması önerilir?

- [X] A) `enumerate()`
- [ ] B) `sum()`
- [ ] C) `sorted()`
- [ ] D) `zip()`

---

### S10.
Negatif adımlı (step) `range(-10, -100, -30)` ifadesi bir listeye dönüştürüldüğünde elde edilecek doğru çıktı aşağıdakilerden hangisidir?

- [ ] A) `[-10, -40, -70, -100]`
- [X] B) `[-10, -40, -70]`
- [ ] C) `[-40, -70, -100]`
- [ ] D) `[]`

---

### S11.
Aşağıdaki `range()` fonksiyonlarından hangisi çıktı olarak `[0, 3, 6, 9]` dizisini üretir?

- [ ] A) `list(range(0, 9, 3))`
- [X] B) `list(range(0, 10, 3))`
- [ ] C) `list(range(3, 10, 3))`
- [ ] D) `list(range(0, 12, 3))`

---

### S12.
`list(range(5, 10))` ifadesinin çıktısında `10` değerinin **yer almamasının** temel nedeni aşağıdakilerden hangisidir?

- [ ] A) Başlangıç değerinin 5 olarak belirlenmiş olması.
- [ ] B) Fonksiyonun varsayılan adım değerinin 1 olması.
- [X] C) Verilen bitiş noktasının hiçbir zaman oluşturulan dizinin bir parçası olmaması.
- [ ] D) `range()` nesnesinin sadece çift sayıları üretmesi.

---

### S13.
Bir listenin indeksleri üzerinde döngü kurmak için kullanılan `range(len(a))` yapısı hakkında aşağıdakilerden hangisi doğrudur?

- [ ] A) Liste elemanlarının sadece kendilerine (değerlerine) erişim sağlar.
- [X] B) `len(a)` ifadesi listenin eleman sayısını verir, `range()` ise 0'dan bu sayıya kadar (bu sayı hariç) geçerli indeksleri üretir.
- [ ] C) Listenin uzunluğu ne olursa olsun her zaman 0 ile 4 arasında sabit değerler üretir.
- [ ] D) Bu yapı kullanıldığında liste elemanlarının sırası otomatik olarak tersine döner.

---

### S14.
Aşağıdaki kod bloğu çalıştırıldığında çıktı olarak ne üretir?

```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
```

- [ ] A) `Mary had a little lamb`
- [ ] B) `0, 1, 2, 3, 4`
- [X] C) `0 Mary` / `1 had` / `2 a` / `3 little` / `4 lamb` (Her biri yeni satırda)
- [ ] D) `1 Mary` / `2 had` / `3 a` / `4 little` / `5 lamb` (Her biri yeni satırda)

---

### S15.
`a = ['X', 'Y', 'Z']` listesi için `range(len(a))` ifadesi döngü içinde sırasıyla hangi `i` değerlerini üretir?

- [ ] A) `[1, 2, 3]`
- [ ] B) `[0, 1, 2, 3]`
- [X] C) `[0, 1, 2]`
- [ ] D) `['X', 'Y', 'Z']`

---

### S16.
Python'da `print(range(10))` komutu çalıştırıldığında ekrana `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` şeklinde bir liste yerine doğrudan `range(0, 10)` yazdırılmasının temel nedeni aşağıdakilerden hangisidir?

- [ ] A) Kodda bir sözdizimi (syntax) hatası olması.
- [ ] B) `range()` fonksiyonunun sadece `sum()` fonksiyonu ile birlikte çalışabilmesi.
- [X] C) `range()` nesnesinin gerçek bir liste oluşturmaması, elemanları döngü esnasında sırayla üreten bellek tasarruflu bir yinelenebilir (iterable) olması.
- [ ] D) Python'ın yazdırma (print) fonksiyonunun sayı dizilerini desteklememesi.

---

### S17.
Aşağıdaki kod satırı çalıştırıldığında çıktı olarak hangi sayısal değeri üretir?

```python
print(sum(range(4)))
```

- [ ] A) `4`
- [X] B) `6`
- [ ] C) `10`
- [ ] D) `0`

---

### S18.
Python dokümantasyonunda geçen "yinelenebilir (iterable)" kavramının tanımı aşağıdakilerden hangisinde en doğru şekilde verilmiştir?

- [ ] A) Sadece tek bir sayısal değeri hafızada tutabilen sabit yapılardır.
- [ ] B) Döngü bittikten sonra kendi kendini tamamen silen fonksiyonlardır.
- [X] C) Kendisinden ardışık öğeler elde edilebilen, `for` veya `sum()` gibi yapıların hedef alıp tüketebileceği nesnelerdir.
- [ ] D) İçeriği hiçbir şekilde değiştirilemeyen ve ekrana yazdırılamayan gizli listelerdir.

---

### S19.
İç içe (nested) döngülerin kullanıldığı bir kod bloğunda, en içteki döngünün altında çalışan bir `break` ifadesinin temel görevi nedir?

- [ ] A) Tüm programın çalışmasını tamamen durdurur.
- [x] B) Sadece içinde bulunduğu en içteki döngüyü sonlandırarak dışarı çıkar.
- [ ] C) Dıştaki döngü dahil olmak üzere tüm döngüleri aynı anda bitirir.
- [ ] D) Döngüyü kırmaz, sadece o adımı atlayıp bir sonraki elemana geçer.

---

### S20.
Aşağıdaki kod bloğu çalıştırıldığında ekrana basılacak ilk satır aşağıdakilerden hangisidir?

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
```

- [ ] A) `2 equals 2 * 1`
- [ ] B) `3 equals 3 * 1`
- [x] C) `4 equals 2 * 2`
- [ ] D) `5 equals 1 * 5`

---

### S21.
Aşağıdaki kod bloğunda yer alan `continue` ifadesinin bu programdaki işlevi nedir?

```python
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
```

- [x] A) Çift bir sayı ekrana yazdırıldıktan sonra, alt satırdaki tek sayı print'ine geçmeden doğrudan döngünün bir sonraki aşamasına (num değerine) atlar.
- [ ] B) Sayı çift olduğunda döngüyü tamamen kırıp programı sonlandırır.
- [ ] C) Kodun sürekli `Found an even number 2` yazdırmasını sağlayarak sonsuz döngü oluşturur.
- [ ] D) `num` değerini otomatik olarak ikişer ikişer artırır.

---

### S22.
Çıktısı ne olur?
```python
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
```
```test
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```
---

### S23.
Python'daki `for` veya `while` döngülerinin hemen ardına eklenen `else:` bloğunun çalışma mantığı hakkında verilen aşağıdaki ifadelerden hangisi **yanlıştır**?

- [ ] A) `for` döngüsünde `else` bloğu, döngünün son yinelemesi başarıyla tamamlandıktan sonra yürütülür.
- [ ] B) `while` döngüsünde `else` bloğu, döngünün koşulu `False` (yanlış) haline geldiğinde çalıştırılır.
- [X] C) Döngü gövdesi içinde bir `break` ifadesi tetiklenirse, döngünün arkasındaki `else` bloğu yine de çalışır.
- [ ] D) Döngüden `return` ile çıkılması veya döngü içinde bir istisna (exception) fırlatılması durumunda `else` bloğu atlanır.

---

### S24.
Aşağıdaki asal sayı bulma algoritmasında `else` anahtar kelimesi hizalama olarak `for` döngüsüne aittir. 

```python
for n in range(2, 5):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'bölündü')
            break
    else:
        print(n, 'asal sayı')
```

Bu kod bloğu çalıştırıldığında ekrana basılacak **ilk iki satır** sırasıyla hangisidir?

- [X] A) `2 asal sayı` ve `3 asal sayı`
- [ ] B) `2 bölündü` ve `3 bölündü`
- [ ] C) `2 asal sayı` ve `4 bölündü`
- [ ] D) `3 asal sayı` ve `4 bölündü`

---

### S25.
Dokümantasyona göre döngülerdeki `else` yan tümcesi, `if` ifadesindeki `else` yapısından ziyade mantıksal olarak **`try...except`** bloklarında bulunan hangi yapının çalışma davranışına benzer?

- [ ] A) `except` (Bir hata yakalandığında çalışır)
- [ ] B) `finally` (Hata olsun ya da olmasın her zaman çalışır)
- [X] C) `else` (Blok içinde hiçbir istisna/hata oluşmadığında çalışır)
- [ ] D) `raise` (Yapay bir hata fırlatmak için kullanılır)

---

### S26.
Çıktı ne olur?
```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```
```test
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```
---

### S27.
Python'da sözdizimsel (syntax) olarak bir kod bloğu yazılması zorunlu olduğunda, ancak programın mantıksal olarak hiçbir işlem yapması istenmediğinde aşağıdaki anahtar kelimelerden hangisi kullanılır?

- [ ] A) `continue`
- [ ] B) `break`
- [x] C) `pass`
- [ ] D) `return`


**Açıklama**:Sonsuz Döngüler (Meşgul Bekleme): Programın bir kesme sinyali (Ctrl+C gibi) gelene kadar hiçbir işlem yapmadan beklemesi istendiğinde kullanılır.
  
- Minimal Sınıf Tanımları: Gövdesi boş, sadece isimden ibaret olan sınıflar oluşturmak için tercih edilir.
- Kod Yer Tutucusu (Placeholder): Yeni bir fonksiyon veya koşul yazarken, detayları sonra düşünmek üzere soyut bir taslak bırakmanızı sağlar.

---

### S28.
Aşağıda verilen `pass` ifadesinin kullanım senaryolarından hangisi dokümantasyona göre **geçersiz veya hatalıdır**?

- [ ] A) `while True: pass` şeklinde klavyeden kesme (Ctrl+C) bekleyen döngüler oluşturmak.
- [ ] B) `class MyEmptyClass: pass` yazarak içi tamamen boş, minimal sınıflar tanımlamak.
- [ ] C) Bir fonksiyonun içini daha sonra doldurmak üzere `def initlog(*args): pass` şeklinde yer tutucu (placeholder) olarak bırakmak.
- [x] D) Döngünün akışını bozup bir sonraki elemana zorla atlamak amacıyla `pass` kullanmak.

---

### S29.
Python'da yeni bir fonksiyon geliştirirken gövdeyi boş bırakmak için geleneksel olarak kullanılan `pass` yerine, dil tanımının resmi bir parçası olmasa da birçok yazılımcı tarafından yer tutucu olarak tercih edilen **üç nokta** simgesinin Python'daki nesne adı nedir?

- [ ] A) `None`
- [x] B) `Ellipsis` (...)
- [ ] C) `Placeholder`
- [ ] D) `Empty`

**Açıklama**: Üç Nokta (...) Nesnesi (Ellipsis)
- Fonksiyon veya koşul gövdelerinde yer tutucu olarak pass yerine sıklıkla üç nokta (...) işareti de kullanılır. 
- Farkı Nedir? Python dil tanımı için özel veya teknik bir üstünlüğü yoktur. Burada herhangi bir sabit (literal) ifade de kullanılabilir.
- Neden Kullanılır? Geleneksel olarak yazılımcılar arasında "buraya daha sonra kod gelecek" anlamına gelen görsel bir işaret (yer tutucu) olarak yaygınlaşmıştır.

---

### S30.
Python'daki `match-case` yapısında kullanılan joker karakter (`_`) ve veya (`|`) operatörü hakkında aşağıdakilerden hangisi doğrudur?

- [ ] A) `case _:` bloğu her zaman en başta tanımlanmalıdır, aksi takdirde kod hata verir.
- [x] B) `case 401 | 403 | 404:` ifadesi, gelen değerin bu üç sabitten herhangi biriyle eşleşmesi durumunda çalışır.
- [ ] C) Joker karakter (`_`) bir değerle eşleştiğinde, o değeri daha sonra kullanabilmemiz için bir değişkene bağlar (bind).
- [ ] D) `match` yapısında hiçbir durum (case) eşleşmezse, Python otomatik olarak bir hata (exception) fırlatır.

---

### S31.
Aşağıdaki kod bloğunda `point = (0, 5)` olarak tanımlanmıştır.

```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case _:
        print("Something else")
```

Bu kod çalıştırıldığında ekrana basılacak çıktı aşağıdakilerden hangisidir?

- [ ] A) `Origin`
- [ ] B) `Y=0`
- [x] C) `Y=5`
- [ ] D) `Something else`

---

### S32.
Bir `case` kalıbına eklenen `if` koşulu (koruma - guard) ile ilgili aşağıda verilen bilgilerden hangisi doğrudur?

- [ ] A) Koruma (`if`) koşulu yanlış (`False`) değerlendirilirse, `match` yapısı doğrudan sonlanır ve sonraki bloklara bakılmaz.
- [x] B) Kalıptaki değer yakalama (değişken bağlama) işlemi, `if` koruma koşulu değerlendirilmeden **önce** gerçekleşir.
- [ ] C) `case` satırlarında `if` kullanıldığında, `else` bloğunun da eklenmesi zorunludur.
- [ ] D) Koruma koşulları sadece liste kalıplarında çalışır; sınıf veya sözlük kalıplarında kullanılamaz.

---

### S33.
Sınıf özniteliklerinin sırasını belirtmek amacıyla tanımlanan özel Python niteliği (`__match_args__ = ('x', 'y')`) sayesinde, `case Point(1, 2):` şeklinde konum parametreli eşleştirme yapılabilmektedir. 

Buna göre, adlandırılmış sabitlerin (örneğin bir `Enum` sınıfının elemanlarının) `case` içinde birer yakalama değişkeni olarak **yorumlanmasını önlemek** için dökümantasyonda önerilen yöntem aşağıdakilerden hangisidir?

- [ ] A) Sabit adlarının önüne alt çizgi (`_`) koymak.
- [ ] B) Sabitleri `as` anahtar kelimesiyle yeniden adlandırmak.
- [ ] C) Sabitleri doğrudan tek bir harf olarak tanımlamak.
- [x] D) `Color.RED` gibi noktalı adlar (dotted names) kullanmak.

---

**Önemli Bilgi**:Python'daki match-case, diğer dillerdeki basit switch-case yapısının çok daha gelişmiş ve akıllı bir versiyonudur:
- Sadece değer kontrolü yapmaz; gelen verinin yapısını, tipini (liste, sözlük, sınıf) ve şeklini inceler.
- Veriyi parçalarına ayırır (Unpacking); eşleşme anında verinin içindeki elemanları doğrudan yeni değişkenlere atayabilir (case (x, 0): gibi).
- Esnektir; if koşulları eklenerek (if x == y) filtreleme derinleştirilebilir.
- Joker Karakter (_); hiçbir kurala uymayan durumları yakalamak için en sona eklenir.
- Yani match-case sadece bir "değer karşılaştırıcı" değil, aynı zamanda güçlü bir "veri ayrıştırıcıdır".

---

### S34.
Aşağıdaki kod bloğunda `point` değişkeni `(0, 5)` şeklinde bir demet (tuple) olarak tanımlanmıştır.

```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

Bu kod çalıştırıldığında ekrana basılacak doğru çıktı aşağıdakilerden hangisidir?

- [ ] A) `Origin`
- [ ] B) `Y=0`
- [x] C) `Y=5`
- [ ] D) `X=0, Y=5`

---

### S35.
Aşağıdaki kod bloğunda `where_is` fonksiyonuna argüman olarak `Point(0, 0)` nesnesi gönderilmiştir.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(0, 0))
```

Bu programın çıktısı aşağıdakilerden hangisidir?

- [x] A) `Origin`
- [ ] B) `Somewhere else`
- [ ] C) `Not a point`
- [ ] D) `Y=0`

---

### S36.
Dokümantasyonda verilen aşağıdaki sınıf tanımına göre, `case [Point(0, y1), Point(0, y2)]:` kalıbının başarıyla eşleşebilmesi için sınıf içinde tanımlanan hangi özel öznitelik (attribute) konum parametrelerinin sırasını belirler?

```python
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

- [ ] A) `__init__`
- [x] B) `__match_args__`
- [ ] C) `__slots__`
- [ ] D) `__dict__`

---

### S37.
Aşağıdaki kod bloğunda bir `if` koşulu (koruma - guard) kullanılmıştır.

```python
point = Point(4, 4)  # x=4, y=4 özellikleri atanmıştır.

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

Bu kodun çıktısı ve çalışma mantığı hakkında aşağıdakilerden hangisi doğrudur?

- [ ] A) Çıktı `Not on the diagonal` olur çünkü `if` korumaları nesne özniteliklerini kontrol edemez.
- [ ] B) Kod hata verir çünkü `case` içinde `if` kullanımı desteklenmez.
- [x] C) Değer yakalama işlemi koruma değerlendirilmeden önce gerçekleşir; `x == y` şartı sağlandığı için çıktı `Y=X at 4` olur.
- [ ] D) İlk `case` atlanır ve doğrudan ikinci `case` çalışır.

---

## 🚀 Tebrikler!
Python Kontrol Akışı (`Control Flow`) konusuna ait tüm temel testleri başarıyla tamamladınız. Bu havuzdaki sorular doğrudan resmi Python dokümantasyonundaki standart senaryolar (indeks döngüleri, nesne kalıpları ve bellek yönetim kuralları) baz alınarak üretilmiştir.

Daha fazla pratik ve yeni konular için depoyu takipte kalın! 💻🐍

### ⭐ GitHub

Bu içerik faydalı olduysa projeye yıldız (⭐) vermeyi ve depoyu takip etmeyi unutmayın.

**Happy Coding! 🐍💻**

> "First, solve the problem. Then, write the code."
> — John Johnson

---

Made with ❤️ and PeonyCode_GNA