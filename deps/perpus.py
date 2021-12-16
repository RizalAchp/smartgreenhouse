from telemetrix import telemetrix
from deps.thecallback import TheCallback
# from deps.liquidcrystal import *
# from deps.query_sql import *
import time
# VARIABLE PIN PADA ARDUINNO
# Analog:

def mainFunctions(board:telemetrix.Telemetrix ,calls:TheCallback)->None:
    """mainFunctions

    fungsi =    memulai semua proses pada arduino berupa loop while
                dan memanggil banyak function maupun library local
                 dengan parameter masing masing.
    """
    call_dht = calls.dhtcallback
    call_soil = calls.soilcallback
    call_hcsr = calls.hcsrcallback
    call_ldr = calls.ldrcallback
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
    a = calls.a     # data callback dht
    b = calls.b     # data callback soil
    c = calls.c     # data callback hcsr
    d = calls.d     # data callback ldr

    # LCD.clear()
    # LCD.enable_backlight()
    # loop fungsinya 
    for loops in range(loop):
    # while True:
        time.sleep(5.0)
        # try:
        # LCD.begin(16,2)
        # LCD.set_cursor(0,0)
        # LCD.print(f'hmty={a[0]}tmp={a[1]}')
        # LCD.set_cursor(0,1)
        # LCD.print(f'wtr={c[0]}soil={b[0]}')

        """
        perkondisian relay pada ketentuan suhu
        maupun kelembapan udara dari dht sensor
        """
        if a[1] < (.1*50):
            print(f'rel1 and rel2 hidup')
            board.digital_write(rel1,0)
            board.digital_write(rel2,0)

        else:
            print(f'rel1 and rel2 mati')
            board.digital_write(rel1,1)
            board.digital_write(rel2,1)


        """
        perkondisian relay dan led sebagai indikator ketinggian air pada tanki
        """
        if c[0] > 120:
            board.digital_write(rel3,1)

        else:
            board.digital_write(rel3,0)


        print(f'\npoll dht: humidity={a[0]} suhu={a[1]} \
                \ndata bacaan soil mosture sensor={b[0]} \
                \npoll pin hcsr={c[0]} \
                \npin ldr={d[0]} \n\n')
        print(f'tipe data dht={type(a[0])}')

        # except KeyboardInterrupt:
        #     board.shutdown()
        #     sys.exit()
        loops +=1

dht         = 11
dht_tipe    = 11
soil        = 0
ldr         = 1
hcsr_trig   = 10
hcsr_echo   = 9

# Digital:
rel1        = 2
rel2        = 3
rel3        = 4
rel4        = 5
led         = [13,12,10,9,8,7,6]
arr_digital = [2,3,4,5,6,7,8,9,10,12,13]
board = telemetrix.Telemetrix()
callbacks = TheCallback()
