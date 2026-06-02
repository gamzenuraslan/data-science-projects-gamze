## Sorular

### Soru 1: Bir fonksiyonun içinde tanımlanan değişkenlere ne ad verilir? Bu değişkenler fonksiyon dışından neden erişilemez?

**Cevap:** Fonksiyon içinde tanımlanan değişkenlere **yerel (local) değişken** denir. Bu değişkenler yalnızca tanımlandıkları fonksiyon çalışırken var olur ve fonksiyonun yerel kapsamında saklanır. Bu nedenle fonksiyon dışından doğrudan erişilemezler.

---

### Soru 2:

```python
def add(a, b):
    return a + b

print(add(4, 6))
```

Bu kodun çıktısı nedir? `return` ifadesinin görevi nedir?

**Çıktı:**

```text
10
```

`return` ifadesi, fonksiyonun ürettiği sonucu çağıran yere geri gönderir. Bu örnekte `a + b` işleminin sonucu olan `10` döndürülmektedir.

---

### Soru 3: Aşağıdaki iki fonksiyon arasındaki temel fark nedir?

```python
def fib(n):
    print(n)

def fib2(n):
    return n
```

Hangi durumda `print()`, hangi durumda `return` kullanılması daha uygundur?

**Cevap:**

* `print()` sonucu ekrana yazdırır ancak başka bir yerde kullanılmak üzere saklamaz.
* `return` sonucu geri döndürür ve bu değer daha sonra değişkene atanabilir veya başka işlemlerde kullanılabilir.

Örnek:

```python
x = fib2(5)
print(x)
```

Bu nedenle, veriyi daha sonra kullanmak gerekiyorsa **return**, yalnızca kullanıcıya göstermek gerekiyorsa **print()** tercih edilir.

---

### Soru 4: 
```python
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
# Now call the function we just defined:
fib(2000)
```
Bu kodun çıktısı nedir?

**Cevap:**
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

---

### Soru 5: Bir fonksiyonda return ifadesi kullanılmazsa hangi değer döndürülür?

**Cevap**: Fonksiyon otomatik olarak None değerini döndürür.

Örnek:
```python
def test():
    pass

print(test())
```
**Çıktı**: None

---

### Soru 6: Aşağıdaki kodun çıktısı nedir?
```python
def hello():
    print("Hello")

print(hello())
```
**Cevap**: Hello None

İlk olarak fonksiyon içindeki print("Hello") çalışır. Daha sonra fonksiyon return kullanmadığı için None döndürür ve dışarıdaki print() bu değeri ekrana yazdırır.

---

### Soru 7: result.append(a) ne işe yarar?

**Cevap**: result.append(a), a değerini result listesinin sonuna ekler.
```python
result = []
result.append(5)
result.append(10)

print(result)
```
**Çıktı**: [5, 10]

append() kullanmak, result = result + [a] yazmaktan daha verimlidir.

---

### Soru 8: Aşağıdaki fonksiyon çağrılarından hangisinde tüm argümanlar verilmiştir?

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    pass

A)
ask_ok('Do you really want to quit?')

B)
ask_ok('OK to overwrite the file?', 2)

C)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

Cevap: C seçeneği. Çünkü prompt, retries ve reminder argümanlarının tamamı verilmiştir.

---

### Soru 9: Aşağıdaki kodun çıktısı nedir?
```python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```
Cevap: 5

Varsayılan argüman değeri fonksiyon tanımlanırken değerlendirilir. Bu nedenle arg değişkeni 5 değerini alır.

---

### Soru 10: Aşağıdaki fonksiyon tanımına göre `ask_ok('Devam edilsin mi?')` çağrısı yapıldığında `retries` değişkeninin başlangıç değeri ne olur?

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
```

- [ ] A) 0
- [ ] B) 1
- [x] C) 4
- [ ] D) None

---

### Soru 11: Python'da bir değişkenin veya değerin bir dizi (set, liste vb.) içinde olup olmadığını test etmek için hangi anahtar kelime kullanılır?

- [ ] A) is
- [x] B) in
- [ ] C) with
- [ ] D) contain

---

### Soru 12: Aşağıdaki kod bloku çalıştırıldığında ekrana hangi çıktı basılır?

```python
i = 10

def test_func(arg=i):
    print(arg)

