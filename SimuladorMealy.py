import sys


class MealyMachine:
    """
    Representa uma Máquina de Mealy.
    Armazena os estados, alfabetos e transições da máquina.
    """

    def __init__(self, states, initial_state, final_states, input_alphabet, output_alphabet, transitions):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        # O dicionário de transições armazena o comportamento da máquina.
        # Chave: (estado_atual, simbolo_de_entrada) -> Valor: (proximo_estado, simbolo_de_saida)
        self.transitions = transitions


def load_machine_from_file(filepath):
    """
    Lê a definição de uma Máquina de Mealy de um arquivo de texto e
    cria um objeto MealyMachine.
    """
    with open(filepath, 'r') as f:
        # Linha 1: Estados
        states = set(f.readline().strip().split())
        # Linha 2: Estado inicial
        initial_state = f.readline().strip()
        # Linha 3: Estados finais
        final_states = set(f.readline().strip().split())
        # Linha 4: Alfabeto de entrada
        input_alphabet = set(f.readline().strip().split())
        # Linha 5: Alfabeto de saída
        output_alphabet = set(f.readline().strip().split())

        transitions = {}
        # Linhas restantes: Transições
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):  # Ignora linhas vazias ou comentários
                parts = line.split()
                if len(parts) == 4:
                    current_state, input_symbol, next_state, output_symbol = parts
                    transitions[(current_state, input_symbol)] = (next_state, output_symbol)
                else:
                    print(f"Aviso: Linha de transição mal formatada ignorada: '{line}'", file=sys.stderr)

    return MealyMachine(states, initial_state, final_states, input_alphabet, output_alphabet, transitions)


def simulate(machine, input_word):
    """
    Simula a execução da Máquina de Mealy com uma palavra de entrada.
    Retorna a string de saída gerada pela máquina.
    """
    current_state = machine.initial_state
    output_string = ""

    for symbol in input_word:
        # Verifica se a transição está definida para o estado e símbolo atuais
        if (current_state, symbol) in machine.transitions:
            next_state, output_symbol = machine.transitions[(current_state, symbol)]

            # Processa o símbolo de saída
            if output_symbol == '\\n':
                output_string += '\n'
            elif output_symbol != "''":  # A palavra '' significa sem saída (palavra vazia)
                output_string += output_symbol

            # Atualiza o estado da máquina
            current_state = next_state
        else:
            # Erro se uma transição não for encontrada
            raise ValueError(
                f"Erro: Transição não definida para o estado '{current_state}' com o símbolo de entrada '{symbol}'")

    return output_string.strip()


def main():
    """
    Função principal que orquestra a execução do simulador.
    """
    # Verifica se os argumentos da linha de comando foram fornecidos corretamente
    if len(sys.argv) != 3:
        print("Uso: python simulador.py <arquivo_maquina.txt> <arquivo_entrada.txt>", file=sys.stderr)
        sys.exit(1)

    machine_filepath = sys.argv[1]
    input_filepath = sys.argv[2]

    try:
        # 1. Carrega a definição da máquina a partir do primeiro arquivo
        mealy_machine = load_machine_from_file(machine_filepath)

        # 2. Lê a palavra de entrada do segundo arquivo
        with open(input_filepath, 'r') as f:
            input_word = f.read().strip()

        # 3. Determina as dimensões da imagem a partir da palavra de entrada
        height = input_word.count('N')
        first_line = input_word.split('N')[0]
        width = first_line.count('.')

        if height == 0 or width == 0:
            print("Aviso: Não foi possível determinar as dimensões da imagem a partir do arquivo de entrada.",
                  file=sys.stderr)

        # 4. Simula a máquina para obter a matriz binária de saída
        binary_matrix_output = simulate(mealy_machine, input_word)

        # 5. Imprime a saída final no formato de imagem .ppm
        # Primeira linha: sistema de cor (P1 para preto e branco)
        print("P1")
        # Segunda linha: largura e altura da imagem
        print(f"{width} {height}")
        # Restante: a matriz binária
        print(binary_matrix_output)

    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e.filename}", file=sys.stderr)
    except ValueError as e:
        print(e, file=sys.stderr)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()