import os

## Criando uma lista de dicionários com lojas pré-cadastradas
restaurantes = [
    {'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
    {'nome':'Sushi Lover', 'categoria':'Sushi', 'ativo':True},
    {'nome':'Pizza do mal', 'categoria':'Pizza', 'ativo':False}
]

## Funcção para exibir nome do programa
def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

## Função para exibir opções
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

## Função para finalizar app
def finalizar_app():
    exibir_subtitulo('Finalizando o app...')

## Função para voltar ao menu inicial
def voltar_ao_menu_inicial(): 
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    main()  

## Função para exibir o subtítulo
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

## Função para opção inválida
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_inicial()

## Função para cadastrar novo restaurante
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {
        'nome': nome_do_restaurante, 
        'categoria':categoria_do_restaurante, 
        'ativo':False
    }

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_inicial()

## Função de listar restaurantes
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_inicial()

## Função para alternar estado do restaurante
def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
        
    voltar_ao_menu_inicial()

## Função de escolher opções
def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except ValueError:
        opcao_invalida()

## Função principal do programas
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()