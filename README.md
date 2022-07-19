# ascension-api

## Sobre o projeto:

API de um game RPG, na qual cada usuário é um personagem(character), que recebe diversas missões, e a medida que vai completando as missões vai ganhando moedas experiência e subindo de nível.

## Link da documentação da API:

[colocar aqui o link da doc]

## Como rodar o projeto na sua máquina:

Com python instalado e o repositório clonado, rode os seguintes comandos na pasta raiz do projeto para criar e ativar um ambiente virtual:

```
python -m venv venv

source venv/bin/activate
```

Com o ambiente virtual ativado, rode o seguinte comando para instalar as dependências:

```
pip install -r requirements.txt
```

Com as dependências instaladas, rode o seguinte comando para levantar o servidor:

```
./manage.py runserver
```

Agora basta testar os endpoints no insomnia seguindo a documentação:

https://api-ascension.herokuapp.com/api/docs/

## Como rodar os testes do projeto:

Com o ambiente virtual ativado e as dependências instaladas, rode o seguinte comando no terminal, na pasta raiz do projeto:

```
./manage.py test -v2
```

## Como ver a porcentagem de código que os testes estão cobrindo:

Confira no arquivo requirements.txt se o pacote coverage está instalado.
Caso não esteja, com o ambiente virtual ativado, instale-o o comando:

```
pip install coverage
```

Agora rode os testes usando o coverage:

```
coverage run ./manage.py test
```

Após executar os testes com coverage, gere um relatório:

```
coverage report
```
