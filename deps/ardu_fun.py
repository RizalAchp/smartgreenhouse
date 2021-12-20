from telemetrix import telemetrix
from deps.thecallback import TheCallback
# from deps.query_sql import *
from deps.termdashboard import *
import time

# from deps.liquidcrystal import *

def mainFunctions(board:telemetrix.Telemetrix ,calls:TheCallback,loop:int=10000)->None:
    """mainFunctions

    fungsi =    memulai semua proses pada arduino berupa loop for
                dan memanggil banyak `function` maupun `library` local
                 dengan parameter masing masing.

    :param board: `telemetrix` board ( arduino board )
    :param calls: `callback` function/class untuk data sensor
    """
    call_dht = calls.dht_callback
    call_soil = calls.soil_callback
    call_hcsr = calls.hcsr_callback
    call_ldr = calls.ldr_callback
    # call_pot1 = calls.pot1_callback
    # call_pot2 = calls.pot2_callback
    call_rel1 = calls.rel1_callback
    call_rel2 = calls.rel2_callback
    call_rel3 = calls.rel3_callback
    call_rel4 = calls.rel4_callback
    loop = 10000

    # LCD = LiquidCrystal_I2C(0x3F, 0, 1, board)
    board.set_pin_mode_analog_input(soil,differential=5,
                                    callback=call_soil)
    board.set_pin_mode_analog_input(ldr,differential=5,
                                    callback=call_ldr)
    board.set_pin_mode_sonar(hcsr_trig,hcsr_echo,
                             callback=call_hcsr)
    board.set_pin_mode_dht(dht,call_dht,dht_tipe)
    board.set_pin_mode_digital_output(rel1)
    board.set_pin_mode_digital_output(rel2)
    board.set_pin_mode_digital_output(rel3)
    board.set_pin_mode_digital_output(rel4)
    call_rel1([0])
    call_rel2([0])
    call_rel3([0])
    call_rel4([0])

    time.sleep(1.0)
    a = calls._a     # data callback dht
    b = calls._b     # data callback soil
    c = calls._c     # data callback hcsr
    d = calls._d     # data callback ldr
    r1 = calls._r1     # data callback relay1
    r2 = calls._r2     # data callback relay2
    r3 = calls._r3     # data callback relay3
    r4 = calls._r4     # data callback relay4

    _chart_soil = b[0]/10
    _chart_hcsrs = c[0]/2
    _chart_ldr = d[0]/10
# access a tile by index
    _chart_log = ui.items[0].items[0]
    _chart_humadity = ui.items[1].items[0]
    _chart_suhu = ui.items[1].items[1]
    _chart_relays = ui.items[0].items[1].items[-1].items
    # LCD.clear()
    # LCD.enable_backlight()
    # loop fungsinya 
    for loops in range(loop):
    # while True:
        time.sleep(5.0)
        # try:

        """
        perkondisian relay pada ketentuan suhu
        maupun kelembapan udara dari dht sensor
        """
        if a[0] < 80.0: # HUMADITY
            board.digital_write(rel1,1)
            call_rel1([1])
            if a[1] >= 25.0: # SUHU
            # print(f'rel1 and rel2 hidup')
                board.digital_write(rel2,1)
                call_rel2([1])
            else:
                board.digital_write(rel2,0)
                call_rel2([0])

        else:
            # print(f'rel1 and rel2 mati')
            board.digital_write(rel1,0)
            call_rel1([0])

        '''
        perkondisian relay pada pada tingkat kebasahan tanah
        dari bacaan `SoilMoistureSensor`
        '''
        if b[0] < 800:
            # print(f'rel4 hidup')
            board.digital_write(rel4,1)
            call_rel4([1])

        else:
            # print(f'rel4 mati')
            board.digital_write(rel4,0)
            call_rel4([0])

        """
        perkondisian relay dan led sebagai indikator ketinggian air pada tanki
        """
        if c[0] > 120:
            board.digital_write(rel3,1)
            call_rel3([1])

        else:
            board.digital_write(rel3,0)
            call_rel3([0])


        ui.items[1].items[2].items[0].value = float(_chart_soil)
        ui.items[1].items[2].items[1].value = float(_chart_ldr)
        ui.items[0].items[2].value = float(_chart_hcsrs)

        _chart_relays[0].value =r1[0]
        _chart_relays[1].value =r2[0]
        _chart_relays[2].value =r3[0]
        _chart_relays[3].value =r4[0]

        _chart_log.append(f'humidity = {str(a[0])} suhu = {str(a[1])}')
        _chart_log.append(f'soilsensor = {str(b[0])}')
        _chart_log.append(f'ldr = {str(d[0])}')
        _chart_log.append(f'hcsr = {str(_chart_hcsrs)}')

        _chart_humadity.append(a[0])
        _chart_suhu.append(a[1])
        ui.display()
        # print(f'\npoll dht: humidity={a[0]} suhu={a[1]} \
        #         \ndata bacaan soil mosture sensor={b[0]} \
        #         \npoll pin hcsr={c[0]} \
        #         \npin ldr={d[0]} \n\n')
        # print(f'tipe data dht={type(a[0])}')

        # except KeyboardInterrupt:
        #     board.shutdown()
        #     sys.exit()
        loops +=1

# DEFINE PIN ARDUINO

# Analog
soil        = 0
ldr         = 1
pot_one     = 4
pot_two     = 5

# Digital:
dht         = 11
dht_tipe    = 11
hcsr_trig   = 10
hcsr_echo   = 9
rel1        = 2
rel2        = 3
rel3        = 4
rel4        = 5
# led         = [13,12,10,9,8,7,6] # < mengganggu kestablilan koneksi
# arr_digital = [2,3,4,5,6,7,8,9,10,12,13]
board = telemetrix.Telemetrix()
callbacks = TheCallback()
