import hashlib





class Roteiro():
        def md5(self, ponto):
                lista_hash = []
                while True:
                        md5 = hashlib.md5()
                        for c in lista_hash:
                                md5.update(chr(c).encode())
                        hash = md5.hexdigest()
                        print("comparadas %s" % hash)
                        if hash == ponto:
                                todas =" {}".format(([chr(c) for c in lista_hash]))
                                print("conclusão = %s" % todas.replace('[', '').replace(",", '').
                                      replace("]", '').replace("'", '').replace(" ", ''))

                                break

                        paronimo = True
                        for i in range(0, len(lista_hash)):
                                lista_hash[i] = (lista_hash[i] + 1) % 256
                                if lista_hash[i] != 0:
                                        paronimo = False
                                        break
                        if paronimo:
                                lista_hash.append(0)




Roteiro().md5("23eeeb4347bdd26bfc6b7ee9a3b755dd")
