from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.contact import ContactSensor


class SensorContact(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(ContactSensor(devices, 'sensor', 'contact'))
