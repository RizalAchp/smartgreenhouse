<h1 id="JUDUL">
    SMART GREENHOUSE WITH ARDUINO AND TELEMETRIX
</h1>
<h4>
    Automisasi pada greenhouse berupa pengukuran dan pengontrol suhu, kelembapan udara, kelembapan tanah, sirkulasi udara, serta besar cahaya pada environment yang di tentukan
</h4>

_oleh:_  
**[TIM TREESAKTI : TKK POLIJE](https://github.com/RizalAchp)**

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

<h2 id="cara-menjalankan">
    cara menjalankan
</h2>

1. download repo ini secara manual atau clone menggunakan git

   ```bash
   git clone --recursive https://github.com/RizalAchp/smartgreenhouse.git
   cd ./smartgreenhouse
   ```

2. install dependensi

   ```bash
   pip install -r ./requirement.txt
   ```

3. buka arduino IDE, dan download Library `Telemetrix4Arduino` pada library manager dan upload Example dari library tersebut pada `Arduino Uno / Nano` minimal yang menggunakan `ATMEGA328` sebagai microcontrollernya.

4. setelah itu kembali pada directory `smartgreenhouse`, dan jalankan program dengan cara:

   ```bash
   python ./main.py
   ```

   atau jika anda berada pada linux:

   ```bash
   python3 ./main.py
   ```

5. Selesai

**untuk definisi pin yang digunakan bisa dihilhat di [DI SINI](#DEFINISI-PIN)**

<h2 id="software-yang-digunakan">
    sofware yang digunakan
</h2>

1. **vim** _( text editor )_
2. **python3** _( bahasa pemrograman yang di pakai )_

   - **Telemetrix** _( module python3 sebagai intrepeter ke arduino
     sama seperti pyfirmata namun fitur lebih banyk )_
   - **dashing** _( module python untuk menampilkan / menvisualisasikan data dalam bentuk gauge
     maupun numerik didalam terminal emulator )_

<h2 id="proses yang dilakukan">
   proses yang dilakukan
</h2>

3. membuat wadah semua module kedalam acrilic untuk mempermudah dan meminimalisir tempat maupun kerapian dalam module

4. menggunakan regulator sebagai pengatur daya agar distribusi daya stabil

5. module sensor dapat di tambah maupun di ubah dengan module sensor lain selama pin yang dibutuhkan sama

6. memrogram full dengn python
7. menvisualisasikan data kedalam TUI ( Terminal User Interface )\
   ~~data value yang didapatkan di simpan didalam database ( mysql )~~\
   <!--TODOO --> ~~memvisualisasikan kedalam web server maupun mobile app~~ ( future )

<h2 id="kelebihan">
    Kelebihan
</h2>

1. minimalis
2. full di program dengan python yang dapat mumudahkan mendeploy dan menjalankan program pada raspberry pi
3. karena data di simpan didalam daabase, memudahkan kita untuk memvisualisasikan kedalam pengaplikasiann kedepannya

<h2 id="DEFINISI-PIN">
    Definisi Pin yang digunakan pada arduino
</h2>

- **PIN ANALOG =**

  | ALAT                 |   PIN    |
  | -------------------- | :------: |
  | Sensor Soil Moisture | Analog 0 |
  | Sensor LDR           | Analog 1 |
  | i2c LCD (SDA)        | Analog 4 |
  | i2c LCD (SCL)        | Analog 5 |

- **PIN DIGITAL =**

  | ALAT             |           PIN            |
  | ---------------- | :----------------------: |
  | Sensor DHT11     |        Digital 11        |
  | Trig pin HCSR-04 |        Digital 9         |
  | Echo Pin HCSR-04 |        Digital 10        |
  | Relay            |        Digital 2         |
  | Relay            |        Digital 3         |
  | Relay            |        Digital 4         |
  | Relay            |        Digital 5         |
  | LED              | Digital 13,12,10,9,8,7,6 |
