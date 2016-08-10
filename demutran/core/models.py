from django.db import models


class Documento(models.Model):
    TIPOS = (
        (None, 'Escolha uma opção'),
        ('alvara', 'Alvará'),
        ('transferencia', 'Transferência'),
    )

    arquivo = models.FileField('arquivo', upload_to='arquivos/%Y/%m/%D')
    tipo_documento = models.CharField('tipo de documento', max_length=30, choices=TIPOS)
    codigo = models.CharField('código hash', max_length=50)
    codigo_verificador = models.CharField('código verificador', max_length=5)
    permissao = models.ForeignKey('sistran.Permissao')
    data_emissao = models.DateField('data da emissão', auto_now_add=True)

    def __str__(self):
        return self.codigo
