import requests

# url = 'https://api.infosimples.com/api/v2/consultas/detran/df/veiculo/mobile'
# args = {
#   "placa":   "JGU8I79",
#   "renavam": "00893956139",
#   "token":   "ezg57QOEI76knEGX5i0JvvU-W7kUp_PjpE_q7LFn",
#   "timeout": 300
# }

# detran_df_situacao = requests.post(url, args)
# detran_df_situacao_dic = detran_df_situacao.json()
# detran_df_situacao.close()


# print(detran_df_situacao_dic) 




url = 'https://api.infosimples.com/api/v2/consultas/detran/df/veiculo/mobile'
args = {
"placa": "JGU8I79", 
"renavam": "00893956139", 
"token":   "ezg57QOEI76knEGX5i0JvvU-W7kUp_PjpE_q7LFn",
"timeout": 300
}

detran_df_situacao = requests.post(url, args)
ddic = detran_df_situacao.json()
dic = ddic
print(dic)