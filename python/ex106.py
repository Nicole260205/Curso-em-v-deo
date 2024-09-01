import pydoc
from colorama import Fore, Style

def interactive_help():
    print(Fore.BLUE + '=-' * 20)
    print(Fore.CYAN + 'SISTEMA DE AJUDA INTERATIVA')
    print(Fore.BLUE + '=-' * 20 + Style.RESET_ALL)

    while True:
        comando = input(Fore.YELLOW + 'Função ou Biblioteca (Digite "FIM" para sair): ').lower()
        
        if comando == 'fim':
            print(Fore.GREEN + 'Encerrando o sistema de ajuda...')
            break

        try:
            help_content = pydoc.render_doc(comando)
            print(Fore.WHITE + help_content)
        except Exception as e:
            print(Fore.RED + f'Erro: {e}')

        print(Fore.BLUE + '=-' * 20 + Style.RESET_ALL)

if __name__ == "__main__":
    interactive_help()
