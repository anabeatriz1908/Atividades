
# 📚 API de Controle de Atividades

Este repositório contém a **API de Atividades**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Atividades é um **microsserviço** que faz parte de um sistema maior de [School System], sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ **Esta API depende de outra API de Gerenciamento Escolar (School System)**, que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se o **Professor** existe (`GET /professores/<id>`)
- 
A Api de gerenciamento escolar, esá disponível no repositório abaixo:

`https://github.com/anabeatriz1908/API-School-System.git`

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (como banco de dados local)
- Requests (para consumo da API externa)
- Docker

---

## ▶️ Como Executar a API localmente

### 1. Clone o repositório

```bash
git clone https://github.com/anabeatriz1908/Atividades.git
cd Atividades
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
📍 localmente --> `http://localhost:5002`


📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 🐳 Como Executar a API com Docker

1. **Clone o repositório**

```bash
git clone https://github.com/anabeatriz1908/Atividades
cd Atividades
```

2. Construa a imagem Docker

```bash
docker build -t atividades .
```

3. Execute o container

```bash
docker run -d -p 5002:5002 atividades
```

4. A aplicação estará disponível em:
📍 `http://localhost:5002`


---

## 📡 Endpoints Principais

- `GET /atividades` – Lista todas as atividades
- `POST /atividades` – Cria uma nova atividade
- `GET /atividades/<id>` – Detalha uma atividade por id


### Exemplo de corpo JSON para criação:

```json
{
  "nome_atividade": "String",
  "descricao": "String",
  "peso_porcento": 0,
  "data_entrega": "String",
  "professor_id": 0
}
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando:

```
localmente --> http://localhost:5036
ou
use o link --> https://apischoolsystem.onrender.com
```

E que os endpoints de `GET /turmas/<id>` estejam funcionando corretamente para que a validação seja feita com sucesso.

---

## 📦 Estrutura do Projeto

```
atividades/
├── clients/
│ ├── client
├── main/
│ ├── atividade_controller.py
│ ├── atividade_model.py
├── app.py
├── config.py
├── readme.md
├── dockerfile
├── .dockerignore
└── requirements.txt
```

---

## 🧑‍💻 Autores

Grupo 10:

Ana Beatriz Silva Santos - RA: 2401228

Luiz Otávio Santos Silva - RA: 2401300

Murillo Rodrigues Santos Pereira - RA: 2400338

Pablo Neves Vavrik - RA: 2400125

Uatila dos Santos Silva - RA: 2400250


– Projeto educativo de arquitetura com Flask e microsserviços.