i = 20
test_func()
```

- [x] A) 10
- [ ] B) 20
- [ ] C) None
- [ ] D) Hata verir (NameError)

**Açıklama:** Varsayılan argüman değerleri fonksiyon tanımlandığı anda değerlendirilir. Bu nedenle `arg`, `i` değişkeninin o andaki değeri olan `10`'u alır.

---

### Soru 13: Aşağıdaki fonksiyon çağrılarından hangisi **geçersizdir**?

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    pass
```

- [ ] A)
```python
parrot(1000)
```

- [ ] B)

```python
parrot(voltage=1000)
```

- [x] C)

```python
parrot(voltage=5.0, 'dead')
```

- [ ] D)

```python
parrot(action='VOOOOOM', voltage=1000000)
```

**Açıklama:** Anahtar kelime argümanından sonra konumsal (positional) argüman kullanılamaz.

---

### Soru 14: Aşağıdaki kod çalıştırıldığında ne olur?

```python
def function(a):
    pass

function(0, a=0)
```

- [ ] A) Sorunsuz çalışır
- [ ] B) `a` değeri 0 olur
- [x] C) TypeError oluşur
- [ ] D) NameError oluşur

**Açıklama:** `a` parametresine hem konumsal hem de anahtar kelime argümanı ile değer verilmiştir. Bir parametre aynı anda iki kez değer alamaz.

---

### Soru 15: Aşağıdaki fonksiyon tanımında `/` ve `*` sembolleri neyi ifade eder?

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass
```

- [ ] A) Matematiksel işlem operatörleridir.
- [x] B) Parametrelerin nasıl gönderileceğini belirler.
- [ ] C) Döngü oluşturur.
- [ ] D) Hata yakalamak için kullanılır.
**Açıklama:**

* `/` işaretinden önceki parametreler → **yalnızca konumsal (positional-only)**
* `/` ile `*` arasındaki parametreler → **konumsal veya anahtar kelime (positional or keyword)**
* `*` işaretinden sonraki parametreler → **yalnızca anahtar kelime (keyword-only)**

---

### Soru 16: Çıktı nedir?
```python
def func(a, b, /):
    return a + b

func(2, 3)
```

**Cevap:** `5`

**Açıklama:** `a` ve `b` positional-only parametrelerdir. Değerler sırayla verildiği için kod çalışır.

---

### Soru 17: Bu kod çalışır mı? Neden?

```python
def func(a, b, /):
    return a * b

func(a=2, b=3)
```

**Cevap:** Hata verir.

**Açıklama:** `/` işaretinden önceki parametreler keyword olarak verilemez.

---

### Soru 18: Kodun sonucu ne olur?

```python
def func(x, y, /):
    print(x, y)

func(5, y=10)
```

**Cevap:** Hata verir.

**Açıklama:** `y` positional-only parametredir. Keyword ile verilmesi yasaktır.

---

### Soru 19: Çıktı nedir?

```python
def func(a, b):
    return a - b

func(10, 3)
```

**Cevap:** `7`

**Açıklama:** Parametreler normal türdedir ve pozisyonel olarak verilebilir.

---

### Soru 20: Çıktı nedir?

```python
def func(a, b):
    return a / b

func(a=20, b=4)
```

**Cevap:** `5.0`

**Açıklama:** Parametreler keyword kullanılarak verilebilir.

---

### Soru 21: Bu çağrı geçerli midir? Sonuç nedir?

```python
def func(a, b):
    return a + b

func(5, b=7)
```

**Cevap:** `12`

**Açıklama:** `a` pozisyonel, `b` keyword olarak verilmiştir. Bu kullanım geçerlidir.

---

### Soru 22: Çıktı nedir?

```python
def func(*, x, y):
    return x + y

func(x=3, y=4)
```

**Cevap:** `7`

**Açıklama:** `x` ve `y` keyword-only parametrelerdir. Keyword ile verildikleri için kod çalışır.

---

### Soru 23: Bu kod çalışır mı? Neden?

```python
def func(*, x, y):
    return x * y

func(3, 4)
```

**Cevap:** Hata verir.

**Açıklama:** `x` ve `y` keyword-only parametrelerdir. Pozisyonel olarak verilemezler.

---

### Soru 24: Çıktı nedir?

```python
def func(a, *, b, c):
    return a + b + c

