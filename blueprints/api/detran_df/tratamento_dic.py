

dic =  [
    {'ano': '2006', 'ano_fabricacao': '2006', 'ano_modelo': '2006', 'capacidade_passageiros': None, 'categoria': 'PARTICULAR', 'chassi': '9BWCA05W26T195569', 'combustivel': None, 'cor': None, 'debitos': {'licenciamentos': [], 'ipva': [], 'dpvat': [], 'detran': []}, 'especie': None, 
     
     'gravame': 
         {'situacao': 'VEÍCULO TEVE GRAVAME BAIXADO PELO AGENTE FINANCEIRO', 'numero_restricao': '01369406', 'numero_contrato': '40430476965', 'uf': 'DF', 'datahora': '04/03/2022 10:54:39', 'financiado_documento': '00064772144153', 'financiado_nome': 'ARNALDO BASSO REBELATO', 'agente_nome': 'HSBC BANK BRASIL S A   BCO MULTIPLO', 'agente_codigo': '000000002073', 'agente_documento': '01701201000189'},
         
         'infracoes': 
             [
                 {'ait': 'SA03352835', 'status': 'Multa DF c/veiculo DF Notificada', 'codigo_renainf': '06520581216', 'orgao_autuador': 'DETRAN - DF', 'regulamento': '252, § ÚNICO', 'descricao': 'DIRIGIR VEÍCULO SEGURANDO TELEFONE CELULAR', 'velocidade_permitida': 0, 'velocidade_aferida': 0, 'local': 'erls, ALTURA, sds', 'data': '19/10/2022', 'hora': '17:45', 'responsavel': 'CONDUTOR', 'natureza': 'GRAVISSIMA', 'pontos': 7, 'data_notificacao': '24/10/2022', 'data_penalidade': '19/10/2022', 'data_limite_defesa': '26/11/2022', 'vencimento': '08/05/2023', 'valor': '293.47', 'valor_com_desconto': '234.78', 'valor_com_correcao': '293.47'},
                 
                 {'ait': 'KK00406697', 'status': 'Multa c/ Autuacao Notificada', 'codigo_renainf': '06755738301', 'orgao_autuador': 'DETRAN - DF', 'regulamento': '218 * I', 'descricao': 'TRANSITAR VELOCIDADE SUPERIOR MAX PERMIT ATE 20%', 'velocidade_permitida': 60, 'velocidade_aferida': 76, 'local': 'EIXO L SQN 210  SENT SUL/NORTE', 'data': '03/02/2023', 'hora': '15:52', 'responsavel': 'CONDUTOR', 'natureza': 'MEDIA', 'pontos': 4, 'data_notificacao': '09/02/2023', 'data_penalidade': '03/02/2023', 'data_limite_defesa': '16/03/2023', 'vencimento': '15/05/2023', 'valor': '130.16', 'valor_com_desconto': '104.13', 'valor_com_correcao': '130.16'}
                 
                 ], 
             
             'marca': 'VW', 'modelo': 'GOL 1.0 COPA', 'municipio': None, 'nacionalidade': None, 'placa': 'JGU8I79', 'potencia_cilindradas': None, 'renavam': '00893956139', 'restricoes': [], 'roubo_furto': 'NADA CONSTA', 'situacao_veiculo': 'EM CIRCULACAO', 'tipo': 'AUTOMOVEL', 'ultimo_licenciamento': '2022', 'site_receipt': None
             }
    ]


# print(dic[0]['gravame']['financiado_nome'])
# print(dic[0]['gravame']['situacao'])

# for infracao in dic[0]['infracoes']:
#     print(infracao['descricao'])
    

