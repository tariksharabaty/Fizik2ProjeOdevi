# Veri Merkezlerinde Fiziksel Limitler ve Mühendislik Optimizasyonu

İstanbul Kent Üniversitesi Fizik-2 proje ödevi kapsamında, modern veri merkezlerinde karşılaşılan fiziksel darboğazları (Joule ısınması, elektromanyetik girişim, fiber optik sinyal zayıflaması) analiz etmek amacıyla Python programlama dili kullanılarak geliştirilmiş bir simülasyon ve modelleme çalışmasıdır.

**Öğrenci Bilgileri:**

* **AD SOYAD:** Tarek Sharabaty
* **ÖĞRENCİ NO:** 2507020015
* **BÖLÜM:** Bilgisayar Mühendisliği
* **DERS:** Fizik-2

**Programın Çalışma Mantığı ve Modellenen Fiziksel Kuramlar:**

1) **Joule Isınması ve Enerji Verimliliği:** **P = I²R** formülü ile yüksek akım taşıyan sunucu hatlarındaki termal güç kayıpları hesaplanır. Ayrıca toplam enerji tüketimi üzerinden veri merkezi verimlilik analizi (PUE) modellenir.
2) **Elektromanyetik Girişim (EMI):** Ampère Yasası (**B = μ₀I / 2πr**) baz alınarak, iletkenlerden geçen akımın çevrede oluşturduğu manyetik alanın mesafeye bağlı değişimi mikroTesla (μT) cinsinden hesaplanır.
3) **Fiber Optik ve Kritik Açı:** Işık sinyallerinin kablo dışına sızmaması için gereken tam iç yansıma prensibi, Snell Yasası kullanılarak analiz edilir ve kritik açı derece cinsinden hesaplanır.
4) **Sinyal Sönümlenmesi (Attenuation):** Fiber hatlarda mesafeye bağlı olarak yaşanan sinyal kayıpları, üstel bir fonksiyon olan **P(x) = P₀e^(-αx)** formülü ile modellenir.
5) **Veri Görselleştirme:** Elde edilen tüm sayısal veriler `matplotlib` kütüphanesi yardımıyla hesaplanarak, tek bir ekranda dört farklı grafik halinde görselleştirilir.

**Kullanılan Kütüphaneler:**
* `numpy`: Sayısal veri setleri ve matris hesaplamaları.
* `matplotlib.pyplot`: Fiziksel modellerin grafiksel dökümü.
* `math`: Trigonometrik ve üstel matematiksel dönüşümler.

**Programdan Ekran Görüntüleri**

**• Simülasyon Çıktısı (Matplotlib Grafik Paneli):**

<img width="1878" height="944" alt="Image" src="https://github.com/user-attachments/assets/ebc97b32-a779-4130-8d78-1affb2fa2e23" />

**• Örnek Konsol Çıktısı:**

<img width="1097" height="213" alt="Image" src="https://github.com/user-attachments/assets/e515b832-1b61-48bb-b317-82965af82e53" />
