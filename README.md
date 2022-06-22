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

