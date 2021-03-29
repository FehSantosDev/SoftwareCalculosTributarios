import tkinter as tk

janela = tk.Tk()
janela.geometry("400x400")

def bt_click():
    print("bt_click")
    num1 = int(ed1.get())
    # num2 = int(ed2.get())

    lb["text"] = num1 * 0.0065

ed1 = tk.Entry(janela)
ed1.place(x="100", y="100")
ed2 = tk.Entry(janela)
ed2.place(x="100", y="130")

bt = tk.Button(janela, text="SOMA", width="20", command=bt_click)
bt.place(x="100", y="150")

lb = tk.Label(janela, text="Labell")
lb.place(x="100", y="200")
janela.mainloop()
