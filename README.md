# CLI de Filmes — SQLite e Python

Programa desenvolvido em Python com banco de dados SQLite que permite gerenciar uma lista de filmes de forma simples, com operações de inserção, exclusão, listagem, busca e filtragem via terminal.

## Tecnologias

- Python 3
- SQLite3 (nativo do Python)

## Funcionalidades

- Inserir novo filme (título, ano opcional, gênero, diretor, nota opcional)
- Excluir filme por ID
- Listar todos os filmes cadastrados
- Buscar filme por título
- Filtrar filmes por gênero, nota mínima e/ou diretor

## Como rodar

### Pré-requisitos

- Python 3 instalado

### Passos

1. Clone o repositório

```bash
git clone git@github.com:babaleca/CLI-de-filmes.git
```

2. Entre na pasta

```bash
cd CLI-de-filmes
```

3. Rode o programa

```bash
python filmes.py [comando]
```

## Comandos

| Comando | Descrição | Exemplo |
|--------|-----------|---------|
| `adicionar` | Adiciona um filme | `python filmes.py adicionar "Inception" 2010 "Ficcao Cientifica" "Nolan" 9.0` |
| `listar` | Lista todos os filmes | `python filmes.py listar` |
| `buscar` | Busca por título | `python filmes.py buscar "Inception"` |
| `remover` | Remove por ID | `python filmes.py remover 1` |
| `filtrar` | Filtra por critérios | `python filmes.py filtrar GENERO="Drama" NOTA_MIN=8.0` |

## Contexto

Projeto desenvolvido por Bárbara Bandarra com parte de um plano de estudos com foco em Python, SQL e estruturas de dados.