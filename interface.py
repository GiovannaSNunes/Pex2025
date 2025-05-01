import tkinter as tk
from tkinter import messagebox
from main import principal

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
janela.geometry("350x200")

lbl_inicio = tk.Label(janela, text="Data Início (YYYY-MM-DD):")
lbl_inicio.pack(pady=(10, 0))
entrada_inicio = tk.Entry(janela, width=30)
entrada_inicio.pack()

lbl_fim = tk.Label(janela, text="Data Fim (YYYY-MM-DD):")
lbl_fim.pack(pady=(10, 0))
entrada_fim = tk.Entry(janela, width=30)
entrada_fim.pack()

btn_gerar = tk.Button(janela, text="Gerar Relatório", command=executar_relatorio)
btn_gerar.pack(pady=20)

janela.mainloop()