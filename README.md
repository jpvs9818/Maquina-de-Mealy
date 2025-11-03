# T1 LFA: Fractais em Máquina de Mealy

Trabalho 1 da disciplina de Linguagens Formais e Autômatos (LFA). O objetivo deste projeto é desenvolver um simulador de Máquina de Mealy em Python, capaz de gerar imagens de fractais no formato `.ppm` a partir da definição de uma máquina e uma palavra de entrada.

## Sobre o Projeto

O simulador (`SimuladorMealy.py`) recebe dois arquivos de texto como entrada:
1.  **`arquivo_maquina.txt` (ex: `MM1.txt`)**: A definição formal da Máquina de Mealy, contendo seus estados, alfabetos e todas as funções de transição.
2.  **`arquivo_entrada.txt` (ex: `w8.txt`)**: Uma única palavra `w` que representa a grade do fractal. Nesta palavra, as "células" (subpalavras) são separadas por `.` e as "linhas" da grade são separadas por `N`.

O simulador processa a palavra `w` símbolo por símbolo, gerando uma matriz binária que é então formatada como uma imagem `.ppm` (P1) e impressa na saída padrão.

## Modelagem e Lógica das Máquinas

O projeto consistiu em modelar três Máquinas de Mealy distintas, cada uma baseada em uma expressão regular (ER) fornecida.

### Expressões Regulares (Objetivo 1)

1.  **Máquina 1 (MM1.txt):** `(1+2+3+4)*(13+31)(1+2+3+4)*`
2.  **Máquina 2 (MM2.txt):** `(1+3)(2+4)(2+3+4)(1+3+4)(1+2+4)(1+2+3)(1+2+3+4)*`
3.  **Máquina 3 (MM3.txt):** `(ε+1+2+3+4)(2+3+4)(1+3+4)(1+2+4)(1+2+3)(1+2+3+4)*`

### Lógica de Saída (Objetivo 2)

Para todas as máquinas, a lógica de transição e saída foi padronizada:

* **Alfabeto de Entrada (Σ):** `{1, 2, 3, 4, N, .}`
* **Alfabeto de Saída (Δ):** `{0, 1, \n, ε}`

A saída é determinada da seguinte forma:
* **Saída `1` (Pixel Preto):** A máquina emite `1` apenas quando está em um **estado final** (que denota o aceite da subpalavra) e lê o símbolo `.`.
* **Saída `0` (Pixel Branco):** A máquina emite `0` quando está em um **estado não-final** e lê o símbolo `.`.
* **Saída `ε` (Palavra Vazia):** A máquina emite `ε` (representado como `''` no código) ao ler qualquer um dos dígitos `{1, 2, 3, 4}`.
* **Saída `\n` (Nova Linha):** A máquina emite `\n` ao ler o símbolo `N` e, em seguida, retorna ao estado inicial para processar a próxima linha da grade.

## Como Executar o Simulador

O script `SimuladorMealy.py` imprime o resultado da imagem `.ppm` na saída padrão. Para salvar a imagem em um arquivo, utilize o operador de redirecionamento (`>`).

**Formato do Comando:**
```bash
python3 SimuladorMealy.py <arquivo_maquina.txt> <arquivo_entrada.txt> > <arquivo_saida.ppm>
