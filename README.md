# Atualizador de Pacotes com Winget

Este script em Python automatiza a verificação e instalação de atualizações de pacotes no Windows utilizando o **Winget**. Além disso, ele mantém um registro detalhado do processo em um arquivo de log localizado em `C:\Logs`.

## Requisitos

- Windows 10 ou superior com **Winget** instalado
- Permissões administrativas para executar o script

## Funcionalidades

- Lista os pacotes que possuem atualizações disponíveis usando o comando `winget upgrade`
- Registra logs detalhados no arquivo `C:\Logs\atualizacao_winget.txt`
- Atualiza automaticamente todos os pacotes disponíveis de forma silenciosa
- Filtra mensagens irrelevantes da saída do Winget para melhor leitura

## Como Usar

1. Baixe o script e salve-o em um diretório de sua escolha.
2. Execute o script no prompt de comando como administrador.
3. O progresso e os resultados serão registrados no arquivo de log localizado em `C:\Logs\atualizacao_winget.txt`.

## Personalização

Caso queira alterar o diretório onde os logs são salvos, modifique a variável responsável por definir o caminho do diretório no código-fonte.

## Contribuição

Se desejar sugerir melhorias ou relatar problemas, abra uma **Issue** neste repositório.