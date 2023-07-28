import random

#Classe Mãe
class Animal:
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y):
        self.nome = nome
        self.cor = cor
        self.sexo = sexo
        self.velocidade = velocidade
        self.peso = peso
        self.estamina = estamina
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getCor(self):
        return self.cor
    
    def setCor(self, cor):
        self.cor = cor
    
    def getSexo(self):
        return self.sexo
    
    def setSexo(self, sexo):
        self.sexo = sexo
    
    def getVelocidade(self):
        return self.velocidade
    
    def setVelocidade(self, velocidade):
        self.velocidade = velocidade
    
    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso
    
    def getEstamina(self):
        return self.estamina
    
    def setEstamina(self, estamina):
        self.estamina = estamina
    
    def getposição_x(self):
        return self.posição_x
    
    def setposição_x(self, posição_x):
        self.posição_x = posição_x
    
    def getposição_y(self):
        return self.posição_y
    
    def setposição_x(self, posição_y):
        self.posição_y = posição_y
    

    def andar(self, rodada):
        if rodada % 2 == 0:
            if self.posicao_x == 0:
                self.posicao_x += self.velocidade
            elif self.posicao_x == dimensoes_tabuleiro[0]:
                self.posicao_x -= self.velocidade
            else:
                self.posicao_x += self.velocidade if random.choice([True, False]) else -self.velocidade
        else:
            if self.posicao_y == 0:
                self.posicao_y += self.velocidade
            elif self.posicao_y == dimensoes_tabuleiro[1]:
                self.posicao_y -= self.velocidade
            else:
                self.posicao_y += self.velocidade if random.choice([True, False]) else -self.velocidade

        self.estamina -= 1

    def checar_colisao(self, outros_animais):
        for animal in outros_animais:
            if animal.posicao_x == self.posicao_x and animal.posicao_y == self.posicao_y:
                if isinstance(animal, Leao):
                    self.morrer()
                elif isinstance(animal, Cachorro) and isinstance(self, Gato):
                    self.morrer()
                elif isinstance(animal, Cachorro) and isinstance(self, Leao):
                    animal.morrer()

    def imprimir_caracteristicas(self):
        print(f"Nome: {self.nome}")
        print(f"Cor: {self.cor}")
        print(f"Sexo: {self.sexo}")
        print(f"Velocidade: {self.velocidade}")
        print(f"Peso: {self.peso}")
        print(f"Estamina: {self.estamina}")
        print(f"Posição: ({self.posicao_x}, {self.posicao_y})")


    def morrer(self):
        if isinstance(self, Leao):
            print(f"{self.nome} morreu. Rugidos silenciosos preenchem a floresta.")
        elif isinstance(self, Cachorro):
            print(f"{self.nome} morreu. Latidos cessam no ar.")
        elif isinstance(self, Gato):
            print(f"{self.nome} morreu. O miau se perde na brisa.")
        elif isinstance(self, Vaca):
            print(f"{self.nome} morreu. O mugido se cala.")
        elif isinstance(self, Elefante):
            print(f"{self.nome} morreu. A tromba se cala.")
        elif isinstance(self, Coelho):
            print(f"{self.nome} morreu. O mugido se cala.")


#Subclasses
class Leao(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y)
        self.idade = idade

    def rugir(self):
        print("O leão está rugindo!")
    
    def andar(self, rodada):
        super().andar(rodada)
    
    def matar(self, animal):
        if isinstance(animal, Cachorro, Gato, Vaca, Elefante, Coelho):
            animal.morrer()


class Cachorro(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y, raca, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y)
        self.raca = raca
        self.idade = idade

    def latir(self):
        print("O cachorro está latindo!")

    def andar(self, rodada):
        super().andar(rodada)
    
    def matar(self, animal):
        if isinstance(animal, Gato):
            animal.morrer()
    
    def morrer(self):
        self.peso += 1



class Gato(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y)
        self.raca = raca

    def miar(self):
        print("O gato está miando!")

    def andar(self, rodada):
        super().andar(rodada)
    
    def morrer(self):
        self.peso += 1


class Vaca(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y)
        self.raca = raca

    def mugir(self):
        print("A vaca está mugindo!")

    def andar(self, rodada):
        super().andar(rodada)

    def morrer(self):
        self.peso += 1


class Elefante(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y)
        self.raca = raca
    
    def trombar(self):
        print("Trombada do elefante!")
        
    def andar(self, rodada):
        super().andar(rodada)
    
    def morrer(self):
        self.peso += 1


class Coelho(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, posicao_x, posicao_y)
        self.raca = raca
        
    def guinchar(self):
        print("O coelho está guinchando!")
    
    def andar(self, rodada):
        super().andar(rodada)
    
    def morrer(self):
        self.peso += 1


# Definir as dimensões do tabuleiro
dimensoes_tabuleiro = (10, 10)

linhas = 10
colunas = 10

tabuleiro = []

for i in range(linhas):
    linha = [0] * colunas
    tabuleiro.append(linha)

for linha in tabuleiro:
    print(linha)

# Criar os animais
leao = Leao("Leão", "amarelo", "macho", 3, 100, 50, 0, 0, 5)
cachorro = Cachorro("Cachorro", "marrom", "macho", 5, 30, 40, 5, 0, "vira-lata", 3)
gato = Gato("Gato", "preto", "fêmea", 2, 10, 30, 0, 5, "persa")
vaca = Vaca("Vaca", "branca e preta", "fêmea", 1, 200, 60, 5, 5, "holandesa")
elefante = Elefante("Elefante", "cinza", "macho", 1, 800, 60, 5, 5, "elephas maximus")
coelho = Coelho("Coelho", "branco", "macho", 1, 3, 80, 5, 5, "rex")

# Quantidade de rodadas de iteração
rodadas = 5

# Iniciar o jogo
for rodada in range(rodadas):
    leao.andar(rodada)
    cachorro.andar(rodada)
    gato.andar(rodada)
    vaca.andar(rodada)
    elefante.andar(rodada)
    coelho.andar(rodada)

    #Verificar colisões
    outros_animais = [cachorro, gato, vaca, elefante, coelho]  # Animais não leões
    leao.checar_colisao(outros_animais)
    cachorro.checar_colisao(outros_animais)
    gato.checar_colisao(outros_animais)
    vaca.checar_colisao(outros_animais)
    elefante.checar_colisao(outros_animais)
    coelho.checar_colisao(outros_animais)

    #Imprimir características dos animais
    print("--- Rodada", rodada + 1, "---")
    leao.imprimir_caracteristicas()
    cachorro.imprimir_caracteristicas()
    gato.imprimir_caracteristicas()
    vaca.imprimir_caracteristicas()
    elefante.imprimir_caracteristicas()
    coelho.imprimir_caracteristicas()
    print("-" * 20)

#Resultado final
print("----- Resultado Final -----")
leao.imprimir_caracteristicas()
cachorro.imprimir_caracteristicas()
gato.imprimir_caracteristicas()
vaca.imprimir_caracteristicas()
elefante.imprimir_caracteristicas()
coelho.imprimir_caracteristicas()