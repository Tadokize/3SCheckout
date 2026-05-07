# Atividade Técnica

Projeto desenvolvido como solução para um desafio técnico backend utilizando Python 3.11, Docker e Pytest.

A proposta foi resolver os problemas apresentados mantendo uma estrutura organizada, testes automatizados e foco em legibilidade e manutenção do código.

---

# Tecnologias utilizadas

- Python 3.11
- Pytest
- Docker
- Docker Compose

---

# Estrutura do projeto

A estrutura foi separada por domínio para manter cada questão isolada junto de seus respectivos testes.

```text
src/
├── q1_strings/
├── q2_math/
├── q3_game/
└── q4_payroll/

tests/
├── q1_strings/
├── q2_math/
├── q3_game/
└── q4_payroll/
```

---

# Executando o projeto

## Subir ambiente com Docker

```bash
docker-compose up --build
```

---

# Executando os testes

## Rodar todos os testes

```bash
pytest
```

## Rodar testes com cobertura

```bash
pytest --cov=src
```

---

# Cobertura de testes

Os testes cobrem:
- cenários principais
- validação de entradas
- edge cases
- regras de negócio

Cobertura atual:

```text
TOTAL 99%
```

---

# Algumas decisões técnicas

Durante o desenvolvimento foram aplicadas algumas abordagens pensando em organização e manutenção:

- separação modular por domínio
- uso de type hints
- dataclasses para modelagem de dados
- testes parametrizados com pytest
- validação de tipos e cenários inválidos
- Docker para garantir reprodutibilidade do ambiente

---

# Observações

O projeto foi desenvolvido buscando manter uma abordagem próxima de aplicações backend reais, priorizando clareza, organização e previsibilidade do código.
