import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Valor já presente na árvore.")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
        

    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    def height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def min_value(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current.data

    def max_value(self, node):
        current = node
        while(current.right is not None):
            current = current.right
        return current.data

    def internal_path_length(self, node, depth=0):
        if node is None:
            return 0
        else:
            return depth + self.internal_path_length(node.left, depth + 1) + self.internal_path_length(node.right, depth + 1)

    def in_order_traversal(self, start, traversal):
        """Percorre a árvore em ordem: esquerda -> raiz -> direita"""
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal += (str(start.data) + " - ")
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    def pre_order_traversal(self, start, traversal):
        if start:
            traversal += (str(start.data) + " - ")
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    def post_order_traversal(self, start, traversal):
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal += (str(start.data) + " - ")
        return traversal

    def level_order_traversal(self, start):
        if start is None:
            return ""
        queue = deque([start])
        traversal = ""
        while queue:
            node = queue.popleft()
            traversal += (str(node.data) + " - ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return traversal
    
    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if node is None:
            return True

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if abs(left_height - right_height) <= 1 and self._is_balanced(node.left) and self._is_balanced(node.right):
            return True

        return False
    
class MinhaGUI:
    def __init__(self, bst):
        self.bst = bst
        self.root = tk.Tk()
        self.root.title("Árvore Binária de Busca")

        self.configurar_tamanho_tela()

        style = ttk.Style()
        style.configure("TButton", font=("Montserrat", 12), padding=10, borderwidth=3)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.lbl_informacoes_selecionadas = tk.Label(self.frame, text="", font=("Montserrat", 12), justify="left")
        self.lbl_informacoes_selecionadas.pack(pady=10)

        self.mostrar_opcoes()
        self.root.mainloop()

    def configurar_tamanho_tela(self):
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x_pos = int((largura_tela - 500) / 2)
        y_pos = int((altura_tela - 300) / 3)
        self.root.geometry(f"500x400+{x_pos}+{y_pos}")

    def mostrar_opcoes(self):        
        for widget in self.frame.winfo_children():
            widget.destroy()

        lbl_menu = tk.Label(self.frame, text="MENU", font=("Montserrat", 16))
        lbl_menu.pack(pady=10, padx=20)

        btn_inserir = ttk.Button(self.frame, text="INSERIR", command=self.mostrar_inserir, width=20)
        btn_buscar = ttk.Button(self.frame, text="BUSCAR", command=self.mostrar_buscar, width=20)
        btn_informacoes = ttk.Button(self.frame, text="INFORMAÇÕES", command=self.mostrar_informacoes, width=20)
        btn_travessias = ttk.Button(self.frame, text="TRAVESSIAS", command=self.mostrar_travessias, width=20)

        btn_inserir.pack(pady=10)
        btn_buscar.pack(pady=10)
        btn_informacoes.pack(pady=10)
        btn_travessias.pack(pady=10)

    def mostrar_inserir(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        lbl_nome = tk.Label(self.frame, text="Digite o nome abaixo", font=("Montserrat", 12))
        lbl_nome.pack(pady=10)

        entrada_nome = ttk.Entry(self.frame, font=("Montserrat", 12))
        entrada_nome.pack(pady=10)

        btn_inserir = ttk.Button(self.frame, text="Inserir", command=lambda: self.inserir_na_arvore(entrada_nome.get()))
        btn_inserir.pack(pady=10)

        btn_voltar = ttk.Button(self.frame, text="Voltar", command=self.mostrar_opcoes)
        btn_voltar.pack(pady=10)

    def inserir_na_arvore(self, nome):
        if nome == "" or nome.isspace():
            messagebox.showerror("Erro", "Nome em branco.")
        elif(bst.find(nome)):
            messagebox.showerror("Erro", "Nome repetido.")
        else:
            messagebox.showinfo("Sucesso", f'"{nome}" foi inserido com sucesso.')
            self.bst.insert(nome)
        self.mostrar_opcoes()

    def mostrar_buscar(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        lbl_buscar = tk.Label(self.frame, text="Digite o nome que deseja buscar", font=("Montserrat", 12))
        lbl_buscar.pack(pady=10)

        entrada_busca = ttk.Entry(self.frame, font=("Montserrat", 12))
        entrada_busca.pack(pady=10)

        btn_buscar = ttk.Button(self.frame, text="Buscar", command=lambda: self.mensagem_busca(entrada_busca.get()))
        btn_buscar.pack(pady=10)

        btn_voltar = ttk.Button(self.frame, text="Voltar", command=self.mostrar_opcoes)
        btn_voltar.pack(pady=10)


    def mensagem_busca(self, termo):
        resultado = self.bst.find(termo)
        if resultado:
            messagebox.showinfo("Resultado da Busca", f'"{termo}" está na árvore')
        else:
            messagebox.showerror("Resultado da Busca", f'"{termo}" não está na árvore')
        self.mostrar_opcoes()
  
    def mostrar_informacoes(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        if self.bst.root is None:
            messagebox.showerror("Erro", "Árvore vazia.")
            self.mostrar_opcoes()
            return

        size_var = tk.BooleanVar()
        height_var = tk.BooleanVar()
        min_value_var = tk.BooleanVar()
        max_value_var = tk.BooleanVar()
        internal_path_length_var = tk.BooleanVar()
        is_balanced_var = tk.BooleanVar()

        chk_size = tk.Checkbutton(self.frame, text="Tamanho", variable=size_var, font=("Montserrat", 12), anchor="w")
        chk_size.pack(pady=5)

        chk_height = tk.Checkbutton(self.frame, text="Altura", variable=height_var, font=("Montserrat", 12), anchor="w")
        chk_height.pack(pady=5)

        chk_min_value = tk.Checkbutton(self.frame, text="Menor valor", variable=min_value_var, font=("Montserrat", 12), anchor="w")
        chk_min_value.pack(pady=5)

        chk_max_value = tk.Checkbutton(self.frame, text="Maior valor", variable=max_value_var, font=("Montserrat", 12), anchor="w")
        chk_max_value.pack(pady=5)

        chk_internal_path_length = tk.Checkbutton(self.frame, text="Comprimento interno", variable=internal_path_length_var, font=("Montserrat", 12), anchor="w")
        chk_internal_path_length.pack(pady=5)

        chk_is_balanced = tk.Checkbutton(self.frame, text="Balanceada", variable=is_balanced_var, font=("Montserrat", 12), anchor="w")
        chk_is_balanced.pack(pady=5)

        btn_mostrar_selecionados = ttk.Button(self.frame, text="Mostrar Selecionados", command=lambda: self.mostrar_selecionados(size_var.get(), height_var.get(), min_value_var.get(), max_value_var.get(), internal_path_length_var.get(), is_balanced_var.get()))
        btn_mostrar_selecionados.pack(pady=10)

        btn_voltar = ttk.Button(self.frame, text="Voltar", command=self.mostrar_opcoes)
        btn_voltar.pack(pady=5)

    def mostrar_selecionados(self, size, height, min_value, max_value, internal_path_length, is_balanced):
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Construir uma string com base nas informações selecionadas
        texto_informacoes = ""
        if size:
            texto_informacoes += f"Tamanho: {self.bst.size(self.bst.root)}\n"
        if height:
            texto_informacoes += f"Altura: {self.bst.height(self.bst.root)}\n"
        if min_value:
            texto_informacoes += f"Menor valor: {self.bst.min_value(self.bst.root)}\n"
        if max_value:
            texto_informacoes += f"Maior valor: {self.bst.max_value(self.bst.root)}\n"
        if internal_path_length:
            texto_informacoes += f"Comprimento interno: {self.bst.internal_path_length(self.bst.root)}\n"
        if is_balanced:
            texto_informacoes += f"Balanceada: {'Sim' if self.bst.is_balanced() else 'Não'}\n"

        lbl_selecionados = tk.Label(self.frame, text=texto_informacoes, font=("Montserrat", 12), anchor="w")
        lbl_selecionados.pack(pady=10)

        btn_voltar = ttk.Button(self.frame, text="Voltar", command=self.mostrar_opcoes, width=20)
        btn_voltar.pack(pady=10)

    def mostrar_travessias(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        if self.bst.root is None:
            messagebox.showerror("Erro", "Árvore vazia.")
            self.mostrar_opcoes()
            return
        
        btn_pre_ordem = ttk.Button(self.frame, text="Pré Ordem", command=self.travessia_pre_ordem, width=20)
        btn_em_ordem = ttk.Button(self.frame, text="Em Ordem", command=self.travessia_em_ordem, width=20)
        btn_pos_ordem = ttk.Button(self.frame, text="Pós Ordem", command=self.travessia_pos_ordem, width=20)
        btn_level_order = ttk.Button(self.frame, text="Level Order", command=self.travessia_level_order, width=20)

        btn_pre_ordem.pack(pady=10)
        btn_em_ordem.pack(pady=10)
        btn_pos_ordem.pack(pady=10)
        btn_level_order.pack(pady=10)

        btn_voltar = ttk.Button(self.frame, text="Voltar", command=self.mostrar_opcoes, width=20)
        btn_voltar.pack(pady=10)

    def mostrar_resultado_travessia(self, titulo, resultado):
        for widget in self.frame.winfo_children():
            widget.destroy()

        lbl_titulo = tk.Label(self.frame, text=titulo, font=("Montserrat", 16))
        lbl_titulo.pack(pady=10)

        txt_resultado = tk.Text(self.frame, wrap="word", font=("Montserrat", 12), height=10, width=40)
        txt_resultado.insert(tk.END, resultado)
        txt_resultado.config(state="disabled")
        txt_resultado.pack(pady=10)

        btn_voltar = ttk.Button(self.frame, text="Voltar", command=self.mostrar_opcoes, width=20)
        btn_voltar.pack(pady=10)


    def travessia_pre_ordem(self):
        result = self.bst.pre_order_traversal(self.bst.root, "")
        self.mostrar_resultado_travessia("Travessia Pré-Ordem", result)

    def travessia_em_ordem(self):
        result = self.bst.in_order_traversal(self.bst.root, "")
        self.mostrar_resultado_travessia("Travessia Em Ordem", result)

    def travessia_pos_ordem(self):
        result = self.bst.post_order_traversal(self.bst.root, "")
        self.mostrar_resultado_travessia("Travessia Pós Ordem", result)

    def travessia_level_order(self):
        result = self.bst.level_order_traversal(self.bst.root)
        self.mostrar_resultado_travessia("Travessia Level Order", result)

bst = BinarySearchTree()
app = MinhaGUI(bst)
