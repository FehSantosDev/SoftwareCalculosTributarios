# Coder: Felipe Natã de Jesus dos Santos
# Date:29/03/2021 


import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter, A4
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

# Título do programa #
app = tk.Tk()
app.title("Software Cálculos Tributários")
app.geometry("700x665")
# Icone do programa
app.iconbitmap('assinaturaFJSpequena.ico')
# Background do programa
img = tk.PhotoImage(file="assinaturaFJS.PNG")
labe_imagem = tk.Label(app, image=img).place(x="160", y="135")
espaco = tk.Label(app, text="", width="1000", height="1000", bg="white")
espaco.place(x="700", y="0")

# Pergunta Inicial #
pergunta = tk.Label(text="Sistema de Cálculos:", bg="#FFD700")
pergunta.configure(font="40")
fill = tk.X
side = tk.TOP
pergunta.pack(fill="x", side="top")


def calcula_pis_cofins():  # Fechou
    def print_empresa():
        webbrowser.open("calculo.pdf")

    def gera_relatorio():
        c = canvas.Canvas("calculo.pdf")

        nome_rel = ed2.get()
        faturamento_rel = int(ed1.get())
        pis = faturamento_rel * 0.0065
        cofins = faturamento_rel * 0.03

        c.setFont("Helvetica-Bold", 22)
        c.drawString(200, 790, 'Cálculo PIS/COFINS')

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 700, 'Nome: ' + nome_rel)
        fat_format = f'{faturamento_rel:,.2f}'
        pis_format = f'{pis:,.2f}'
        cofins_format = f'{cofins:,.2f}'
        c.drawString(50, 670, 'Faturamento Bruto: ' + f'R${str(fat_format)}')
        c.drawString(50, 640, 'PIS: ' + f'R${str(pis_format)}')
        c.drawString(50, 610, 'COFINS: ' + f'R${str(cofins_format)}')

        c.rect(20, 570, 550, 170, fill=False, stroke=True)

        c.showPage()
        c.save()
        print_empresa()

    def limpa_tela():
        ed1.delete(0, tk.END)
        ed2.delete(0, tk.END)

    def add_empresa():
        faturamento = int(ed1.get())
        empresa = ed2.get()
        pis = faturamento * 0.0065
        cofins = faturamento * 0.03
        listacl.insert("", tk.END, values=(empresa, f'R${faturamento:,.2f}', f'R${pis:,.2f}', f'R${cofins:,.2f}'))

    def deleta_calculo():
        item_selecionado = listacl.selection()[0]
        listacl.delete(item_selecionado)

    appcalculapis = tk.Tk()
    appcalculapis.title("Calcular PIS/COFINS")
    appcalculapis.geometry("920x500")
    appcalculapis.configure(background="white")
    appcalculapis.iconbitmap('ulianoerochalogo.ico')
    texto = tk.Label(appcalculapis, text="Realizando Cálculo de PIS/COFINS", bg="#FFD700")
    texto.pack(fill="x", side="top")
    espaco1 = tk.Label(appcalculapis, text="", width="1000", height="2", bg="black")
    espaco1.place(x="0", y="20")
    espaco2 = tk.Label(appcalculapis, text="", width="50", height="1000", bg="black")
    espaco2.place(x="0", y="55")
    ed1 = tk.Entry(appcalculapis)
    ed1.place(x="30", y="180")
    ed2 = tk.Entry(appcalculapis)
    ed2.place(x="30", y="125")
    mensagem = tk.Label(appcalculapis, text="Faturamento Bruto da Empresa(R$ sem ponto e sem vírgula): ", bg="black", fg="white")
    mensagem.place(x="15", y="150")
    mensagem2 = tk.Label(appcalculapis, text="Nome da Empresa: ", bg="black", fg="white")
    mensagem2.place(x="15", y="100")
    # Botão Limpar
    bt_limpar = tk.Button(appcalculapis, text="Limpar", command=limpa_tela, bg="black", fg="white")
    bt_limpar.place(x="30", y="210")
    # Botão Adicionar/Calcular
    bt_adicionar = tk.Button(appcalculapis, text="Adicionar e Calcular PIS/COFINS", command=add_empresa, bg="black", fg="white")
    bt_adicionar.place(x="30", y="240")
    # Botão Deletar Cálculo
    bt_deletar = tk.Button(appcalculapis, text="Deletar Cálculos/Empresas", command=deleta_calculo, bg="black", fg="white")
    bt_deletar.place(x="30", y="270")
    # Botão Exportar
    bt_exportar = tk.Button(appcalculapis, text="Gerar PDF", command=gera_relatorio, bg="black", fg="white")
    bt_exportar.place(x="30", y="300")
    listacl = ttk.Treeview(appcalculapis, height="1", column=("col0", "col1", "col2", "col3", "col4"))
    listacl.heading("#0", text="")
    listacl.heading("#1", text="Nome da Empresa")
    listacl.heading("#2", text="Faturamento Bruto")
    listacl.heading("#3", text="PIS")
    listacl.heading("#4", text="COFINS")

    listacl.column("#0", width=0)
    listacl.column("#1", width=70)
    listacl.column("#2", width=70)
    listacl.column("#3", width=50)
    listacl.column("#4", width=50)

    listacl.place(relx="0.26", rely="0.07", relwidth="0.74", relheight="0.99")

    scrolllista = tk.Scrollbar(appcalculapis, orient="vertical")
    scrolllista.pack(side="right", fill="y")


# Fechou #

