from ecu.engine import Engine
from ecu.battery import Battery
from ecu.cooling import CoolingSystem
from ecu.gearbox import Gearbox

from sensors.rpm import RPMSensor
from sensors.temperature import TemperatureSensor
from sensors.speed import SpeedSensor
from sensors.fuel import FuelSensor
from sensors.gps import GPSSensor


def main():
    engine = Engine()
    battery = Battery()
    cooling = CoolingSystem()
    gearbox = Gearbox()

    rpm_sensor = RPMSensor()
    temp_sensor = TemperatureSensor()
    speed_sensor = SpeedSensor()
    fuel_sensor = FuelSensor()
    gps_sensor = GPSSensor()

    engine.start()

    for _ in range(10):
        engine.accelerate(500)
        engine.update_temperature()

        battery.consume()
        fuel_sensor.consume()
        cooling.update(engine)

        if engine.rpm > 3000:
            gearbox.shift_up()

        gps_sensor.update()

        rpm = rpm_sensor.read(engine)
        temp = temp_sensor.read(engine)
        speed = speed_sensor.calculate(rpm, gearbox.gear)
        fuel = fuel_sensor.read()
        lat, lon = gps_sensor.read()

        print("=" * 40)
        print("SMART TELEMETRY ECU SIMULATION")
        print("=" * 40)
        print(f"RPM         : {rpm}")
        print(f"Speed       : {speed:.1f} km/h")
        print(f"Gear        : {gearbox.gear}")
        print(f"Temperature : {temp:.1f} °C")
        print(f"Battery     : {battery.level:.1f}%")
        print(f"Fuel        : {fuel:.1f}%")
        print(f"GPS         : ({lat:.4f}, {lon:.4f})")
        print(f"Cooling Fan : {'ON' if cooling.fan_on else 'OFF'}")
        print()

    engine.stop()


if __name__ == "__main__":
    main()