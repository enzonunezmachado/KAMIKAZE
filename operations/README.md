# Operations — Índice operacional do Kamikaze

Esta pasta contém controles de execução e registros estruturados da operação. Não é a base de conhecimento metodológica nem o histórico de pesquisa.

## Leitura obrigatória

1. [Estado estruturado canônico](state.toml) — RUN_ID, fase/gate, restrições e métricas.
2. [Estado humano](STATE.md) — visão compacta e instruções de retomada.
3. [Histórico preservado](STATE_HISTORY.md) — snapshots e registros antigos; não é estado atual.
4. [Recursos disponíveis](AVAILABLE_RESOURCES.md) — inventário de ferramentas e capacidades.
5. [Company Solutions](COMPANY_SOLUTIONS/README.md) — ler antes de operar esse módulo.

## Regras de gravação

- state.toml é a fonte estruturada; STATE.md é sua projeção humana e deve ser validada pela CI.
- Não acumular diário em STATE.md; registros históricos ficam em STATE_HISTORY.md e logs.
- Registros de empresas, contatos, projetos, contratos e finanças pertencem a COMPANY_SOLUTIONS.
- Não inserir senhas, tokens, dados pessoais desnecessários ou segredos.
- Não iniciar contatos, propostas, contratos, despesas ou deploys sem autorização.
