# Arquitetura de fases — PV-2026-11-25-TOTALMENTE-GRATUITA

## Princípio
A arquitetura é dinâmica. PHASE_00–PHASE_05 são referências iniciais, não uma sequência obrigatória nem limite de fases. Consultar o protocolo central em `PROMPT_VIVO/EXECUTION_PROTOCOL.md`.

## Histórico de versões

### v1.0 — 2026-11-25 — Arquitetura inicial
- PHASE_00_SCOPE
- PHASE_01_LANDSCAPE
- PHASE_02_DEMAND
- PHASE_03_VALIDATION
- PHASE_04_FEASIBILITY
- PHASE_05_SYNTHESIS

### v2.0 — 2026-11-25 — Governança adaptativa
**Motivo:** explicitar que o Prompt Vivo pode administrar o número e a ordem das fases sem multiplicar etapas por formalidade.

### v3.0 — 2026-11-25 — Transição autorizada para PHASE_03_VALIDATION
**ID:** PA-003  
**Motivo:** o usuário autorizou avançar para validação e apontou duas hipóteses conectadas: pesquisa de mercado como serviço e sistema de pesquisa recorrente com ChatGPT/IA. Também pediu que a aquisição não dependa de disputas de propostas não remuneradas em plataformas freelancer.  
**Fases afetadas:** PHASE_02_DEMAND e PHASE_03_VALIDATION.  
**Mudança:** PHASE_02 encerrada para priorização com PASS WITH GAPS, sem apagar lacunas; PHASE_03 iniciada com escopo adaptado para validar serviço e produto potencial.  
**Lacunas transferidas:** aquisição direta sem spam; preço líquido e prazo de pagamento; prova de disposição a pagar; capacidade prática; frequência/valor do monitoramento recorrente.  
**Comparador secundário:** planilhas padronizadas e rápidas, somente para avaliar se uma entrega de baixo esforço pode ser vendida fora de leilão de propostas.  
**Dependências/cotas:** pesquisa pública e ferramentas gratuitas; nenhuma API, assinatura, anúncio ou automação paga. Quota continua opaca; respeitar RESOURCE_BUDGET_POLICY.md.  
**Entregáveis:** VALIDATION_MATRIX.md e PHASE_03_VALIDATION_CHECKPOINT.md, além de atualização de RUN_STATE, RESEARCH_PLAN e MEMORY_HANDOFF.  
**Decisão de gate:** PHASE_02 = PASS WITH GAPS por transição explicitamente solicitada; PHASE_03 = IN_PROGRESS.

## Decisões atuais
| Fase | Estado | Gate/observação |
|---|---|---|
| PHASE_00_SCOPE | Concluída | PASS WITH GAPS |
| PHASE_01_LANDSCAPE | Concluída | PASS WITH GAPS |
| PHASE_02_DEMAND | Encerrada para transição | PASS WITH GAPS; lacunas não resolvidas foram transferidas |
| PHASE_03_VALIDATION | Em andamento | Pesquisa concorrencial inicial feita; falta prova de compra, canal de aquisição e disposição a pagar |
| PHASE_04_FEASIBILITY | Planejada | Avaliar apenas hipóteses que sobreviverem à validação |
| PHASE_05_SYNTHESIS | Planejada | Pode ser antecipada ou adaptada |

## Regra de atualização
Toda mudança futura deve acrescentar linha ao histórico e atualizar RESEARCH_PLAN.md, RUN_STATE.md e MEMORY_HANDOFF.md. Não apagar fases ou registros anteriores.
