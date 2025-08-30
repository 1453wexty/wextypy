"""
BİRİNCİ DERS
"""

# Python dilinde "print" fonksiyonu bir nesneyi ekrana yazdırmak için kullanılır.
# Python dilinde text ile uğraşırken, text tırnak (" ") içerisine alınmalıdır.
print("Hello, World!")

# Python dilinde girintiler (indentation) önemlidir.
# Örneğin, bir koşul ifadesi yazarken koşulun içindeki kod bloğu girintili olmalıdır.
if 5 < 10:
    print("5, 10'dan küçüktür.")

# Birden fazla satır açıklama yazmak için genellikle # tercih edilir.
# Ama """ üçlü tırnak """ da kullanılabilir. Bu aslında teknik olarak bir string literal’dır,
# ancak bir değişkene atanmadığı için ekranda gözükmez. Genelde uzun notlar veya docstring için kullanılır.
"""
Bu birden fazla satırlık bir açıklama örneğidir.
Python'da bu şekilde de not ekleyebilirsiniz.
"""

"""
DEĞİŞKENLER
"""

# Python programlama dilinde bir değişken, verileri saklamak için kullanılan bir isimdir.
# Değişkenler, programın çalışması sırasında farklı değerler alabilir.

x = 5

# Değişkenin tipini görmek için "type()" fonksiyonu kullanılır.
# Ancak sadece type(x) yazmak ekrana çıktı vermez. print ile yazdırmak gerekir.
print(type(x))

"""
Bu sayede program çalıştırıldığında, print komutu sayesinde x değişkeninin tipi
ekrana yazdırılacaktır.
type fonksiyonunu daha estetik şu şekilde kullanabiliriz:
"""
print("Değişkenin tipi:", type(x))

# Eğer değişken tipini kendimiz tanımlamak istersek:
x = int(3)
y = str("Naber?")   # string
y = str(3)          # string '3'
z = float(3.5)      # float

# Ancak Python dili çoğu durumda tipini otomatik algılar.
# Bu nedenle elle tip belirtmek çoğu zaman gerekli değildir.

"""
Python dili, kodu yukarıdan aşağıya sırayla okur.
Diyelim ki 3. satırda x değişkeni tanımladınız ve print ile çıktı aldınız.
6. satırda yeniden bir x değişkeni tanımladınız ve tekrar print ile yazdırdınız.
Python en son tanımlanan değeri dikkate alır.
Bu nedenle x değişkeni önceki değerini kaybeder ve yeni değerle overwrite edilir.
"""

x = 3
print(x)
x = 5
print(x)

# Ayrıca, Python dilinde değişken atanırken büyük harf ve küçük harf duyarlılığı vardır.
# Örneğin, "X" ve "x" farklı değişkenlerdir.

x = "Wex"
X = "Ty"

print(x)  # Bu print fonksiyonunda küçük "x" yazdırılacaktır.
print(X)  # Bu print fonksiyonunda büyük "X" yazdırılacaktır.

# Bu durumda, overwrite işlemi gerçekleşmez çünkü "x" ve "X" farklı değişkenlerdir.

"""
Değişkenlerin kısa isimleri ya da daha açıklayıcı uzun isimleri olabilir.
Bir değişken adı bir harf veya alt çizgi karakteri ile başlamalıdır. Sayı ile başlayamaz.
Sadece alfanümerik karakterler ve alt çizgi karakteri içerebilir.
Önceden de söylediğimiz gibi, değişken adları büyük küçük harf duyarlıdır.
Bir değişkenin adı, Python anahtar kelimelerinden biri olamaz.
Genelde açıklayıcı değişken isimleri tercih edilir.
Bu sayede, kodu sizden farklı biri de okuyabilir.
"""

"""
Birden fazla kelimelerden oluşan değişken adlarını okumak zor olabilir.
Bunları daha okunaklı hale getirmek için birkaç teknik kullanılabilir:

- Camel Case: Değişken adı; ilk kelime küçük, diğer kelimelerin ilk harfleri büyük olacak şekilde yazılır. Örneğin: "myVariableName"
- Pascal Case: Değişken adı; kelimelerin ilk harfleri büyük olacak şekilde yazılır. Örneğin: "MyVariableName"
- Snake Case: Kelimeler alt çizgi ile ayrılır. Örneğin: "my_variable_name"
"""

