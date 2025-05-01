import requests
import pandas as pd
import json
import sys

def listar_campanhas_ativas(token, conta_id, versao_api):
    try:
        url = f"https://graph.facebook.com/{versao_api}/act_{conta_id}/campaigns"
        campos = ['id', 'name', 'account_id', 'start_time', 'updated_time', 'status']
        parametros = {
            'limit': 100,
            'fields': ','.join(campos),
            'access_token': token
        }
        resposta = requests.get(url, params=parametros)
        conteudo = resposta.json()
        if resposta.status_code == 200:
            campanhas = [c for c in conteudo['data'] if c['status'] not in ['DELETED', 'ARCHIVED']]
            return pd.DataFrame(campanhas)
        else:
            print("Erro ao obter campanhas:", conteudo)
            return pd.DataFrame()
    except Exception as e:
        print(f"Erro na função listar_campanhas_ativas: {e}")
        return pd.DataFrame()

def coletar_metricas_campanhas(token, versao_api, ids_campanhas, data_inicio, data_fim):
    campos = [
        'date_start', 'campaign_name', 'spend', 'clicks', 'impressions', 'reach', 'cpm',
        'actions', 'ad_name', 'adset_name'
    ]

    dados = []
    for campanha_id in ids_campanhas:
        url = f"https://graph.facebook.com/{versao_api}/{campanha_id}/insights"
        parametros = {
            "access_token": token,
            "fields": ','.join(campos),
            "time_range": json.dumps({"since": data_inicio, "until": data_fim}),
            "time_increment": "1",
            "limit": "500"
        }
        resposta = requests.get(url, params=parametros)
        if resposta.status_code == 200:
            registros = resposta.json().get('data', [])
            for item in registros:
                acoes = {
                    'Leads': 0,
                    'Conversas Iniciadas': 0,
                    'Cliques no Link': 0,
                    'Visualizações da Página de Destino': 0,
                    'Compartilhamentos': 0,
                    'Salvamentos': 0,
                    'Comentários': 0
                }
                mapa_acoes = {
                    'lead': 'Leads',
                    'messaging_conversation_started_7d': 'Conversas Iniciadas',
                    'link_click': 'Cliques no Link',
                    'landing_page_view': 'Visualizações da Página de Destino',
                    'post_share': 'Compartilhamentos',
                    'onsite_conversion.post_save': 'Salvamentos',
                    'post_comment': 'Comentários'
                }
                for acao in item.get('actions', []):
                    tipo = acao.get('action_type')
                    if tipo in mapa_acoes:
                        nome_coluna = mapa_acoes[tipo]
                        acoes[nome_coluna] = int(acao['value'])

                item.update(acoes)
                item.pop('actions', None)
                dados.append(item)
        else:
            print(f"Erro ao obter métricas da campanha {campanha_id}: {resposta.text}")

    df = pd.DataFrame.from_records(dados)
    df.rename(columns={
        'date_start': 'Data',
        'campaign_name': 'Campanha',
        'spend': 'Gasto (R$)',
        'clicks': 'Cliques',
        'impressions': 'Impressões',
        'reach': 'Alcance Estimado',
        'cpm': 'CPM (Custo por 1000 impressões)',
        'ad_name': 'Anúncio',
        'adset_name': 'Conjunto de Anúncios'
    }, inplace=True)
    return df