func(1, b=2, c=3)
```

**Cevap:** `6`

**Açıklama:** `a` pozisyonel, `b` ve `c` keyword olarak verilmiştir. Kullanım doğrudur.

---

### Soru 25: Çıktı nedir?

```python
def f(a, b, /, c, *, d):
    return a + b + c + d

f(1, 2, 3, d=4)
```

**Cevap:** `10`

**Açıklama:** `a` ve `b` positional-only, `c` normal, `d` keyword-only parametredir. Tüm kurallara uyulmuştur.

---

### Soru 26: Bu kod çalışır mı? Neden?

```python
def f(a, b, /, c, *, d):
    return a + b + c + d

f(a=1, b=2, c=3, d=4)
```

**Cevap:** Hata verir.

**Açıklama:** `a` ve `b` positional-only olduğu için keyword ile verilemez.

---

### Soru 27: Bu çağrı geçerli midir? Sonuç nedir?

```python
def f(a, b, /, c, *, d):
    return a + b + c + d

f(1, 2, c=3, d=4)
```

**Cevap:** `10`

**Açıklama:** `a` ve `b` pozisyonel verilmiş, `c` keyword kullanılmış ve `d` keyword-only kuralına uygun verilmiştir.

**Açıklama2:** Sınıfta öğretmenin yoklama alıyor:

- Positional-only (/) → "İsmini söyleme, sırandaki numarayı ver."
- Keyword-only (*) → "Numara söyleme, mutlaka adını söyle."
- Normal parametre → "İster adını söyle ister numaranı."

---

### Soru 28:

```python
def greet(name):
    print(f"Hello, {name}")

greet("Gamze")
```

**Cevap:** `Hello, Gamze`

**Açıklama:** `name` parametresi positional-or-keyword türündedir. Argüman pozisyonel olarak verilmiştir.

---

### Soru 29:

```python
def greet(name):
    print(f"Hello, {name}")

greet(name="Gamze")
```

**Cevap:** `Hello, Gamze`

**Açıklama:** `name` parametresi keyword olarak verilmiştir. Positional-or-keyword parametrelerde bu kullanım geçerlidir.

---

### Soru 30:

```python
def add(a, b):
    return a + b

print(add(5, b=10))
```

**Cevap:** `15`

**Açıklama:** `a` pozisyonel, `b` keyword argüman olarak verilmiştir.

---

### Soru 31:

```python
def divide(x, y, /):
    return x / y

print(divide(10, 2))
```

**Cevap:** `5.0`

**Açıklama:** `x` ve `y` positional-only parametrelerdir. Doğru şekilde pozisyonel verilmiştir.

---

### Soru 32:

```python
def divide(x, y, /):
    return x / y

print(divide(x=10, y=2))
```

**Cevap:** `TypeError`

**Açıklama:** `x` ve `y`, `/` işaretinden önce bulunduğu için keyword ile verilemez.

---

### Soru 33:

```python
def multiply(a, b, /, c):
    return a * b * c

print(multiply(2, 3, c=4))
```

**Cevap:** `24`

**Açıklama:** `a` ve `b` positional-only, `c` ise positional-or-keyword parametresidir.

---

### Soru 34:

```python
def create_user(*, username):
    print(username)

create_user(username="gamze")
```

**Cevap:** `gamze`

**Açıklama:** `username` keyword-only parametredir ve adıyla verilmelidir.

---

### Soru 35:

```python
def create_user(*, username):
    print(username)

create_user("gamze")
```

**Cevap:** `TypeError`

**Açıklama:** `username` keyword-only parametredir. Pozisyonel olarak verilemez.

---

### Soru 36:

```python
def register(name, *, age):
    print(name, age)

register("Gamze", age=21)
```

**Cevap:** `Gamze 21`

**Açıklama:** `name` normal parametre, `age` keyword-only parametredir.

---

### Soru 37:

```python
def func(a, b, /, c, *, d):
    print(a, b, c, d)

func(1, 2, 3, d=4)
```

**Cevap:** `1 2 3 4`

**Açıklama:** Tüm parametreler kurallarına uygun şekilde verilmiştir.

---

### Soru 38:

```python
def func(a, b, /, c, *, d):
    print(a, b, c, d)

func(a=1, b=2, c=3, d=4)
```

**Cevap:** `TypeError`

**Açıklama:** `a` ve `b` positional-only parametrelerdir. Keyword olarak verilemezler.

---

### Soru 39:

```python
def func(a, b, /, c, *, d):
    print(a, b, c, d)

