from dashing.dashing import VGauge,HSplit,Text,Log,ColorRangeVGauge,\
    VSplit,HChart,HGauge

ui = VSplit(
        HSplit(
            Log(title="log data",border_color=3,color=3),
            VSplit(
                Text("TIM TREESAKTI - TKK POLIJE",
                     color=1,border_color=1),
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
                    (33, 1),
                    (66, 3),
                    (100, 2),
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
