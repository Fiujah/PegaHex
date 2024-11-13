import pyautogui
from PIL import ImageGrab
import customtkinter as ctk
import pyperclip
import keyboard
import pandas as pd
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


# Variável para controlar o estado da janela
is_minimized = False

# Definindo Tabela pra Salvar Histórico
historico = pd.DataFrame(columns=["Hexadecimal"])

def get_color_at_mouse_position():
    x, y = pyautogui.position()
    screen = ImageGrab.grab()
    color = screen.getpixel((x, y))
    r = color[0]
    g = color[1]
    b = color[2]
    hex_color = f'#{r:02x}{g:02x}{b:02x}'
    return hex_color

def update_color_label():
    hex_color = get_color_at_mouse_position()
    color_label.configure(text=hex_color, fg_color=hex_color)
    root.after(100, update_color_label)

def ctrl_c(event=None):
    hex_color = color_label.cget("text")
    pyperclip.copy(hex_color)
    print(f'Cor {hex_color} copiada para a área de transferência!')

    # Adicionar ao histórico (no topo)
    global historico
    nova_linha = pd.DataFrame({"Hexadecimal": [hex_color]})
    historico = pd.concat([nova_linha, historico], ignore_index=True)
    update_history_display()

def update_history_display():
    # Atualiza o texto na caixa de histórico para refletir o conteúdo do DataFrame
    history_text = historico.to_string(index=False, header=True)
    history_display.delete(1.0, ctk.END)
    history_display.insert(ctk.END, history_text)

def janela_on_off():
    global is_minimized
    if is_minimized:
        root.deiconify()  # Restaura a janela se estiver minimizada
    else:
        root.iconify()  # Minimiza a janela se não estiver minimizada
    is_minimized = not is_minimized

def minimize_window():
    # Minimiza a janela
    root.iconify()

def export_to_csv():
    global historico
    # Abre a caixa de diálogo para selecionar o local e nome do arquivo
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                                           title="Salvar Histórico como")
    if file_path:
        historico.to_csv(file_path, index=False, encoding='utf-8')
        messagebox.showinfo("Exportação", f"Histórico exportado para '{file_path}'")    

# Configura a interface customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("PegaHex")
root.geometry("300x500")
# Definindo o ícone para a barra de tarefas e janela
icon_window = "image.ico"
icon_path = "image.ico"


icon_image = ImageTk.PhotoImage(Image.open(icon_path))

root.iconbitmap(icon_window)  # Para Windows
root.iconphoto(True, icon_image)

color_label = ctk.CTkLabel(root, text="Move o mouse para ver a cor", text_color="#FFF", font=("Helvetica", 20), width=280, height=40)
color_label.pack(padx=20, pady=(20, 10), anchor='n')

export_button = ctk.CTkButton(root, text="Exportar para CSV", command=export_to_csv)
export_button.pack(pady=(10, 10), anchor='s')

history_display = ctk.CTkTextbox(root, width=280, height=250, font=("Helvetica", 14))
history_display.pack(padx=20, pady=20, fill='both', expand=True)
#history_display.configure(anchor='center')

#Assinatura
assinatura = ctk.CTkLabel(root, text="Desenvolvido por: Renan Fiuja", text_color="#00FF00")
assinatura.pack(padx=23, pady=23, fill='both', expand=False)

# Atalhos de teclado
keyboard.add_hotkey("alt+'", janela_on_off)
keyboard.add_hotkey('ctrl+c', ctrl_c)

# Inicia o loop para atualizar a cor
update_color_label()

root.mainloop()
