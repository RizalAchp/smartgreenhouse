import time
from telemetrix import telemetrix
from .datasensor import TheCallback

class MainFunction:
    """MainFunction.

    type: `class` function sebagai fungsi utama dari jalannya program
    """

    SOIL = 0
    LDR = 1
    DHT = 11
    DHTTIPE = 11
    HCSRTRIG = 10
    HCSRECHO = 9
    REL1 = 2
    REL2 = 3
    REL3 = 4
    REL4 = 5
    LED = [13, 12, 8, 7, 6]

    def __init__(self, board:telemetrix.Telemetrix, call:TheCallback, ui, loops=int, delay=float, konds=list):
        """__init__.

        :param board:
        :type board: `telemetrix.Telemetrix` sebagai API board arduino
        :param call:
        :type call: `TheCallback` class dari bacaan sensor
        :param ui:
        :type ui: tupple items dari `dashing` sebagai visualisasi data
        :param loo1s:
        :type loops: jumlah banyaknya loop yang berjalan
        :param delay:
        :type delay: delay yang dibutuhkan setiap loop data
        :param konds:
        :type konds: list kondisi dari configparser file `config.ini` 
            pada parrent directory
        """
        self.board = board
        self.call = call
        self.ui = ui
        self.loop = loops
        self.delay = delay
        self.kond = konds

        self.board.set_pin_mode_analog_input(self.SOIL, differential=5,
                                             callback=self.call.soil_callback)

        self.board.set_pin_mode_analog_input(self.LDR, differential=5,
                                             callback=self.call.ldr_callback)

        self.board.set_pin_mode_sonar(self.HCSRTRIG, self.HCSRECHO,
                                      callback=self.call.hcsr_callback)

        self.board.set_pin_mode_dht(self.DHT, self.call.dht_callback,
                                    self.DHTTIPE)

        self.board.set_pin_mode_digital_output(self.REL1)
        self.board.set_pin_mode_digital_output(self.REL2)
        self.board.set_pin_mode_digital_output(self.REL3)
        self.board.set_pin_mode_digital_output(self.REL4)
        self.board.set_pin_mode_digital_output(self.LED[0])
        self.board.set_pin_mode_digital_output(self.LED[1])
        self.board.set_pin_mode_digital_output(self.LED[2])
        self.board.set_pin_mode_digital_output(self.LED[3])
        self.board.set_pin_mode_digital_output(self.LED[4])
        self.call.rel1_callback([0])
        self.call.rel2_callback([0])
        self.call.rel3_callback([0])
        self.call.rel4_callback([0])

        time.sleep(0.5)
        self.start(looping=self.loop, delay=self.delay, kond=self.kond)

    def start(self, looping, delay, kond) -> None:
        """start.

        :param looping:
        :param delay:
        :param kond:
        :rtype: None
        """
        self.a = self.call._a     # data callback dht
        self.b = self.call._b     # data callback SOIL
        self.c = self.call._c     # data callback hcsr
        self.d = self.call._d     # data callback LDR
        self.r1 = self.call._r1     # data callback relay1
        self.r2 = self.call._r2     # data callback relay2
        self.r3 = self.call._r3     # data callback relay3
        self.r4 = self.call._r4     # data calback relay4
        self._chart_log = self.ui.items[0].items[0]
        self._chart_humadity = self.ui.items[1].items[0]
        self._chart_suhu = self.ui.items[1].items[1]
        self._chart_relays = self.ui.items[0].items[1].items[-1].items

        for loop in range(looping):
            time.sleep(delay)

            # perkondisian relay pada ketentuan suhu
            # maupun kelembapan udara dari dht sensor

            if self.a[0] <= kond[3]:  # humadity
                self.board.digital_write(self.REL1, 1)
                self.call.rel1_callback([1])

            elif self.a[0] <= kond[4]:
                self.board.digital_write(self.REL1, 1)
                self.call.rel1_callback([1])

            else:
                # print(f'rel1 and rel2 mati')
                self.board.digital_write(self.REL1, 0)
                self.call.rel1_callback([0])


            if self.a[1] >= kond[2]:  # suhu
                # print(f'rel1 and rel2 hidup')
                self.board.digital_write(self.REL2, 1)
                self.call.rel2_callback([1])

            elif self.a[1] >= kond[1]:
                self.board.digital_write(self.REL2, 1)
                self.call.rel2_callback([1])

            else:
                self.board.digital_write(self.REL2, 0)
                self.call.rel2_callback([0])


            # perkondisian relay pada pada tingkat kebasahan tanah
            # dari bacaan `soilmoisturesensor`
            if self.b[0] >= kond[6]:
                # print(f'rel4 hidup')
                self.board.digital_write(self.REL4, 1)
                self.call.rel4_callback([1])

            elif self.b[0] >= kond[5]:
                # print(f'rel4 hidup')
                self.board.digital_write(self.REL4, 1)
                self.call.rel4_callback([1])

            else:
                # print(f'rel4 mati')
                self.board.digital_write(self.REL4, 0)
                self.call.rel4_callback([0])

            # perkondisian relay dan led sebagai
            # indikator ketinggian air pada tanki
            if self.c[0] >= kond[7]:
                self.board.digital_write(self.REL3, 1)
                self.board.digital_write(self.LED[0] , 1)
                self.board.digital_write(self.LED[1] , 0)
                self.board.digital_write(self.LED[2] , 0)
                self.board.digital_write(self.LED[3] , 0)
                self.board.digital_write(self.LED[4] , 0)
                self.call.rel3_callback([1])

            elif self.c[0] >= kond[8]:
                self.board.digital_write(self.REL3, 1)
                self.board.digital_write(self.LED[0] , 1)
                self.board.digital_write(self.LED[1] , 1)
                self.board.digital_write(self.LED[2] , 0)
                self.board.digital_write(self.LED[3] , 0)
                self.board.digital_write(self.LED[4] , 0)
                self.call.rel3_callback([1])

            elif self.c[0] >= kond[9]:
                self.board.digital_write(self.REL3, 1)
                self.board.digital_write(self.LED[0] , 1)
                self.board.digital_write(self.LED[1] , 1)
                self.board.digital_write(self.LED[2] , 1)
                self.board.digital_write(self.LED[3] , 0)
                self.board.digital_write(self.LED[4] , 0)
                self.call.rel3_callback([1])

            elif self.c[0] >= kond[10]:
                self.board.digital_write(self.REL3, 1)
                self.board.digital_write(self.LED[0] , 1)
                self.board.digital_write(self.LED[1] , 1)
                self.board.digital_write(self.LED[2] , 1)
                self.board.digital_write(self.LED[3] , 1)
                self.board.digital_write(self.LED[4] , 0)
                self.call.rel3_callback([1])

            else:
                self.board.digital_write(self.REL3, 0)
                self.board.digital_write(self.LED[0] , 1)
                self.board.digital_write(self.LED[1] , 1)
                self.board.digital_write(self.LED[2] , 1)
                self.board.digital_write(self.LED[3] , 1)
                self.board.digital_write(self.LED[4] , 1)
                self.call.rel3_callback([0])

            # UI DASHBOARD TERMINAL ELEMENT DAN DATA
            self.ui.items[1].items[2].items[0].value = float(self.b[0]/10)
            self.ui.items[1].items[2].items[1].value = float(self.c[0]/2)
            self.ui.items[0].items[2].value = float(self.d[0]/10)

            self._chart_relays[0].value = self.r1[0]
            self._chart_relays[1].value = self.r2[0]
            self._chart_relays[2].value = self.r3[0]
            self._chart_relays[3].value = self.r4[0]

            self._chart_log.append(f'humidity = {str(self.a[0])} %')
            self._chart_log.append(f'Suhu= {str(self.a[1])} \u2103')
            self._chart_log.append(f'SOILsensor = {str(self.b[0])}')
            self._chart_log.append(f'LDR = {str(self.d[0]/10)}')
            self._chart_log.append(f'hcsr = {str(self.c)} cm')

            self._chart_humadity.append(self.a[0])
            self._chart_suhu.append(self.a[1])
            self.ui.display()

            loop += 1
