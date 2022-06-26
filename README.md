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

### Possíveis problemas:

##### Código do SCD30 não detectando firmware ou dando erro:

Instale e utilize o I2C-tools para detectar se a Odroid está detectando o sensor:

```
sudo apt update
sudo apt install i2c-tools
i2cdetect -y 0
```
Caso o sensor esteja conectado corretamente, ele deve ocupar o endereço 0x61

##### US100 não está sendo detectado:

Tente inverter a conexão do pino Rx e Tx

##### Erro com a porta serial do US100:

Tente mudar a porta serial utilizada no código dos sensores, instruções detalhadas estão nos comentários do próprio código

## É necessário colocar no código o caminho para o arquivo de texto que erá usado para arquivar os dados em CSV

### OBS:

Esse código foi testado individualmente porém o código do repositório ainda não foi testado na odroid XU4, porém isso deve ser feito em breve
