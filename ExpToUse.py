from TwoBasNumBerSyS import TwoBaseNumSys
from pathlib import Path

BASE = Path(__file__).resolve().parent

A = BASE / "ExpHpwToUseFile.txt"

TwoBaseNumSys.Sys1(A, Name= "Test", Count= (2 , 2), CountADV= (1, 2, 0))