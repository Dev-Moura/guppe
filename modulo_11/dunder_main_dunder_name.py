"""
Dunder Name e Dunder Main

Dunder -> Doble Under -> _

Dunder Name -> __name__

Dunder Main -> __main__

Em python, são utilizados Dunder para criar funções, atributos, e propriedades e etc utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:

int main(){
    printf("Hello World");
    return 0;
}



# Na linguagem na Java, temos um programa da seguinte forma:

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}


# Em python, se executarmos um módulo Python diretamente na linha de comnando, internamente
# o Python atribui a variável __name__ o valor __main__. Isso significa que quando um módulo é executado
# diretamente, o código dentro do bloco if __name__ == "__main__": será executado. No entanto, se o módulo 
# for importado por outro módulo, o valor de __name__ será o nome do módulo e o código dentro do bloco
# if __name__ == "__main__": não será executado.


Main -> significa principal.

"""
import primeiro
import segundo





