import random


class RaphaelPhrases(object):
    def __init__(self):
        self.phrases = [
            'Tem dia que de noite é foda.',
            'Manaus de noite é um cu... escuro, quente e úmido.',
            'Antes que eu me esqueça... vão tomar no cu',
            'Em chuva de pica, pega a menor e senta',
            'O que é um peido pra quem já tá cagado?',
            'Vão tomar no cu da bunda de vcs',
            'Vcs são muito fuleiros',
            'Fala que é comunista, mas coloca senha no wifi.',
            'Esse aí chora quando escapole!',
            'Dexa eu ver se acho no Google a graça dessa tua piada',
            'Vou digitar com os pés, pois to com as mãos ocupadas aplaudindo tua ignorância.',
            'Vai dar meia hora de cú.',
            'Essa tua cara é tão feia, que trincou o display do meu celular',
            'Porra, tá foda lembrar tudo',
            'Carro, dinheiro e mulher, não se empresta.',
            'Cabeça, joelho e buceta, depois que abre não é mais a mesma coisa.',
            'Quer um pouco de papel higiênico pra passar nessa tua cara de cú?',
            'Joga a mãe, pra ver se vaca voa.',
            'Ta suando mais que tampa de marmita',
            'Os adultos programam e as crianças testam',
            'Acho muito errado quando falam que testador tem que programar testes. Afinal se ele soubesse programar não seria testador.',
            'Cu que não meu, pau nele',
            'Toma um real aqui só pra dizer que essa não foi de graça (ft Xyah)'
        ]

    def predict(self):
        return random.choice(self.phrases)


if __name__ == "__main__":
    raphael = RaphaelPhrases()
    print(raphael.predict())
