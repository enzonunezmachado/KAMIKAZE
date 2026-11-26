# Arquitetura de fases — PV-2026-11-25-TOTALMENTE-GRATUITA

## Princípio
A arquitetura é dinâmica. PHASE_00–PHASE_05 são referências iniciais, não sequência obrigatória nem limite de fases. Consultar PROMPT_VIVO/EXECUTION_PROTOCOL.md e PHASE_CONTROL.md.

## Histórico
- **v1.0 — 25/11/2026:** arquitetura inicial PHASE_00–PHASE_05.
- **v2.0 — 25/11/2026:** governança adaptativa; permitir dividir, mesclar, reordenar, modificar, adicionar, pular e reabrir fases, preservando histórico.
- **v3.0 / PA-003:** PHASE_02 encerrada com PASS WITH GAPS por autorização do usuário; lacunas transferidas.
- **v4.0 / PA-004:** PHASE_03 encerrada para transição com PASS WITH GAPS; Fase 04 planejada, sem teste operacional.
- **v5.0 / PA-005:** auditoria encontrou lacunas críticas em compra, comprador, canal e recorrência; abriu PHASE_03.1. Fase 04 voltou a QUEUED/NOT_STARTED.
- **v6.0 / PA-006:** criados BOOTSTRAP.md, RESUME_PACKET.md e USER_INPUT_LOG.md para retomada entre chats e incorporação de feedback. Corrigida divergência em que Fase 04 aparecia como em andamento.

## Estado atual
| Fase | Estado | Gate |
|---|---|---|
| PHASE_00_SCOPE | Concluída | PASS WITH GAPS |
| PHASE_01_LANDSCAPE | Concluída | PASS WITH GAPS |
| PHASE_02_DEMAND | Encerrada para transição | PASS WITH GAPS |
| PHASE_03_VALIDATION | Encerrada para transição | PASS WITH GAPS; sem compra/recorrência comprovada |
| PHASE_03.1_PURCHASE_EVIDENCE | IN_PROGRESS | CONTINUE |
| PHASE_04_FEASIBILITY | QUEUED / NOT_STARTED | Nenhum teste operacional executado |
| PHASE_05_SYNTHESIS | Planejada/adaptável | Reavaliar |

## PA-007 — Segunda rodada de evidência em PHASE_03.1
**Data:** 25/11/2026.  
**Motivo:** aprofundar compra concluída, intenção de recorrência e demanda por monitoramento competitivo.

**Fontes novas:** S062–S066.
- S062: pedido Workana com intenção de repetir pesquisa de preços a cada 3–4 meses; comprador com 76 projetos pagos, mas pedido específico aberto.
- S063: pedido de análise competitiva documentada; comprador sem histórico de pagamentos.
- S064: 99Freelas, pesquisa de preços/estoque em pontos de venda, concluído parcialmente e com vencedor; trabalho de campo.
- S065: oferta VintePila de pesquisa/validação com zero vendas visíveis.
- S066: pedido Workana para SaaS de monitoramento de anúncios com IA, orçamento R$500–R$1.000; aberto, sem prova de contratação/assinantes.

**Decisão:** CONTINUE PHASE_03.1. Evidência melhorou para procura e necessidade recorrente declarada, mas não comprova venda repetida de relatório remoto competitivo, assinatura recorrente ou canal sem leilão. Fase 04 continua QUEUED/NOT_STARTED.

## Regra de atualização
Toda mudança futura deve registrar motivo, arquivos afetados, dependências e impacto; sincronizar RUN_STATE, RESEARCH_PLAN, MEMORY_HANDOFF, RESUME_PACKET, USER_INPUT_LOG e operations/STATE. Não apagar histórico.

## PA-008 — Terceira rodada: canais de aquisição e urgência
**Data:** 25/11/2026. **Fontes:** S067–S070.
- S067 mostra parceiros/pares e conversas setoriais como fontes de informação para PMEs, além de uso de consultoria.
- S068 reforça WhatsApp como canal operacional dominante em serviços, mas não prova aquisição nem autoriza mensagens não solicitadas.
- S069 documenta networking, rodadas e agentes B2B no programa subsidiado Move+ do Sebrae.
- S070 oferece referência de escopo profissional de pesquisa, sem comparação direta de preço.
**Decisão:** CONTINUE PHASE_03.1. Canais gerais de confiança são plausíveis; canal específico para vender benchmarking ainda não foi demonstrado. Fase 04 continua QUEUED/NOT_STARTED.

## PA-009 — Quarta rodada: contratação concluída e pesquisa recorrente
**Data:** 25/11/2026. **Fontes:** S071–S075.
- S071: pesquisa de preços de catálogo com 44 vinhos, concluída e vencedora identificada; concorrência alta.
- S072: pricing estratégico de 6–8 SKUs, concluído e vencedor; requer especialização, NDA e tratamento cuidadoso de tributação.
- S073: cliente espião mensal, histórico de pagamento do comprador e recorrência declarada; status contraditório, não contar como concluído.
- S074: curadoria de fornecedores/produtos para e-commerce, concluída; continuidade apenas potencial.
- S075: pesquisa de tendências três vezes por semana, concluída; duração e renovação não conhecidas.
**Decisão:** CONTINUE PHASE_03.1. Compra de pesquisa aplicada a decisões/rotinas está bem demonstrada, mas canais sem leilão, recompra e adequação de habilidade ainda faltam. PHASE_04 permanece QUEUED/NOT_STARTED.
