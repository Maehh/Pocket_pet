import json


class animal_generator:
    nome_cientifico = 'Canis lupus familiaris'
    ano_atual = 2023

    def __init__(self, nome, idade=0, raca=None, genero=None):
        self.nome = nome     
        self.idade = idade  
        self.raca = raca    
        self.genero = genero
  #test
    
    def get_idade_cachorro(self):
        return animal_generator.ano_atual - self.idade

    def registrar_dog(self, acrchive_name):
        with open(f'{acrchive_name}.json', 'w+', encoding='utf8') as file:
            json.dump(vars(self), file, ensure_ascii=False)


def importar_dog(archive_name_load):
    with open(f'{archive_name_load}', 'r') as file:
        return animal_generator(**json.load(file))
