from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfessorViewSet, 
    TurmaViewSet, 
    HorarioViewSet, 
    EventoViewSet, 
    PalestraViewSet,
    DisciplinaViewSet
)

router = DefaultRouter()
router.register('professores', ProfessorViewSet)
router.register('turmas', TurmaViewSet)
router.register('horarios', HorarioViewSet)
router.register('eventos', EventoViewSet)
router.register('palestras', PalestraViewSet)
router.register('disciplinas', DisciplinaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
