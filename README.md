# Como rodar as ferramentas de Qualidade:

Requisitos de sistema:
- Python

## 1)Crie o ambiente virtual usando esse comando:
```
python -m venv venv
```

## 2)Acesse o ambiente virtual com esse comando:
- Windows
```
source venv/scripts/activate
```
- Linux
```
source venv/bin/activate
```

## 3)Instale as dependências(Teste e Linters):
```
pip install -r requirements.txt
```

# Agora vamos aos testes e linters:

# Para manter a qualidade e confiabilidade do código, utilizei o Pytest para a criação de alguns testes unitários

## Para rodar os testes unitários rode esse comando no seu terminal:
```
pytest
```
## Observação: Temos todos os métodos testados (98% de cobertura)

## Para ver a porcentagem e também gerar um relatório em HTML para ver oque foi coberto pelos testes unitários, basta executar o comando abaixo no seu terminal:
```
coverage run -m pytest && coverage report -m && coverage html
```
## Após rodar esse comando basta abrir com seu navegador o arquivo que se localiza na pasta htmlcov chamado index.html

## Para rodar o Flake8 para validar que o código segue os padrões PEP8 basta rodar o comando abaixo no seu terminal:
```
flake8 src/
```
