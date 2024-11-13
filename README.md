# Pega Hexadecimal

Este projeto é um programa desenvolvido em Python que captura o código hexadecimal da cor do pixel onde o ponteiro do mouse estiver posicionado. É uma ferramenta útil para designers e desenvolvedores que precisam rapidamente de referências de cor na tela.

## 🎨 Funcionalidades

- Exibe o código hexadecimal da cor onde o ponteiro do mouse está posicionado.
- Copia automaticamente o código hexadecimal para a área de transferência ao pressionar **Ctrl+C**.
- Armazena o histórico de cores capturadas, exibindo-as na interface.
- Permite exportar o histórico de cores para um arquivo CSV.
- Interface escura moderna desenvolvida com **customtkinter**.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento do programa.
- **customtkinter**: Biblioteca usada para criar uma interface gráfica personalizada e responsiva.
- **Pandas**: Utilizado para gerenciar o histórico de cores capturadas.
- **Pillow (PIL)**: Para capturar a cor dos pixels.
- **pyautogui**: Para acessar a posição do mouse.
- **pyperclip**: Para copiar automaticamente o código hexadecimal para a área de transferência.

## 📁 Como Usar

1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias usando:
   ```bash
   pip install -r requirements.txt

## 📝 Observações

O histórico de cores capturadas é exibido em uma caixa de texto e pode ser exportado para um arquivo CSV para fácil compartilhamento.
Para garantir que o programa funcione corretamente, verifique se possui as permissões necessárias para capturar a tela e acessar o mouse.

## Autor

Renan Fiuja - renanfiujah@gmail.com