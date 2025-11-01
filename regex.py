import sys
import re


def main():
    """
    Script para verificar a lógica de um arquivo de entrada
    contra uma expressão regular do Python.
    """

    # 1. Verificar se os argumentos estão corretos
    if len(sys.argv) != 3:
        print("Uso: python verificar_logica.py \"<regex_python>\" <arquivo_palavra.txt>")
        print("Exemplo: python verificar_logica.py \"[234]*\" w8.txt")
        print("\nAtenção: Coloque a expressão regular entre ASPAS DUPLAS.")
        sys.exit(1)

    regex_pattern = sys.argv[1]
    input_filepath = sys.argv[2]

    try:
        # 2. Compilar a expressão regular
        pattern = re.compile(regex_pattern)

        # 3. Ler o arquivo de palavra (w8.txt, etc.)
        with open(input_filepath, 'r') as f:
            input_word = f.read().strip()

        output_matrix = ""

        # 4. Processar a palavra
        #    Divide a palavra inteira em linhas (separadas por 'N')
        linhas = input_word.split('N')

        for linha in linhas:
            # Remove linhas vazias (pode acontecer no final do arquivo)
            if not linha:
                continue

            # Divide a linha em células (separadas por '.')
            celulas = linha.split('.')

            linha_de_saida = ""
            for celula in celulas:
                # Remove células vazias (ex: se a linha termina com '.')
                if not celula:
                    continue

                # 5. O TESTE LÓGICO:
                #    re.fullmatch() verifica se a string 'celula' inteira
                #    corresponde ao padrão, do início ao fim.
                if pattern.fullmatch(celula):
                    linha_de_saida += "1"
                else:
                    linha_de_saida += "0"

            output_matrix += linha_de_saida + "\n"

        # 6. Imprimir a matriz binária resultante
        print(output_matrix.strip())

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado - {input_filepath}", file=sys.stderr)
    except re.error as e:
        print(f"Erro na sua expressão regular: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()