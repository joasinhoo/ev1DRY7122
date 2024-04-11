aclNum = int(input("ingresa numero de acl ipv4: "))
if aclNum >= 1 and aclNum <= 99:
    print("este es un acl ipv4 estandar")
elif aclNum >=100 and aclNum <= 199:
    print("este es una acl ipv4 extendido")
else:
    print("el número no corresponde a una lista de acceso")
