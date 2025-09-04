# Neste programa iremos definir quantos blocos tem uma pirâmede com base quantos blocos tem a base,
# a tal pirâmede poderá ser assim: 
#
#    # 
#   ### 
#  #####
# #######

blocosTotal = 0 
blocosBase = int(input("Quantos blocos tem na base na pirãmede? "))
dimininuir = 2

if (blocosBase >= 3): # Verificando se é possível fazer a pirâmede a partir dos blocos da base. 
    blocosTotal += blocosBase
    for i in range(1, blocosBase-1):
        blocosTotal+=blocosBase - dimininuir

        if ((blocosBase - dimininuir) <= 0):
            break

        dimininuir += 2 

    print(blocosTotal)
else: 
    print("Não é nem possível fazer uma pirâmede. ")