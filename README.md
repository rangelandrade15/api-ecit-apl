# Escola API

API REST para gerenciamento de professores, turmas e horários escolares.

## Configuração do Ambiente

1. Crie um ambiente virtual:
```bash
python -m venv venv
```

2. Ative o ambiente virtual:
```bash
venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Execute o servidor:
```bash
python manage.py runserver
```

## Endpoints da API

- `/api/professores/` - Gerenciamento de professores
- `/api/turmas/` - Gerenciamento de turmas
- `/api/horarios/` - Gerenciamento de horários
- `/admin/` - Painel administrativo
