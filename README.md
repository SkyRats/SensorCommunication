# SensorCommunication

Esse repositório tem a função de realizar a integração do código dos sensores US100 e SCD30, e retornar os dados deles em um único código

# Instruções para uso:

#### Instalando o módulo US100 do circuitpython Blinka:

```
pip install adafruit-circuitpython-us100
```
#### Instalando o módulo SCD30 da Sensirion:

Clone o repositório python-i2c-scd30
```
git clone https://github.com/Sensirion/python-i2c-scd30
```

Dentro da pasta python-i2c-scd30:

```
python3 setup.py install
```
Conecte os sensores da seguinte forma (para a Odroid):

<p align="center">
  <img src="https://pi4j.com/1.2/images/odroid-xu4-con10-pinout.png" />
</p>

#### Conexão do SCD30:

GPIO#| GPIO Pin Name| Sensor Pin | Description     | Comments |
----- | ------------- | ----------- | -----------   | -------- |
  ⠀  |  5V VDC          | VDD         |   Supply Voltage          | 3.3 to 5V        |
  ⠀  |  GND       | GND         |    Ground         |        | 
   9 | SCL(I2C_1) | SCL   | I2C: Serial clock input   |     |
   8 | SDA(I2C_2) | SDA   | I2C: Serial data input / output   |     |
   
   ###### Obs: deixe os outros pinos em modo floating
   
#### Conexão do US100:

GPIO#| GPIO Pin Name| Sensor Pin | Description     | Comments |
----- | ------------- | ----------- | -----------   | -------- |
  ⠀  |  5V VDC          | VDD         |   Supply Voltage          | 5V        |
  ⠀  |  GND       | GND         |    Ground         |        | 
   16 | RxD(UART0) | Rx   |    |     |
   15 | TxD(UART1) | Tx   |   |     |

     