func(1, 2, c=3, d=4)
```

**Cevap:** `1 2 3 4`

**Açıklama:** `c`, positional-or-keyword olduğu için keyword ile verilebilir.

---

### Soru 40:

```python
def standard_arg(arg):
    print(arg)

standard_arg(2)
```

**Cevap:** `2`

**Açıklama:** Fonksiyonda `/` veya `*` yoktur. Argüman pozisyonel olarak verilebilir.

---

### Soru 41:

```python
def standard_arg(arg):
    print(arg)

standard_arg(arg=2)
```

**Cevap:** `2`

**Açıklama:** `arg` normal parametredir. Keyword olarak da verilebilir.

---

### Soru 42:

```python
def pos_only_arg(arg, /):
    print(arg)

pos_only_arg(1)
```

**Cevap:** `1`

**Açıklama:** `arg`, `/` öncesinde olduğu için positional-only parametredir ve pozisyonel verilmiştir.

---

### Soru 43:

```python
def pos_only_arg(arg, /):
    print(arg)

pos_only_arg(arg=1)
```

**Cevap:** `TypeError`

**Açıklama:** `arg` positional-only olduğu için keyword olarak verilemez.

---

### Soru 44:

```python
def kwd_only_arg(*, arg):
    print(arg)

kwd_only_arg(3)
```

**Cevap:** `TypeError`

**Açıklama:** `arg`, `*` sonrasında olduğu için keyword-only parametredir. Pozisyonel verilemez.

---

### Soru 45:

```python
def kwd_only_arg(*, arg):
    print(arg)

kwd_only_arg(arg=3)
```

**Cevap:** `3`

**Açıklama:** `arg` keyword-only parametredir ve doğru şekilde keyword ile verilmiştir.

---

### Soru 46:

```python
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1, 2, 3)
```

**Cevap:** `TypeError`

**Açıklama:** `kwd_only`, `*` sonrasında olduğu için keyword ile verilmelidir. Pozisyonel verilemez.

---

### Soru 47:

```python
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1, 2, kwd_only=3)
```

**Cevap:** `1 2 3`

**Açıklama:** `pos_only` pozisyonel, `standard` pozisyonel, `kwd_only` keyword olarak verilmiştir.

---

### Soru 48:

```python
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1, standard=2, kwd_only=3)
```

**Cevap:** `1 2 3`

**Açıklama:** `standard`, positional-or-keyword olduğu için keyword ile verilebilir.

---

### Soru 49:

```python
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(pos_only=1, standard=2, kwd_only=3)
```

**Cevap:** `TypeError`

**Açıklama:** `pos_only`, `/` öncesinde olduğu için keyword olarak verilemez.

---

### Soru 50:

```python
def foo(name, **kwds):
    return 'name' in kwds

print(foo(1, **{'name': 2}))
```

**Cevap:** `TypeError`

**Açıklama:** `name` hem ilk parametreye hem de `**kwds` içine verilmek istenir. Bu yüzden çakışma olur.

---

### Soru 51:

```python
def foo(name, /, **kwds):
    return 'name' in kwds

print(foo(1, **{'name': 2}))
```

**Cevap:** `True`

**Açıklama:** `name` positional-only olduğu için `1` değeri ilk parametreye gider. `**kwds` içinde ayrıca `'name'` anahtarı bulunabilir.

---

### Soru 52:

Aşağıdaki parametrelerden hangisi **sadece pozisyonel (positional-only)** parametredir?

```python
def f(a, b, /, c, *, d):
    pass
```

- [ ] A) `c`  
- [ ] B) `d`  
- [x] C) `a` ve `b`  
- [ ] D) Tümü

**Açıklama:** `/` işaretinden önce bulunan `a` ve `b` positional-only parametrelerdir.

---

### Soru 53:

Aşağıdaki parametrelerden hangisi **keyword-only** parametredir?

```python
def f(a, b, /, c, *, d):
    pass