dic = {'code': 200, 'code_message': 'A requisição foi processada com sucesso.', 
       'header':
        {'api_version': 'v2', 'api_version_full': '2.2.6-20230403101550', 'product': 'Consultas', 'service': 'detran/df/veiculo/mobile', 
         'parameters': 
            {'placa': 'JGU8I79', 'renavam': '00893956139'}, 'client_name': 'Trovale Tecnologia Ltda', 'token_name': 'Trovale Tecnologia Ltda', 'billable': True, 'price': '0.2', 'requested_at': '2023-04-03T11:14:42.000-03:00', 'elapsed_time_in_milliseconds': 2988, 'remote_ip': '177.73.68.143', 'signature': 'U2FsdGVkX19bKdbrJPKB+21lkl85h/eIl4BluHhleN6cDmFhyDfrOPlxMyKE9BkUWGJKcRMcZvZnYbsXaPNoYg=='}
            ,'data_count': 1,
        
            'data': [{'ano': '2006', 'ano_fabricacao': '2006', 'ano_modelo': '2006', 'capacidade_passageiros': None, 'categoria': 'PARTICULAR', 'chassi': '9BWCA05W26T195569', 'combustivel': None, 'cor': None, 'debitos': {'licenciamentos': [], 'ipva': [], 'dpvat': [], 'detran': []}, 'especie': None, 
                      'gravame': {'situacao': 'VEÍCULO TEVE GRAVAME BAIXADO PELO AGENTE FINANCEIRO', 'numero_restricao': '01369406', 'numero_contrato': '40430476965', 'uf': 'DF', 'datahora': '04/03/2022 10:54:39', 'financiado_documento': '00064772144153', 'financiado_nome': 'ARNALDO BASSO REBELATO', 'agente_nome': 'HSBC BANK BRASIL S A   BCO MULTIPLO', 'agente_codigo': '000000002073', 'agente_documento': '01701201000189'}, 
                      
                      'infracoes': 
                          [{'ait': 'SA03352835', 'status': 'Multa DF c/veiculo DF Notificada', 'codigo_renainf': '06520581216', 'orgao_autuador': 'DETRAN - DF', 'regulamento': '252, § ÚNICO', 'descricao': 'DIRIGIR VEÍCULO SEGURANDO TELEFONE CELULAR', 'velocidade_permitida': 0, 'velocidade_aferida': 0, 'local': 'erls, ALTURA, sds', 'data': '19/10/2022', 'hora': '17:45', 'responsavel': 'CONDUTOR', 'natureza': 'GRAVISSIMA', 'pontos': 7, 'data_notificacao': '24/10/2022', 'data_penalidade': '19/10/2022', 'data_limite_defesa': '26/11/2022', 'vencimento': '08/05/2023', 'valor': '293.47', 'valor_com_desconto': '234.78', 'valor_com_correcao': '293.47'}, 
                           
                           {'ait': 'KK00406697', 'status': 'Multa c/ Autuacao Notificada', 'codigo_renainf': '06755738301', 'orgao_autuador': 'DETRAN - DF', 'regulamento': '218 * I', 'descricao': 'TRANSITAR VELOCIDADE SUPERIOR MAX PERMIT ATE 20%', 'velocidade_permitida': 60, 'velocidade_aferida': 76, 'local': 'EIXO L SQN 210  SENT SUL/NORTE', 'data': '03/02/2023', 'hora': '15:52', 'responsavel': 'CONDUTOR', 'natureza': 'MEDIA', 'pontos': 4, 'data_notificacao': '09/02/2023', 'data_penalidade': '03/02/2023', 'data_limite_defesa': '16/03/2023', 'vencimento': '18/05/2023', 'valor': '130.16', 'valor_com_desconto': '104.13', 'valor_com_correcao': '130.16'}],
                          
                          'marca': 'VW', 'modelo': 'GOL 1.0 COPA', 'municipio': None, 'nacionalidade': None, 'placa': 'JGU8I79', 'potencia_cilindradas': None, 'renavam': '00893956139', 'restricoes': [], 'roubo_furto': 'NADA CONSTA', 'situacao_veiculo': 'EM CIRCULACAO', 'tipo': 'AUTOMOVEL', 'ultimo_licenciamento': '2022', 'site_receipt': None}],
            
            'errors': [], 'site_receipts': []}

    
print(dic['data'][0]['gravame']['situacao'])
print(dic['data'][0]['gravame']['financiado_nome'])
print(dic['data'][0]['gravame']['datahora'])
print(dic['data'][0]['gravame']['agente_nome'])
