import time
from turtle import distance
import sensirion_i2c_scd30
import serial
import adafruit_us100
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection, CrcCalculator
from sensirion_i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_scd30.device import Scd30Device
st = time.time()
class SCD30:
    def medicaoSCD30(self):
        with LinuxI2cTransceiver('/dev/i2c-0') as i2c_transceiver:
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
            print(f"firmware version major: {major}; minor: {minor};")
            sensor.start_periodic_measurement(0)
            for i in range(30):
                try:
                    time.sleep(1.5)
                    (co2_concentration, temperature, humidity) = sensor.blocking_read_measurement_data()
                    print(f"co2_concentration: {co2_concentration}; temperature: {temperature}; humidity: {humidity}; ")
                except BaseException:
                    continue
            sensor.soft_reset()
            return (co2_concentration, temperature, humidity)
        
class US100:
    def medicaoUS100(self):
        uart = serial.Serial("/dev/ttySAC0", baudrate=9600, timeout=1)
        # uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
        # uart = serial.Serial("/dev/ttyAML0", baudrate=9600, timeout=1)
        us100 = adafruit_us100.US100(uart)
        while True:
            print("-----")
            print("Temperature: ", us100.temperature)
            time.sleep(0.5)
            distmedida = us100.distance
            print("Distance: ", us100.distance)
            time.sleep(0.5)
        return (distmedida)
class CSVconverter:
    def __init__(self, CO2, Temperatura, Umidade, Distancia):
        import csv  
        import time
        et = time.time()
        Tempo = et - st
        header = ['CO2', 'Temperatura', 'Umidade', 'Distância', 'Tempo']
        data = [CO2,Temperatura,Umidade,Distancia,Tempo]
        with open('path to file', 'w', encoding='UTF8') as f: #Coloque o path para um arquivo de texto para salvar os dados
            writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
        return("1")
class Main:
    def Main():
        (a,b,c) = SCD30().medicaoSCD30()
        d = US100().medicaoUS100()
        z = CSVconverter().__init__(self,a,b,c,d)
while 1==1:
    Main().Main()
    time.sleep(1)
        