def calcula_icms():  # Fechou

    def print_produto():
        webbrowser.open("calculo.pdf")

    def gera_relatorio():
        c = canvas.Canvas("calculo.pdf")

        valor = int(ed1.get())
        nomeproduto = ed3.get()
        icms_intra = int(ed2.get())
        icms = valor * (icms_intra / 100)

        c.setFont("Helvetica-Bold", 22)
        c.drawString(200, 790, 'Cálculo ICMS')

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 700, 'Produto: ' + nomeproduto)
        valor_format = f'{valor:,.2f}'
        c.drawString(50, 670, 'Valor:  ' + f'R${str(valor_format)}')
        c.drawString(50, 640, 'ICMS Intra: ' + f'{str(icms_intra)}%')
        icms_format = f'{icms:,.2f}'
        c.drawString(50, 610, 'ICMS: ' + f'R${str(icms_format)}')

        c.rect(20, 570, 550, 170, fill=False, stroke=True)

        c.showPage()
        c.save()
        print_produto()

    def limpa_tela():
        ed1.delete(0, tk.END)
        ed2.delete(0, tk.END)
        ed3.delete(0, tk.END)

    def add_produto():
        valor = int(ed1.get())
        nomeproduto = ed3.get()
        icms_intra = int(ed2.get())
        icms = valor * (icms_intra / 100)
        listacl.insert("", tk.END, values=(nomeproduto, f'R${valor:,.2f}', f'{icms_intra}%', f'R${icms:,.2f}'))

    def deleta_calculo():
        item_selecionado = listacl.selection()[0]
        listacl.delete(item_selecionado)

    appcalculaicms = tk.Tk()
    appcalculaicms.title("Calcular ICMS")
    appcalculaicms.geometry("900x400")
    appcalculaicms.configure(background="white")
    appcalculaicms.iconbitmap("ulianoerochalogo.ico")
    espaco1 = tk.Label(appcalculaicms, text="", width="1000", height="2", bg="black")
    espaco1.place(x="0", y="20")
    espaco2 = tk.Label(appcalculaicms, text="", width="50", height="1000", bg="black")
    espaco2.place(x="0", y="55")
    texto = tk.Label(appcalculaicms, text="Realizando Cálculo de ICMS", bg="#FFD700")
    texto.pack(fill="x", side="top")
    ed1 = tk.Entry(appcalculaicms)
    ed1.place(x="30", y="150")
    ed2 = tk.Entry(appcalculaicms)
    ed2.place(x="30", y="200")
    ed3 = tk.Entry(appcalculaicms)
    ed3.place(x="30", y="100")
    mensagem = tk.Label(appcalculaicms, text="Valor do Produto(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem.place(x="25", y="125")
    mensagem2 = tk.Label(appcalculaicms, text="ICMS Intra do Estado Brasileiro: ", bg="black", fg="white")
    mensagem2.place(x="25", y="175")
    mensagem3 = tk.Label(appcalculaicms, text="Nome do Produto:", bg="black", fg="white")
    mensagem3.place(x="25", y="75")
    # Botão Limpar
    bt_limpar = tk.Button(appcalculaicms, text="Limpar", command=limpa_tela, bg="black", fg="white")
    bt_limpar.place(x="30", y="230")
    # Botão Adicionar/Calcular
    bt_adicionar = tk.Button(appcalculaicms, text="Adicionar e Calcular ICMS", command=add_produto, bg="black", fg="white")
    bt_adicionar.place(x="30", y="260")
    # Botão Deletar Cálculo
    bt_deletar = tk.Button(appcalculaicms, text="Deletar Produto", command=deleta_calculo, bg="black", fg="white")
    bt_deletar.place(x="30", y="290")
    # Botão Exportar
    bt_exportar = tk.Button(appcalculaicms, text="Gerar PDF", command=gera_relatorio, bg="black", fg="white")
    bt_exportar.place(x="30", y="320")
    listacl = ttk.Treeview(appcalculaicms, height="1", column=("col0", "col1", "col2", "col3", "col4"))
    listacl.heading("#0", text="")
    listacl.heading("#1", text="Produto")
    listacl.heading("#2", text="Valor")
    listacl.heading("#3", text="ICMS Intra")
    listacl.heading("#4", text="ICMS")

    listacl.column("#0", width=0)
    listacl.column("#1", width=2)
    listacl.column("#2", width=2)
    listacl.column("#3", width=20)
    listacl.column("#4", width=2)

    listacl.place(relx="0.26", rely="0.07", relwidth="0.74", relheight="0.99")

    scrolllista = tk.Scrollbar(appcalculaicms, orient="vertical")
    scrolllista.pack(side="right", fill="y")
    #  Fechou


def credito_icms():

    def print_produto():
        webbrowser.open("calculo.pdf")

    def gera_relatorio():
        c = canvas.Canvas("calculo.pdf")

        nome = ed5.get()
        valor_compra = int(ed1.get())
        valor_venda = int(ed2.get())
        num3 = int(ed3.get())
        num4 = int(ed4.get())
        imposto_compra = valor_venda * (num3 / 100)
        imposto_venda = valor_compra * (num4 / 100)
        creditoicms = imposto_compra - imposto_venda

        c.setFont("Helvetica-Bold", 22)
        c.drawString(200, 790, 'Cálculo Crédito ICMS')

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 700, 'Produto: ' + nome)
        vc_format = f'{valor_compra:,.2f}'
        c.drawString(50, 670, 'Valor da Compra:  ' + f'R${str(vc_format)}')
        vv_format = f'{valor_venda:,.2f}'
        c.drawString(50, 640, 'Valor da Venda: ' + f'R${str(vv_format)}')
        c.drawString(50, 610, 'Alíquota da Compra: ' + f'{str(num3)}%')
        c.drawString(50, 580, 'Alíquota da venda: ' + f'{str(num4)}%')
        ci_format = f'{creditoicms:,.2f}'
        c.drawString(50, 550, 'Crédito ICMS: ' + f'R${str(ci_format)}')

        c.rect(20, 530, 550, 210, fill=False, stroke=True)

        c.showPage()
        c.save()
        print_produto()

    def limpa_tela():
        ed1.delete(0, tk.END)
        ed2.delete(0, tk.END)
        ed3.delete(0, tk.END)
        ed4.delete(0, tk.END)
        ed5.delete(0, tk.END)

    def calcula_credito():
        nome = ed5.get()
        valor_compra = int(ed1.get())
        valor_venda = int(ed2.get())
        num3 = int(ed3.get())
        num4 = int(ed4.get())
        imposto_compra = valor_venda * (num3 / 100)
        imposto_venda = valor_compra * (num4 / 100)
        creditoicms = imposto_compra - imposto_venda
        listacl.insert("", tk.END, values=(nome, f'R$ {valor_compra:,.2f}', f'R$ {valor_venda:,.2f}', f'{num3}%', f'{num4}%', f'R${creditoicms:,.2f}'))

    def deleta_calculo():
        item_selecionado = listacl.selection()[0]
        listacl.delete(item_selecionado)

    appcreditoicms = tk.Tk()
    appcreditoicms.title("Calcular Crédito do ICMS: ")
    appcreditoicms.geometry("1280x500")
    appcreditoicms.iconbitmap("ulianoerochalogo.ico")
    appcreditoicms.configure(background="white")
    texto = tk.Label(appcreditoicms, text="Realizando Cálculo de Créditos do ICMS", bg="#FFD700")
    texto.pack(fill="x", side="top")
    espaco1 = tk.Label(appcreditoicms, text="", width="1000", height="2", bg="black")
    espaco1.place(x="0", y="20")
    espaco2 = tk.Label(appcreditoicms, text="", width="50", height="1000", bg="black")
    espaco2.place(x="0", y="55")
    ed1 = tk.Entry(appcreditoicms)
    ed1.place(x="30", y="165")
    ed2 = tk.Entry(appcreditoicms)
    ed2.place(x="30", y="215")
    ed3 = tk.Entry(appcreditoicms)
    ed3.place(x="30", y="265")
    ed4 = tk.Entry(appcreditoicms)
    ed4.place(x="30", y="315")
    ed5 = tk.Entry(appcreditoicms)
    ed5.place(x="30", y="115")
    mensagem = tk.Label(appcreditoicms, text="Valor da Compra(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem.place(x="25", y="140")
    mensagem2 = tk.Label(appcreditoicms, text="Valor da Venda(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem2.place(x="25", y="190")
    mensagem3 = tk.Label(appcreditoicms, text="Alíquota da compra(sem ponto e sem vírgula) %: ", bg="black", fg="white")
    mensagem3.place(x="25", y="240")
    mensagem4 = tk.Label(appcreditoicms, text="Alíquota da Venda (sem ponto e sem vírgula) %: ", bg="black", fg="white")
    mensagem4.place(x="25", y="290")
    mensagem5 = tk.Label(appcreditoicms, text="Nome da Compra:", bg="black", fg="white")
    mensagem5.place(x="25", y="90")
    # Botão Limpar
    bt_limpar = tk.Button(appcreditoicms, text="Limpar", command=limpa_tela, bg="black", fg="white")
    bt_limpar.place(x="30", y="350")
    # Botão Adicionar/Calcular
    bt_adicionar = tk.Button(appcreditoicms, text="Adicionar e Calcular ICMS", command=calcula_credito, bg="black", fg="white")
    bt_adicionar.place(x="30", y="380")
    # Botão Deletar Cálculo
    bt_deletar = tk.Button(appcreditoicms, text="Deletar Produto", command=deleta_calculo, bg="black", fg="white")
    bt_deletar.place(x="30", y="410")
    # Botão Exportar
    bt_exportar = tk.Button(appcreditoicms, text="Gerar PDF", command=gera_relatorio, bg="black", fg="white")
    bt_exportar.place(x="30", y="440")
    listacl = ttk.Treeview(appcreditoicms, height="1", column=("col0", "col1", "col2", "col3", "col4", "col5", "col6"))
    listacl.heading("#0", text="")
    listacl.heading("#1", text="Produto")
    listacl.heading("#2", text="Valor da Compra")
    listacl.heading("#3", text="Valor da Venda")
    listacl.heading("#4", text="Alíquota da Compra")
    listacl.heading("#5", text="Alíquota da Venda")
    listacl.heading("#6", text="Crédito ICMS")

    listacl.column("#0", width=0)
    listacl.column("#1", width=30)
    listacl.column("#2", width=40)
    listacl.column("#3", width=40)
    listacl.column("#4", width=60)
    listacl.column("#5", width=50)
    listacl.column("#6", width=40)

    listacl.place(relx="0.26", rely="0.07", relwidth="0.74", relheight="0.99")

    scrolllista = tk.Scrollbar(appcreditoicms, orient="vertical")
    scrolllista.pack(side="right", fill="y")


def icms_st():

    def print_produto():
        webbrowser.open("calculo.pdf")

    def gera_relatorio():
        c = canvas.Canvas("calculo.pdf")

        nome = ed1.get()
        valor_produto = int(ed2.get())
        frete = int(ed3.get())
        seguro = int(ed4.get())
        despesas = int(ed5.get())
        descontos = int(ed6.get())
        aliquota_inter = int(ed7.get())
        ipi = int(ed8.get())
        mva = int(ed9.get())
        aliquota_intra = int(ed10.get())
        base_icms_inter = valor_produto + frete + seguro + despesas - descontos
        valor_icms_inter = base_icms_inter * (aliquota_inter / 100)
        base_icms_st = valor_produto + ipi + frete + seguro + despesas - descontos * (1 + (mva / 100))
        valor_icms_st = (base_icms_st * (aliquota_intra / 100)) - valor_icms_inter

        c.setFont("Helvetica-Bold", 22)
        c.drawString(200, 790, 'Cálculo ICMS ST')

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 700, 'Produto: ' + nome)
        vp_format = f'{valor_produto:,.2f}'
        c.drawString(50, 670, 'Valor:  ' + f'R${str(vp_format)}')
        frete_format = f'{frete:,.2f}'
        c.drawString(50, 640, 'Frete: ' + f'R${str(frete_format)}')
        seg_format = f'{seguro:,.2f}'
        c.drawString(50, 610, 'Seguro: ' + f'R${str(seg_format)}')
        desp_format = f'{despesas:,.2f}'
        c.drawString(50, 580, 'Despesas Acessórias: ' + f'R${str(desp_format)}')
        desc_foramt = f'{descontos:,.2f}'
        c.drawString(50, 550, 'Descontos: ' + f'R${str(desc_foramt)}')
        vis_format = f'{valor_icms_st:,.2f}'
        c.drawString(50, 520, 'ICMS ST: ' + f'R${str(vis_format)}')

        c.rect(20, 500, 560, 240, fill=False, stroke=True)

        c.showPage()
        c.save()
        print_produto()

    def limpa_tela():
        ed1.delete(0, tk.END)
        ed2.delete(0, tk.END)
        ed3.delete(0, tk.END)
        ed4.delete(0, tk.END)
        ed5.delete(0, tk.END)
        ed6.delete(0, tk.END)
        ed7.delete(0, tk.END)
        ed8.delete(0, tk.END)
        ed9.delete(0, tk.END)
        ed10.delete(0, tk.END)

    def add_produto():
        nome = ed1.get()
        valor_produto = int(ed2.get())
        frete = int(ed3.get())
        seguro = int(ed4.get())
        despesas = int(ed5.get())
        descontos = int(ed6.get())
        aliquota_inter = int(ed7.get())
        ipi = int(ed8.get())
        mva = int(ed9.get())
        aliquota_intra = int(ed10.get())
        base_icms_inter = valor_produto + frete + seguro + despesas - descontos
        valor_icms_inter = base_icms_inter * (aliquota_inter / 100)
        base_icms_st = valor_produto + ipi + frete + seguro + despesas - descontos * (1 + (mva / 100))
        valor_icms_st = (base_icms_st * (aliquota_intra / 100)) - valor_icms_inter
        listacl.insert("", tk.END, values=(nome, f'R$ {valor_produto:,.2f}', f'R$ {frete:,.2f}', f'R${seguro:,.2f}', f'R${despesas:,.2f}', f'R${descontos:,.2f}', f'R${valor_icms_st:,.2f}'))

    def deleta_calculo():
        item_selecionado = listacl.selection()[0]
        listacl.delete(item_selecionado)

    appicmsst = tk.Tk()
    appicmsst.title("Calcular ICMS ST")
    appicmsst.geometry("1300x500")
    appicmsst.iconbitmap("ulianoerochalogo.ico")
    espaco1 = tk.Label(appicmsst, text="", width="1000", height="2", bg="black")
    espaco1.place(x="0", y="20")
    espaco2 = tk.Label(appicmsst, text="", width="50", height="1000", bg="black")
    espaco2.place(x="0", y="55")
    texto = tk.Label(appicmsst, text="Realizando Cálculo de ICMS ST", bg="#FFD700")
    texto.pack(fill="x", side="top")
    mensagem = tk.Label(appicmsst, text="Valor do Produto(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem.place(x="25", y="125")
    mensagem2 = tk.Label(appicmsst, text="Valor do Frete(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem2.place(x="25", y="175")
    mensagem3 = tk.Label(appicmsst, text="Valor do Seguro(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem3.place(x="25", y="225")
    mensagem4 = tk.Label(appicmsst, text="Outras Despesas Acessórias(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem4.place(x="25", y="275")
    mensagem5 = tk.Label(appicmsst, text="Descontos(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem5.place(x="25", y="325")
    mensagem6 = tk.Label(appicmsst, text="Alíquota ICMS Inter: ", bg="black", fg="white")
    mensagem6.place(x="25", y="375")
    mensagem7 = tk.Label(appicmsst, text="Valor IPI: ", bg="black", fg="white")
    mensagem7.place(x="25", y="425")
    mensagem8 = tk.Label(appicmsst, text="Valor MVA(%): ", bg="black", fg="white")
    mensagem8.place(x="25", y="475")
    mensagem9 = tk.Label(appicmsst, text="Alíquota do ICMS Intra do Estado Brasileiro: ", bg="black", fg="white")
    mensagem9.place(x="25", y="525")
    mensagem10 = tk.Label(appicmsst, text="Nome do Produto:", bg="black", fg="white")
    mensagem10.place(x="25", y="80")
    ed1 = tk.Entry(appicmsst)
    ed1.place(x="30", y="103")
    ed2 = tk.Entry(appicmsst)
    ed2.place(x="30", y="148")
    ed3 = tk.Entry(appicmsst)
    ed3.place(x="30", y="198")
    ed4 = tk.Entry(appicmsst)
    ed4.place(x="30", y="248")
    ed5 = tk.Entry(appicmsst)
    ed5.place(x="30", y="298")
    ed6 = tk.Entry(appicmsst)
    ed6.place(x="30", y="348")
    ed7 = tk.Entry(appicmsst)
    ed7.place(x="30", y="398")
    ed8 = tk.Entry(appicmsst)
    ed8.place(x="30", y="448")
    ed9 = tk.Entry(appicmsst)
    ed9.place(x="30", y="498")
    ed10 = tk.Entry(appicmsst)
    ed10.place(x="30", y="548")
    # Botão Limpar
    bt_limpar = tk.Button(appicmsst, text="Limpar", command=limpa_tela, bg="black", fg="white")
    bt_limpar.place(x="30", y="585")
    # Botão Adicionar/Calcular
    bt_adicionar = tk.Button(appicmsst, text="Adicionar e Calcular ICMS", command=add_produto, bg="black", fg="white")
    bt_adicionar.place(x="30", y="615")
    # Botão Deletar Cálculo
    bt_deletar = tk.Button(appicmsst, text="Deletar Produto", command=deleta_calculo, bg="black", fg="white")
    bt_deletar.place(x="30", y="645")
    # Botão Exportar
    bt_exportar = tk.Button(appicmsst, text="Gerar PDF", command=gera_relatorio, bg="black", fg="white")
    bt_exportar.place(x="30", y="675")
    listacl = ttk.Treeview(appicmsst, height="1", column=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
    listacl.heading("#0", text="")
    listacl.heading("#1", text="Produto")
    listacl.heading("#2", text="Valor")
    listacl.heading("#3", text="Frete")
    listacl.heading("#4", text="Seguro")
    listacl.heading("#5", text="Desp. Acessórias")
    listacl.heading("#6", text="Descontos")
    listacl.heading("#7", text="ICMS ST")

    listacl.column("#0", width=0)
    listacl.column("#1", width=130)
    listacl.column("#2", width=70)
    listacl.column("#3", width=70)
    listacl.column("#4", width=70)
    listacl.column("#5", width=110)
    listacl.column("#6", width=80)
    listacl.column("#7", width=80)

    listacl.place(relx="0.26", rely="0.07", relwidth="0.74", relheight="0.99")

    scrolllista = tk.Scrollbar(appicmsst, orient="vertical")
    scrolllista.pack(side="right", fill="y")


def calcula_difal():

    def print_produto():
        webbrowser.open("calculo.pdf")

    def gera_relatorio():
        c = canvas.Canvas("calculo.pdf")

        nome = ed0.get()
        valor_produto = int(ed1.get())
        frete = int(ed2.get())
        despesas = int(ed3.get())
        descontos = int(ed4.get())
        ipi = int(ed5.get())
        aliquota_inter = float(ed6.get())  # inter
        aliquota_intra = int(ed7.get())  # intra
        uf_origem = int(ed8.get())
        uf_destino = int(ed9.get())
        baseicms = valor_produto + frete + despesas - descontos + ipi
        calc_difal = baseicms * ((aliquota_intra - aliquota_inter) / 100)
        difal_origem = calc_difal * (uf_origem / 100)
        difal_destino = calc_difal * (uf_destino / 100)

        c.setFont("Helvetica-Bold", 22)
        c.drawString(200, 790, 'Cálculo Partilha(DIFAL)')

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 700, 'Produto: ' + nome)
        vp_format = f'{valor_produto:,.2f}'
        c.drawString(50, 670, 'Valor:  ' + f'R${str(vp_format)}')
        frete_format = f'{frete:,.2f}'
        c.drawString(50, 640, 'Frete: ' + f'R${str(frete_format)}')
        desc_foramt = f'{descontos:,.2f}'
        c.drawString(50, 610, 'Desconto: ' + f'R${str(desc_foramt)}')
        ipi_format = f'{ipi:,.2f}'
        c.drawString(50, 580, 'IPI: ' + f'R${str(ipi_format)}')
        cd_format = f'{calc_difal:,.2f}'
        c.drawString(50, 550, 'Difal: ' + f'R${str(cd_format)}')
        do_format = f'{difal_origem:,.2f}'
        c.drawString(50, 520, 'Partilha(Origem): ' + f'R${str(do_format)}')
        dd_format = f'{difal_destino:,.2f}'
        c.drawString(50, 490, 'Partilha(Destino): ' + f'R${str(dd_format)}')

        c.rect(20, 470, 560, 270, fill=False, stroke=True)

        c.showPage()
        c.save()
        print_produto()

    def limpa_tela():
        ed0.delete(0, tk.END)
        ed1.delete(0, tk.END)
        ed2.delete(0, tk.END)
        ed3.delete(0, tk.END)
        ed4.delete(0, tk.END)
        ed5.delete(0, tk.END)
        ed6.delete(0, tk.END)
        ed7.delete(0, tk.END)
        ed8.delete(0, tk.END)
        ed9.delete(0, tk.END)

    def difal():
        nome = ed0.get()
        valor_produto = int(ed1.get())
        frete = int(ed2.get())
        despesas = int(ed3.get())
        descontos = int(ed4.get())
        ipi = int(ed5.get())
        aliquota_inter = float(ed6.get())  # inter
        aliquota_intra = int(ed7.get())  # intra
        uf_origem = int(ed8.get())
        uf_destino = int(ed9.get())
        baseicms = valor_produto + frete + despesas - descontos + ipi
        calc_difal = baseicms * ((aliquota_intra - aliquota_inter) / 100)
        difal_origem = calc_difal * (uf_origem / 100)
        difal_destino = calc_difal * (uf_destino / 100)
        listacl.insert("", tk.END, values=(nome, f'R${valor_produto:,.2f}', f'R${frete:,.2f}', f'R${descontos:,.2f}', f'R${ipi:,.2f}', f'R${calc_difal:,.2f}', f'R${difal_origem:,.2f}', f'R${difal_destino:,.2f}'))

    def deleta_calculo():
        item_selecionado = listacl.selection()[0]
        listacl.delete(item_selecionado)

    appdifal = tk.Tk()
    appdifal.title("Calcular Partilha (Difal)")
    appdifal.geometry("1300x500")
    appdifal.iconbitmap("ulianoerochalogo.ico")
    espaco1 = tk.Label(appdifal, text="", width="1000", height="2", bg="black")
    espaco1.place(x="0", y="20")
    espaco2 = tk.Label(appdifal, text="", width="50", height="1000", bg="black")
    espaco2.place(x="0", y="55")
    texto = tk.Label(appdifal, text="Realizando Cálculo de Partilha (Difal)", background="#FFD700")
    texto.pack(fill="x", side="top")
    ed0 = tk.Entry(appdifal)
    ed0.place(x="30", y="100")
    ed1 = tk.Entry(appdifal)
    ed1.place(x="30", y="150")
    ed2 = tk.Entry(appdifal)
    ed2.place(x="30", y="200")
    ed3 = tk.Entry(appdifal)
    ed3.place(x="30", y="250")
    ed4 = tk.Entry(appdifal)
    ed4.place(x="30", y="300")
    ed5 = tk.Entry(appdifal)
    ed5.place(x="30", y="350")
    ed6 = tk.Entry(appdifal)
    ed6.place(x="30", y="400")
    ed7 = tk.Entry(appdifal)
    ed7.place(x="30", y="450")
    ed8 = tk.Entry(appdifal)
    ed8.place(x="30", y="500")
    ed9 = tk.Entry(appdifal)
    ed9.place(x="30", y="550")
    # Botão Limpar
    bt_limpar = tk.Button(appdifal, text="Limpar", command=limpa_tela, bg="black", fg="white")
    bt_limpar.place(x="30", y="580")
    # Botão Adicionar/Calcular
    bt_adicionar = tk.Button(appdifal, text="Adicionar e Calcular ICMS", command=difal, bg="black", fg="white")
    bt_adicionar.place(x="30", y="610")
    # Botão Deletar Cálculo
    bt_deletar = tk.Button(appdifal, text="Deletar Produto", command=deleta_calculo, bg="black", fg="white")
    bt_deletar.place(x="30", y="640")
    # Botão Exportar
    bt_exportar = tk.Button(appdifal, text="Gerar PDF", command=gera_relatorio, bg="black", fg="white")
    bt_exportar.place(x="30", y="670")
    mensagem = tk.Label(appdifal, text="Nome do Produto:", bg="black", fg="white")
    mensagem.place(x="25", y="75")
    mensagem1 = tk.Label(appdifal, text="Valor do Produto(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem1.place(x="25", y="125")
    mensagem2 = tk.Label(appdifal, text="Valor do Frete(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem2.place(x="25", y="175")
    mensagem3 = tk.Label(appdifal, text="Outras Despesas Acessórias(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem3.place(x="25", y="225")
    mensagem4 = tk.Label(appdifal, text="Descontos(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem4.place(x="25", y="275")
    mensagem5 = tk.Label(appdifal, text="Valor do IPI: ", bg="black", fg="white")
    mensagem5.place(x="25", y="325")
    mensagem6 = tk.Label(appdifal, text="Alíquota ICMS Inter: ", bg="black", fg="white")
    mensagem6.place(x="25", y="375")
    mensagem7 = tk.Label(appdifal, text="Valor ICMS Intra do Estado Brasileiro: ", bg="black", fg="white")
    mensagem7.place(x="25", y="425")
    mensagem8 = tk.Label(appdifal, text="UF Origem: ", bg="black", fg="white")
    mensagem8.place(x="25", y="475")
    mensagem9 = tk.Label(appdifal, text="UF Destino: ", bg="black", fg="white")
    mensagem9.place(x="25", y="525")
    listacl = ttk.Treeview(appdifal, height="1", column=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
    listacl.heading("#0", text="")
    listacl.heading("#1", text="Produto")
    listacl.heading("#2", text="Valor")
    listacl.heading("#3", text="Frete")
    listacl.heading("#4", text="Descontos")
    listacl.heading("#5", text="IPI")
    listacl.heading("#6", text="Difal")
    listacl.heading("#7", text="Partilha(Origem)")
    listacl.heading("#8", text="Partilha(Destino)")

    listacl.column("#0", width=0)
    listacl.column("#1", width=130)
    listacl.column("#2", width=70)
    listacl.column("#3", width=70)
    listacl.column("#4", width=70)
    listacl.column("#5", width=90)
    listacl.column("#6", width=80)
    listacl.column("#7", width=100)
    listacl.column("#8", width=100)

    listacl.place(relx="0.26", rely="0.07", relwidth="0.74", relheight="0.99")

    scrolllista = tk.Scrollbar(appdifal, orient="vertical")
    scrolllista.pack(side="right", fill="y")


def calcula_ipi():

    def print_produto():
        webbrowser.open("calculo.pdf")

    def gera_relatorio():
        c = canvas.Canvas("calculo.pdf")

        nome = ed0.get()
        valor_produto = int(ed1.get())
        frete = int(ed2.get())
        seguro = int(ed3.get())
        despesas = int(ed4.get())
        aliquota_tipi = float(ed5.get())
        calculo_base = valor_produto + frete + seguro + despesas
        valor_ipi = calculo_base * (aliquota_tipi / 100)

        c.setFont("Helvetica-Bold", 22)
        c.drawString(200, 790, 'Cálculo IPI')

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 700, 'Produto: ' + nome)
        vp_format = f'{valor_produto:,.2f}'
        c.drawString(50, 670, 'Valor:  ' + f'R${str(vp_format)}')
        frete_format = f'{frete:,.2f}'
        c.drawString(50, 640, 'Frete: ' + f'R${str(frete_format)}')
        seg_format = f'{seguro:,.2f}'
        c.drawString(50, 610, 'Seguro: ' + f'R${str(seg_format)}')
        desp_format = f'{despesas:,.2f}'
        c.drawString(50, 580, 'Despesas Acessórias: ' + f'R${str(desp_format)}')
        c.drawString(50, 550, 'Alíquota(TIPI): ' + f'{str(aliquota_tipi)}%')
        vi_format = f'{valor_ipi:,.2f}'
        c.drawString(50, 520, 'IPI: ' + f'R${str(vi_format)}')

        c.rect(20, 490, 560, 250, fill=False, stroke=True)

        c.showPage()
        c.save()
        print_produto()

    def limpa_tela():
        ed0.delete(0, tk.END)
        ed1.delete(0, tk.END)
        ed2.delete(0, tk.END)
        ed3.delete(0, tk.END)
        ed4.delete(0, tk.END)
        ed5.delete(0, tk.END)

    def base_calculo():
        nome = ed0.get()
        valor_produto = int(ed1.get())
        frete = int(ed2.get())
        seguro = int(ed3.get())
        despesas = int(ed4.get())
        aliquota_tipi = float(ed5.get())
        calculo_base = valor_produto + frete + seguro + despesas
        valor_ipi = calculo_base * (aliquota_tipi / 100)
        listacl.insert("", tk.END, values=(nome, f'R${valor_produto:,.2f}', f'R${frete:,.2f}', f'R${seguro:,.2f}', f'R${despesas:,.2f}', f'R${aliquota_tipi:,.2f}', f'R${valor_ipi:,.2f}'))

    def deleta_calculo():
        item_selecionado = listacl.selection()[0]
        listacl.delete(item_selecionado)

    appipi = tk.Tk()
    appipi.title("Calcular IPI")
    appipi.geometry("1300x500")
    appipi.iconbitmap("ulianoerochalogo.ico")
    espaco1 = tk.Label(appipi, text="", width="1000", height="2", bg="black")
    espaco1.place(x="0", y="20")
    espaco2 = tk.Label(appipi, text="", width="50", height="1000", bg="black")
    espaco2.place(x="0", y="55")
    texto = tk.Label(appipi, text="Realizando Cálculo de IPI", bg="#FFD700")
    texto.pack(fill="x", side="top")
    ed0 = tk.Entry(appipi)
    ed0.place(x="30", y="100")
    ed1 = tk.Entry(appipi)
    ed1.place(x="30", y="150")
    ed2 = tk.Entry(appipi)
    ed2.place(x="30", y="200")
    ed3 = tk.Entry(appipi)
    ed3.place(x="30", y="250")
    ed4 = tk.Entry(appipi)
    ed4.place(x="30", y="300")
    ed5 = tk.Entry(appipi)
    ed5.place(x="30", y="350")
    mensagem = tk.Label(appipi, text="Nome do Produto:", bg="black", fg="white")
    mensagem.place(x="25", y="75")
    mensagem1 = tk.Label(appipi, text="Valor do Produto(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem1.place(x="25", y="125")
    mensagem2 = tk.Label(appipi, text="Valor do Frete(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem2.place(x="25", y="175")
    mensagem3 = tk.Label(appipi, text="Valor do Seguro(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem3.place(x="25", y="225")
    mensagem4 = tk.Label(appipi, text="Outras Despesas Acessórias(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem4.place(x="25", y="275")
    mensagem5 = tk.Label(appipi, text="Alíquota(tabela TIPI pode ser vizualizada no site da receita): ", bg="black", fg="white")
    mensagem5.place(x="25", y="325")
    # Botão Limpar
    bt_limpar = tk.Button(appipi, text="Limpar", command=limpa_tela, bg="black", fg="white")
    bt_limpar.place(x="30", y="385")
    # Botão Adicionar/Calcular
    bt_adicionar = tk.Button(appipi, text="Adicionar e Calcular ICMS", command=base_calculo, bg="black", fg="white")
    bt_adicionar.place(x="30", y="415")
    # Botão Deletar Cálculo
    bt_deletar = tk.Button(appipi, text="Deletar Produto", command=deleta_calculo, bg="black", fg="white")
    bt_deletar.place(x="30", y="445")
    # Botão Exportar
    bt_exportar = tk.Button(appipi, text="Gerar PDF", command=gera_relatorio, bg="black", fg="white")
    bt_exportar.place(x="30", y="475")
    listacl = ttk.Treeview(appipi, height="1", column=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
    listacl.heading("#0", text="")
    listacl.heading("#1", text="Produto")
    listacl.heading("#2", text="Valor")
    listacl.heading("#3", text="Frete")
    listacl.heading("#4", text="Seguro")
    listacl.heading("#5", text="Despesas Acessórias")
    listacl.heading("#6", text="Alíquota(TIPI)")
    listacl.heading("#7", text="IPI")

    listacl.column("#0", width=0)
    listacl.column("#1", width=130)
    listacl.column("#2", width=70)
    listacl.column("#3", width=70)
    listacl.column("#4", width=70)
    listacl.column("#5", width=90)
    listacl.column("#6", width=80)
    listacl.column("#7", width=80)

    listacl.place(relx="0.26", rely="0.07", relwidth="0.74", relheight="0.99")

    scrolllista = tk.Scrollbar(appipi, orient="vertical")
    scrolllista.pack(side="right", fill="y")


def calcula_ibpt():

    def print_produto():
        webbrowser.open("calculo.pdf")

    def gera_relatorio():
        c = canvas.Canvas("calculo.pdf")

        nome = ed0.get()
        num1 = float(ed1.get())
        num2 = float(ed2.get())
        num3 = float(ed3.get())
        num4 = float(ed4.get())
        num5 = float(ed5.get())
        tfppn = num1 * (num2 / 100)
        tfppi = num1 * (num3 / 100)
        te = num1 * (num4 / 100)
        tm = num1 * (num5 / 100)

        c.setFont("Helvetica-Bold", 22)
        c.drawString(200, 790, 'Cálculo IBPT')

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 700, 'Produto: ' + nome)
        valor_format = f'{num1:,.2f}'
        c.drawString(50, 670, 'Valor:  ' + f'R${str(valor_format)}')
        tfppn_format = f'{tfppn:,.2f}'
        c.drawString(50, 640, 'TF Produtos Nacionais: ' + f'R${str(tfppn_format)}')
        tfppi_format = f'{tfppi:,.2f}'
        c.drawString(50, 610, 'TF Produtos Importados: ' + f'R${str(tfppi_format)}')
        td_format = f'{te:,.2f}'
        c.drawString(50, 580, 'Tributação Estadual: ' + f'R${str(td_format)}')
        tm_format = f'{tm:,.2f}'
        c.drawString(50, 550, 'Tributação Municipal: ' + f'R${str(tm_format)}')

        c.rect(20, 525, 560, 200, fill=False, stroke=True)

        c.showPage()
        c.save()
        print_produto()

    def limpa_tela():
        ed0.delete(0, tk.END)
        ed1.delete(0, tk.END)
        ed2.delete(0, tk.END)
        ed3.delete(0, tk.END)
        ed4.delete(0, tk.END)
        ed5.delete(0, tk.END)

    def add_ibpt():
        nome = ed0.get()
        num1 = float(ed1.get())
        num2 = float(ed2.get())
        num3 = float(ed3.get())
        num4 = float(ed4.get())
        num5 = float(ed5.get())
        tfppn = num1 * (num2 / 100)
        tfppi = num1 * (num3 / 100)
        te = num1 * (num4 / 100)
        tm = num1 * (num5 / 100)
        listacl.insert("", tk.END, values=(nome, f'R${num1:,.2f}', f'R${tfppn:,.2f}', f'R${tfppi:,.2f}', f'R${te:,.2f}', f'R${tm:,.2f}'))

    def deleta_calculo():
        item_selecionado = listacl.selection()[0]
        listacl.delete(item_selecionado)

    appibpt = tk.Tk()
    appibpt.title("Calcular IBPT")
    appibpt.geometry("1300x500")
    appibpt.iconbitmap("ulianoerochalogo.ico")
    texto = tk.Label(appibpt, text="Realizando Cálculo de IBPT", bg="#FFD700")
    texto.pack(fill="x", side="top")
    espaco1 = tk.Label(appibpt, text="", width="1000", height="2", bg="black")
    espaco1.place(x="0", y="20")
    espaco2 = tk.Label(appibpt, text="", width="50", height="1000", bg="black")
    espaco2.place(x="0", y="55")
    ed0 = tk.Entry(appibpt)
    ed0.place(x="30", y="75")
    ed1 = tk.Entry(appibpt)
    ed1.place(x="30", y="125")
    ed2 = tk.Entry(appibpt)
    ed2.place(x="30", y="175")
    ed3 = tk.Entry(appibpt)
    ed3.place(x="30", y="225")
    ed4 = tk.Entry(appibpt)
    ed4.place(x="30", y="275")
    ed5 = tk.Entry(appibpt)
    ed5.place(x="30", y="325")
    mensagem = tk.Label(appibpt, text="Nome do Produto:", bg="black", fg="white")
    mensagem.place(x="25", y="50")
    mensagem1 = tk.Label(appibpt, text="Valor do Produto(sem ponto e sem vírgula) R$: ", bg="black", fg="white")
    mensagem1.place(x="25", y="100")
    mensagem2 = tk.Label(appibpt, text="Tributação Federal para Produtos Nacionais: ", bg="black", fg="white")
    mensagem2.place(x="25", y="150")
    mensagem3 = tk.Label(appibpt, text="Tributação Federal para Produtos Importados: ", bg="black", fg="white")
    mensagem3.place(x="25", y="200")
    mensagem4 = tk.Label(appibpt, text="Tributação Estadual: ", bg="black", fg="white")
    mensagem4.place(x="25", y="250")
    mensagem5 = tk.Label(appibpt, text="Tributação municipal: ", bg="black", fg="white")
    mensagem5.place(x="25", y="300")
    # Botão Limpar
    bt_limpar = tk.Button(appibpt, text="Limpar", command=limpa_tela, bg="black", fg="white")
    bt_limpar.place(x="30", y="350")
    # Botão Adicionar/Calcular
    bt_adicionar = tk.Button(appibpt, text="Adicionar e Calcular ICMS", command=add_ibpt, bg="black", fg="white")
    bt_adicionar.place(x="30", y="380")
    # Botão Deletar Cálculo
    bt_deletar = tk.Button(appibpt, text="Deletar Produto", command=deleta_calculo, bg="black", fg="white")
    bt_deletar.place(x="30", y="410")
    # Botão Exportar
    bt_exportar = tk.Button(appibpt, text="Gerar PDF", command=gera_relatorio, bg="black", fg="white")
    bt_exportar.place(x="30", y="440")
    listacl = ttk.Treeview(appibpt, height="1", column=("col1", "col2", "col3", "col4", "col5", "col6"))
    listacl.heading("#0", text="")
    listacl.heading("#1", text="Produto")
    listacl.heading("#2", text="Valor")
    listacl.heading("#3", text="TF Produtos Nacionais")
    listacl.heading("#4", text="TF Produtos Importados")
    listacl.heading("#5", text="Tributação Estadual")
    listacl.heading("#6", text="Tributação Municipal")

    listacl.column("#0", width=0)
    listacl.column("#1", width=100)
    listacl.column("#2", width=70)
    listacl.column("#3", width=70)
    listacl.column("#4", width=70)
    listacl.column("#5", width=90)
    listacl.column("#6", width=80)

    listacl.place(relx="0.26", rely="0.07", relwidth="0.74", relheight="0.99")

    scrolllista = tk.Scrollbar(appibpt, orient="vertical")
    scrolllista.pack(side="right", fill="y")

# Opções #
po = tk.Button(
    text="PIS/COFINS",
    width=15,
    height=3,
    bg="#FFD700",
    fg="black",
    command=calcula_pis_cofins
)
po.place(x="5", y="28")

so = tk.Button(
    text="ICMS",
    width=15,
    height=3,
    bg="#FFD700",
    fg="black",
    command=calcula_icms
)
so.place(x="5", y="110")

to = tk.Button(
    text="Crédito ICMS",
    width=15,
    height=3,
    bg="#FFD700",
    fg="black",
    command=credito_icms
)
to.place(x="5", y="200")

qo = tk.Button(
    text="ICMS ST",
    width=15,
    height=3,
    bg="#FFD700",
    fg="black",
    command=icms_st
)
qo.place(x="5", y="290")

quio = tk.Button(
    text="Partilha (Difal)",
    width=15,
    height=3,
    bg="#FFD700",
    fg="black",
    command=calcula_difal
)
quio.place(x="5", y="380")

seo = tk.Button(
    text="IPI",
    width=15,
    height=3,
    bg="#FFD700",
    fg="black",
    command=calcula_ipi
)
seo.place(x="5", y="470")

seto = tk.Button(
    text="IBPT",
    width=15,
    height=3,
    bg="#FFD700",
    fg="black",
    command=calcula_ibpt
)
seto.place(x="5", y="560")

app.mainloop()
