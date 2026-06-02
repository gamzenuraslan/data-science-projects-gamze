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

