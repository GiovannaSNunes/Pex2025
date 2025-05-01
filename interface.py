import tkinter as tk
from tkinter import messagebox
from main import principal

COR_BG = "#1e1e1e"         
COR_FG = "#ffffff"         
COR_ENTRADA = "#2a2a2a"    
COR_BOTAO = "#0077cc"      
COR_BOTAO_HOVER = "#005999" 


def ao_passar_mouse(event):
    event.widget.config(bg=COR_BOTAO_HOVER)

def ao_sair_mouse(event):
    event.widget.config(bg=COR_BOTAO)

def executar_relatorio():
    data_inicio = entrada_inicio.get()
    data_fim = entrada_fim.get()

    if not data_inicio or not data_fim:
        messagebox.showerror("Erro", "Preencha as duas datas")
        return

    try:
        principal(data_inicio, data_fim)
        messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro na execução", str(e))

janela = tk.Tk()
janela.title("Relatório de Campanhas - Meta Ads")
janela.geometry("400x250")
janela.configure(bg=COR_BG)

fonte_padrao = ("Segoe UI", 11)

lbl_inicio = tk.Label(janela, text="Data Início (AAAA-MM-DD):", bg=COR_BG, fg=COR_FG, font=fonte_padrao)
lbl_inicio.pack(pady=(15, 5))
entrada_inicio = tk.Entry(janela, width=25, font=fonte_padrao, bg=COR_ENTRADA, fg=COR_FG, insertbackground=COR_FG, relief="flat")
entrada_inicio.pack(ipady=6)

lbl_fim = tk.Label(janela, text="Data Fim (AAAA-MM-DD):", bg=COR_BG, fg=COR_FG, font=fonte_padrao)
lbl_fim.pack(pady=(15, 5))
entrada_fim = tk.Entry(janela, width=25, font=fonte_padrao, bg=COR_ENTRADA, fg=COR_FG, insertbackground=COR_FG, relief="flat")
entrada_fim.pack(ipady=6)

btn_gerar = tk.Button(janela, text="Gerar Relatório", bg=COR_BOTAO, fg=COR_FG, font=fonte_padrao, relief="flat", activebackground=COR_BOTAO_HOVER, activeforeground=COR_FG, cursor="hand2", command=executar_relatorio)
btn_gerar.pack(pady=30, ipadx=10, ipady=5)

btn_gerar.bind("<Enter>", ao_passar_mouse)
btn_gerar.bind("<Leave>", ao_sair_mouse)

janela.mainloop()