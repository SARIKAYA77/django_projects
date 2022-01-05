Bu repo django ile geliştirme asamalarını not ederek örnek uygulamalar barındırmak için yapılmıstır

# git notlar
#git reset --hard
#git log
#git branch
#git rm --cached dosyadi.txt
#gitignore en basta oluşturmayı unutursan "git rm -rf --cached ."
yazıp tekrar commit yapman gerekir


# django  notlar

->projeyi startproject ile oluşturduktan sonra,runserver ile ayağa kaldırırsan; auth, admin session gibi migrationsların
uygulanmadıgını django söyler,bunlar bazı applerdir,django tarafından belli bir taban yapıdır aslında.

->sonrasında migrate komutu ile tüm bu applerin db tablolarını oluşturursun.Her sey OK ise artık sorun yoktur,superuser oluşturup django yu runserver
ile ayaga kaldırabilirsin

->appler uygulamanın belli parçalarıdır iletişim hakkında gibi sayfaları app oluşturursun ornek olarak

-->startapp ile uygulamanı oluşturursun,git e göndermek istemediğin dosyaları (örneğin pycache) belirtmen gerekir,

--> models veritabanı işlemleri, views urllerin üreteceği cevabın bulanacagı kısımlar, bunlar app oluşunca otomatik gelir, admin.py gibi..


# models yapısı

--> models demek veritabanı demek, App içerisindeki models.py silindi onun yerine models klasörunde db tabloları oluşturuldu.
-->INSTALLED_APPS e app eklenerek  uygulamayı djangonun algılaması saglanır.
--> category,Author,article bizim blog sayfamızda bulunan tablolarımız
