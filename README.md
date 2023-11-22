# Sistema de Gerenciamento CRUD para Restaurantes

## Objetivo
Desenvolver um sistema CRUD utilizando um arquivo JSON para "persistir" os dados e aplicar algumas outras funcionalidades que seriam interessantes no sistema.

## Membros da Equipe
- Caio Bueno
- Carlos do Amaral
- Julianna Dantas
- Mauricio Benjamin
- Neto Araújo
- Abel Nandza

## Descrição
Este repositório contém o projeto CRUD para gestão de restaurantes. O sistema permite a criação, leitura, atualização e exclusão de registros de restaurantes e seus respectivos cardápios utilizando um arquivo JSON para armazenamento dos dados.

## Estrutura de Dados
O arquivo JSON contém registros de restaurantes, onde cada um possui:

- Nome (name)
- CNPJ (cnpj)
- Endereço (address)
- Telefone (phone)
- Tempo médio de entrega (time)
- Menu: um objeto contendo pares de pratos e preços.

Exemplo de estrutura JSON:

```json
{
    "1": {
        "name": "Nome do Restaurante",
        "cnpj": "Número do CNPJ",
        "address": "Endereço do Restaurante",
        "phone": "Número de Telefone",
        "time": "Tempo Médio de Entrega em minutos",
        "menu": {
            "Prato 1": "Preço",
            "Prato 2": "Preço"
        }
    }
}
```

## Funcionalidades
- **Criação de dados**: Adiciona novos restaurantes ao arquivo JSON.
- **Leitura de dados**: Exibe informações dos restaurantes cadastrados.
- **Atualização de dados**: Edita informações de restaurantes existentes.
- **Exclusão de dados**: Remove registros de restaurantes do arquivo JSON.
- **Filtragem de dados**: Filtra restaurantes por critérios específicos.
- **Regras de negócio**: Aplica lógicas específicas como cálculo de faturamento baseado em vendas.
- **Estatísticas**: Gera estatísticas a partir dos dados dos restaurantes.

## Como Executar
1. Certifique-se de que o Python está instalado na sua máquina.
2. Clone ou faça o download deste repositório.
3. Navegue até o diretório do projeto via terminal.
4. Execute o arquivo `main.py` com o comando:
    ```
    python main.py
    ```
5. Siga as instruções no terminal para usar o sistema.

## Contribuições
Contribuições são bem-vindas! Para contribuir, por favor siga as diretrizes de contribuição disponíveis em `CONTRIBUTING.md`.

## Licença
Este projeto é licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
