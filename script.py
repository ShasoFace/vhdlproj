import os
import sys

n = len(sys.argv)          
i = 1                       
while i < n:                                                    
    k = os.system('cmd /c ghdl -s '+ sys.argv[i]+".vhdl")           
    if k == 0:                                                     
        print("Syntax-Check Ok")
    else:                                                         
        print(sys.argv[i])
        print("Syntax-Check failed")
        sys.exit()
    k = os.system('cmd /c ghdl -a '+ sys.argv[i]+".vhdl")
    if k == 0:
        print("Analyse Ok")
    else:
        print("Analyse failed")
        sys.exit()
    k = os.system('cmd /c ghdl -e ' + sys.argv[i])
    if k == 0:
        print("Build Ok")
    else:
        print("Build failed")
        sys.exit()
    i=i+1                                                          

i=i-1                                                                       
k = os.system('cmd /c ghdl -r ' + sys.argv[i] + " --vcd=testbench.vcd")
if k == 0:
    print("VCD-Dump Ok")
else:
    print("VCD-Dump failed")
    sys.exit()
k = os.system('cmd /c gtkwave testbench.vcd ')
if k == 0:
     print("Starting GTKWave") 
else:
    print("GTKWave failed")
    sys.exit()
sys.exit()
