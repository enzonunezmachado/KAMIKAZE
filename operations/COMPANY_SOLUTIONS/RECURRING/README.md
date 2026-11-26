# Contratos Recorrentes e Manutenção

Cada acordo recorrente recebe uma pasta:
`RECURRING/CTR-YYYY-NNNN-slug/CONTRACT.md`

Não tratar uma mensalidade proposta como MRR ativo. Só contar contrato após aceite e considerar receita recebida após compensação.

## Tipos
- MAINTENANCE: manutenção técnica e correções delimitadas.
- HOSTING_MANAGED: hospedagem/monitoramento quando permitido e economicamente viável.
- SUPPORT: suporte com janela e limite.
- CONTENT_UPDATE: atualização de conteúdo com quantidade definida.
- OPERATIONS: operação recorrente de workflow.
- SUBSCRIPTION: licença/uso recorrente de produto próprio, se aplicável.

## Estados
DRAFT, PROPOSED, ACTIVE, PAYMENT_DUE, OVERDUE, PAUSED, CANCELLATION_REQUESTED, ENDED.

## Regras
- Um contrato por acordo comercial; aditivos versionados.
- Definir preço, periodicidade, vencimento, reajuste, renovação, cancelamento, SLA, suporte, limites e exclusões.
- Especificar custos de terceiros e quem os paga.
- Nunca prometer suporte 24/7 ou alterações ilimitadas sem capacidade e preço.
- Registrar cobranças e recebimentos no registro financeiro.
- MRR ativo só inclui contratos ACTIVE e valores recorrentes válidos; separar valores vencidos e pausados.
- Encerramento deve incluir exportação/entrega de dados, revogação de acessos, transferência de domínio/contas e retenção/exclusão conforme combinado e lei.

Copiar [CONTRACT_TEMPLATE.md](CONTRACT_TEMPLATE.md).
