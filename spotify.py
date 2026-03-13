from datetime import date
import getpass
import time

def criar():
    print('teste')
    print('Vamos criar sua conta:')
    print('-'*50)
    time.sleep(1)
    email=input('Digite seu melhor email: ').lower().strip()
    senha=getpass.getpass('Crie uma senha: ').strip()
    senha2=getpass.getpass('Digite a senha novamente: ').strip()
    if senha==senha2:
        print('-'*50)
        time.sleep(1)
        try:
            with open('usuarios.txt','r',encoding='utf-8') as usuarios:
                lista=usuarios.readlines()
                for linha in lista:
                    if email==linha.split(',')[0]:
                        print('ja tem uma conta com esse email')
                        print('-'*50)
                        time.sleep(1)
                        print('voltando para o menu principal...')
                        time.sleep(1)
                        return main()
        except Exception as erro:
            print(erro)
        with open('usuarios.txt','a',encoding='utf-8') as usuarios:
            usuarios.write(f'{email},{senha}\n')
            return menu()
    else:
        print('-'*50)
        time.sleep(1)
        print('As senhas não coincidem')
        print('-'*50)
        time.sleep(1)
        print('voltando para o menu principal...')
        time.sleep(1)
        return main()

def login():
    time.sleep(1)
    print('Vamos fazer o seu login!')
    print('-'*50)
    time.sleep(1)
    email=input('Digite seu melhor email: ').lower().strip()
    senha=getpass.getpass('Digite sua senha: ').strip()
    print('-'*50)
    with open('usuarios.txt','r',encoding='utf-8') as usuarios:
        lista=usuarios.readlines()
        if len(lista)==0:
            print('ainda não existem usuarios cadastrados')
            return main()
        for linha in lista:
            email_arquivo=linha.split(',')[0].strip()
            senha_arquivo=linha.split(',')[1].strip()
            if email==email_arquivo and senha==senha_arquivo:
                time.sleep(1)
                print('carregando')
                print('-'*50)
                time.sleep(1)
                return menu()
            else:
                time.sleep(1)
                print('email ou senha incorretos')
                print('-'*50)
                time.sleep(1)
                return main()
        
            
def main():
    data_atual = date.today().strftime('%d/%m/%Y')
    print('-'*50)
    print(f'{data_atual}')
    print('-'*50)
    time.sleep(1)
    print('Bem-Vindo usuário!!')
    print('-'*50)
    time.sleep(1)
    escolha=input('[1] - login\n[2] - criar conta\n[3] - sair\nescolha: ').strip()
    print('-'*50)
    try:
        escolha=int(escolha)
    except:
        time.sleep(1)
        print('Digite um numero válido.')
        print(f'Você digitou: {escolha}')
        time.sleep(1)
        return main()
    match escolha:
        case 1:
            print('carregando...')
            print('-'*50)
            time.sleep(1)
            return login()
        case 2:
            print('carregando...')
            print('-'*50)
            time.sleep(1)
            return criar()
        case 3:
            exit()
        case _:
            time.sleep(1)
            print(f'digite um número válido.')
            print(f'Você digitou: {escolha}')
            time.sleep(1)
            return main()


def menu():
    print('Bem-Vindo ao menu!')
    print('-'*50)
    escolha=input('[1] - pesquisar artistas\n[2] - pesquisar músicas\n[3] - playlists\n[4] - musicas curtidas/descurtidas\n[5] - sair\nescolha: ').strip()
    print('-'*50)
    try:
        escolha=int(escolha)
    except:
        time.sleep(1)
        print('digite um número válido')
        print('-'*50)
        time.sleep(1)
        print(f'Você digitou: {escolha}')
        print('-'*50)
        time.sleep(1)
        return menu()
    match escolha:
        case 1:
            print('carregando...')
            print('-'*50)
            time.sleep(1)
            return artistas()
        case 2:
            print('carregando...')
            print('-'*50)
            time.sleep(1)
            return musicas()
        case 3:
            print('carregando...')
            print('-'*50)
            time.sleep(1)
            return playlist()
        case 4:
            print('carregando...')
            print('-'*50)
            time.sleep(1)
            return musicascd()
        case 5:
            print('carregando...')
            print('-'*50)
            time.sleep(1)
            return main()
        case _:
            print('Digite um numero válido')
            print('-'*50)
            time.sleep(1)
            return menu()

