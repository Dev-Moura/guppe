"""
Decoradores (Descoretors)

O que sao decorators?

- Decorators sao funçoes;
- Decorators envolvem outras funcoes e aprimoram seus comportamentos;
- Decorators tambem sao exemplos de HOF;
- Decorators tem uma sintaxe propria, usnado "@" (Syntact sugar / sintaxe bonita)

  /------------------------------------------------/
 /           Function decorators                  /
/------------------------------------------------/

========================================================

"""

# Decorators como funçoes (sintaxe nao recomendada)

def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer voce!")
        funcao()
        print("Tenha um otimo dia")
    return sendo

def saudacao():
    print("seja bem-vindo(a) a Geek unniversity")

teste = seja_educado(saudacao)

teste()


def raiva():
    print('EU TE ODEIO!')

raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorator com Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer voce!")
        funcao()
        print("Tenha um otimo dia")
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print("Meu nome e Michael")

apresentando()

@seja_educado_mesmo
def dormir():
    print("quero dormir...")

dormir()

# Exemplo, nao e codigo funcional

def checa_login(request):
    if not request.user:
        redirect("http://www.suaempresa.com.br")

def home(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login
def admin(request):
    return 'Pode acessar admin'