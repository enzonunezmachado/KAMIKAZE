# Arquitetura de fases — PV-2026-11-25-TOTALMENTE-GRATUITA

## Princípio
A arquitetura é dinâmica. PHASE_00–PHASE_05 são referências iniciais, não uma sequência obrigatória nem limite de fases. Consultar o protocolo central em PROMPT_VIVO/EXECUTION_PROTOCOL.md.

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
**Motivo:** usuário autorizou avançar e destacou serviço de pesquisa de mercado e sistema de monitoramento assistido por IA; pediu para não priorizar leilões de propostas.  
**Mudança:** PHASE_02 encerrada com PASS WITH GAPS e lacunas transferidas à Fase 03.

### v4.0 — 2026-11-25 — Transição autorizada para PHASE_04_FEASIBILITY
**ID:** PA-004  
**Motivo:** usuário solicitou avançar para a próxima fase após a rodada inicial de validação.  
**Fases afetadas:** PHASE_03_VALIDATION e PHASE_04_FEASIBILITY.  
**Mudança:** Fase 03 encerrada para transição com PASS WITH GAPS; não houve prova de compra, recorrência ou disposição a pagar. Fase 04 aberta para avaliar fluxo de entrega, fontes, ferramentas gratuitas, qualidade, tempo, capacidade e economia unitária.  
**Lacunas transferidas:** comprador e disposição a pagar; prova de compra; canal de aquisição; frequência real da dor; preço e prazo de recebimento; diferenciação frente a ferramentas existentes.  
**Entregáveis:** PHASE_04_FEASIBILITY.md, PHASE_04_FEASIBILITY_CHECKPOINT.md, DELIVERY_WORKFLOW.md, UNIT_ECONOMICS.md e TOOL_STACK_AUDIT.md.  
**Cotas:** R$0; quota de pesquisa permanece opaca; fallback manual obrigatório.

## Decisões atuais
| Fase | Estado | Gate/observação |
|---|---|---|
| PHASE_00_SCOPE | Concluída | PASS WITH GAPS |
| PHASE_01_LANDSCAPE | Concluída | PASS WITH GAPS |
| PHASE_02_DEMAND | Encerrada para transição | PASS WITH GAPS; lacunas preservadas |
| PHASE_03_VALIDATION | Encerrada para transição | PASS WITH GAPS; nenhuma venda/compra validada |
| PHASE_04_FEASIBILITY | Em andamento | Escopo e critérios definidos; teste de entrega pendente |
| PHASE_05_SYNTHESIS | Planejada/adaptável | Depende dos resultados; pode ser reestruturada |

## Regra de atualização
Toda mudança futura deve acrescentar linha ao histórico e atualizar RESEARCH_PLAN.md, RUN_STATE.md e MEMORY_HANDOFF.md. Não apagar fases ou registros anteriores.
