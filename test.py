import pandas as pd


teste = {
    'cod_venda': "V-23-02-09-521",
    'nome_cliente': 'Daniel Haas Zanotto',
    'cpf': '01234567890',
    'cidade': 'Curitibanos',
    'uf': 'SC',
    'itens': '65532 36280',
    'valor_total': 80,
    'valor_entrega': 5,
    'tipo_entrega': 'Retirada',
    'valor_desconto': 0,
    'valor_final': 85,
    'forma_pagamento': 'Pix',
    'data': '2023-02-08'
}


# df_estoque = pd.read_excel("data.xlsx", sheet_name="estoque")
# teste_df = pd.DataFrame(teste, index=[0])
# print(teste_df)
# print(teste_df['cod_venda'].values)
# produtos = list(teste_df["itens"])[0].split(" ")
# for produto in produtos:
#     df_estoque.loc[df_estoque['cod'] == int(
#         produto), 'cod_venda'] = teste_df['cod_venda'].values[0]


# print(df_estoque)

# df = pd.read_excel("data.xlsx", sheet_name="estoque")
# df = df.loc[df['cod'] == 65532]
# print(df['cod_venda'].values[0] == 0)
comprovante = f"Vibe Verde Bazar\n@instagram\nsite.com.br\nCuritibanos-SC                 {teste['data']}\n--------------------\n{teste['nome_cliente']}\nCPF: {teste['cpf']}\n{teste['cidade']}-{teste['uf']}\n--------------------\n\nPRODUTOS\n\n--------------------\nValor Total:                     R${teste['valor_total']},00\nValor Desconto:                - R${teste['valor_desconto']},00\nValor Entrega:                 + R${teste['valor_entrega']},00\n                                 R${teste['valor_final']},00\n--------------------\nCOMPRE VERDE!"
with open(f"comprovantes/{teste['cod_venda']}.txt", 'w') as f:
    f.write(comprovante)

str.l