#the most useless thing make by me
#how to use:
#a = BASE / "Texts" / "a.txt"
#b = BASE / "Texts" / "b.txt"
#TwoBaseNumSys.Sys1(a)  # Song A
#TwoBaseNumSys.Sys1(b)  # Song B
#version: 1.0Demo

from pathlib import Path

BASE = Path(__file__).resolve().parent
TbN = BASE / "TBNBStxtF" / "TBNBStxt.txt"
CASs = BASE / "TBNBStxtF" / "CA256S.txt"

class TwoBaseNumSys():
   def Sys1(TbN = TbN, Name="Count", Count=(1 , 1), CountADV=(1 , 1 , 0)):
        CountSet , CountTime = Count
        CountTimeBIN , CountFD , CountSet2 = CountADV
        ConutAFER256 = 0
        TbNW = (TbN , "w")
        TbNR = (TbN , "r")
        Op1 = (CASs , "w")
        Op2 = (CASs , "r")

        with open(*Op2) as Op3:
         Op3b = Op3.read()

        if Op3b == "0000 0000":
         ConutAFER256 = 0
        elif Op3b == "0000 0001":
          ConutAFER256 = 99
        elif Op3b == "0000 0010":
           ConutAFER256 = 198
        elif Op3b == "0000 0011":
           ConutAFER256 = 297
        elif Op3b == "0000 0100":
           ConutAFER256 = 396
        elif Op3b == "0000 0101":
           ConutAFER256 = 495

        elif Op3b == "0000 0110":
           ConutAFER256 = 594
        elif Op3b == "0000 0111":
           ConutAFER256 = 693
        elif Op3b == "0000 1000":
           ConutAFER256 = 792
        elif Op3b == "0000 1001":
           ConutAFER256 = 891
        elif Op3b == "0000 1010":
           ConutAFER256 = 990

        elif Op3b == "0000 1011":
           ConutAFER256 = 1089
        elif Op3b == "0000 1100":
           ConutAFER256 = 1188
        elif Op3b == "0000 1101":
           ConutAFER256 = 1287
        elif Op3b == "0000 1110":
           ConutAFER256 = 1386
        elif Op3b == "0000 1111":
           ConutAFER256 = 1485

        elif Op3b == "0001 0000":
           ConutAFER256 = 1584

        with open(*TbNR) as ReadSys:
           ReadSy = ReadSys.read()

        def Testi():
         with open(*Op2) as Op3:
          Op3b = Op3.read()

          if Op3b == "0000 0000":
           with open(*Op1) as Op3a:
            Op3a.write("0000 0001")

          elif Op3b == "0000 0001":
            with open(*Op1) as Op3a:
             Op3a.write("0000 0010")
          elif Op3b == "0000 0010":
            with open(*Op1) as Op3a:
             Op3a.write("0000 0011")

          elif Op3b == "0000 0011":
            with open(*Op1) as Op3a:
             Op3a.write("0000 0100")
          elif Op3b == "0000 0100":
            with open(*Op1) as Op3a:
             Op3a.write("0000 0101")

          elif Op3b == "0000 0101":
            with open(*Op1) as Op3a:
             Op3a.write("0000 0110")
          elif Op3b == "0000 0110":
            with open(*Op1) as Op3a:
             Op3a.write("0000 0111")

          elif Op3b == "0000 0111":
            with open(*Op1) as Op3a:
             Op3a.write("0000 1000")
          elif Op3b == "0000 1000":
            with open(*Op1) as Op3a:
             Op3a.write("0000 1001")

          elif Op3b == "0000 1001":
            with open(*Op1) as Op3a:
             Op3a.write("0000 1010")

          elif Op3b == "0000 1010":
            with open(*Op1) as Op3a:
             Op3a.write("0000 1011")
          elif Op3b == "0000 1011":
            with open(*Op1) as Op3a:
             Op3a.write("0000 1100")

          elif Op3b == "0000 1100":
            with open(*Op1) as Op3a:
             Op3a.write("0000 1101")
          elif Op3b == "0000 1101":
            with open(*Op1) as Op3a:
             Op3a.write("0000 1110")
          elif Op3b == "0000 1110":
            with open(*Op1) as Op3a:
             Op3a.write("0000 1111")

          elif Op3b == "0000 1111":
            with open(*Op1) as Op3a:
             Op3a.write("0001 0000")
          elif Op3b == "0001 0000":
             with open(*Op1) as Op3a:
               Op3a.write("0000 0000")
             print("ERORR. this is the end D;")

        #TBN 0-10
        if ReadSy == "0000 0000":
           Number = (((0 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 0001")
        elif ReadSy == "0000 0001":
           Number = (((1 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 0010")
        elif ReadSy == "0000 0010":
           Number = (((2 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 0011")

        elif ReadSy == "0000 0011":
           Number = (((3 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 0100")
        elif ReadSy == "0000 0100":
           Number = (((4 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 0101")
        elif ReadSy == "0000 0101":
           Number = (((5 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 0110")
        elif ReadSy == "0000 0110":
           Number = (((6 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 0111")
        elif ReadSy == "0000 0111":
           Number = (((7 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 1000")
        elif ReadSy == "0000 1000":
           Number = (((8 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 1001")
        elif ReadSy == "0000 1001":
           Number = (((9 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 1010")


        #TBN 11 - 20
        elif ReadSy == "0000 1010":
           Number = (((10 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 1011")
        elif ReadSy == "0000 1011":
           Number = (((11 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 1100")
        elif ReadSy == "0000 1100":
           Number = (((12 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 1101")
        elif ReadSy == "0000 1101":
           Number = (((13 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 1110")
        elif ReadSy == "0000 1110":
           Number = (((14 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 1111")
        elif ReadSy == "0000 1111":
           Number = (((15 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 0000")
        elif ReadSy == "0001 0000":
           Number = (((16 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 0001")
        elif ReadSy == "0001 0001":
           Number = (((17 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 0010")
        elif ReadSy == "0001 0010":
           Number = (((18 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 0011")
        elif ReadSy == "0001 0011":
           Number = (((19 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 0100")


        #TBN 21 - 30
        elif ReadSy == "0001 0100":
           Number = (((20 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 0101")
        elif ReadSy == "0001 0101":
           Number = (((21 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 0110")
        elif ReadSy == "0001 0110":
           Number = (((22 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 0111")
        elif ReadSy == "0001 0111":
           Number = (((23 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 1000")
        elif ReadSy == "0001 1000":
           Number = (((24 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 1001")
        elif ReadSy == "0001 1001":
           Number = (((25 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 1010")
        elif ReadSy == "0001 1010":
           Number = (((26 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 1011")
        elif ReadSy == "0001 1011":
           Number = (((27 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 1100")
        elif ReadSy == "0001 1100":
           Number = (((28 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 1101")
        elif ReadSy == "0001 1101":
           Number = (((29 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 1110")

        #TBN 31 - 40
        elif ReadSy == "0001 1110":
           Number = (((30 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0001 1111")
        elif ReadSy == "0001 1111":
           Number = (((31 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 0000")
        elif ReadSy == "0010 0000":
           Number = (((32 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 0001")
        elif ReadSy == "0010 0001":
           Number = (((33 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 0010")
        elif ReadSy == "0010 0010":
           Number = (((34 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 0011")
        elif ReadSy == "0010 0011":
           Number = (((35 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 0100")
        elif ReadSy == "0010 0100":
           Number = (((36 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 0101")
        elif ReadSy == "0010 0101":
           Number = (((37 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 0110")
        elif ReadSy == "0010 0110":
           Number = (((38 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 0111")
        elif ReadSy == "0010 0111":
           Number = (((39 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 1000")


        #TBN 41 - 50
        elif ReadSy == "0010 1000":
           Number = (((40 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 1001")
        elif ReadSy == "0010 1001":
           Number = (((41 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 1010")
        elif ReadSy == "0010 1010":
           Number = (((42 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 1011")
        elif ReadSy == "0010 1011":
           Number = (((43 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 1100")
        elif ReadSy == "0010 1100":
           Number = (((44 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 1101")
        elif ReadSy == "0010 1101":
           Number = (((45 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 1110")
        elif ReadSy == "0010 1110":
           Number = (((46 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0010 1111")
        elif ReadSy == "0010 1111":
           Number = (((47 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 0000")
        elif ReadSy == "0011 0000":
           Number = (((48 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 0001")
        elif ReadSy == "0011 0001":
           Number = (((49 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 0010")

        #char2 51 - 100 (Nothing yup)

        #TBN 51 - 60
        elif ReadSy == "0011 0010":
           Number = (((50 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 0011")
        elif ReadSy == "0011 0011":
           Number = (((51 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 0100")
        elif ReadSy == "0011 0100":
           Number = (((52 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 0101")
        elif ReadSy == "0011 0101":
           Number = (((53 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 0110")
        elif ReadSy == "0011 0110":
           Number = (((54 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 0111") ##
        elif ReadSy == "0011 0111":
           Number = (((55 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 1000")
        elif ReadSy == "0011 1000":
           Number = (((56 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 1001")
        elif ReadSy == "0011 1001":
           Number = (((57 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 1010")
        elif ReadSy == "0011 1010":
           Number = (((58 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 1011")
        elif ReadSy == "0011 1011":
           Number = (((59 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 1100")


        #TBN 61 - 70
        elif ReadSy == "0011 1100":
           Number = (((60 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 1101")
        elif ReadSy == "0011 1101":
           Number = (((61 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 1110")
        elif ReadSy == "0011 1110":
           Number = (((62 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0011 1111")
        elif ReadSy == "0011 1111":
           Number = (((63 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 0000") ##
        elif ReadSy == "0100 0000":
           Number = (((64 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 0001")
        elif ReadSy == "0100 0001":
           Number = (((65 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 0010")
        elif ReadSy == "0100 0010":
           Number = (((66 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 0011")
        elif ReadSy == "0100 0011":
           Number = (((67 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 0100")
        elif ReadSy == "0100 0100":
           Number = (((68 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 0101")
        elif ReadSy == "0100 0101":
           Number = (((69 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 0110")

        #TBN 71 - 80
        elif ReadSy == "0100 0110":
           Number = (((70 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 0111")
        elif ReadSy == "0100 0111":
           Number = (((71 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 1000")
        elif ReadSy == "0100 1000":
           Number = (((72 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 1001")
        elif ReadSy == "0100 1001":
           Number = (((73 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 1010")
        elif ReadSy == "0100 1010":
           Number = (((74 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 1011")
        elif ReadSy == "0100 1011":
           Number = (((75 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 1100")
        elif ReadSy == "0100 1100":
           Number = (((76 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 1101")
        elif ReadSy == "0100 1101":
           Number = (((77 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 1110")
        elif ReadSy == "0100 1110":
           Number = (((78 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0100 1111")
        elif ReadSy == "0100 1111":
           Number = (((79 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 0000")


        #TBN 81 - 90
        elif ReadSy == "0101 0000":
           Number = (((80 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 0001")
        elif ReadSy == "0101 0001":
           Number = (((81 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 0010")
        elif ReadSy == "0101 0010":
           Number = (((82 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 0011")
        elif ReadSy == "0101 0011":
           Number = (((83 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 0100")
        elif ReadSy == "0101 0100":
           Number = (((84 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 0101")
        elif ReadSy == "0101 0101":
           Number = (((85 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 0110")
        elif ReadSy == "0101 0110":
           Number = (((86 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 0111")
        elif ReadSy == "0101 0111":
           Number = (((87 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 1000")
        elif ReadSy == "0101 1000":
           Number = (((88 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 1001")
        elif ReadSy == "0101 1001":
           Number = (((89 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 1010")

        #TBN 91 - 100
        elif ReadSy == "0101 1010":
           Number = (((90 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 1011")
        elif ReadSy == "0101 1011":
           Number = (((91 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 1100")
        elif ReadSy == "0101 1100":
           Number = (((92 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 1101")
        elif ReadSy == "0101 1101":
           Number = (((93 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 1110")
        elif ReadSy == "0101 1110":
           Number = (((94 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0101 1111")
        elif ReadSy == "0101 1111":
           Number = (((95 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0110 0000")
        elif ReadSy == "0110 0000":
           Number = (((96 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0110 0001")
        elif ReadSy == "0110 0001":
           Number = (((97 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0110 0010")
        elif ReadSy == "0110 0010":
           Number = (((98 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0110 0011")
        elif ReadSy == "0110 0011":
           Number = (((99 + CountSet + CountSet2 + ConutAFER256) *CountTime) //CountFD)**CountTimeBIN
           print(f"{Name}: {Number}")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0110 0100")
           Testi()

        #more than 255
        else:
           print("ERORR D:")
           with open(*TbNW) as ReadSys2:
              ReadSys2.write("0000 0000")