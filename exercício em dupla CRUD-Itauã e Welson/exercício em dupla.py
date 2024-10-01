import os
os.system("cls || clear")
from dataclasses import dataclass

#função.
def limpa_tela():
    os.system("cls || clear")
    
#class ou CRUD.
@dataclass
class Prefeitura:
    salario: float
    filhos: int
    
# Lista.
lista_dados = []

# primeiro laço de repetição.
while True:
    print("""
Código  |  Descrição
1-Adicionar Família
2-Exibir dados
3-Sair
          """)
    
    opcao = input("Escolha uma opção exibida acima: ")
    #condições para as opções acima.
    if opcao == '1':
        limpa_tela()
        salario = float(input("Salário da família: "))
        filhos = int(input("Número de filhos: "))
        nova_familia = Prefeitura(salario, filhos)
        lista_dados.append(nova_familia)
        
        # Salvar dados do "usuario".
        with open("pesquisa_prefeitura.txt", "w") as file:
            for familia in lista_dados:
                file.write(f"{Prefeitura.salario},{Prefeitura.filhos}\n")

    elif opcao == '2':
        limpa_tela()
        # Calculando informações ou verificando
        total_familias = len(lista_dados)
        total_salario = sum(familia.salario for familia in lista_dados)
        total_filhos = sum(familia.filhos for familia in lista_dados)
        
        if total_familias > 0:
            media_salario = total_salario / total_familias
            media_filhos = total_filhos / total_familias
            
            # Encontra o maior e o menor salario.
            maior_salario = max(familia.salario for familia in lista_dados)
            menor_salario = min(familia.salario for familia in lista_dados)

            # Exibindo dados do usuario.
            print(f"Quantidade de famílias: {total_familias}")
            print(f"Média salarial: R$ {media_salario:.2f}")
            print(f"Média de filhos: {media_filhos:.2f}")
            print(f"Maior salário: R$ {maior_salario:.2f}")
            print(f"Menor salário: R$ {menor_salario:.2f}")
        else:
            print("Insira dados de uma familia.")

    elif opcao == '3':
        print("Obrigada por utilizar o GOV.com.Bahia! Pelo seu futuro nos unimos.")
        break
    