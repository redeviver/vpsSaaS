# ⚡ SaaS VPN + VPS Manager — Cyber Edition

Plataforma SaaS para gerenciamento de VPS e criação de conexões VPN, com autenticação segura e painel web estilo **cyberpunk**.

---

## 🧠 Visão Geral

Este projeto é um **MVP funcional** que combina:

* 🔐 Sistema de autenticação (JWT + bcrypt)
* 🌐 API backend para gerenciamento
* 🧬 Base para criação de VPN (WireGuard-ready)
* 🎨 Dashboard web com estilo cyberpunk
* 🖥️ Controle básico de status de servidor

---

## 🏗️ Arquitetura

```
Frontend (React)
        ↓
Backend API (FastAPI)
        ↓
Banco de dados (SQLite / PostgreSQL)
        ↓
Infra (VPS + WireGuard)
```

---

## 📁 Estrutura do Projeto

```bash
saas-vpn/
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   └── routes/
│       ├── auth.py
│       └── vpn.py
├── frontend/
│   └── src/
│       ├── App.js
│       ├── pages/
│       │   ├── Login.js
│       │   └── Dashboard.js
│       └── services/api.js
```

---

## 🚀 Tecnologias Utilizadas

### Backend

* FastAPI
* SQLAlchemy
* JWT
* Passlib

### Frontend

* React
* Axios

### Infra (planejado)

* WireGuard

---

## ⚙️ Instalação

### 1. Clonar o projeto

```bash
git clone https://seu-repositorio.git
cd saas-vpn
```

---

### 2. Backend

```bash
cd backend

pip install fastapi uvicorn sqlalchemy passlib python-jose

uvicorn main:app --reload
```

API disponível em:

```
http://localhost:8000
```

---

### 3. Frontend

```bash
npx create-react-app frontend
cd frontend

npm install axios

npm start
```

App disponível em:

```
http://localhost:3000
```

---

## 🔐 Autenticação

### Registro

```
POST /register
```

```json
{
  "email": "user@email.com",
  "password": "123456"
}
```

---

### Login

```
POST /login
```

Resposta:

```json
{
  "access_token": "JWT_TOKEN"
}
```

O token é armazenado no navegador e enviado automaticamente nas requisições.

---

## 🎨 Interface (Cyberpunk)

O frontend utiliza:

* fundo escuro
* cores neon (#00ffcc)
* tipografia monospace
* visual minimalista estilo terminal futurista

---

## 📡 Endpoints disponíveis

| Método | Rota        | Descrição          |
| ------ | ----------- | ------------------ |
| POST   | /register   | Criar usuário      |
| POST   | /login      | Autenticar usuário |
| GET    | /vpn/status | Status da VPN      |

---

## 🔒 Segurança

✔ Senhas com hash (bcrypt)
✔ Tokens JWT com expiração
✔ Estrutura pronta para middleware de autenticação

⚠️ Melhorias recomendadas:

* Rate limiting
* HTTPS obrigatório
* Validação de entrada (Pydantic)
* Proteção contra brute force

---

## 🚀 Roadmap

### 🔥 Próximos passos

* [ ] Criar VPN real com WireGuard
* [ ] Gerar QR Code para conexão
* [ ] Multi-servidores VPS
* [ ] Dashboard com gráficos
* [ ] Integração com pagamentos (ex: Stripe)
* [ ] Sistema de planos e limites

---

## ⚠️ Aviso

Este projeto é para:

* aprendizado
* administração de servidores
* desenvolvimento de SaaS

❌ Não deve ser usado para atividades ilegais ou bypass de políticas de rede.

---

## 📄 Licença

MIT License

---

## 👨‍💻 Autor

Projeto desenvolvido como base para um SaaS moderno de VPN + VPS Management.

---

## 💡 Contribuição

Pull requests são bem-vindos.
Sugestões e melhorias também 🚀