# Birden fazla değişken atayabilirsiniz.
x, y, z = 1, 2, 3
print(x, y, z)
print(x)
print(y)
print(z)

# Ya da birden fazla değişkene tek bir değer atayabilirsiniz.
x = y = z = 0
print(x, y, z)

# Ya da birden fazla değer içeren bir liste oluşturabilirsiniz.
fruits = ["apple", "banana", "cherry"]
# Daha sonrasında ise birden fazla değişkene bu listeyi atayabilirsiniz.
x, y, z = fruits
print(x, y, z)
print(x)
print(y)
print(z)

"""
# Ancak, listeye 2 eleman koyup 3 tane değişken tanımlarsanız, hata alırsınız.
# devices = ["phone", "tablet"]
# x, y, z = devices
# print(x, y, z)  # Bu satır hata verecektir çünkü devices listesi 2 elemanlıdır. Expected 3, got 2 hatası alırsınız.

# Aynı şekilde 2 değişkene 3 tane liste elemanı tanımlayamazsınız. Bu sefer expected 2, got 3 hatası alırsınız.
# students = ["Ali", "Ayşe", "Fatma"]
# x, y = students
# print(x, y)

# Liste dediğimiz şeye "array" denir.
# Listeler bir değere eşitlenir ve [] ile tanımlanır.
"""

# Kullanmayacağınız durumlarda "_" kullanabilirsiniz.
brands = ["Apple", "Samsung", "Sony"]
x, y, _ = brands
print(x, y)
# Bu durumda print fonksiyonunda "z" değerini görüntülemeye çalışırsanız hata alırsınız.
# "_" değişkeni, herhangi bir değer eşitlenmez.
# Oluşturduğumuz her değişken RAM'de bir yer kaplar.
# Bu nedenle, kullanılmayan değişkenler bellek israfına neden olabilir.
# StackOverflow hatalarına yol açabilir. Bunun için genelde kullanmadığımız değişkenleri "_" ile adlandırırız.
# Kısaca, alt çizgi karakterini çöp kutusu olarak düşünebilirsiniz.

# Ayrıca, kodda belirli bir satırda hata alındığında kodun geri kalan kısmı çalışmayabilir.

# Python'daki eşittir işareti matematikteki eşittir ile aynı değildir.
# Python'da bu işareti sağdaki değeri soldaki değere atamak için kullanırız.
# Atama operatörü olarak adlandırılır.
# 5 = x diyemeyiz çünkü soldaki değer bir değişken olmalıdır.
# Değişkenlerin sayı olamayacağını ve sayı ile başlayamayacağını öğrenmiştik.
# Matematiksel eşittir işaretini == ile gösteririz.

# Print fonksiyonun içerisine ardışık olarak birden fazla değişken yazdırabilirsiniz.
x = "2025"
y = "Yılından"
z = "Merhaba"
print(x, y, z)
# Python bu tarz print işlemlerinde değişkenlerinin değerlerinin arasına standart olarak bir boşluk koyar.
# İstersek bu ayırma yöntemini sep ile değiştirebiliriz.
print(x, y, z, sep="-")
# Bu durumda print fonksiyonunda değişkenlerinin değerleri arasına "-" karakteri yerleştirilecektir.
# Çıktı: "2025-Yılından-Merhaba" şeklinde olacaktır.

# Print fonksiyonuyla toplama, çıkarma, çarpma, bölme gibi işlemleri yapabilirsiniz.
x = 8
y = 2
print(x + y)  # Toplama işlemi
print(x - y)  # Çıkarma işlemi
print(x * y)  # Çarpma işlemi
print(x / y)  # Bölme işlemi

# Bu durum, yalnızca sayılarda değil stringlerde de geçerlidir.
x = "Hello"
y = "World"
print(x + y)        # Stringleri birleştirme işlemi
print(x + " " + y)  # Stringleri aralarına boşluk koyarak birleştirme işlemi.
# Bu şekilde asterisk (*) ile stringleri tekrar edebilirsiniz.
print(x * 3, y * 3)
# print(x / y)      # Bu satır hata verecektir. Çünkü stringleri birbirlerine bölemezsiniz.

