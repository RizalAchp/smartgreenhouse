# SMART GREENHOUSE WITH ARDUINO AND TELEMETRIX

Automisasi pada greenhouse berupa pengukuran dan pengontrol suhu, kelembapan udara, kelembapan tanah, sirkulasi udara, serta besar cahaya pada environment yang di tentukan

_oleh:_  
**[Rizal Achmad Pahlevi `E32201406`](https://github.com/RizalAchp)**

## alat dan bahan

1. **Arduino Uno Ref3 ATMEGA328** _( module arduino )_
2. **dht11 sensor** _( sensor humadity dan suhu ruangan )_
3. **4 relays** _( coil 12 v )_
4. **kipas 12v/5v** _( kipas DC kecil )_
5. **pump 12v** _( water pump )_
6. **hcsr04** _( ultrasonic sensor )_
7. **soil moisture sensor** _( sensor kelembapan tanah )_
8. **Light Depentent Resistor** _( ldr / sensor cahaya )_
9. **supply power/regulator** _( 12v and 5v )_
10. **acrilic** _( tempat dudukan semua module )_
    <!-- 11. **12c LCD 16x2** _( lcd sebagai indikator tambahan )_ -->
    <!-- 12. **LED array** _( led sebagai indikator tambahan )_ -->

## sofware yang digunakan

1. **vim** _( text editor )_
2. **python3** _( bahasa pemrograman yang di pakai )_

   - **Telemetrix** _( module python3 sebagai intrepeter ke arduino
     sama seperti pyfirmata namun fitur lebih banyk )_
   - **dashing** _( module python untuk menampilkan / menvisualisasikan data dalam bentuk gauge
     maupun numerik didalam terminal emulator )_

## proses yang dilakukan

1. membuat wadah semua module kedalam acrilic untuk mempermudah dan meminimalisir tempat maupun kerapian dalam module

2. menggunakan regulator sebagai pengatur daya agar distribusi daya stabil

3. module sensor dapat di tambah maupun di ubah dengan module sensor lain selama pin yang dibutuhkan sama

4. memrogram full dengn python
5. menvisualisasikan data kedalam TUI ( Terminal User Interface )\
   ~~data value yang didapatkan di simpan didalam database ( mysql )~~\
   <!--TODOO --> ~~memvisualisasikan kedalam web server maupun mobile app~~ ( future )

## kelebihan

1. minimalis
2. full di program dengan python yang dapat mumudahkan mendeploy dan menjalankan program pada raspberry pi
3. karena data di simpan didalam daabase, memudahkan kita untuk memvisualisasikan kedalam pengaplikasiann kedepannya

## Definisi Pin yang digunakan pada arduino

- PIN ANALOG =

  1. A0 = sensor soil moisture
  2. A1 = sensor ldr\
     ~~A4 = 12c LCD (sda)~~\
     ~~A5 = 12c LCD (scl)~~

- PIN DIGITAL =

  1. sensor dht = 11
  2. Trig Pin HCSR = 9
  3. Echo Pin HCSR = 10\
  4. relay 1 = 2
  5. relay 2 = 3
  6. relay 3 = 4
  7. relay 4 = 5\
     ~~LED = 13,12,10,9,8,7,6~~
