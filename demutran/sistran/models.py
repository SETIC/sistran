from demutran.localizacao.models import *
from demutran.pessoal.models import *
from django.shortcuts import resolve_url as r
from django.utils.html import format_html


class Permissao(models.Model):
    id = models.AutoField(primary_key=True)
    num_permissao = models.IntegerField(null=True, blank=True, verbose_name='Número da Permissão')
    data = models.DateField(auto_now=True)
    TIPO_CONCESSAO_CHOICES = (("TÁXI","TÁXI"), ("ALTERNATIVO","ALTERNATIVO"), ("ESCOLAR","ESCOLAR"), ("FRETE","FRETE"))
    tipo_concessao = models.CharField(max_length=20, choices=TIPO_CONCESSAO_CHOICES, verbose_name='Tipo do Veículo')

    def __str__(self):
        return str(self.num_permissao) + " / " + str(self.tipo_concessao)

    class Meta:
        ordering = ['num_permissao']


class AnexoCidadao(models.Model):
    id = models.AutoField(primary_key=True)
    cidadao = models.ForeignKey('pessoal.Cidadao')
    nome_documento = models.CharField(max_length=255)
    caminho = models.FileField()


class AnexoPermissao(models.Model):
    id = models.AutoField(primary_key=True)
    permissao = models.ForeignKey('Permissao')
    nome_documento = models.CharField(max_length=255)
    caminho = models.FileField()


class Proprietario(models.Model):
    id = models.OneToOneField('pessoal.Cidadao', primary_key=True)

    def __str__(self):
        return self.id


class Motorista(models.Model):
    id = models.OneToOneField('pessoal.Cidadao', primary_key=True)

    def __str__(self):
        return self.id.id.id.nome


class Cobrador(models.Model):
    id = models.OneToOneField('pessoal.Cidadao', primary_key=True)

    def __str__(self):
        return self.id.id.id.nome


class Veiculo(models.Model):
    codigo_renavan = models.BigIntegerField(primary_key=True, verbose_name='Código Renavan')
    veiculo_proprio = models.BooleanField(default=True)
    exercicio = models.CharField(max_length=255, null=False, blank=False, verbose_name='Ano de Exercício')
    placa = models.CharField(max_length=8, blank=False, verbose_name='Placa do Veículo')
    chassi = models.CharField(max_length=255, null=False, blank=False, verbose_name='Chassi do Veículo')
    num_passageiros = models.IntegerField(verbose_name='Número de Passageiros')
    combustivel = models.CharField(max_length=255, blank=False, verbose_name='Combustível')
    MARCA_CHOICES = (("AGRALE","AGRALE"), ("ASTON MARTIN","ASTON MARTIN"), ("AUDI","AUDI"), ("BENTLEY","BENTLEY"), ("BMW","BMW"), ("CHANGAN","CHANGAN"), ("CHERY","CHERY"), ("CHEVROLET","CHEVROLET"), ("CHRYSLER","CHRYSLER"), ("CITROËN","CITROËN"), ("DODGE","DODGE"), ("EFFA","EFFA"), ("FERRARI","FERRARI"), ("FIAT","FIAT"), ("FORD","FORD"), ("GEELY","GEELY"), ("HAFEI","HAFEI"), ("HONDA","HONDA"), ("HYUNDAI","HYUNDAI"), ("IVECO","IVECO"), ("JAC MOTORS","JAC MOTORS"), ("JAGUAR","JAGUAR"), ("JEEP","JEEP"), ("JINBEI","JINBEI"), ("KIA","KIA"), ("LAMBORGHINI","LAMBORGHINI"), ("LAND ROVER","LAND ROVER"), ("LEXUS","LEXUS"), ("LIFAN","LIFAN"), ("MAHINDRA","MAHINDRA"), ("MASERATI","MASERATI"), ("MERCEDES-BENZ","MERCEDES-BENZ"), ("MG MOTORS","MG MOTORS"), ("MINI","MINI"), ("MITSUBISHI","MITSUBISHI"), ("NISSAN","NISSAN"), ("PEUGEOT","PEUGEOT"), ("PORSCHE","PORSCHE"), ("RAM","RAM"), ("RENAULT","RENAULT"), ("SMART","SMART"), ("SSANGYONG","SSANGYONG"), ("SUBARU","SUBARU"), ("SUZUKI","SUZUKI"), ("TOYOTA","TOYOTA"), ("TROLLER","TROLLER"), ("VOLKSWAGEN","VOLKSWAGEN"), ("VOLVO","VOLVO"))
    marca = models.CharField(max_length=255, choices=MARCA_CHOICES, null=False, blank=False, verbose_name='Marca')
    modelo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Modelo')
    ano_fabricacao = models.CharField(max_length=255, null=False, blank=False, verbose_name='Ano de Fabricação')
    ano_modelo = models.CharField(max_length=255, null=True, blank=False, verbose_name='Ano do Modelo')
    CATEGORIA_CHOICES = (("OFICIAL","OFICIAL"), ("REPRESENTAÇÃO DIPLOMÁTICA","REPRESENTAÇÃO DIPLOMÁTICA"), ("PARTICULAR","PARTICULAR"), ("ALUGUEL","ALUGUEL"), ("APRENDIZAGEM","APRENDIZAGEM"))
    categoria = models.CharField(max_length=155, choices=CATEGORIA_CHOICES, verbose_name='Categoria')
    COR_CHOICES = (("BRANCA","BRANCA"), ("PRATA","PRATA"), ("PRETA","PRETA"), ("CINZA","CINZA"), ("VERMELHA","VERMELHA"), ("MARROM","MARROM"), ("BEGE","BEGE"), ("AZUL","AZUL"), ("VERDE","VERDE"), ("AMARELA","AMARELA"), ("DOURADA","DOURADA"))
    cor_predominante = models.CharField(max_length=255, blank=False, choices=COR_CHOICES, verbose_name='Cor Predominante')

    def __str__(self):
        return self.marca + "/" + self.modelo + " - " + self.placa