```

- [ ] A) `a`  
- [ ] B) `b`  
- [ ] C) `c`  
- [x] D) `d`

**Açıklama:** `*` işaretinden sonra bulunan parametreler keyword-only'dir.

---

### Soru 54:

Aşağıdakilerden hangisi positional-only parametre kullanımının amaçlarından biridir?

- [ ] A) Parametrelerin keyword ile verilmesini zorunlu kılmak

- [x] B) Parametre isimlerini kullanıcıdan gizlemek

- [ ] C) Fonksiyona varsayılan değer atamak

- [ ] D) Parametre sayısını artırmak

**Açıklama:** Positional-only parametrelerde kullanıcı parametre adını kullanamaz.

---

### Soru 55:

Aşağıdakilerden hangisi keyword-only parametre kullanımının avantajlarından biridir?

- [ ] A) Argümanların sırasını zorunlu kılmak

- [ ] B) Parametre isimlerini gizlemek

- [x] C) Fonksiyon çağrılarının daha okunabilir olmasını sağlamak

- [ ] D) Tüm parametreleri pozisyonel yapmak

**Açıklama:** Keyword-only parametreler fonksiyon çağrılarında açıklık ve okunabilirlik sağlar.

---

### Soru 56:

Bir API geliştirirken gelecekte parametre adını değiştirmek istiyorsanız hangi parametre türü tercih edilmelidir?

- [ ] A) Keyword-only

- [x] B) Positional-only

- [ ] C) Varsayılan parametre

- [ ] D) `*args`

**Açıklama:** Kullanıcı parametre adını kullanamayacağı için isim değişikliği API'yi bozmaz.

---

### Soru 57:

Aşağıdaki fonksiyon çağrılarından hangisi geçerlidir?

```python
def f(a, /, b, *, c):
    pass
```

- [ ] A)

```python
f(a=1, b=2, c=3)
```

- [x] B)

```python
f(1, 2, c=3)
```

- [ ] C)

```python
f(1, b=2, 3)
```

- [ ] D)

```python
f(1, 2, 3)
```

**Açıklama:** `a` positional-only, `c` keyword-only olduğu için yalnızca B seçeneği kurallara uygundur.

---

### Soru 58:

Aşağıdaki ifadelerden hangisi doğrudur?

- [ ] A) `/` işaretinden sonraki tüm parametreler keyword-only olur.

- [ ] B) `*` işaretinden sonraki tüm parametreler positional-only olur.

- [x] C) `*` işaretinden sonraki tüm parametreler keyword-only olur.

- [ ] D) `/` işareti tüm parametreleri keyword-only yapar.

**Açıklama:** `*` sonrasındaki parametreler yalnızca keyword ile verilebilir.

---

### Soru 59:

Aşağıdaki fonksiyon tanımında `username` hangi tür parametredir?

```python
def create_user(*, username):
    pass
```

- [ ] A) Positional-only

- [ ] B) Positional-or-keyword

- [x] C) Keyword-only

- [ ] D) Variable-length

**Açıklama:** `*` sonrasında bulunduğu için keyword-only parametredir.

---

### Soru 60:

Aşağıdaki fonksiyon tanımında `id` hangi tür parametredir?

```python
def get_user(id, /):
    pass
```

- [x] A) Positional-only

- [ ] B) Keyword-only

- [ ] C) Positional-or-keyword

- [ ] D) Optional

**Açıklama:** `/` öncesinde bulunduğu için positional-only parametredir.

---

### Soru 61:

Aşağıdaki ifadelerden hangisi yanlıştır?

- [ ] A) Positional-only parametreler keyword ile verilemez.

- [ ] B) Keyword-only parametreler pozisyonel olarak verilemez.

- [ ] C) Positional-or-keyword parametreler her iki şekilde de verilebilir.

- [x] D) Keyword-only parametreler sadece pozisyonel olarak verilebilir.

**Açıklama:** Keyword-only parametreler yalnızca keyword kullanılarak verilebilir.

---

## 🚀 Tebrikler!

Python **Functions (Fonksiyonlar)** konusuna ait tüm temel testleri başarıyla tamamladınız. Bu havuzdaki sorular doğrudan resmi Python dokümantasyonundaki fonksiyon tanımları, varsayılan argümanlar, anahtar kelime argümanları, positional-only ve keyword-only parametreler gibi standart senaryolar baz alınarak hazırlanmıştır.

Daha fazla pratik ve yeni konular için depoyu takipte kalın! 💻🐍

### ⭐ GitHub

Bu içerik faydalı olduysa projeye yıldız (⭐) vermeyi ve depoyu takip etmeyi unutmayın.

**Happy Coding! 🐍💻**

> "Code is like humor. When you have to explain it, it’s bad."
> — Cory House

---

Made with ❤️ and PeonyCode_GNA