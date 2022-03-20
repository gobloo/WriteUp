from Crypto.Util.number import inverse, long_to_bytes
print("RSA decoder : ")

#Change the value depend the message you want to decryt
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537 
# c : CYPHER that you need to decrypt
c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185 
# use https://www.alpertron.com.ar/ECM.HTM to factorize n and get p and q

p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063

phi=(p-1)*(q-1) #calculate phi
d=inverse(e, phi) #calculate d the private key
message = pow(c, d, n)
print(long_to_bytes(message).decode())

print("I Hope u solve it, #GOBLO")
