# Taxonomia de Status — Empresa, Contato, Venda, Projeto e Contrato

Não usar um único status para representar tudo. Cada dimensão responde a uma pergunta diferente.

## 1. Pesquisa (research_status)
- DISCOVERED — encontrada, ainda sem triagem.
- SCREENED — identidade/atividade e dados básicos verificados.
- RANKED — analisada e ranqueada em lote.
- HOLD — suspensa por incerteza, timing ou falta de evidência.
- DISQUALIFIED — duplicata, inativa, identidade duvidosa ou sem fit.
- REASSESSMENT — reaberta com motivo novo e vínculo ao histórico.

## 2. Decisão de priorização (priority_decision)
- PRIORITY_A — alta prioridade.
- PRIORITY_B — potencial, requer validação.
- HOLD — não agir agora.
- NOT_SELECTED — ficou abaixo do corte ou não justifica esforço.
- DO_NOT_APPROACH — não abordar.
- DISQUALIFIED — não elegível.

## 3. Contato (contact_status)
- NOT_CONTACTED — não foi selecionada para contato ou nenhuma tentativa foi feita; pode ser reavaliada conforme os critérios do lote.
- NOT_ELIGIBLE — não há caminho legítimo/adequado de contato.
- PERMISSION_NEEDED — é necessário pedir autorização antes de encaminhar proposta pelo canal desejado.
- PERMISSION_REQUESTED — pedido de autorização feito.
- PERMISSION_GRANTED — permissão específica registrada.
- CONTACTED — apresentação/proposta enviada pelo canal autorizado.
- NO_RESPONSE — sem resposta após cadência limitada e registrada.
- WRONG_CONTACT — destinatário/canal incorreto.
- DECLINED — recusou a abordagem/oferta.
- DO_NOT_CONTACT — opt-out/pedido de não contato.

## 4. Vendas (sales_status)
- NOT_APPROACHED — nenhuma oferta apresentada.
- QUALIFICATION — conversa para confirmar necessidade/decisor.
- PROPOSAL — proposta formal enviada.
- NEGOTIATION — escopo/preço em negociação.
- WON — aceite comercial documentado.
- LOST — oportunidade encerrada sem venda.
- NOT_A_FIT — necessidade/solução não adequada.

## 5. Entrega (delivery_status)
- NOT_STARTED, DISCOVERY, DEMO_ONLY, APPROVED, IN_PROGRESS, QA, CLIENT_REVIEW, ACCEPTED, DELIVERED, SUPPORT, PAUSED, CANCELLED, CLOSED.

## 6. Contrato recorrente (contract_status)
- NONE, DRAFT, PROPOSED, ACTIVE, PAYMENT_DUE, OVERDUE, PAUSED, CANCELLATION_REQUESTED, ENDED.

## 7. Reavaliação
- YES — pode entrar em rodada futura com nova justificativa.
- CONDITIONAL — só se surgir evidência, necessidade ou trigger novo.
- NO — recusa/opt-out/supressão ou motivo impeditivo.

## Regras para cenários comuns
| Cenário | Pesquisa | Contato | Venda | Reavaliação |
|---|---|---|---|---|
| Ficou no fim do ranking, sem contato | RANKED | NOT_CONTACTED | NOT_APPROACHED | YES/CONDITIONAL |
| Não havia canal apropriado | HOLD | NOT_ELIGIBLE | NOT_APPROACHED | CONDITIONAL |
| Pediu autorização e não respondeu | SCREENED | PERMISSION_REQUESTED | NOT_APPROACHED | CONDITIONAL |
| Autorizou, recebeu proposta, não respondeu | RANKED | NO_RESPONSE | LOST (após encerrar ciclo) | CONDITIONAL |
| Recusou a oferta | RANKED | DECLINED | LOST | NO para mesma oferta; outra só com novo convite/contexto legítimo |
| Pediu para não receber contato | qualquer | DO_NOT_CONTACT | encerrada | NO |
| Aceitou e está em execução | RANKED | CONTACTED | WON | não se aplica |
| Projeto entregue, sem mensalidade | RANKED | CONTACTED | WON | relacionamento normal, sem prospecção repetida |
| Cliente com manutenção ativa | RANKED | CONTACTED | WON | gestão de cliente, não lead |

"Não respondeu", "não ouviu", "recusou", "não é prioridade" e "não é elegível" são estados diferentes e nunca devem ser agrupados.
