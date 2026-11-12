# 📘 Guia Completo de Estilização em Markdown

Markdown é uma linguagem de marcação simples para formatar textos usando símbolos visuais.

---

## 1. Títulos e Cabeçalhos
Use o caractere `#` seguido de um espaço. Quanto mais `#`, menor o título (vai do 1 ao 6).

# Título 1 (Principal)
## Título 2 (Seções)
### Título 3 (Subseções)
#### Título 4

---

## 2. Formatação de Texto
Deixe textos em destaque usando asteriscos `*` ou underlines `_`.

* **Negrito:** Use `**texto**` ou `__texto__` -> **Resultado**
* *Itálico:* Use `*texto*` ou `_texto_` -> *Resultado*
* ~~Tachado (Riscado):~~ Use `~~texto~~` -> ~~Resultado~~
* ***Negrito e Itálico:*** Use `***texto***` -> ***Resultado***

---

## 3. Listas
Organize informações em tópicos com facilidade.

### Lista Não Ordenada (Marcadores)
Use `*`, `-` ou `+` seguido de espaço.
* Item A
* Item B
  * Subitem B.1 (Dê 2 ou 4 espaços de recuo)

### Lista Ordenada (Numérica)
Use o número seguido de ponto e espaço.
1. Primeiro passo
2. Segundo passo

---

## 4. Blocos de Código
Essenciais para documentar programação.

### Código na mesma linha (Inline)
Use uma crase (`) antes e depois da palavra.
O método `print()` exibe mensagens na tela.

### Bloco de Código Inteiro
Use três crases (```) para abrir e três para fechar. Indique a linguagem ao lado das primeiras crases para ativar o realce de cores.

```python
def ola_mundo():
    print("Olá, Dev!")
```

```html
<h1>Isso é HTML colorido</h1>
```

---

## 5. Links e Imagens
* **Link:** `[Texto do Link](URL)` -> [Google](https://google.com)
* **Imagem:** `![Texto Alternativo](URL_da_Imagem)`

---

## 6. Blocos de Citação (Destaques)
Use o caractere `>` para criar recuos visuais de avisos ou citações.

> 💡 **Dica de Ouro:** Use emojis junto com o bloco de citação para criar caixas de alerta muito mais visuais e elegantes!

---

## 7. Tabelas
Use barras verticais `|` para separar colunas e hifens `-` para separar o cabeçalho.

| Função | Tipo | O que faz |
| :--- | :---: | ---: |
| `.lower()` | String | Transforma em minúscula (Alinhado à esquerda) |
| `.append()` | Lista | Adiciona elemento (Alinhado ao centro) |
| `print()` | Saída | Mostra na tela (Alinhado à direita) |

*Nota: Os dois pontos `:` definem o alinhamento da coluna (esquerda `:---`, centro `:---:`, direita `---:`).*

---

## 8. Linhas Divisórias
Para criar uma linha horizontal de separação, use três hifens `---` ou três asteriscos `***` em uma linha isolada.