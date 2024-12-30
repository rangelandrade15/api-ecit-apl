from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    formacao_academica = models.CharField(max_length=200, blank=True, default='')
    foto = models.ImageField(upload_to='professores/', blank=True, null=True, verbose_name='Foto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['nome']

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['nome']

class Horario(models.Model):
    DIAS_SEMANA = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]

    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='horarios')
    dia_semana = models.CharField(max_length=3, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.turma.nome} - {self.get_dia_semana_display()} ({self.hora_inicio} - {self.hora_fim})"

    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'
        ordering = ['dia_semana', 'hora_inicio']
        unique_together = ['turma', 'dia_semana', 'hora_inicio']

class Evento(models.Model):
    TIPO_EVENTO = [
        ('AULA_EXTRA', 'Aula Extra'),
        ('REUNIAO', 'Reunião'),
        ('WORKSHOP', 'Workshop'),
        ('PALESTRA', 'Palestra'),
        ('OUTRO', 'Outro'),
    ]

    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    tipo = models.CharField(max_length=20, choices=TIPO_EVENTO, verbose_name='Tipo')
    data = models.DateField(verbose_name='Data')
    hora_inicio = models.TimeField(verbose_name='Hora de Início')
    hora_fim = models.TimeField(verbose_name='Hora de Término')
    local = models.CharField(max_length=200, verbose_name='Local')
    turmas = models.ManyToManyField(Turma, related_name='eventos', blank=True, verbose_name='Turmas')
    professor_responsavel = models.ForeignKey(
        Professor, 
        on_delete=models.CASCADE, 
        related_name='eventos', 
        verbose_name='Professor Responsável'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.data}"

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['data', 'hora_inicio']

class Palestra(models.Model):
    CATEGORIA_CHOICES = [
        ('TECNOLOGIA', 'Tecnologia'),
        ('EDUCACAO', 'Educação'),
        ('SAUDE', 'Saúde'),
        ('CARREIRA', 'Carreira'),
        ('MOTIVACIONAL', 'Motivacional'),
        ('OUTRO', 'Outro'),
    ]

    titulo = models.CharField(max_length=200, verbose_name='Título')
    palestrante = models.CharField(max_length=100, verbose_name='Palestrante')
    email_palestrante = models.EmailField(verbose_name='E-mail do Palestrante', blank=True)
    telefone_palestrante = models.CharField(max_length=15, verbose_name='Telefone do Palestrante', blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, verbose_name='Categoria')
    descricao = models.TextField(verbose_name='Descrição')
    data = models.DateField(verbose_name='Data')
    hora_inicio = models.TimeField(verbose_name='Hora de Início')
    hora_fim = models.TimeField(verbose_name='Hora de Término')
    local = models.CharField(max_length=200, verbose_name='Local')
    capacidade = models.PositiveIntegerField(verbose_name='Capacidade de Participantes')
    publico_alvo = models.TextField(verbose_name='Público Alvo')
    requisitos = models.TextField(verbose_name='Requisitos', blank=True, help_text='Requisitos ou materiais necessários para participar')
    turmas_convidadas = models.ManyToManyField(Turma, related_name='palestras', blank=True, verbose_name='Turmas Convidadas')
    professor_responsavel = models.ForeignKey(
        Professor, 
        on_delete=models.CASCADE, 
        related_name='palestras', 
        verbose_name='Professor Responsável'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.palestrante} ({self.data})"

    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'
        ordering = ['data', 'hora_inicio']
        unique_together = ['data', 'hora_inicio', 'local']

class Disciplina(models.Model):
    DIAS_SEMANA = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]

    nome = models.CharField(max_length=100, verbose_name='Nome da Disciplina')
    professor = models.ForeignKey(
        Professor, 
        on_delete=models.CASCADE, 
        related_name='disciplinas',
        verbose_name='Professor'
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='disciplinas',
        verbose_name='Turma'
    )
    dia_semana = models.CharField(
        max_length=3,
        choices=DIAS_SEMANA,
        verbose_name='Dia da Semana'
    )
    hora_inicio = models.TimeField(verbose_name='Hora de Início')
    hora_fim = models.TimeField(verbose_name='Hora de Término')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.turma.nome} - {self.professor.nome} - {self.get_dia_semana_display()}"

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['dia_semana', 'hora_inicio']
        unique_together = ['turma', 'dia_semana', 'hora_inicio']  # Evita conflitos de horário
