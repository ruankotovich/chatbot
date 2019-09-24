import re
import requests
import PyPDF2
from os.path import exists
from datetime import datetime

def all_isupper(text):
    return all([w.isupper() for w in text.split()])


def is_date(text, format='%d/%m/%y'):
    try:
        datetime.strptime(text, format)
        return True
    except ValueError:
        return False


def today():
    return datetime.now().strftime("%m-%d-%Y")


class BNP(object):

    def __init__(self):
        self.download()
        self.parser()

    def download(self):
        url = 'https://www.bnpparibas.com.br/RentabilidadeCotaFundos/Rentabilidade_Diaria.pdf'

        if not exists('/tmp/Rentabilidade_Diaria_{}.pdf'.format(today())):
            print('downloading .pdf')
            download_file = requests.get(url, allow_redirects=True)
            writer = open(
                '/tmp/Rentabilidade_Diaria_{}.pdf'.format(today()), 'wb')
            writer.write(download_file.content)
            writer.close()

        filename = '/tmp/Rentabilidade_Diaria_{}.pdf'.format(today())
        infile = open(filename, 'rb')
        self.pdf_reader = PyPDF2.PdfFileReader(infile)

    def parser(self):
        page = self.pdf_reader.getPage(0)
        data = page.extractText()

        #print(data)
        """
        O extração dos dados consiste no seguinte padrão de valores.
        NOME DO FUNDO: Nome do fundo com todas as letras em maiúsculo.
        DATA DE CRIAÇÃO: Data de criação do fundo no formato dd/mm/aa
        APELIDO: Apelido do fundo com todas as letras em maniúsculo.
        Rentabilidade %: Match exato com a string "Rentabilidade %"
        line +3: Três linas contendo as rentabilidades.
        """

        lines = data.split('\n')
        pivot = 0
        self.fundos = dict()
        self.fundos['current_day'] = lines[1]
        
        for pos, _ in enumerate(lines):
            if pos <= pivot:
                continue

            try:
                content = dict()
                if all_isupper(lines[pos]):
                    content['titulo'] = lines[pos]
                    pivot = pos

                    if is_date(lines[pos+1]):
                        content['inicio'] = lines[pos+1]
                        pivot = pos + 1

                        if all_isupper(lines[pos+2]):
                            content['subtitulo'] = lines[pos+2]
                            pivot = pos + 2

                            if lines[pos+3] == "Rentabilidade %":
                                offset = (pos + 3) + 3

                                text = "".join(lines[pos+3+1: offset])
                                # Dis, Mes, Mes-1, Mes-2....
                                content['rentabilidade'] = re.findall(
                                    r"[-+]*[\d{0,3}].\d{0,3}%", text)[:5]
                                self.fundos[content['titulo']] = content

            except IndexError:
                break

    def data(self):
        return {
            'fund_name': 'FUNDO BNP PARIBAS FIC INFLAÇÃO',
            'current_day': self.fundos['current_day'],
            'daily_profitability': self.fundos['FIC INFLACAO']['rentabilidade'][0], 
            'monthly_profitability': self.fundos['FIC INFLACAO']['rentabilidade'][0],
        }

    
if __name__ == "__main__":    
    bnp = BNP()
    print(bnp.data())