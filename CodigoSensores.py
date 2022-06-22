import time
import sensirion_i2c_scd30
import serial
import adafruit_us100
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection, CrcCalculator
from sensirion_i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_scd30.device import Scd30Device
class SCD30:
    def medicaoSCD30(self): #Faz a medição do SCD30
        with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver: #Talvez seja necessário mudar o bus do i2c, para ver qual é o correto utilize o i2c tools como exemplificado no Readme
            channel = I2cChannel(I2cConnection(i2c_transceiver),
                                slave_address=0x61,
                                crc=CrcCalculator(8, 0x31, 0xff, 0x0))
            sensor = Scd30Device(channel)
            try:
                sensor.stop_periodic_measurement()
                sensor.soft_reset()
                time.sleep(2.0)
            except BaseException:
                ...

            (major, minor) = sensor.read_firmware_version()
            print(f"firmware version major: {major}; minor: {minor};") #Mostra a versão do firmware
            sensor.start_periodic_measurement(0)
            for i in range(30):
                try:
                    time.sleep(1.5)
                    (co2_concentration, temperature, humidity) = sensor.blocking_read_measurement_data()
                    print(f"co2_concentration: {co2_concentration}; temperature: {temperature}; humidity: {humidity}; ")
                except BaseException:
                    continue
            sensor.soft_reset()
        
class US100:
    def medicaoUS100(self): #Essa função faz a medição do US100
        # Caso ocorra algum erro, troque a porta que o USB está conectado ou troque a porta especificada na variável UART
        uart = serial.Serial("/dev/ttySAC0", baudrate=9600, timeout=1)
        # uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
        # uart = serial.Serial("/dev/ttyAML0", baudrate=9600, timeout=1)
        us100 = adafruit_us100.US100(uart)
        while True:
            print("-----")
            print("Temperature: ", us100.temperature)
            time.sleep(0.5)
            print("Distance: ", us100.distance)
            time.sleep(0.5)
        
a = SCD30()
x = a.medicaoSCD30()
print = x 
