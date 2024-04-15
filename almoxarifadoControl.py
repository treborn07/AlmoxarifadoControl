import tkinter as tk

class LoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.label = tk.Label(master, text="Login de Trabalhador")
        self.label.pack()

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Aqui você pode adicionar lógica para verificar o nome de usuário e senha
        if username == "admin" and password == "admin":
            self.master.destroy()  # Fecha a janela de login
            root = tk.Tk()
            app = MainApp(root)
            root.mainloop()
        else:
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            print("Login falhou. Tente novamente.")

class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Controle de Almoxarifado")

        self.label = tk.Label(master, text="Bem-vindo ao Controle de Almoxarifado")
        self.label.pack()

        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack()

        self.cadastrar_item_button = tk.Button(self.menu_frame, text="Cadastrar Item", command=self.abrir_cadastro_item)
        self.cadastrar_item_button.pack(side=tk.LEFT)

        self.fazer_pedido_button = tk.Button(self.menu_frame, text="Fazer Pedido", command=self.abrir_fazer_pedido)
        self.fazer_pedido_button.pack(side=tk.LEFT)

        self.cadastrar_transportadora_button = tk.Button(self.menu_frame, text="Cadastrar Transportadora", command=self.abrir_cadastro_transportadora)
        self.cadastrar_transportadora_button.pack(side=tk.LEFT)

        self.consultar_cadastrados_button = tk.Button(self.menu_frame, text="Consultar Cadastros", command=self.consultar_cadastrados)
        self.consultar_cadastrados_button.pack(side=tk.LEFT)

        self.logout_button = tk.Button(master, text="Logout", command=self.logout)
        self.logout_button.pack()

        self.itens_cadastrados = []  # Lista para armazenar os itens cadastrados

    def abrir_cadastro_item(self):
        self.new_window = tk.Toplevel(self.master)
        self.cadastro_item_window = CadastroItemApp(self.new_window, self.itens_cadastrados)

    def abrir_fazer_pedido(self):
        self.new_window = tk.Toplevel(self.master)
        self.fazer_pedido_window = FazerPedidoApp(self.new_window)

    def abrir_cadastro_transportadora(self):
        self.new_window = tk.Toplevel(self.master)
        self.cadastro_transportadora_window = CadastroTransportadoraApp(self.new_window)

    def consultar_cadastrados(self):
        self.new_window = tk.Toplevel(self.master)
        self.consultar_cadastrados_window = ConsultaCadastradosApp(self.new_window, self.itens_cadastrados)

    def logout(self):
        self.master.destroy()  # Fecha a janela principal
        root = tk.Tk()
        app = LoginApp(root)
        root.mainloop()

class CadastroItemApp:
    def __init__(self, master, itens_cadastrados):
        self.master = master
        self.itens_cadastrados = itens_cadastrados
        master.title("Cadastro de Item")

        self.label = tk.Label(master, text="Cadastre um novo item")
        self.label.pack()

        self.nome_label = tk.Label(master, text="Nome:")
        self.nome_label.pack()

        self.nome_entry = tk.Entry(master)
        self.nome_entry.pack()

        self.quantidade_label = tk.Label(master, text="Quantidade:")
        self.quantidade_label.pack()

        self.quantidade_entry = tk.Entry(master)
        self.quantidade_entry.pack()

        self.localizacao_label = tk.Label(master, text="Localização:")
        self.localizacao_label.pack()

        self.localizacao_entry = tk.Entry(master)
        self.localizacao_entry.pack()

        self.cadastrar_button = tk.Button(master, text="Cadastrar", command=self.cadastrar_item)
        self.cadastrar_button.pack()

    def cadastrar_item(self):
        nome = self.nome_entry.get()
        quantidade = self.quantidade_entry.get()
        localizacao = self.localizacao_entry.get()
        # Aqui você pode adicionar a lógica para cadastrar o item
        novo_item = {"Nome": nome, "Quantidade": quantidade, "Localização": localizacao}
        self.itens_cadastrados.append(novo_item)
        print(f"Item cadastrado: {novo_item}")
        self.master.destroy()

class FazerPedidoApp:
    def __init__(self, master):
        self.master = master
        master.title("Fazer Pedido")

        self.label = tk.Label(master, text="Faça um novo pedido")
        self.label.pack()

        # Aqui você pode adicionar os widgets para capturar informações do pedido

class CadastroTransportadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Transportadora")

        self.label = tk.Label(master, text="Cadastre uma nova transportadora")
        self.label.pack()

        # Aqui você pode adicionar os widgets para capturar informações da transportadora

class ConsultaCadastradosApp:
    def __init__(self, master, itens_cadastrados):
        self.master = master
        self.itens_cadastrados = itens_cadastrados
        master.title("Itens Cadastrados")

        self.label = tk.Label(master, text="Itens Cadastrados:")
        self.label.pack()

        self.lista_itens = tk.Text(master, width=40, height=10)
        self.lista_itens.pack()

        self.mostrar_itens()

    def mostrar_itens(self):
        for item in self.itens_cadastrados:
            self.lista_itens.insert(tk.END, f"Nome: {item['Nome']}, Quantidade: {item['Quantidade']}, Localização: {item['Localização']}\n")
        self.lista_itens.config(state=tk.DISABLED)

root = tk.Tk()
app = LoginApp(root)
root.mainloop()
