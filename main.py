import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import pandas as pd
import pywhatkit as kit
import win32com.client as win32
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dados_facebook import listar_campanhas_ativas, coletar_metricas_campanhas

load_dotenv()

TOKEN = os.getenv("ACCESS_TOKEN")
CONTA_ID = os.getenv("ACCOUNT_ID")
VERSAO_API = os.getenv("API_VERSION")
WHATSAPP = os.getenv("WHATSAPP_NUMBER")
EMAIL_DESTINO = os.getenv("EMAIL_DESTINATARIO")

if not TOKEN or not CONTA_ID or not VERSAO_API:
    print("Erro: .env incompleto.")
    sys.exit(1)

def enviar_email(destinatario, assunto, corpo, anexo):
    outlook = win32.Dispatch('outlook.application')
    email = outlook.CreateItem(0)
    email.To = destinatario
    email.Subject = assunto
    email.Body = corpo
    email.Attachments.Add(anexo)
    email.Send()

def enviar_para_google_drive(caminho_arquivo, nome_arquivo):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    arquivo = drive.CreateFile({'title': nome_arquivo})
    arquivo.SetContentFile(caminho_arquivo)
    arquivo.Upload()

def validar_datas(data_inicio, data_fim):
    try:
        inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
        fim = datetime.strptime(data_fim, "%Y-%m-%d")
        if inicio > fim:
            print("Erro: a data inicial é maior que a data final.")
            return False
        return True
    except ValueError:
        print("Erro: formato de data inválido. Use YYYY-MM-DD.")
        return False

def principal(data_inicio, data_fim):
    campanhas_df = listar_campanhas_ativas(TOKEN, CONTA_ID, VERSAO_API)
    if campanhas_df.empty:
        print("Nenhuma campanha encontrada.")
        return

    ids = campanhas_df['id'].tolist()
    metricas_df = coletar_metricas_campanhas(TOKEN, VERSAO_API, ids, data_inicio, data_fim)
    if metricas_df.empty:
        print("Nenhuma métrica encontrada.")
        return

    nome_arquivo = f"relatorio_campanhas_{data_inicio}.xlsx"
    metricas_df.to_excel(nome_arquivo, index=False)

    if WHATSAPP:
        agendamento = datetime.now() + timedelta(minutes=2)
        kit.sendwhatmsg(WHATSAPP, f"Relatório atualizado: {data_inicio} a {data_fim}", agendamento.hour, agendamento.minute)

    if EMAIL_DESTINO:
        assunto = "Relatório de campanhas"
        corpo = f"Relatório gerado para o período {data_inicio} a {data_fim}."
        anexo = os.path.abspath(nome_arquivo)
        enviar_email(EMAIL_DESTINO, assunto, corpo, anexo)

    try:
        enviar_para_google_drive(nome_arquivo, nome_arquivo)
    except Exception as e:
        print(f"Erro no Google Drive: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py <data_inicial> <data_final>")
        sys.exit(1)

    data_inicio = sys.argv[1]
    data_fim = sys.argv[2]

    if validar_datas(data_inicio, data_fim):
        principal(data_inicio, data_fim)
