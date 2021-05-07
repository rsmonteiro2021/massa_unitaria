""" Observe atentamente os dados do projeto e escreva um algorítmo (MEMORIAL DE CÁLCULO) que calcule:
    a) a capacidade de armazenamento total de resíduos brutos e de resíduos beneficiados;
    b) a altura que deverá ter cada pilha de resíduos bruto e beneficiados;
    c) o volume de reíduos beneficiados produzidos em 1 hora de trabalho;
    d) o volume de resíduos beneficiados em um jornada de trabalho;
    d) o tempo necessário para que se tenha todas as pilhas de resíduos beneficiados totalmente preenchidas.
    DADOS:
    A usina deverá conter:
        - 14 pilhas para armazenar os Resíduos Bruto, cada pilha deverá ter diâmetro = 6.8m e capacidade volumétrica = 21.65m³;
        - 05 pilhas para armazenar os Resíduos Beneficiados, cada pilha deverá ter diâmetro = 11.8 m e capacidade volumétrica = 107.8m³;
        - será utilizado um britador com capacidade de produção horária = 100 t/h (considere que serão produzidas 100t de resíudos beneficiados por hora);
        - considere que a massa unitária do material produzido será mu = 1.2 t/m³;
        - considere uma jornada de trabalho de 8h/dia.
    Ao fim do memorial escreva um pequeno relatório dos dados obtidos;
    Considerando que o serviço durará 5 dias de trabalho (5 jornadas) qual ou quais solução (numérica) você adotaria para não parar a produção? 
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
        volume_total = self.volume * self.quantidade
        return volume_total

    def altura_leiras(self):
        """Retorna a altura de cada leira."""
        import math
        area_leira = (math.pi * pow(self.diametro, 2))/4
        altura_leira = self.volume/area_leira
        return altura_leira
class Britador(Leiras):
    """Tentativa de criar uma classe filha referente a um britador."""
    def __init__(self, quantidade, diametro, volume):
        """Retorna a capacidade de produção do britador."""
        self.producao = producao
        self.densidade = densidade
        self.jornada = jornada
    def producao_britador(self):
        """Exibe a produção do britador em horas e numa jornada de trabalho."""
        volume_hora = (self.producao/self.densidade)
        volume_jornada = volume_hora * self.jornada
        print('\t(b) Em uma hora de trabalho serão produzidos %5.3f m³ de resíduos beneficiados;' % volume_hora)
        print('\t(c) Ao final de uma jornada de trabalho serão produzidos %5.2f m³ de resíduos beneficiados.' % volume_jornada)
    
    def producao_hora(self):
        """Retorna a produção do britador em horas e numa jornada de trabalho."""
        volume_hora = (self.producao/self.densidade)
        return volume_hora

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
print('\n----------------ANÁLISE DOS DADOS:----------------')
print('\nSerão utilizadas %5.2f leiras para armazenamento de RCD bruto, com diâmetro de %5.3f m cada.\nPortanto:' % (quantidade_bruto, diametro_bruto))
print('\n1 - Altura das Pilhas de Resíduos e Volume Total Armazenado (Material Bruto):')
print('\t(b) Altura Máxima das Pilhas: %5.3f m;' % leira_bruto.altura_leiras())
print('\t(a) Capacidade de Armazenamento Total: %5.3f m³;' % leira_bruto.volume_leiras())


leira_beneficiado = Leiras(quantidade_beneficiado, diametro_beneficiado, volume_beneficiado)
print('\nSerão utilizadas %5.2f leiras para armazenamento de RCD beneficiado, com diâmetro de %5.3f m cada.\nPortanto:' % (quantidade_beneficiado, diametro_beneficiado))
print('\n2 - Altura das Pilhas de Reciclados e Volume Total Armazenado (Material Beneficiado):')
print('\t(b) Altura das Pilhas: %5.3f m;' % leira_beneficiado.altura_leiras())
print('\t(a) Volume Total: %5.3f m³.' % leira_beneficiado.volume_leiras())

print('\n---- OBSERVAÇÕES:----')
bruto_beneficiado = leira_beneficiado.volume_leiras()/leira_bruto.volume_leiras()
print('\n\t(a) A capacidade de armazenamento de RCD beneficiado é %5.3f vezes a capacidade do RCD bruto.' % bruto_beneficiado)

britador = Britador(producao, densidade, jornada)
britador.producao_britador()

producao_horaria = Britador(producao, densidade, jornada)
x = leira_beneficiado.volume_leiras()/producao_horaria.producao_hora()

print('\t(d) Em %5.2f horas todas as leiras de resíduos beneficados estarão preenchidas.\n' % x)