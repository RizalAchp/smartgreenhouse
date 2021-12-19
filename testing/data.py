from dashing.dashing import HSplit,Text,Log,ColorRangeVGauge,VSplit,HChart,HGauge,VGauge
import random
import time
ui = VSplit(
        HSplit(
            Log(title="log",border_color=3,color=3),
            VSplit(
                Text("KELOMPOK MATAKULIAH WORKSHOP SISTEM TERTANAM",color=1,border_color=1),
                HSplit(
                    VGauge(title="relay1", val=0, border_color=2, color=2),
                    VGauge(title="relay2", val=0, border_color=2, color=2),
                    VGauge(title="relay3", val=0, border_color=2, color=2),
                    ColorRangeVGauge(
                        title="relay4",
                        val=0,
                        border_color=2,
                        colormap=(
                            (0,1),
                            (100,2),
                        )
                    )
                )
            ),
            ColorRangeVGauge(
                title="Isi Air",
                val=100,
                border_color=2,
                colormap=(
                    (33, 2),
                    (66, 3),
                    (100, 1),
                )
            ),
        ),
        VSplit(
            HChart(title="Humadity",val=100, border_color=6,color=6),
            HChart(title="Temperature",val=40, border_color=6,color=6),
            HSplit(
                HGauge(val=100, label="Moisture", border_color=11,color=7),
                HGauge(val=100, label="ldr", border_color=11,color=7),
            )
        ),
    title="SMART GREENHOUSE 🌱 WITH PYTHON",
    color=4,
    border_color=4

    )

# access a tile by index
log = ui.items[0].items[0]
humadity = ui.items[1].items[0]
suhu = ui.items[1].items[1]

for x in range(1,1000):
    i = random.randint(30,100)
    b = random.randint(500,1000)
    chart_soil = b/100
    chart_ldr = b/100
    ui.items[1].items[2].items[1].value = float(chart_soil)
    ui.items[1].items[2].items[0].value = float(chart_ldr)
    ui.items[0].items[2].value = float(i)
    vgauges = ui.items[0].items[1].items[-1].items
    vgauges[0].value =(random.randint(0,1)*100)
    vgauges[1].value =(random.randint(0,1)*100)
    vgauges[2].value =(random.randint(0,1)*100)
    vgauges[3].value =(random.randint(0,1)*100)
    log.append(f'humidity = {str(i)} suhu = {str(i)}')
    log.append(f'soilsensor = {str(i)}')
    log.append(f'ldr = {str(i)}')
    log.append(f'hcsr = {str(i)}')
    humadity.append(i)
    suhu.append(i)
    ui.display()
    time.sleep(5.0)
    x+=1
