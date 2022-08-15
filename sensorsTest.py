import greenSensors
import time

class Main:
    def Main():
        (a,b,c) = SCD30().medicaoSCD30()
        d = US100().medicaoUS100()
        z = CSVconverter().__init__(self,a,b,c,d)

while 1==1:
    Main().Main()
    time.sleep(1)