# 📚 API de Gestão Educacional  
API REST desenvolvida em **Flask**, documentada com **Swagger (Flasgger)** e utilizando arquivos **CSV como banco de dados simples**.  
Permite o gerenciamento completo de:

- 👨‍🎓 **Alunos**
- 👩‍🏫 **Professores**
- 📘 **Cursos**
- 📝 **Avaliações**
- 🧮 **Resultados**
- 🏫 **Matrículas**

---

## 🚀 Tecnologias Utilizadas

- **Python 3+**
- **Flask**
- **Flasgger (Swagger UI)**
- **CSV para persistência de dados**
- Estrutura organizada em:
  - `docs/` → documentação Swagger (YAML)
  - `data/` → dados salvos no csv
  - `utils/` → funções utilitárias
  - `swagger_config.py` → configuração global da documentação

---

## Estrutura do Projeto

```text
├── app.py
├── swagger_config.py
├── utils.py
├── data/
│   ├── alunos.csv
│   ├── professores.csv
│   ├── cursos.csv
│   ├── matriculas.csv
│   ├── avaliacoes.csv
│   └── resultados.csv
├── docs/
│   ├── alunos/
│   │   ├── listar_alunos.yml
│   │   └── criar_aluno.yml
│   ├── professores/
│   │   ├── listar_professores.yml
│   │   └── criar_professor.yml
│   ├── cursos/
│   │   ├── listar_cursos.yml
│   │   └── criar_curso.yml
│   ├── matriculas/
│   │   ├── listar_matriculas.yml
│   │   └── criar_matriculas.yml
│   ├── avaliacoes/
│   │   ├── listar_avaliacoes.yml
│   │   └── criar_avaliacao.yml
│   └── resultados/
│       ├── listar_resultados.yml
│       └── criar_resultado.yml
└── README.md
