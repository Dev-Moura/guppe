# 🐍 Guppe — Programação em Python: Essencial

> Repositório de estudos do curso **Programação em Python: Essencial** da Geek University.
> Contém **125 arquivos Python** organizados em **21 módulos** (Módulos 2 a 22), cobrindo desde fundamentos até tópicos avançados como POO, concorrência e tipagem estática.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Módulo_22_Completo-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Estudos-blue?style=for-the-badge)

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Progresso por Módulo](#-progresso-por-módulo)
  - [Módulo 2 — Introdução ao Python](#módulo-2--introdução-ao-python)
  - [Módulo 3 — Variáveis e Tipos de Dados](#módulo-3--variáveis-e-tipos-de-dados)
  - [Módulo 4 — Estruturas Condicionais](#módulo-4--estruturas-condicionais)
  - [Módulo 5 — Estruturas de Repetição](#módulo-5--estruturas-de-repetição)
  - [Módulo 6 — Coleções](#módulo-6--coleções)
  - [Módulo 7 — Funções](#módulo-7--funções)
  - [Módulo 8 — Comprehensions](#módulo-8--comprehensions)
  - [Módulo 9 — Funções Built-in e Lambdas](#módulo-9--funções-built-in-e-lambdas)
  - [Módulo 10 — Tratamento de Erros](#módulo-10--tratamento-de-erros)
  - [Módulo 11 — Módulos e Pacotes](#módulo-11--módulos-e-pacotes)
  - [Módulo 12 — Manipulação de Arquivos](#módulo-12--manipulação-de-arquivos)
  - [Módulo 13 — Iteradores e Geradores](#módulo-13--iteradores-e-geradores)
  - [Módulo 14 — Decoradores](#módulo-14--decoradores)
  - [Módulo 15 — POO (Parte 1)](#módulo-15--poo-parte-1)
  - [Módulo 16 — POO (Parte 2)](#módulo-16--poo-parte-2)
  - [Módulo 17 — Manipulação de CSV, Pickle e JSON](#módulo-17--manipulação-de-csv-pickle-e-json)
  - [Módulo 18 — Data e Hora](#módulo-18--data-e-hora)
  - [Módulo 19 — Testes](#módulo-19--testes)
  - [Módulo 20 — Concorrência e Paralelismo](#módulo-20--concorrência-e-paralelismo)
  - [Módulo 21 — Tipagem e Type Hinting](#módulo-21--tipagem-e-type-hinting)
  - [Módulo 22 — Novidades do Python 3.8+](#módulo-22--novidades-do-python-38)
- [Como Executar](#-como-executar)

---

## 🔭 Visão Geral

Este repositório documenta toda a minha jornada de aprendizado em Python, partindo dos conceitos mais básicos (tipos de dados, variáveis) até tópicos avançados (decoradores, concorrência, tipagem estática). Cada módulo corresponde a uma seção do curso, com múltiplos arquivos contendo **teoria em docstrings** e **código prático** com exemplos funcionais.

---

## 🛠 Tecnologias

| Ferramenta | Descrição |
|---|---|
| **Python 3.12+** | Linguagem principal |
| **uv** | Gerenciador de pacotes e ambientes virtuais |
| **jsonpickle** | Serialização JSON de objetos Python |
| **mypy** | Verificador de tipos estáticos |
| **textblob** | Processamento de linguagem natural |
| **passlib** | Hashing de senhas (usado no módulo 15) |

---

## 📁 Estrutura do Projeto

```
guppe/
├── modulo_2/            # Introdução ao Python (3 arquivos)
├── modulo_3/            # Variáveis e Tipos de Dados (5 arquivos)
├── modulo_4/            # Estruturas Condicionais (2 arquivos)
├── modulo_5/            # Estruturas de Repetição (4 arquivos)
├── modulo_6/            # Coleções (12 arquivos)
├── modulo_7/            # Funções (8 arquivos)
├── modulo_8/            # Comprehensions (5 arquivos)
├── modulo_9/            # Funções Built-in e Lambdas (10 arquivos)
├── modulo_10/           # Tratamento de Erros (5 arquivos)
├── modulo_11/           # Módulos e Pacotes (8 arquivos)
├── modulo_12/           # Manipulação de Arquivos (8 arquivos)
├── modulo_13/           # Iteradores e Geradores (6 arquivos)
├── modulo_14/           # Decoradores (5 arquivos)
├── modulo_15/           # POO - Parte 1 (9 arquivos)
├── modulo_16/           # POO - Parte 2 (7 arquivos)
├── modulo_17/           # CSV, Pickle e JSON (5 arquivos)
├── modulo_18/           # Data e Hora (3 arquivos)
├── modulo_19/           # Testes (3 arquivos)
├── modulo_20/           # Concorrência e Paralelismo (4 arquivos)
├── modulo_21/           # Tipagem e Type Hinting (7 arquivos)
├── modulo_22/           # Novidades do Python 3.8+ (5 arquivos)
├── pyproject.toml       # Configuração do projeto
└── README.md            # Este arquivo
```

---

## 📚 Progresso por Módulo

### Módulo 2 — Introdução ao Python
> ✅ **Concluído** · 3 arquivos

| Arquivo | Tópico |
|---|---|
| `pep8.py` | Convenções PEP 8 — CamelCase para classes, snake_case para funções/variáveis, indentação com 4 espaços, organização de imports |
| `dir_e_help.py` | Utilitários `dir()` e `help()` para introspecção de tipos e objetos |
| `recebendo_dados_usuario.py` | Entrada de dados com `input()`, f-strings, casting de tipos, evolução do `print()` (2.x → 3.x → 3.7+) |

**Conceitos-chave:** The Zen of Python (`import this`), PEP 8, entrada/saída de dados, type casting.

---

### Módulo 3 — Variáveis e Tipos de Dados
> ✅ **Concluído** · 5 arquivos

| Arquivo | Tópico |
|---|---|
| `tipo_string.py` | Strings — `upper()`, `lower()`, `split()`, slicing, `replace()`, palíndromos |
| `tipo_numerico.py` | Tipo `int` — operações básicas com inteiros |
| `tipo_float.py` | Tipo `float` — decimais, conversão float→int, números complexos (`5j`) |
| `tipo_booleano.py` | Tipo `bool` — operadores `not`, `or`, `and`, Álgebra Booleana |
| `escopo_de_variaveis.py` | Escopo global vs. local, tipagem dinâmica do Python |

**Conceitos-chave:** Tipagem dinâmica/fraca, mutabilidade, comparação com Java/C.

---

### Módulo 4 — Estruturas Condicionais
> ✅ **Concluído** · 2 arquivos

| Arquivo | Tópico |
|---|---|
| `if_else_elif.py` | Estruturas `if`, `elif`, `else` — comparação sintática com Java |
| `and_or_not_is.py` | Operadores lógicos — `and`, `or`, `not`, `is` (unários vs. binários) |

**Conceitos-chave:** Controle de fluxo, operadores unários vs. binários.

---

### Módulo 5 — Estruturas de Repetição
> ✅ **Concluído** · 4 arquivos

| Arquivo | Tópico |
|---|---|
| `loop_for.py` | Loop `for` — iteração em strings, listas, ranges, `enumerate()`, loops aninhados |
| `loop_while.py` | Loop `while` — critério de parada, comparação com `do-while` de C/Java |
| `break.py` | Instrução `break` para interrupção de loops |
| `entendendo_explorando_range.py` | Função `range()` — `start`, `stop`, `step` |

**Conceitos-chave:** Iteração, `enumerate()`, descarte de variáveis com `_`, emojis em loops 😍.

---

### Módulo 6 — Coleções
> ✅ **Concluído** · 12 arquivos

O módulo mais extenso do curso, cobrindo todas as estruturas de dados fundamentais do Python.

| Arquivo | Tópico |
|---|---|
| `listas.py` | Listas — `append`, `extend`, `insert`, `pop`, `sort`, `reverse`, slicing, deep/shallow copy, `sum`, `max`, `min`, `len`, desempacotamento |
| `tuplas.py` | Tuplas — imutabilidade, desempacotamento, `count()`, `index()`, concatenação |
| `dicionarios.py` | Dicionários — `get()`, `update()`, `pop()`, `del`, `fromkeys()`, tuplas como chaves |
| `conjuntos.py` | Sets — `add`, `remove`, `discard`, `union`, `intersection`, `difference`, operadores `\|` e `&` |
| `mapas.py` | Mapas — estruturas de mapeamento |
| `none.py` | O tipo `None` em Python |
| `counter.py` | `collections.Counter` — contagem de ocorrências, `most_common()` |
| `default_dict.py` | `collections.defaultdict` — dicionários com valores padrão |
| `deque.py` | `collections.deque` — fila de duas pontas |
| `ordered_dict.py` | `collections.OrderedDict` — dicionários ordenados |
| `named_tuple.py` | `collections.namedtuple` — tuplas nomeadas com acesso por atributo |
| `exercicio_modulo_6.py` | Exercício prático de consolidação |

**Conceitos-chave:** Deep copy vs. shallow copy, teoria dos conjuntos, módulo `collections`, carrinho de compras com dicionários.

---

### Módulo 7 — Funções
> ✅ **Concluído** · 8 arquivos

| Arquivo | Tópico |
|---|---|
| `definindo_funcoes.py` | Definição de funções — `def`, DRY, funções como objetos de primeira classe |
| `funcoes_com_parametro.py` | Funções com parâmetros — passagem de argumentos |
| `funcoes_com_parametro_padrao.py` | Parâmetros com valores padrão |
| `funcoes_com_retorno.py` | Funções com `return` |
| `funcao_com_retorno.py` | Retorno de valores em funções |
| `args._funcoes.py` | `*args` — empacotamento de argumentos em tupla |
| `kwargs_funcoes.py` | `**kwargs` — empacotamento em dicionário, ordem de parâmetros, desempacotamento |
| `docstrings_funcoes.py` | Documentação de funções com docstrings |

**Conceitos-chave:** `*args` e `**kwargs`, ordem obrigatória de parâmetros, desempacotamento de listas/tuplas/dicionários com `*` e `**`.

---

### Módulo 8 — Comprehensions
> ✅ **Concluído** · 5 arquivos

| Arquivo | Tópico |
|---|---|
| `list_comprehension_p1.py` | List comprehension — sintaxe, funções dentro de comprehensions, comparação com loops |
| `list_comprehension_p2.py` | List comprehension avançado — filtros com condicionais |
| `dictionary_comprehension.py` | Dict comprehension |
| `set_comprehension.py` | Set comprehension |
| `nested_list.py` | Listas aninhadas e comprehensions aninhadas |

**Conceitos-chave:** `[expr for item in iterável]`, comprehensions com filtros, comprehensions aninhadas.

---

### Módulo 9 — Funções Built-in e Lambdas
> ✅ **Concluído** · 10 arquivos

| Arquivo | Tópico |
|---|---|
| `lambdas.py` | Expressões lambda — funções anônimas, múltiplas entradas, geradoras de funções quadráticas |
| `map.py` | `map()` — aplicação de funções a iteráveis |
| `filter.py` | `filter()` — filtragem de elementos |
| `reduce.py` | `functools.reduce()` — redução de iteráveis |
| `sorted.py` | `sorted()` — ordenação com `key` e `reverse` |
| `reversed.py` | `reversed()` — inversão de sequências |
| `zip.py` | `zip()` — combinação de iteráveis |
| `len_abs_sum_round.py` | `len()`, `abs()`, `sum()`, `round()` |
| `anyAndAll.py` | `any()` e `all()` — verificações booleanas |
| `generator.py` | Generator expressions |

**Conceitos-chave:** Programação funcional, funções de alta ordem, sorting com lambdas por sobrenome.

---

### Módulo 10 — Tratamento de Erros
> ✅ **Concluído** · 5 arquivos

| Arquivo | Tópico |
|---|---|
| `try_except.py` | Blocos `try/except` — tratamento genérico vs. específico, `as err` |
| `try_except_else_finally.py` | Blocos `else` e `finally` |
| `raise.py` | Levantamento de exceções com `raise` |
| `erros_mais_comuns.py` | `NameError`, `TypeError`, `IndexError`, `KeyError`, `ValueError`, etc. |
| `debugando_com_pdb.py` | Debugging com `pdb` — breakpoints, step, next, continue |

**Conceitos-chave:** Hierarquia de exceções, boas práticas de tratamento de erros, depuração interativa.

---

### Módulo 11 — Módulos e Pacotes
> ✅ **Concluído** · 8 arquivos

| Arquivo | Tópico |
|---|---|
| `modulos_built_in.py` | Módulos integrados do Python |
| `modulos_customizados.py` | Criação e importação de módulos próprios |
| `modulos_externos.py` | Instalação e uso de módulos externos (`pip`) |
| `modulo_random.py` | Módulo `random` — `random()`, `choice()`, `randint()`, `shuffle()` |
| `dunder_main_dunder_name.py` | `__name__` e `__main__` — execução condicional |
| `pacotes.py` | Organização em pacotes com `__init__.py` |
| `primeiro.py` / `segundo.py` | Módulos auxiliares para testes de importação |

**Conceitos-chave:** `import`, `from ... import`, aliases com `as`, `if __name__ == '__main__'`.

---

### Módulo 12 — Manipulação de Arquivos
> ✅ **Concluído** · 8 arquivos

| Arquivo | Tópico |
|---|---|
| `file_reading.py` | Leitura de arquivos com `open()` e `read()`, modos de abertura (`r`, `w`, `x`, `a`, `b`, `t`) |
| `escrevendo_em_arquivos.py` | Escrita em arquivos |
| `modos_aberturas_arquivos.py` | Modos de abertura detalhados |
| `seek_and_cursors.py` | Manipulação de cursor com `seek()` e `tell()` |
| `bloco_with.py` | Context manager `with` para gerenciamento automático de recursos |
| `sistema_de_arquivos_navegação.py` | Navegação no sistema de arquivos com `os` e `os.path` |
| `sistema_de_arquivos_manipulacao.py` | Manipulação de arquivos/diretórios — criar, mover, copiar, deletar |
| `stringIO.py` | `io.StringIO` — arquivos em memória |

**Conceitos-chave:** Context managers, cursor de arquivo, `os.path`, `StringIO`.

---

### Módulo 13 — Iteradores e Geradores
> ✅ **Concluído** · 6 arquivos

| Arquivo | Tópico |
|---|---|
| `iterators_e_iterables.py` | Diferença entre `iterator` e `iterable`, `iter()`, `next()` |
| `geradores.py` | Generator functions — `yield` vs. `return`, comparação com funções normais |
| `iterador_customizado.py` | Criação de iteradores personalizados com `__iter__` e `__next__` |
| `criando_proprio_loop.py` | Implementação de um loop customizado |
| `teste_memoria_generators.py` | Benchmark de memória — generators vs. listas |
| `teste_velocidade_generator.py` | Benchmark de velocidade — generators vs. listas |

**Conceitos-chave:** Lazy evaluation, eficiência de memória com generators, protocolo de iteração.

---

### Módulo 14 — Decoradores
> ✅ **Concluído** · 5 arquivos

| Arquivo | Tópico |
|---|---|
| `funcoes_de_grandeza.py` | Higher Order Functions (HOF) — nested functions, closures, funções retornando funções |
| `decoradores.py` | Decorators — sintaxe manual e syntax sugar com `@`, exemplo de autenticação |
| `decoradores_assinatura.py` | Decoradores com preservação de assinatura |
| `metadada_wraps.py` | `functools.wraps` — preservação de metadados |
| `forçando_tipos.py` | Decorador para validação de tipos |

**Conceitos-chave:** Closures, `@decorator`, `functools.wraps`, HOF, first-class functions.

---

### Módulo 15 — POO (Parte 1)
> ✅ **Concluído** · 9 arquivos

| Arquivo | Tópico |
|---|---|
| `poo.py` | Introdução à POO — classes, atributos, métodos, construtores, objetos |
| `classes.py` | Definição de classes — `class`, CamelCase, entidades, `pass` |
| `atributos.py` | Atributos de instância e de classe |
| `metodos.py` | Métodos de instância, `@classmethod`, `@staticmethod`, `__init__`, criptografia de senhas com `passlib` |
| `objetos.py` | Instanciação de objetos |
| `abstracao_encapsulamento.py` | Abstração e encapsulamento — atributos privados com `__`, classe `Conta` (extrato, depósito, saque, transferência) |
| `exercicio1.py` | Exercício prático 1 |
| `exercicio2.py` | Exercício prático 2 |
| `exercicio3.py` | Exercício prático 3 |

**Conceitos-chave:** `self`, `__init__`, name mangling (`__atributo`), `@classmethod` vs `@staticmethod`, encapsulamento.

---

### Módulo 16 — POO (Parte 2)
> ✅ **Concluído** · 7 arquivos

| Arquivo | Tópico |
|---|---|
| `heranca.py` | Herança — `super()`, sobrescrita de métodos (overriding), classes `Pessoa`, `Cliente`, `Funcionario` |
| `heranca_multipla.py` | Herança múltipla em Python |
| `mro_method_resolution_order.py` | MRO — ordem de resolução de métodos |
| `metodo_super.py` | Uso do método `super()` |
| `polimorfismo.py` | Polimorfismo — `Animal`, `Cachorro`, `Gato`, `Rato` com `NotImplementedError` |
| `propriedades.py` | Properties — `@property`, `@setter`, getter/setter Pythônico vs. estilo Java |
| `metodos_magicos.py` | Métodos mágicos (dunder) — `__repr__`, `__str__`, `__len__`, `__del__`, `__add__`, `__mul__` |

**Conceitos-chave:** Herança, polimorfismo, MRO, properties, dunder methods, design patterns OOP.

---

### Módulo 17 — Manipulação de CSV, Pickle e JSON
> ✅ **Concluído** · 5 arquivos

| Arquivo | Tópico |
|---|---|
| `lendo_csv.py` | Leitura de CSV com `csv.reader` e `csv.DictReader` |
| `escrevendo_no_csv.py` | Escrita em arquivos CSV |
| `conhecendo_pickle.py` | Módulo `pickle` — serialização/deserialização binária de objetos |
| `json_pickle.py` | Serialização JSON com `jsonpickle` |
| `lutadores.csv` | Dataset de exemplo para exercícios |

**Conceitos-chave:** Serialização, CSV, pickle (binário), JSON, persistência de dados.

---

### Módulo 18 — Data e Hora
> ✅ **Concluído** · 3 arquivos

| Arquivo | Tópico |
|---|---|
| `manipulando_data_hora.py` | Módulo `datetime` — `datetime.now()`, `replace()`, acesso individual (year, month, day, etc.) |
| `metodos_data_horas.py` | Métodos de formatação — `strftime()`, `strptime()` |
| `trabalhando_deltas_de_data_hora.py` | `timedelta` — aritmética com datas |

**Conceitos-chave:** `datetime`, `timedelta`, formatação e parsing de datas.

---

### Módulo 19 — Testes
> ✅ **Concluído** · 3 arquivos

| Arquivo | Tópico |
|---|---|
| `por_que_testar_codigo.py` | Importância dos testes, introdução ao TDD (Red → Green → Refactor) |
| `assertion.py` | `assert` — afirmações para validação, mensagens customizadas, cuidados com `-O` |
| `docstests.py` | Doctests — testes dentro de docstrings, `python -m doctest -v`, TDD na prática |

**Conceitos-chave:** TDD, `assert`, doctests, testes como documentação.

---

### Módulo 20 — Concorrência e Paralelismo
> ✅ **Concluído** · 4 arquivos

| Arquivo | Tópico |
|---|---|
| `alocacao_e_gerencia_memoria.py` | Annotations, tipagem em classes, gerenciamento de memória |
| `single_thread.py` | Execução single-threaded — benchmark (≈7.18s) |
| `multi_thread.py` | Multi-threading com `threading.Thread` — benchmark (≈7.16s, limitado pelo GIL) |
| `multi_processing.py` | Multi-processing com `multiprocessing.Pool` — benchmark (≈3.78s, bypass do GIL) |

**Conceitos-chave:** GIL (Global Interpreter Lock), `threading` vs. `multiprocessing`, paralelismo real com processos.

---

### Módulo 21 — Tipagem e Type Hinting
> ✅ **Concluído** · 7 arquivos

| Arquivo | Tópico |
|---|---|
| `tipagemDinamica.py` | Tipagem dinâmica do Python |
| `duck_typing.py` | Duck typing — "se anda como um pato..." |
| `type_hinting.py` | Type hints (PEP 484) — anotações de tipos em funções |
| `tipos_e_comentários.py` | Comentários de tipo |
| `tipos_dados_na_pratica.py` | Tipos de dados na prática |
| `annotations.py` | Annotations em variáveis e classes |
| `jogo_de_cartasv2.py` | Projeto prático com tipagem — jogo de cartas |

**Conceitos-chave:** Type hints, duck typing, `mypy`, tipagem estática vs. dinâmica.

---

### Módulo 22 — Novidades do Python 3.8+
> ✅ **Concluído** · 5 arquivos

| Arquivo | Tópico |
|---|---|
| `walrus.py` | Operador walrus (`:=`) — atribuição e retorno em uma expressão (Python 3.8+) |
| `argumentos_somente_posicionais.py` | Argumentos posicionais (`/`) e nomeados (`*`) — PEP 570 |
| `dados_precisos.py` | `Literal`, `Union`, `Final`, `TypedDict`, `Protocol` do módulo `typing` |
| `matemática_estatísticas.py` | `math.prod`, `math.isqrt`, `math.dist`, `math.hypot`, `statistics.fmean`, `statistics.geometric_mean`, `statistics.multimode` |
| `debugger_Fstrings.py` | Debugging com f-strings (`f"{var=}"`) |

**Conceitos-chave:** Walrus operator, positional-only parameters, novos tipos do `typing`, funções matemáticas e estatísticas avançadas.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (gerenciador de pacotes)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Dev-Moura/guppe.git
cd guppe

# Instale as dependências com uv
uv sync
```

### Execução

```bash
# Executar qualquer arquivo de módulo
uv run python modulo_3/tipo_string.py

# Executar doctests
uv run python -m doctest -v modulo_19/docstests.py

# Verificar tipos com mypy
uv run mypy modulo_21/
```

---

## 📊 Resumo do Progresso

| Módulo | Tema | Arquivos | Status |
|:---:|---|:---:|:---:|
| 2 | Introdução ao Python | 3 | ✅ |
| 3 | Variáveis e Tipos de Dados | 5 | ✅ |
| 4 | Estruturas Condicionais | 2 | ✅ |
| 5 | Estruturas de Repetição | 4 | ✅ |
| 6 | Coleções | 12 | ✅ |
| 7 | Funções | 8 | ✅ |
| 8 | Comprehensions | 5 | ✅ |
| 9 | Funções Built-in e Lambdas | 10 | ✅ |
| 10 | Tratamento de Erros | 5 | ✅ |
| 11 | Módulos e Pacotes | 8 | ✅ |
| 12 | Manipulação de Arquivos | 8 | ✅ |
| 13 | Iteradores e Geradores | 6 | ✅ |
| 14 | Decoradores | 5 | ✅ |
| 15 | POO — Parte 1 | 9 | ✅ |
| 16 | POO — Parte 2 | 7 | ✅ |
| 17 | CSV, Pickle e JSON | 5 | ✅ |
| 18 | Data e Hora | 3 | ✅ |
| 19 | Testes | 3 | ✅ |
| 20 | Concorrência e Paralelismo | 4 | ✅ |
| 21 | Tipagem e Type Hinting | 7 | ✅ |
| 22 | Novidades do Python 3.8+ | 5 | ✅ |
| | **Total** | **125** | **21/21** |

