# Registro Financeiro — Empresas e Projetos

Registrar movimentos efetivos e compromissos separadamente. Não somar orçamento/proposta/contrato como dinheiro recebido.

| Transaction ID | Data | Company ID | Project ID | Contract ID | Tipo | Descrição | Valor bruto | Taxas/impostos/custos diretos | Valor líquido | Status | Comprovante/ref. |
|---|---|---|---|---|---|---|---:|---:|---:|---|---|
| — | — | — | — | — | Nenhuma transação | — | — | — | — | — | — |

## Categorias
- SETUP_REVENUE: implantação/desenvolvimento recebido.
- ONE_TIME_REVENUE: venda pontual.
- RECURRING_REVENUE: mensalidade recebida.
- ADDON_REVENUE: melhoria/serviço adicional.
- REFUND: reembolso realizado.
- PAYMENT_FEE: taxa de pagamento.
- HOSTING_OR_DOMAIN: hospedagem/domínio.
- API_OR_USAGE: consumo de API/serviço.
- OTHER_DIRECT_COST: custo diretamente atribuível.
- SUPPORT_COST: custo de suporte/manutenção.

## Métricas que não podem ser confundidas
- Receita proposta: valor apresentado, ainda não aceito.
- Receita contratada: valor acordado, ainda não necessariamente recebido.
- Receita faturada/cobrada: valor cujo pagamento foi solicitado.
- Receita recebida: dinheiro efetivamente compensado.
- Receita líquida: recebimento menos taxas, reembolsos e custos diretamente atribuíveis, conforme política contábil definida.
- MRR contratado: valor mensal recorrente ativo, normalizado para mês; não é caixa recebido.
- MRR recebido: mensalidades efetivamente recebidas no período.
- ARR: anualização indicativa do MRR; não tratar como receita realizada.
- Inadimplência: valor vencido não recebido.
- Churn: contrato recorrente encerrado; registrar data e motivo.

## Regras
- Cada movimento tem ID único e referência ao documento de origem.
- Separar dinheiro do cliente para custos de terceiros de receita própria.
- Não considerar domínio/API/hospedagem como custo zero só porque há plano gratuito; verificar termos, limites e elegibilidade comercial.
- Registrar horas de trabalho por projeto para estimar margem por hora.
- Atualizar este registro apenas após confirmação de pagamento/custo; propostas e previsões ficam nos respectivos documentos.
