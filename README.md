# Automação de Relatórios Meta Ads — Projeto PEX 2025

[![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-concluído-success)]()

Automação completa de coleta de dados do Facebook/Meta Ads com geração de relatório em Excel, envio automático por WhatsApp (via WhatsApp Web), e-mail via Outlook e integração com o Google Drive para visualização no Looker Studio.

## Sobre o projeto

Este projeto foi desenvolvido como parte da PEX 2025 no curso de Análise e Desenvolvimento de Sistemas. O objetivo é demonstrar automação aplicada ao marketing digital, com foco em integração de dados e geração de relatórios.

## Tecnologias utilizadas

- Python 3.10+
- Facebook Graph API
- Google Drive API (via PyDrive)
- PyWhatKit
- pywin32 (Outlook)
- python-dotenv
- tkinter (interface gráfica)

## Como usar

### Executar pela interface gráfica

1. Verifique se o `.env` está corretamente configurado (baseado no `.env.example`).

2. No terminal:

```bash
python interface.py
```

3. Uma janela será aberta para preencher as datas. Ao clicar em "Gerar Relatório", o sistema executará todo o processo automaticamente.

### Executar via terminal diretamente

```bash
python main.py 2025-03-19 2025-03-25
```

## Estrutura

```
Pex2025/
├── main.py
├── dados_facebook.py
├── interface.py
├── .env.example
├── requirements.txt
├── README.md
└── client_secrets.json  (não versionar)
```

## Funcionalidades

- Coleta de campanhas ativas via API
- Geração de relatório em Excel
- Envio automático por WhatsApp Web
- Envio por e-mail via Outlook (desktop)
- Upload do relatório para o Google Drive
- Interface gráfica com Tkinter

## Segurança

- Variáveis sensíveis estão armazenadas no arquivo `.env`, que é ignorado pelo Git
- O `client_secrets.json` deve ser mantido localmente e fora do versionamento

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