def artistas():
    escolha=input('[1] - pesquisar artistas\n[2] - sair\nescolha: ').strip()
    print('-'*50)
    try:
        escolha=int(escolha)
    except:
        print('Digite um numero válido')
        print('-'*50)
        time.sleep(1)
        print(f'Você digitou: {escolha}')
        print('-'*50)
        time.sleep(1)
        return artistas()
    match escolha:
        case 1:
            print('Esses são os artistas:')
            print('-'*50)
            time.sleep(1)
            with open('artistas.txt','r',encoding='utf-8') as arquivo:
                lista=arquivo.readlines()
                for linha in lista:
                    nome=linha.split(',')[0]
                    info=linha.split(',')[1]
                    print(nome)
                    time.sleep(0.5)
            print('-'*50)
            artista=input('Pesquisar artistas: ').strip()
            print('-'*50)
            time.sleep(1)
            for linha in lista:
                nome = linha.split(',')[0]
                info = linha.split(',')[1].strip()
                if artista.lower()==nome.lower():
                    print(f'Informação do artista: {nome}')
                    print('-'*50)
                    time.sleep(1)
                    print(info)
                    print('-'*50)
                    time.sleep(1)
                    return menu()
            else:
                print('Artista não encontrado')
                time.sleep(1)
                return artistas()
        case 2:
            print('saindo...')
            time.sleep(1)
            return menu()
        case _:
            print('Digite um número válido')
            print('-'*50)
            time.sleep(1)
            return artistas()
    

def musicas():
    escolha=input('[1] - pesquisar músicas\n[2] - curtir músicas\n[3] - descurtir musicas\n[4] - sair\nescolha:  ').strip()
    try:
        escolha=int(escolha)
    except:
        print('Digite um numero válido')
        print('-'*50)
        time.sleep(1)
        print(f'Você digitou: {escolha}')
        print('-'*50)
        time.sleep(1)
        return musicas()
    match escolha:
        case 1:
            with open('musicas.txt','r',encoding='utf-8') as arquivo:
                lista=arquivo.readlines()
            artistas=set()
            for linha in lista:
                nome = linha.split(';')[1].strip()
                artistas.add(nome)
            print('-'*50)
            print('Artistas cadastrados:')
            print('-'*50)
            for artista in artistas:
                print(artista)
                time.sleep(0.5)
            print('-'*50)
            artista_escolhido=input('Qual artista deseja ver as musicas: ').strip().lower()
            achou=False
            print('-'*50)
            for linha in lista:
                musica=linha.split(';')[0]
                artista=linha.split(';')[1].strip().lower()
                if artista==artista_escolhido:
                    print(musica)
                    time.sleep(0.5)
                    achou=True
            print('-'*50)
            if achou==False:
                print('Artista não encontrado')
            time.sleep(1)
            return menu()
        case 2:
            with open('musicas.txt','r',encoding='utf-8') as arquivo:
                lista=arquivo.readlines()
            print('-'*50)
            print('Músicas disponíveis:')
            print('-'*50)
            achou=False
            for linha in lista:
                musica=linha.split(',')[0]
                print(musica)
                time.sleep(0.5)
            print('-'*50)
            curtir=input('Qual musica quer curtir? ').strip()
            print('-'*50)
            for linha in lista:
                musica = linha.split(',')[0].strip()
                if curtir == musica:
                    achou = True
            if achou == False:
                print('Essa música não existe')
                print('-'*50)
                time.sleep(1)
                return musicas()
            with open('musicas_curtidas.txt','a', encoding='utf-8') as arquivo:
                arquivo.write(curtir + '\n')
            print('Música curtida!')
            print('-'*50)
            time.sleep(1)
            return menu()
        case 3:
            with open('musicas.txt','r',encoding='utf-8') as arquivo:
                lista=arquivo.readlines()
            print('-'*50)
            print('Músicas disponíveis:')
            print('-'*50)
            achou=False 
            for linha in lista:
                musica=linha.split(',')[0]
                print(musica)
                time.sleep(0.5)
            print('-'*50)
            descurtir=input('Qual musica quer descurtir? ').strip()
            print('-'*50)
            for linha in lista:
                musica = linha.split(',')[0].strip()
                if descurtir == musica:
                    achou = True
            if achou == False:
                print('Essa música não existe')
                print('-'*50)
                time.sleep(1)
                return musicas()
            with open('musicas_descurtidas.txt','a', encoding='utf-8') as arquivo:
                arquivo.write(descurtir + '\n')
            print('Música descurtida!')
            print('-'*50)
            time.sleep(1)
            return menu()
        case 4:
            print('saindo...')
            time.sleep(1)
            return menu()
        case _:
            print('Digite um número válido')
            print('-'*50)
            time.sleep(1)
            return musicas()

