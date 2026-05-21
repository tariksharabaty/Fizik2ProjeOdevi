# Gerekli kütüphanelerin içeri aktarılması
# np: Sayısal hesaplamalar ve diziler için, plt: Grafik çizimleri için, math: Matematiksel dönüşümler için.
import numpy as np
import matplotlib.pyplot as plt
import math

class TeknikRaporSimulasyonu:
    def __init__(self):
        # Boşluğun manyetik geçirgenliği sabiti (mu_0), birim: T*m/A
        # Ampere yasası hesaplamalarında kullanılmaktadır.
        self.mu_0 = 4 * np.pi * 10**-7  

    def joule_isinmasi(self, I, R):
        """
        Raporun 2.1 numaralı bölümünde belirtilen Joule Isınması hesaplanmaktadır.
        I: Akım (Amper), R: Direnç (Ohm)
        Dönüş: Isıya dönüşen kayıp güç (Watt)
        """
        P = (I**2) * R
        return P

    def pue_hesapla(self, toplam_enerji, bt_enerji):
        """
        Veri merkezinin Power Usage Effectiveness (PUE) değerini hesaplar.
        Sonuç 1.0 değerine yaklaştıkça sistemin daha verimli olduğu anlaşılır.
        """
        return toplam_enerji / bt_enerji

    def ampere_yasasi(self, I, r):
        """
        Kablodan geçen akımın, belirli bir mesafede oluşturduğu manyetik alanı hesaplar.
        Formül: B = (mu_0 * I) / (2 * pi * r)
        Sıfıra bölme hatası almamak adına 'r' mesafesine küçük bir tolerans (1e-10) eklenmiştir.
        """
        r = np.where(r == 0, 1e-10, r)
        B = (self.mu_0 * I) / (2 * np.pi * r)
        return B

    def snell_yasasi_kritik_aci(self, n1, n2):
        """
        Fiber optik iletimde tam iç yansımanın gerçekleşmesi için gereken kritik açıyı hesaplar.
        n1: Çekirdek (core) kırıcılık indisi, n2: Kılıf (cladding) kırıcılık indisi.
        """
        if n2 > n1:
            return None # Fiziksel olarak kritik açı oluşmaz.
        
        # Radyan cinsinden hesaplanan sonuç derece birimine dönüştürülerek döndürülür.
        theta_c_radyan = math.asin(n2 / n1)
        theta_c_derece = math.degrees(theta_c_radyan)
        return theta_c_derece

    def fiber_sonumlenme(self, P0, alpha, x):
        """
        Işık sinyalinin fiber optik hat boyunca ilerledikçe yaşadığı zayıflamayı (attenuation) hesaplar.
        P0: Başlangıç gücü, alpha: Zayıflama katsayısı, x: Mesafe (km)
        """
        P_x = P0 * np.exp(-alpha * x)
        return P_x

def simulasyonu_calistir():
    # Simülasyon sınıfından bir nesne üretilir.
    sim = TeknikRaporSimulasyonu()

    # === 1. KISIM: TEORİK ÖRNEKLERİN HESAPLANMASI ===
    print("--- TEKNİK RAPOR HESAPLAMALARI ---")

    ornek_I = 20.0
    ornek_R = 0.4
    ornek_P = sim.joule_isinmasi(ornek_I, ornek_R)
    print(f"Joule Isınması (I={ornek_I}A, R={ornek_R} ohm): {ornek_P} Watt ısı açığa çıkar.")

    ornek_n1 = 1.5
    ornek_n2 = 1.3
    ornek_aci = sim.snell_yasasi_kritik_aci(ornek_n1, ornek_n2)
    print(f"Snell Yasası (n1={ornek_n1}, n2={ornek_n2}): Kritik Açı = {ornek_aci:.2f} derece.")
    print("-" * 34)

    # === 2. KISIM: GRAFİK VERİ SETLERİNİN OLUŞTURULMASI ===
    akimlar = np.linspace(0, 50, 100)
    direnc = 0.4
    guc_kayiplari = sim.joule_isinmasi(akimlar, direnc)

    mesafeler_m = np.linspace(0.01, 0.5, 100)
    kablo_akimi = 20.0
    # Okunabilirliği artırmak için Tesla değeri MikroTesla (uT) birimine çevrilmiştir.
    manyetik_alan_uT = sim.ampere_yasasi(kablo_akimi, mesafeler_m) * 1e6

    bt_enerjisi = 1000
    toplam_enerjiler = np.linspace(1000, 2500, 100)
    pue_degerleri = sim.pue_hesapla(toplam_enerjiler, bt_enerjisi)

    mesafe_km = np.linspace(0, 100, 100)
    baslangic_gucu = 1.0
    alfa = 0.05
    sinyal_gucleri = sim.fiber_sonumlenme(baslangic_gucu, alfa, mesafe_km)

    # === 3. KISIM: MATPLOTLIB İLE GÖRSELLEŞTİRME ===
    plt.figure(figsize=(14, 10))
    plt.suptitle("Veri Merkezlerinde Fiziksel Limitler (Teknik Rapor Analizi)", fontsize=16, fontweight='bold')

    plt.subplot(2, 2, 1)
    plt.plot(akimlar, guc_kayiplari, color='red', linewidth=2)
    plt.title("Joule Isınması ($P = I^2 R$)")
    plt.xlabel("Akım (Amper)")
    plt.ylabel("Güç Kaybı / Isı (Watt)")
    plt.plot(20, 160, 'ko')
    plt.text(22, 140, 'Rapor Örneği\n(20A, 160W)', fontsize=9)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.subplot(2, 2, 2)
    plt.plot(mesafeler_m * 100, manyetik_alan_uT, color='purple', linewidth=2)
    plt.title("Elektromanyetik Girişim ($B = \mu_0 I / 2\pi r$)")
    plt.xlabel("Kablodan Uzaklık (cm)")
    plt.ylabel("Manyetik Alan ($\mu$T)")
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.subplot(2, 2, 3)
    plt.plot(toplam_enerjiler, pue_degerleri, color='green', linewidth=2)
    plt.axhline(y=1, color='gray', linestyle='--')
    plt.title("PUE Enerji Verimliliği Analizi")
    plt.xlabel("Toplam Tüketilen Enerji (Birim)")
    plt.ylabel("PUE Değeri (İdeal = 1.0)")
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.subplot(2, 2, 4)
    plt.plot(mesafe_km, sinyal_gucleri, color='blue', linewidth=2)
    plt.title("Fiber Optik Sinyal Sönümlenmesi ($P(x) = P_0 e^{-\\alpha x}$)")
    plt.xlabel("Mesafe (km)")
    plt.ylabel("Kalan Sinyal Gücü")
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    simulasyonu_calistir()
