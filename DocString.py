# DocString
# Comentários são sempre ignorados, docstring não.
# 3 " ou 3 ' 

class Pessoa:
    """
    Representa uma pessoa com nome e idade.
    Atributos:
        nome (str): O nome da pessoa.
        idade (int): A idade da pessoa.
    """
    def __init__(self, nome, idade):
        """Inicializa uma nova instância de Pessoa."""
        self.nome = nome
        self.idade = idade


"""
Uma docstring (abreviação de documentation string) em Python é uma string usada para documentar módulos, classes, funções ou métodos. Ela fornece uma explicação sobre o que o código faz, como deve ser usado e, às vezes, exemplos de uso.

Características principais:
Delimitação: É definida usando aspas triplas no início de uma função, classe ou módulo.
Disponibilidade em tempo de execução: Pode ser acessada pelo atributo __doc__.

Boas práticas:
Clareza: Descreva o objetivo da função/classe/módulo de forma simples e direta.
Consistência: Use um formato padrão, como o estilo Google, reStructuredText ou NumPy/SciPy.
Documente argumentos e retornos: Explique os parâmetros e o que a função retorna.
As docstrings tornam seu código mais legível e ajudam outras pessoas (ou você mesmo no futuro) a entender rapidamente o que foi implementado.
"""