import time
from telemetrix import telemetrix
from .dashboard import ui
from .datasensor import TheCallback

# from deps.query_sql import *
# from deps.liquidcrystal import *
def main_functions(board: telemetrix.Telemetrix, calls: TheCallback, loop: int)->None:
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
    call_REL1 = calls.rel1_callback
    call_REL2 = calls.rel2_callback
    call_REL3 = calls.rel3_callback
    call_REL4 = calls.rel4_callback

    # LCD = LiquidCrystal_I2C(0x3F, 0, 1, board)
    board.set_pin_mode_analog_input(SOIL, differential=5,
                                    callback=call_soil)
    board.set_pin_mode_analog_input(LDR, differential=5,
                                    callback=call_ldr)
    board.set_pin_mode_sonar(HCSRTRIG, HCSRECHO,
                             callback=call_hcsr)
    board.set_pin_mode_dht(DHT, call_dht, DHTTIPE)

    board.set_pin_mode_digital_output(REL1)
    board.set_pin_mode_digital_output(REL2)
    board.set_pin_mode_digital_output(REL3)
    board.set_pin_mode_digital_output(REL4)

    call_REL1([0])
    call_REL2([0])
    call_REL3([0])
    call_REL4([0])

    time.sleep(1.0)
    a = calls._a     # data callback dht
    b = calls._b     # data callback SOIL
    c = calls._c     # data callback hcsr
    d = calls._d     # data callback LDR
    r1 = calls._r1     # data callback relay1
    r2 = calls._r2     # data callback relay2
    r3 = calls._r3     # data callback relay3
    r4 = calls._r4     # data calback relay4

    _chart_SOIL = b[0]/10
    _chart_hcsrs = c[0]/2
    _chart_LDR = d[0]/10
    # access a tile by index
    _chart_log = ui.items[0].items[0]
    _chart_humadity = ui.items[1].items[0]
    _chart_suhu = ui.items[1].items[1]
    _chart_relays = ui.items[0].items[1].items[-1].items
    # LCD.clear()
    # LCD.enable_backlight()
    # loop fungsinya
    # while True:
    for loops in range(loop):
        # try:
        time.sleep(5.0)

        # perkondisian relay pada ketentuan suhu
        # maupun kelembapan udara dari DHT sensor
        if a[0] < 80.0:  # HUMADITY
            board.digital_write(REL1, 1)
            call_REL1([1])
            if a[1] >= 25.0:  # SUHU
                # print(f'REL1 and REL2 hidup')
                board.digital_write(REL2, 1)
                call_REL2([1])
            else:
                board.digital_write(REL2, 0)
                call_REL2([0])

        else:
            # print(f'REL1 and REL2 mati')
            board.digital_write(REL1, 0)
            call_REL1([0])

        # perkondisian relay pada pada tingkat kebasahan tanah
        # dari bacaan `SOILMoistureSensor`
        if b[0] < 800:
            # print(f'REL4 hidup')
            board.digital_write(REL4, 1)
            call_REL4([1])

        else:
            # print(f'REL4 mati')
            board.digital_write(REL4, 0)
            call_REL4([0])

        # perkondisian relay dan led sebagai indikator ketinggian air pada tanki
        if c[0] > 120:
            board.digital_write(REL3, 1)
            call_REL3([1])

        else:
            board.digital_write(REL3, 0)
            call_REL3([0])

        # UI DASHBOARD TERMINAL ELEMENT DAN DATA
        ui.items[1].items[2].items[0].value = float(_chart_SOIL)
        ui.items[1].items[2].items[1].value = float(_chart_LDR)
        ui.items[0].items[2].value = float(_chart_hcsrs)

        _chart_relays[0].value = r1[0]
        _chart_relays[1].value = r2[0]
        _chart_relays[2].value = r3[0]
        _chart_relays[3].value = r4[0]

        _chart_log.append(f'humidity = {str(a[0])} suhu = {str(a[1])}')
        _chart_log.append(f'SOILsensor = {str(b[0])}')
        _chart_log.append(f'LDR = {str(d[0])}')
        _chart_log.append(f'hcsr = {str(_chart_hcsrs)}')

        _chart_humadity.append(a[0])
        _chart_suhu.append(a[1])
        ui.display()
        loops += 1
        # except KeyboardInterrupt:
        #     board.shutdown()
        #     sys.exit()


# DEFINE PIN ARDUINO
# Analog
SOIL = 0
LDR = 1
# POT_ONE = 4
# POT_TWO = 5

# Digital:
DHT = 11
DHTTIPE = 11
HCSRTRIG = 10
HCSRECHO = 9
REL1 = 2
REL2 = 3
REL3 = 4
REL4 = 5
