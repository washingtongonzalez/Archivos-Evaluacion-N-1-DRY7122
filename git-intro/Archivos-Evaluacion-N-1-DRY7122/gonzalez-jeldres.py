vlannum = int(input("cual es el numero de vlan?"))
if vlannum >= 1 and vlannum <=1005:
    print("este es una vlan estandar")
elif vlannum >=1005 and vlannum <= 4096:
    print("esta es una vlan extendida")
else:
    print("esta vlan no es ni estandar ni extendida.")

    