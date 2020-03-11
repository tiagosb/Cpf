#-*- encoding:utf-8 -*-
import random

class Cpf:
    
    def _soma(self, peso, cpf):
        i, soma = 0, 0
        while not peso == 1:
            soma += peso * int(cpf[i])
            i += 1
            peso -= 1
        return soma

    def _calcular_digito(self, peso, cpf):
        soma = self._soma(peso, cpf)
        resto = soma % 11
        if not resto == 0 and not resto == 1:
            return 11 - resto
        return resto

    def _str2list(self, str):
        ilist = []
        for ch in str:
            ilist.append(ch)
        return ilist
   
    def validar(self, cpf):
        if not len(cpf) == 11:
            return False
        
        digito1 = self._calcular_digito(10, cpf)
        
        if not str(digito1) == cpf[9]:
            return False
        
        cpf = self._str2list(cpf)
        cpf[9] = str(digito1)

        digito2 = self._calcular_digito(11, cpf)
        if not str(digito2) == cpf[10]:
            return False
        return True 

    def gerar(self):
        base = []
        for i in range(0,9):
            base.append(str(random.randint(0,9)))
        base.append(str(self._calcular_digito(10, base)))
        base.append(str(self._calcular_digito(11, base)))
        
        cpf = ''.join(base)
        return self.formatar(cpf)
    
    def formatar(self, cpf):
        cpf = cpf.replace('.','').replace('-','')
        return "{}.{}.{}-{}".format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])

if __name__ == "__main__":
    cpf = Cpf()
    while True:
        try:
            print("Gerar CPF(g) | Validar(v) | Formatar(f) | Sair(ctrl+c)")
            op = input(": ")
            if op == 'g':
                print("**",cpf.gerar(),"**")
            if op == 'v':
                cpf_input = input("cpf: ")
                print("O cpf informado é", "** válido **" if cpf.validar(cpf_input) else "** inválido **")
            if op == 'f':
                cpf_input = input("cpf: ")
                if cpf.validar(cpf_input):
                    print(cpf.formatar(cpf_input))
                else:
                    print("CPF inválido.")
            print("-----------------------------------------------------------")
        except KeyboardInterrupt:
            print("bye")
            exit()
