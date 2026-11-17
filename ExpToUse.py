from TwoBasNumBerSyS import TwoBaseNumSys , colorTextSys
from pathlib import Path

BASE = Path(__file__).resolve().parent

#Set Path For Use
#A = BASE / "ExpHpwToUseFile.txt"
#B = BASE / "ExpHowToUseFile2.txt"

#Command For Count. go see HowToUse.txt to see how to use
#TwoBaseNumSys.Sys1(A,B, Name= "Test", Count= (2 , 2), CountADV= (1, 2, 0))

Stext = colorTextSys.Stext
print(Stext(text="Hello!", fg="black", bg="white"))

#Command to Reset Count. yea same too
#TwoBaseNumSys.Sys1RS(A,B)