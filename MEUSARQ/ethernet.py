import tkinter as tk
from tkinter import messagebox
import subprocess
import ctypes
import sys

# --- CONFIGURAÇÃO ---
NOME_INTERFAZ = "Ethernet 2"
# ---------------------


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def alterar_status_rede(status):
    if not is_admin():
        messagebox.showwarning("Aviso", "Execute como Administrador!")
        return

    acao = "enabled" if status else "disabled"
    comando = f'netsh interface set interface name="{NOME_INTERFAZ}" admin={acao}'

    try:
        result = subprocess.run(comando, shell=True,
                                capture_output=True, text=True)
        if result.returncode == 0:
            status_texto = "HABILITADA" if status else "DESABILITADA"
            label_status.config(
                text=f"Status: {status_texto}", fg="green" if status else "red")
        else:
            messagebox.showerror("Erro", result.stderr)
    except Exception as e:
        messagebox.showerror("Erro Fatal", str(e))


# --- INTERFACE ---
app = tk.Tk()
app.title("Controle de Rede")
app.geometry("300x200")

label_status = tk.Label(app, text="Status: Aguardando...", font=("Arial", 11))
label_status.pack(pady=20)

tk.Button(app, text="LIGAR REDE", bg="lightgreen", width=20,
          command=lambda: alterar_status_rede(True)).pack(pady=5)

tk.Button(app, text="DESLIGAR REDE", bg="salmon", width=20,
          command=lambda: alterar_status_rede(False)).pack(pady=5)

app.mainloop()
