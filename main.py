Ping = 0

def on_forever():
    global Ping
    Ping = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
    led.plot_bar_graph(Ping, 0)
basic.forever(on_forever)
