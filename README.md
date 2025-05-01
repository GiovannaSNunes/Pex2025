# Facebook Campaign Report Automation – Projeto PEX

Este projeto coleta dados de campanhas do Meta Ads (Facebook Ads), gera um relatório em Excel, envia um aviso por WhatsApp e encaminha o relatório por e-mail via Outlook. O relatório também é enviado automaticamente para o Google Drive, permitindo integração com dashboards no Looker Studio.

## Funcionalidades

- Coleta campanhas ativas do Facebook Ads
- Obtém métricas como impressões, cliques, gasto, alcance, entre outras
- Gera relatório `.xlsx` com colunas em português
- Envia aviso automático via WhatsApp
- Envia o relatório por e-mail com anexo via Outlook
- Envia automaticamente o relatório para o Google Drive

## Como usar

### 1. Clone o repositório e instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Configure o arquivo `.env`

Crie um arquivo `.env` com base no modelo abaixo:

```env
ACCESS_TOKEN=SEU_TOKEN_DO_FACEBOOK
ACCOUNT_ID=SEU_ID_DE_CONTA
API_VERSION=vXX.X
WHATSAPP_NUMBER=+55SEUNUMERO
EMAIL_DESTINATARIO=seuemail@empresa.com.br
```

### 3. Configure o acesso ao Google Drive

- Vá até https://console.cloud.google.com/
- Crie um projeto e ative a API do Google Drive
- Crie credenciais do tipo "ID do cliente OAuth" (aplicativo para computador)
- Faça o download do arquivo JSON e salve como `client_secrets.json` na pasta do projeto

### 4. Execute o script

```bash
python main.py 2025-03-19 2025-03-25
```

### 5. Resultado

- Um arquivo chamado `relatorio_campanhas_2025-03-19.xlsx` será salvo
- A mensagem será enviada pelo WhatsApp Web
- O arquivo será enviado por e-mail via Outlook (desktop)
- O relatório será enviado para sua conta do Google Drive

---

**Observações:**
- O WhatsApp Web precisa estar logado na máquina para envio automático
- O Outlook precisa estar instalado e configurado