# Ancak bir sayı ile stringi birleştiremezsiniz.
# Örneğin:
# print(x + " yılından") Bu satır hata verecektir.

# print fonksiyonuyla 2 tane değişkeni birleştireceğiniz zaman, değişkenlerin ikisinin de aynı türde olması gerekir.
x = 2
y = "3"
# print(x + y)  # Bu satır hata verecektir. Biri integer biri string olduğu için birleştirilemez.
# Toplamak yerine, yan yana görüntüleyebiliriz.
print(x, y)

# Stringleri çarparak tekrar edebilirsiniz.
x = "Wexty"
print(x * 5)

# Integer'leri stringler gibi çarparak tekrar edemezsiniz, Python bunun yerine integer değerini matematiksel olarak çarpar.
x = 5
# Bu çıktı sonucunda 5'in 3 ile çarpımı olan 15 değeri elde edilir.
print(x * 3)


# Programlamada, veri türleri önemlidir.
# Değişkenlerin türleri, hangi işlemlerin yapılabileceğini belirler.
# Değişkenler, farklı türde veriler saklayabilir ve bu veriler üzerinde çeşitli işlemler gerçekleştirebilir.

"""
 # Veri Tipleri:

 Text: str,
 Numeric: int, float, complex
 Sequence Types: list, tuple, range
 Mapping Types: dict
 Set Types: set, frozenset
 Boolean Type: bool (True, False)
 Binary Types: bytes, bytearray, memoryview
 None Type: NoneType

 # Veri türlerine örnekler:
 x = "Hello, World!" - str (string)
 x = 20 - int (integer)
 x = 20.5 - float (floating point)
 x = 1 + 2j - complex (complex number)
 x = [1, 2, 3] - list (list)
 x = (1, 2, 3) - tuple (tuple)
 x = range(1, 4) - range (range)
 x = {"name": "Ali", "age": 25} - dict (dictionary)
 x = {"1", "2", "3"} - set (set)
 x = frozenset({"1", "2", "3"}) - frozenset (frozenset)
 x = True - bool (boolean)
 x = False - bool (boolean)
 x = b"Hello" - bytes (bytes)
 x = bytearray(5) - bytearray (bytearray)
 x = memoryview(bytes(5)) - memoryview (memoryview)
 x = None - NoneType (NoneType)
"""

# # SAYISAL VERİ TÜRLERİ
# Python dilinde 3 tane sayısal veri türü bulunmaktadır:
# 1. int (tam sayılar - sınırsız uzunlukta, pozitif negatif olabilir ancak ondalık olamaz)
# 2. float (ondalık sayılar - bir veya daha fazla ondalık sayı içeren pozitif ya da negatif değişkenlerdir)
# 3. complex (karmaşık sayılar - matematikteki "i" harfinin aksine Python'da j harfi ile gösterilir: 4j gerçek ve imajiner kısımlardan oluşur: 1 + 2j)

x = 1  # int
y = 2.5  # float
z = 4j  # complex

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

print(" ")

# TİP DÖNÜŞÜMÜ

x = 1  # int
y = 2.5  # float
z = 4j  # complex without real number
Z = 5 + 4j  # complex with real number

print(x)
print(y)
print(z)

print(" ")

# convert from int to float
a = float(x)

# convert from float to int
b = int(y)

# convert from int to complex
c = complex(x)

# convert from float to complex
d = complex(y)

# convert from complex to int
# - Burada "z" değişkeninin complex verisinde gerçek sayı olmadığı için 0 çıktısı alınır.
e = int(z.real)

# convert from complex to int with real number
# - Burada "Z" değişkeninin complex verisinde gerçek 5 sayısı bulunduğu için 5 çıktısı alınır.
f = int(Z.real)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(" ")

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Bazı veriler dönüştürülemez. Örneğin:
x = "1"
a = float(x)
print(a)
# Bu veri dönüştürülebilir çünkü string değerindeki veri sayısal bir ifade. Ancak içerisine yazı karakteri eklendiğinde dönüşüm sağlanamaz ve kod hata döndürür.
# x = "naber"
# a = float(x)
# print(a)
# Bu durumda, "could not convert string to float" hatası alırız.
# Bu nedenler verileri dönüştürürken birbirine dönüşebilen veriler kullanmaya dikkat etmeliyiz.
# Sayı değeri olduğu sürece stringleri diğer sayı tiplerine dönüştürebiliriz.

