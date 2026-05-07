# Sistema Rede de Cinemas

## Engenharia de Software – Caso Rede de Cinemas

## Requisitos Funcionais

RF01 - O sistema deve permitir o cadastro de cinemas.

RF02 - O sistema deve permitir o cadastro de filmes.

RF03 - O sistema deve permitir o cadastro de sessões.

RF04 - O sistema deve permitir registrar o público de uma sessão.

RF05 - O sistema deve permitir consultar o público por sessão.

RF06 - O sistema deve permitir consultar informações dos filmes, como gênero, diretor e elenco.

## Regras de Negócio

RN01 - O público registrado em uma sessão não pode ultrapassar a capacidade máxima da sala ou cinema.

RN02 - Uma mesma sala não pode possuir duas sessões no mesmo horário.

RN03 - A organização das sessões deve respeitar a duração dos filmes.

RN04 - Deve existir um intervalo obrigatório entre uma sessão e outra.

RN05 - O público deve ser registrado individualmente para cada sessão.

---

## Visão geral do diagrama dos casos de uso


<img width="490" height="569" alt="image" src="https://github.com/user-attachments/assets/a6c4cf60-4159-4970-a195-c01f45844275" />

---

## Diagrama de Classes do Domínio

<img width="200" height="364" alt="image" src="https://github.com/user-attachments/assets/b6928f7a-c01b-4204-9c01-5213504f5186" />

---

## Diagramas de Atividade

<img width="322" height="422" alt="image" src="https://github.com/user-attachments/assets/b0e8b31a-9ec7-47b4-85bf-2ccd3b39d972" />

<img width="389" height="422" alt="image" src="https://github.com/user-attachments/assets/ae2e1513-70bf-46dd-8e43-ebf8b8d3cdd9" />

---

## Diagramas de Sequência

<img width="696" height="570" alt="image" src="https://github.com/user-attachments/assets/820a5c49-a40f-460d-92da-647cbb5d6ee0" />

---

## Implementação

O caso de uso implementado foi o registro de público da sessão.

A implementação foi desenvolvida utilizando a arquitetura MVC com as camadas:
- View
- Controller
- Service
- Repository

O banco de dados utilizado foi o SQLite.

O sistema realiza:
- busca da sessão;
- validação da capacidade;
- atualização do público registrado.

Exemplo de validação implementada:

```python
if publico > sessao.capacidade:
    return "O público não pode ultrapassar a capacidade."

