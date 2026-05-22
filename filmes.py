import sys
from database import criar_tabela, adicionar_filme, listar_filmes, remover_filme, buscar_filme_por_titulo, filtrar_filmes 

def main():
    criar_tabela()

    if len(sys.argv) < 2:
        print("USO: faltou algum argumento no seu prompt, ordem = filmes.py [comando]")
        print("COMANDOS: adicionar, listar, remover, buscar, filtrar")
        return
    
    comando = sys.argv[1]

    if comando == "listar":
        filmes = listar_filmes()
        if not filmes:
            print("Nenhum filme cadastrado!")
        else:
            for FILME in filmes:
                print(f"ID: {FILME[0]}, Título: {FILME[1]}, Ano: {FILME[2]}, Gênero: {FILME[3]}, Diretor: {FILME[4]}, Nota: {FILME[5]}")

    elif comando == "adicionar":
        if len(sys.argv) < 5:
            print("USO: faltum algum parametro no filme que deseja adicionar, ordem = filmes.py adicionar [TITULO] [ANO-opcional] [GENERO] [DIRETOR] [NOTA-opcional]")
            return
        TITULO = sys.argv[2]
        ANO = int(sys.argv[3]) if len(sys.argv) > 3 else None
        GENERO = sys.argv[4]
        DIRETOR = sys.argv[5]
        NOTA = float(sys.argv[6]) if len(sys.argv) > 6 else None
        adicionar_filme(TITULO, ANO, GENERO, DIRETOR, NOTA)
        print(f"Filme '{TITULO}' adicionado!")

    elif comando == "remover":
        if len(sys.argv) < 3:
            print("USO: faltum algum parametro no filme que deseja remover, ordem = filmes.py remover [ID]")
            return
        ID = int(sys.argv[2])
        remover_filme(ID)
        print(f"Filme com ID {ID} removido!")

    elif comando == "buscar":
        if len(sys.argv) < 3:
            print("USO: faltum algum parametro no filme que deseja buscar, ordem = filmes.py buscar [TITULO]")
            return
        TITULO = sys.argv[2]
        filmes = buscar_filme_por_titulo(TITULO)
        if not filmes:
            print(f"Nenhum filme encontrado com o título '{TITULO}'!")
        else:
            for FILME in filmes:
                print(f"ID: {FILME[0]}, Título: {FILME[1]}, Ano: {FILME[2]}, Gênero: {FILME[3]}, Diretor: {FILME[4]}, Nota: {FILME[5]}")
        
    elif comando == "filtrar":
        GENERO = None
        NOTA_MIN = None
        DIRETOR = None

        for arg in sys.argv[2:]:
            if arg.startswith("GENERO="):
                GENERO = arg.split("=", 1)[1]
            elif arg.startswith("NOTA_MIN="):
                NOTA_MIN = float(arg.split("=", 1)[1])
            elif arg.startswith("DIRETOR="):
                DIRETOR = arg.split("=", 1)[1]

        filmes = filtrar_filmes(GENERO, NOTA_MIN, DIRETOR)
        if not filmes:
            print("Nenhum filme encontrado com esses filtros!")
        else:
            for FILME in filmes:
                print(f"ID: {FILME[0]}, Título: {FILME[1]}, Ano: {FILME[2]}, Gênero: {FILME[3]}, Diretor: {FILME[4]}, Nota: {FILME[5]}")

if __name__ == "__main__":
    main()