# STRINGS
# String ifadeleri kullanırken texti çift ya da tek tırnak içine almalıyız.
print("Hello, World!")  # çift tırnak
print('Hello, World!')  # tek tırnak

# Stringlerin içerisinde alıntı yapacağımız zaman:
print("Benim adım 'Ali'.")  # çift tırnak içinde tek tırnak
print('Benim adım "Ali".')  # tek tırnak içinde çift tırnak
# Şeklinde bir kullanım yapabiliriz.

# String değerini bir değişkene atayıp print fonksiyonu ile yazdırabiliriz.
x = "Hello, World!"
print(x)

# 3 tırnaklı, bu dosyanın bazı yerlerinde yorum satırı olarak kullandığımız şeyleri bir değişkene atayıp birden fazla satır içeren string oluşturabiliriz.
x = """Bu birden fazla
satır içeren bir
string örneğidir."""
# Bu stringi print ile yazdırabiliriz.
print(x)

# Bu uygulamayı yalnızca çift tırnak arasında kullanamayız.
# y = "Bu birden fazla"
# satır içeren bir
# string örneğinin yanlış kullanımıdır."

print(" ")

# İlla böyle kullanacaksak kaçış karakteri kullanmalıyız.
y = "Bu birden fazla\nsatır içeren bir\nstring örneğidir."
print(y)

print(" ")

# Stringler birden fazla değer içeren listeler gibidir. İçine yazılan cümlenin ya da kelimenin her karakteri ayrı ayrı değerlendirilebilir.
a = "Wexty"
print(a)  # Wexty
print(a[0])  # W
print(a[1])  # e
print(a[2])  # x
print(a[3])  # t
print(a[4])  # y

# İçinde birden fazla değer tutan her öğeden birinci değer "0" indeksine karşılık gelir.
# Sonuncu karakteri "-1" indekine de karşılık gelir.
print(a[4])  # y
print(a[-1])  # y
# Bu durumu, birinci değerden "0" indeksinden geriye sayma olarak da görebiliriz. Bu nedenle "-3" indeksi "x" harfine karşılık gelir.
print(a[-3])  # x

for x in "banana":
    print(x)
# Buradaki for döngüsü bize şunu söylüyor:
# "banana" kelimesinin her bir karakterini ayrı ayrı değerlendir.
# '"banana" kelimesinde 6 karakter var, bu stringin içindeki her bir karakteri sırayla al' demek gibi bir şey.
# İlk değerden son değere kadar döngü devam eder. Son karakter de çıktı alındığında döngü sona erer.
# Döngümüzdeki "banana" ifadesini bir değişkene de atayabiliriz.
a = "banana"
for x in a:
    print(x)

# String uzunluğunu görmek için "len" fonksiyonunu kullanabiliriz.
print(len(a))  # 6

# Bir değişkenin içerisindeki string ifadesinde bir değerin var olup olmadığını kontrol etmek için "in" anahtar kelimesini kullanabiliriz.
a = "Merhaba, nasılsın?"
print("Merhaba" in a)  # True

# Bunu "not in" olarak da kullanabiliriz.
print("Merhaba" not in a)  # False
# İçinde yok mu? gibi bir anlama gelir.

# Bunu bir koşulla da kullanabiliz.
if "Merhaba" in a:
    print("Evet, stringin içerisinde 'Merhaba' mevcut.")
# Aynı durum "not in" için de geçerli.
if "Merhaba" not in a:
    print("Evet, stringin içerisinde 'Merhaba' mevcut değil.")
# Stringde "Merhaba" mevcut olduğu için bu yapı boş dönecektir. Aksini kastettiğimiz zaman "else" kullanabiliriz.
else:
    print("Hayır, stringin içerisinde 'Merhaba' mevcut.")
# Else yapısı da bu şekildedir.

# Input ile kullanıcıdan giriş alabiliriz.
