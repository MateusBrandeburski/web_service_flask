




@app.route('/ativar_conta/<token>')
def ativar_conta(token):
    # Verificar se o token é válido e existe na tabela de usuários
    usuario = Usuarios.query.filter_by(token_ativacao=token).first()
    if usuario is None:
        return 'Token inválido ou expirado'

    # Atualizar a coluna 'ativado' para True
    usuario.ativado = True
    db.session.commit()

    return 'Sua conta foi ativada com sucesso!'
