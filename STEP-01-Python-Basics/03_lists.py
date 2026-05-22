# ---------------------------------------------
# 03 - LISTS
# ---------------------------------------------

# Listeler birden fazla değeri tek bir değişkende tutmamızı sağlar.
numbers = [10, 20, 30, 40, 50, 60, 10, 10]

print(numbers)

# Listenin ilk elemanına erişme
print(numbers[0])

# Listenin son elemanına erişme
print(numbers[-1])

# Liste uzunluğunu bulma
print(len(numbers))

# append() listenin sonuna yeni bir eleman ekler.
numbers.append(100)
print(numbers)

# insert() belirli bir index'e eleman ekler.
numbers.insert(1, 15)
print(numbers)

# remove() listedeki ilk eşleşen değeri siler.
numbers.remove(20)
print(numbers)

# pop() listenin son elemanını siler ve döndürür.
last_number = numbers.pop()
print(last_number)
print(numbers)

# count() listede bir değerden kaç tane olduğunu sayar.
number_count = numbers.count(10)
print(number_count)

# sort() listeyi küçükten büyüğe sıralar.
numbers.sort()
print(numbers)

# reverse() listenin sırasını tersine çevirir.
numbers.reverse()
print(numbers)

# copy() listenin bir kopyasını oluşturur.
copied_numbers = numbers.copy()
print(copied_numbers)

# Bir değerin listede olup olmadığını kontrol etme
print(30 in numbers)
print(500 in numbers)

# Liste üzerinde for döngüsü ile gezinme
for number in numbers:
    print(number)

# sum(), min(), max() kullanımı
print(sum(numbers))
print(min(numbers))
print(max(numbers))

# clear() listenin içindeki tüm elemanları siler.
numbers.clear()
print(numbers)

# Not: Daha fazla liste metoduna ulaşmak için editörde "numbers." yazdıktan sonra çıkan önerileri inceleyebilirsiniz.