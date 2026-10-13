# Extração de Tabelas Logísticas

Projeto de estudo em Python para automação de web scraping com Selenium. O script acessa uma página web, extrai os dados de uma tabela HTML, converte-os em um `DataFrame` do pandas e exporta o resultado para uma planilha Excel.

> ⚠️ Projeto criado apenas para fins de estudo/aprendizado de web scraping, Selenium e manipulação de dados com pandas.

## Funcionalidades

- Abre o navegador Chrome via Selenium e acessa a página de exemplo [the-internet.herokuapp.com/tables](https://the-internet.herokuapp.com/tables).
- Localiza a tabela (`table1`) e percorre todas as linhas do corpo (`tbody`), extraindo o texto de cada célula.
- Monta um `DataFrame` do pandas com as colunas: `Sobrenome`, `Nome`, `Email`, `Valor`, `Site`, `Acoes`.
- Converte a coluna `Valor` (originalmente em formato monetário, ex: `$100`) para um tipo numérico.
- Exporta os dados para um arquivo Excel em `~/Downloads/relatorios_logisticos/relatorio_tabelas.xlsx`.
- Exibe no terminal a tabela extraída e os tipos de dados de cada coluna.

## Pré-requisitos

- Python 3.10+
- Google Chrome instalado (o Selenium Manager cuida automaticamente do ChromeDriver compatível)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Ronyfranzini84/extracao_tabelas_logisticas.git
   cd extracao_tabelas_logisticas
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como usar

Execute o script principal:

```bash
python main.py
```

O Chrome será aberto automaticamente, os dados da tabela serão extraídos e exibidos no terminal, e a planilha Excel será salva em `~/Downloads/relatorios_logisticos/relatorio_tabelas.xlsx`.

## Estrutura do projeto

```
extracao_tabelas_logisticas/
├── main.py            # Script principal: scraping, tratamento e exportação dos dados
├── scraper.py          # Reservado para futura modularização do código de scraping
├── requirements.txt    # Dependências do projeto
└── README.md
```

## Dependências principais

- [Selenium](https://www.selenium.dev/) — automação do navegador e extração dos dados da página.
- [pandas](https://pandas.pydata.org/) — manipulação e tratamento dos dados extraídos.
- [openpyxl](https://openpyxl.readthedocs.io/) — exportação dos dados para o formato `.xlsx`.

## Próximos passos (ideias de estudo)

- Mover a lógica de scraping para `scraper.py`, deixando `main.py` responsável apenas pela orquestração.
- Adicionar tratamento de erros e logs.
- Parametrizar a URL e o caminho de saída via argumentos de linha de comando ou variáveis de ambiente.
- Adicionar testes automatizados.
