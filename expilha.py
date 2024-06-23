class Pilha:
  class Livro:
    def __init__(self, titulo, autor, paginas):
      self.titulo = titulo
      self.autor = autor
      self.paginas = paginas
      self.proximo = None
      
    def __repr__(self):
      return f"{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
    def __str__(self):
      return self.__repr__()
  
  def __init__(self):
    self.top = None
    self._size = 0
    
  def __len__(self):
    return self._size
  
  def inserir(self, titulo, autor, paginas):
    #insere o elemento no topo da pilha
    livro = self.Livro(titulo, autor, paginas)
    livro.proximo = self.top
    self.top = livro
    self._size = self._size + 1
    return
  
  def retirar(self):
    # remove o elemento da pilha
    if self._size > 0:
      livro = self.top
      self.top = self.top.proximo
      self._size = self._size - 1
      return livro
    raise IndexError("A pilha de livros ta vazia")
    
  def topo(self):
    #retorna o topo da pilha
    if self._size > 0:
      return str(self.top)
    raise IndexError('A pilha de livros ta vazia')
  
  def __repr__(self):
    r = ""
    pointer = self.top
    while(pointer):
      r = r + str(pointer) + "\n"
      pointer = pointer.proximo
    return r
  
pilha = Pilha()
pilha.inserir("Hobbit", "J.R.R.Tolkien", "300")
pilha.inserir("Codigo Limpo", "Robert.C.Marin", "500")
pilha.inserir("Harry Potter", "J.K.Rowling", "650")
print(pilha)