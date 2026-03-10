import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import ctypes
import os

# --- FUNÇÕES DE SISTEMA ---


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def executar_comando(comando):
    try:
        # Usamos shell=True para comandos netsh e shutdown
        result = subprocess.run(comando, shell=True,
                                capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao executar comando: {e}")
        return False

# --- LÓGICA DAS AÇÕES ---


def gerenciar_rede(status, tipo="Ethernet"):
    # IMPORTANTE: Verifique se o nome da sua interface é "Ethernet 2" ou "Wi-Fi"
    nome_interface = "Wi-Fi" if tipo == "WiFi" else "Ethernet 2"
    acao = "enabled" if status else "disabled"
    comando = f'netsh interface set interface name="{nome_interface}" admin={acao}'

    if executar_comando(comando):
        msg = "Ligada" if status else "Desligada"
        color = "green" if status else "red"
        label_status.config(text=f"{tipo}: {msg}", fg=color)
    else:
        messagebox.showerror(
            "Erro", f"Não foi possível alterar a interface {nome_interface}.\nVerifique se o nome está correto.")


def gerenciar_bluetooth(status):
    # Resolve o erro de sintaxe separando a lógica das strings
    estado_servico = "Running" if status else "Stopped"
    # Comando via PowerShell para gerenciar o serviço de suporte Bluetooth
    comando_ps = f"Get-Service bthserv | Set-Service -Status {estado_servico}"
    comando_final = f'powershell -Command "Start-Process powershell -ArgumentList \'-Command {comando_ps}\' -Verb RunAs"'

    executar_comando(comando_final)

    if status:
        # Abre a tela de dispositivos para "Ver aparelhos disponíveis e conectar"
        os.system("start ms-settings:bluetooth")
        label_status.config(text="Bluetooth: Ativando...", fg="blue")
    else:
        label_status.config(text="Bluetooth: Desativando...", fg="gray")


def confirmar_desligamento():
    resposta = messagebox.askyesno(
        "Confirmar", "Deseja mesmo desligar o seu PC?")
    if resposta:
        os.system("shutdown /s /t 5")  # Desliga em 5 segundos

# --- INTERFACE ---


def disparar_acao(ligar):
    opcao = selected_option.get()

    if not is_admin() and "Desligar" not in opcao:
        messagebox.showwarning(
            "Admin", "Por favor, execute como Administrador para alterar redes!")
        return

    if "Rede" in opcao:
        gerenciar_rede(ligar, "Ethernet")
    elif "WiFi" in opcao:
        gerenciar_rede(ligar, "WiFi")
    elif "Bluetooth" in opcao:
        gerenciar_bluetooth(ligar)
    elif "Desligar" in opcao:
        if ligar:  # Só executa se clicar no botão de "Ligar/Executar"
            confirmar_desligamento()


app = tk.Tk()
app.title("Controle de Sistema")
app.geometry("350x280")

# Dropdown (Lista Suspensa)
options = [
    "Conexão de Rede (Ethernet 2)",
    "Conexão de WiFi",
    "Conexão Bluetooth",
    "Desligar o Computador"
]
selected_option = tk.StringVar(app)
selected_option.set(options[0])

tk.Label(app, text="Escolha uma função:",
         font=("Arial", 10, "bold")).pack(pady=10)
menu = ttk.OptionMenu(app, selected_option, options[0], *options)
menu.pack(pady=5)

label_status = tk.Label(
    app, text="Status: Aguardando comando...", font=("Arial", 9, "italic"))
label_status.pack(pady=15)

# Botões de Ação
frame_botoes = tk.Frame(app)
frame_botoes.pack(pady=10)

btn_ligar = tk.Button(frame_botoes, text="LIGAR / EXECUTAR", bg="#90ee90", width=18, height=2,
                      command=lambda: disparar_acao(True))
btn_ligar.pack(side=tk.LEFT, padx=5)

btn_desligar = tk.Button(frame_botoes, text="DESLIGAR / PARAR", bg="#ffcccb", width=18, height=2,
                         command=lambda: disparar_acao(False))
btn_desligar.pack(side=tk.LEFT, padx=5)

app.mainloop()
