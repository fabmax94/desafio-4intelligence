# Desafio 4intelligence

Para o desenvolvimento deste desafio, foram considerados 4 camadas:

* models -> Camada responsável por modelar as entidades do desafio
* schemas -> Camada responsável por interfacear os parâmetros de entrada com a camada de modelo (similar a um view model)
* repostiories -> Camada responsável por fazer acessos a base de dados
* main -> Camada responsável por gerenciar os endpoints da aplicação (similar a um controller)


Os endpoints fornecidos seguem esse padrão:
* /providers/<provider_id> (GET) -> Responsável por retornar um JSON com as informações do fornecedor especificado pelo ID
* /providers (POST) -> Responsável por criar um fornecedor especificado no payload
* /providers/<provider_id> (PUT) -> Responsável por atualizar um fornecedor especificado no payload
* /providers/<provider_id> (DELETE) -> Responsável por deletar um fornecedor especificado pelo ID


## Testes

Para testar a solução é necessário instalar as dependências obrigatórias:

`
pip install -r requirements.txt
`

Depois é necessário executar o projeto:

`
uvicorn main:app --reload
`

Com isso, é possível acessar a documentação Swagger através desta URL:

`
http://localhost:8000/docs
`