class PermissaoTemProprietario(models.Model):
    permissao_veiculo = models.ForeignKey('PermissaoTemVeiculo')
    proprietario = models.ForeignKey('Proprietario')
    data_posse = models.DateField(auto_now=True)
    STATUS_CHOICE = (('ATIVO','ATIVO'),	('TRANSFERIDO','TRANSFERIDO'), ('INATIVO','INATIVO'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)


class PermissaoTemVeiculo(models.Model):
    permissao = models.ForeignKey('Permissao')
    veiculo = models.ForeignKey('Veiculo')
    data_posse = models.DateField(auto_now=True)
    STATUS_CHOICE = (('ATIVO','ATIVO'),	('TRANSFERIDO','TRANSFERIDO'), ('INATIVO','INATIVO'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)


class PermissaoTemMotorista(models.Model):
    permissao_veiculo = models.ForeignKey('PermissaoTemVeiculo')
    motorista = models.ForeignKey('Motorista')
    data_posse = models.DateField(auto_now=True)
    STATUS_CHOICE = (('ATIVO','ATIVO'),	('INATIVO','INATIVO'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)


class PermissaoTemCobrador(models.Model):
    permissao_veiculo = models.ForeignKey('PermissaoTemVeiculo')
    cobrador = models.ForeignKey('Cobrador')
    data_posse = models.DateField(auto_now=True)
    STATUS_CHOICE = (('ATIVO','ATIVO'),	('INATIVO','INATIVO'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)


class VistoriaItem(models.Model):
    id = models.AutoField(primary_key=True)
    nome_item = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_item


class Vistoria(models.Model):
    id = models.AutoField(primary_key=True)
    veiculo = models.ForeignKey('Veiculo')
    aprovado = models.BooleanField('aprovado', default=False)
    observacao = models.TextField(max_length=255)
    ordem_servico = models.OneToOneField('OrdemServico', default=False)
    criado_em = models.DateTimeField('criado em', auto_now_add=True, null=True, blank=True)


class VistoriaTemVistoriaItem(models.Model):
    id_vistoria = models.ForeignKey('Vistoria')
    id_vistoria_item = models.ForeignKey('VistoriaItem')


class TipoServico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome


class OrdemServico(models.Model):
    permissao = models.ForeignKey('Permissao')
    tipo_servico = models.ForeignKey('TipoServico')
    data = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField()

    def __str__(self):
        return str(self.permissao) + " " + str(self.tipo_servico)

    def get_label_pago(self):
        status_label = 'warning'
        status_name = 'Aguardando'
        if self.pago:
            status_label = 'success'
            status_name = 'Pago'

        return format_html('<span class="label label-{}">{}</span>',
                           status_label,
                           status_name)

    def get_absolute_url(self):
        return r('ordem_servico_detail', self.pk)