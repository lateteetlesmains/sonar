let Ping = 0
basic.forever(function () {
    Ping = sonar.ping(
    DigitalPin.P1,
    DigitalPin.P2,
    PingUnit.Centimeters
    )
    led.plotBarGraph(
    Ping,
    0
    )
})
