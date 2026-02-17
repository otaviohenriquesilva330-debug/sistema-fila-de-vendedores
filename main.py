import tkinter as tk
from tkinter import messagebox

fila_vendedores = []
vendedor_em_atendimento = None

def atualizar_lista():
    lista_vendedores.delete(0, tk.END)
    for vendedor in fila_vendedores:
        lista_vendedores.insert(tk.END, vendedor)

def atualizar_atendimento():
    if vendedor_em_atendimento:
        label_atendimento.config(text=f"Em atendimento: {vendedor_em_atendimento}")
    else:
        label_atendimento.config(text="Nenhum vendedor em atendimento")

def cadastrar_vendedor():
    nome = entry_nome.get()

    if nome == "":
        messagebox.showwarning("Erro", "Digite um nome!")
        return

    fila_vendedores.append(nome)
    entry_nome.delete(0, tk.END)
    atualizar_lista()

def remover_vendedor():
    selecionado = lista_vendedores.curselection()
    if selecionado:
        indice = selecionado[0]
        fila_vendedores.pop(indice)
        atualizar_lista()

def iniciar_atendimento():
    global vendedor_em_atendimento

    if vendedor_em_atendimento:
        messagebox.showwarning("Aviso", "Já existe vendedor em atendimento!")
        return

    if len(fila_vendedores) == 0:
        messagebox.showwarning("Aviso", "Fila vazia!")
        return

    vendedor_em_atendimento = fila_vendedores.pop(0)
    atualizar_lista()
    atualizar_atendimento()

def finalizar_atendimento():
    global vendedor_em_atendimento

    if not vendedor_em_atendimento:
        messagebox.showwarning("Aviso", "Nenhum atendimento ativo!")
        return

    abrir_janela_avaliacao()

def abrir_janela_avaliacao():
    janela_avaliacao = tk.Toplevel(janela)
    janela_avaliacao.title("Finalizar Atendimento")

    tk.Label(janela_avaliacao, text="Converteu em venda?").pack()

    resultado = tk.StringVar()
    resultado.set("Sim")

    tk.Radiobutton(janela_avaliacao, text="Sim", variable=resultado, value="Sim").pack()
    tk.Radiobutton(janela_avaliacao, text="Não", variable=resultado, value="Não").pack()

    tk.Label(janela_avaliacao, text="Se não, qual motivo?").pack()

    motivo = tk.StringVar()
    motivo.set("Preço")

    opcoes = ["Preço", "Curiosidade", "Não tinha o produto"]
    for opcao in opcoes:
        tk.Radiobutton(janela_avaliacao, text=opcao, variable=motivo, value=opcao).pack()

    def confirmar():
        global vendedor_em_atendimento

        print("Vendedor:", vendedor_em_atendimento)
        print("Converteu:", resultado.get())

        if resultado.get() == "Não":
            print("Motivo:", motivo.get())

        fila_vendedores.append(vendedor_em_atendimento)
        vendedor_em_atendimento = None

        atualizar_lista()
        atualizar_atendimento()

        janela_avaliacao.destroy()

    tk.Button(janela_avaliacao, text="Confirmar", command=confirmar).pack(pady=10)

janela = tk.Tk()
janela.title("Sistema de Fila Inteligente")
janela.geometry("500x500")

tk.Label(janela, text="Cadastrar Vendedor").pack(pady=5)

entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Button(janela, text="Adicionar à Fila", command=cadastrar_vendedor).pack(pady=5)
tk.Button(janela, text="Remover Selecionado", command=remover_vendedor).pack(pady=5)

tk.Label(janela, text="Fila de Atendimento").pack(pady=5)

lista_vendedores = tk.Listbox(janela)
lista_vendedores.pack(fill=tk.BOTH, expand=True)

tk.Button(janela, text="Iniciar Atendimento", command=iniciar_atendimento).pack(pady=10)

label_atendimento = tk.Label(janela, text="Nenhum vendedor em atendimento", fg="blue")
label_atendimento.pack(pady=10)

tk.Button(janela, text="Finalizar Atendimento", command=finalizar_atendimento).pack(pady=10)

janela.mainloop()
