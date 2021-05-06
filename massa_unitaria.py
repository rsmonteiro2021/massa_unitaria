""" Cálculo da Capacidade de Produção de uma Usina de Beneficiamento de Resíduos.
Dados obtidos:
    Leiras de Resíduos Bruto:
        volume_bruto = 21.65m³; diâmetro_bruto = 6.8m; quantidade_bruto = 14
    Leiras de Resíduos Beneficiado:
        volume_beneficiado = 107.8m³; diâmetro_beneficiado = 11.8m; quantidade_beneficiado = 5
    densidade_aparente_média (RSD) = 1.20 t/m³; capacidade de produção do britador = 100 t/h
    jornada de trabalho de 8h/dia.
"""

# Leiras de armazenamento de resíduos bruto de geometria cilindrica:

class Leiras():
    """Tentativa de representar uma leira para armazenamento de materiais de construção."""

    def __init__(self, quantidade, diametro, volume):
        """Inicializa os atributos das leiras."""
        self.quantidade = quantidade
        self.diametro = diametro
        self.volume = volume
    
    def volume_leiras(self):
        """Retorna a capacidade total volumétrica das leiras."""
        import math
        area_leira = (math.pi * pow(self.diametro, 2))/4
        volume_total = self.volume * self.quantidade
        return volume_total

    def altura_leiras(self):
        """Retorna a altura de cada leira."""
        import math
        area_leira = (math.pi * pow(self.diametro, 2))/4
        altura_leira = self.volume/area_leira
        return altura_leira
class Britador():
    """Tentativa de criar um britador."""
    def __init__(self, producao, densidade, jornada):
        """Retorna a capacidade de produção do britador."""
        self.producao = producao
        self.densidade = densidade
        self.jornada = jornada
    def producao_britador(self):
        volume_hora = (self.producao/self.densidade)
        volume_jornada = volume_hora * self.jornada
        print('Em uma hora de trabalho serão produzidos ' + str(volume_hora) + 'm³ de resíduos beneficiados;')
        print('Ao final de uma jornada de trabalho serão produzidos ' + str(volume_jornada) + 'm³ de resíduos beneficiados.')

print('\nDigite os dados para as leiras de resíduos BRUTOS:')
quantidade_bruto = float(input('Digite a quantidade de leiras para armazenamento de RCD bruto:\n'))
diametro_bruto = float(input('Digite o diâmetro de cada leira para armazenamento de RCD bruto:\n'))
volume_bruto = float(input('Digite o volume de cada leira para armazenamento de RCD bruto:\n'))
print('\nDigite os dados para as leiras de resíduos BENEFICIADOS:')
quantidade_beneficiado = float(input('Digite a quantidade de leiras para armazenamento de RCD beneficiado:\n'))
diametro_beneficiado = float(input('Digite o diâmetro de cada leira para armazenamento de RCD beneficiado:\n'))
volume_beneficiado = float(input('Digite o volume de cada leira para armazenamento de RCD beneficiado:\n'))
print('\nDigite os Dados do Britador:')
producao = float(input('Digite a capacidade de produção horária do britador (t/h):\n'))
densidade = float(input('Digite a densidade aparente dos resíduos beneficiados (t/m³):\n'))
jornada = float(input('Digite a jornada de trabalho do britador :\n'))


leira_bruto = Leiras(quantidade_bruto, diametro_bruto, volume_bruto)
print('\n\t\t\tANÁLISE DOS DADOS:')
print(f'\nSerão utilizadas {quantidade_bruto} leiras para armazenamento de RCD bruto, com diâmetro de {diametro_bruto}m cada.\nPortanto:')
print('\n1 - Altura das Pilhas de Resíduos e Volume Total Armazenado (Material Bruto):')
print('\t(b) Altura Máxima das Pilhas: ' + str(leira_bruto.altura_leiras()) + 'm;')
print('\t(a) Capacidade de Armazenamento Total: ' + str(leira_bruto.volume_leiras()) + 'm³.')


leira_beneficiado = Leiras(quantidade_beneficiado, diametro_beneficiado, volume_beneficiado)
print(f'\nSerão utilizadas {quantidade_beneficiado} leiras para armazenamento de RCD beneficiado, com diâmetro de {diametro_beneficiado}m cada.\nPortanto:')
print('\n2 - Altura das Pilhas de Reciclados e Volume Total Armazenado (Material Beneficiado):')
print('\t(b) Altura das Pilhas: ' + str(leira_beneficiado.altura_leiras()) + 'm;')
print('\t(a) Volume Total: ' + str(leira_beneficiado.volume_leiras()) + 'm³.')

bruto_beneficiado = volume_beneficiado/volume_bruto
print(f'\nA capacidade de armazenamento de RCD beneficiado é de {bruto_beneficiado} da capacidade do RCD bruto.')

britador = Britador(producao, densidade, jornada)
britador.producao_britador()