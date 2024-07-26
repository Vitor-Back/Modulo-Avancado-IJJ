#language: pt

Funcionalidade: Envio de dados ao formulário
    Cenário: Envio de dados com assunto quero ser facilitador

        Dado que estou na página de contato do instituto joga junto
        Quando preencho o formulário de contato
        E envio o formulário
        Então os dados são recebidos com sucesso