def playlist():
    print('Área de playlists')
    print('-'*50)
    time.sleep(1)
    escolha=input('[1] - acessar playlists\n[2] - criar playlist\n[3] - editar playlist\n[4] - sair\nescolha: ').strip()
    try:
        escolha=int(escolha)
    except:
        print('Digite um numero válido')
        time.sleep(1)
        return playlist()
    match escolha:
        case 1:
            try:
                with open('playlists.txt','r',encoding='utf-8') as arquivo:
                    linhas=arquivo.readlines()
                if len(linhas)==0:
                    print('Não há playlists')
                    time.sleep(1)
                    return playlist()
                print('-'*50)
                for linha in linhas:
                    print(linha.strip())
                    time.sleep(0.5)
                print('-'*50)
            except:
                print('Não há playlists')
                time.sleep(1)
                return playlist()
            time.sleep(1)
            return menu()
        case 2:
            with open('musicas.txt','r',encoding='utf-8') as arquivo:
                musicas=arquivo.readlines()
            artistas=set()
            for linha in musicas:
                artistas.add(linha.split(';')[1].strip())
            print('-'*50)
            for a in artistas:
                print(a)
                time.sleep(0.5)
            print('-'*50)
            artista=input('Digite o artista: ').strip().lower()
            achou=False
            musicas_artista=[]
            print('-'*50)
            for linha in musicas:
                nome_musica=linha.split(';')[0].split(',')[0]
                nome_artista=linha.split(';')[1].strip().lower()
                if nome_artista==artista:
                    print(nome_musica)
                    time.sleep(0.5)
                    musicas_artista.append(nome_musica)
                    achou=True
            print('-'*50)
            if achou==False:
                print('Artista não encontrado')
                time.sleep(1)
                return playlist()
            nome_playlist=input('Nome da playlist: ').strip()
            selecionadas=[]
            print('Digite as músicas (0 para sair)')
            while True:
                m=input('Música: ').strip()
                if m=='0':
                    break
                if m in musicas_artista:
                    selecionadas.append(m)
                else:
                    print('Música não existe')
            if len(selecionadas)==0:
                print('Nenhuma música adicionada')
                time.sleep(1)
                return playlist()
            with open('playlists.txt','a',encoding='utf-8') as arquivo:
                arquivo.write(nome_playlist+': '+', '.join(selecionadas)+'\n')
            print('Playlist criada')
            time.sleep(1)
            return menu()
        case 3:
            try:
                with open('playlists.txt','r',encoding='utf-8') as arquivo:
                    linhas=arquivo.readlines()
                if len(linhas)==0:
                    print('Não há playlists')
                    time.sleep(1)
                    return playlist()
            except:
                print('Não há playlists')
                time.sleep(1)
                return playlist()
            print('-'*50)
            for linha in linhas:
                print(linha.strip())
                time.sleep(0.5)
            print('-'*50)
            nome_escolhido=input('Digite o nome da playlist: ').strip()
            indice=-1
            for i in range(len(linhas)):
                if linhas[i].split(':')[0]==nome_escolhido:
                    indice=i
            if indice==-1:
                print('Playlist não encontrada')
                time.sleep(1)
                return playlist()
            escolha_edit=input('[1] - apagar playlist\n[2] - adicionar músicas\nescolha: ').strip()
            if escolha_edit=='1':
                linhas.pop(indice)
                with open('playlists.txt','w',encoding='utf-8') as arquivo:
                    arquivo.writelines(linhas)
                print('Playlist apagada')
                time.sleep(1)
                return menu()
            if escolha_edit=='2':
                base=linhas[indice].strip()
                nome=base.split(':')[0]
                musicas_existentes=base.split(':')[1].split(', ')
                with open('musicas.txt','r',encoding='utf-8') as arquivo:
                    musicas=arquivo.readlines()
                print('Digite músicas para adicionar (0 para sair)')
                while True:
                    m=input('Música: ').strip()
                    if m=='0':
                        break
                    existe=False
                    for linha in musicas:
                        nome_musica=linha.split(';')[0].split(',')[0]
                        if nome_musica==m:
                            existe=True
                    if existe and m not in musicas_existentes:
                        musicas_existentes.append(m)
                    else:
                        print('Música inválida ou já existe')
                linhas[indice]=nome+': '+', '.join(musicas_existentes)+'\n'
                with open('playlists.txt','w',encoding='utf-8') as arquivo:
                    arquivo.writelines(linhas)
                print('Playlist atualizada')
                time.sleep(1)
                return menu()
            print('Opção inválida')
            time.sleep(1)
            return playlist()
        case 4:
            print('saindo...')
            time.sleep(1)
            return menu()
        case _:
            print('Digite um número válido')
            time.sleep(1)
            return playlist()

def musicascd():
    escolha=input('[1] - músicas curtidas\n[2] - músicas descurtidas\n[3] - sair\nescolha: ').strip()
    print('-'*50)
    try:
        escolha=int(escolha)
    except:
        print('Digite um numero válido')
        print('-'*50)
        time.sleep(1)
        print(f'Você digitou: {escolha}')
        print('-'*50)
        time.sleep(1)
        return musicascd()
    match escolha:
        case 1:
            print('Musicas descurtidas')
            print('-'*50)
            with open('musicas_curtidas.txt','r') as arquivo:
                lista=arquivo.readlines()
                for musica in lista:
                    print(musica)
                    time.sleep(0.3)
            print('-'*50)
            return musicascd()
        case 2:
            print('Musicas descurtidas')
            print('-'*50)
            with open('musicas_descurtidas.txt','r') as arquivo:
                lista=arquivo.readlines()
                for musica in lista:
                    print(musica)
                    time.sleep(0.3)
            print('-'*50)
            return musicascd()
        case 3:
            print('saindo...')
            print('-'*50)
            time.sleep(1)
            return menu()
        case _:
            print('Digite um número válido')
            print('-'*50)
            time.sleep(1)
            return musicascd()

if __name__ == "__main__":
    main()

