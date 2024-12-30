from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Professor, Turma, Horario, Evento, Palestra, Disciplina
from .serializers import (
    ProfessorSerializer, 
    TurmaSerializer, 
    HorarioSerializer, 
    EventoSerializer, 
    PalestraSerializer,
    DisciplinaSerializer
)

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [AllowAny]

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [AllowAny]

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [AllowAny]

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [AllowAny]

class PalestraViewSet(viewsets.ModelViewSet):
    queryset = Palestra.objects.all()
    serializer_class = PalestraSerializer
    permission_classes = [AllowAny]

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [AllowAny]
