Repositório para desenvolvimento de Atividades, com Flask.

Grupo 10:

Ana Beatriz Silva Santos - 2401228
Luiz Otávio RA: 2401300
Murillo Rodrigues Santos Pereira - 2400338
Pablo Vavrik RA: 2400125
Uatila dos Santos Silva - 2400250


# 📚 API de Controle de Atividades

Este repositório contém a **API de Atividades**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Atividades é um **microsserviço** que faz parte de um sistema maior de [School System](#colocar link do nosso github), sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ **Esta API depende de outra API de Gerenciamento Escolar (School System)**, que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se a **Turma** existe (`GET /turmas/<id>`)

A Api de gerenciamento escolar, está disponivél no repositório listado abaixo.

https://github.com/anabeatriz1908/API-School-System.git


---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (como banco de dados local)
- Requests (para consumo da API externa)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/anabeatriz1908/Atividades.git
cd reserva-salas
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:5002`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

- `GET /atividades` – Lista todas as atividades
- `POST /atividades` – Cria uma nova atividade
- `GET /atividades/<id>` – Detalha uma atividade


### Exemplo de corpo JSON para criação:

```json
{
  "turma_id": 1,
  "sala": "101",
  "data": "2025-05-06",
  "hora_inicio": "14:00",
  "hora_fim": "16:00"
}
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando em:

```
http://localhost:5036
```

E que os endpoints de `GET /turmas/<id>` (e opcionalmente `GET /alunos/<id>`) estejam funcionando corretamente para que a validação seja feita com sucesso.

---

## 📦 Estrutura do Projeto

```
atividades/
├── clients/
├── main/
│ ├── atividade_controller.py
│ ├── atividade_model.py
├── app.py
├── config.py
├── readme.md
└── requirements.txt
```

---

## 🧑‍💻 Autores

Ana Beatriz Silva Santos - RA: 2401228

Luiz Otávio Santos Silva - RA: 2401300

Murillo Rodrigues Santos Pereira - RA: 2400338

Pablo Neves Vavrik - RA: 2400125

Uatila dos Santos Silva - RA: 2400250

– Projeto educativo de arquitetura com Flask e microsserviços.
