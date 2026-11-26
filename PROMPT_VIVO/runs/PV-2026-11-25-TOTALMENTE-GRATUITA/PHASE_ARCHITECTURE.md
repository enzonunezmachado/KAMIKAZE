# Arquitetura de fases — PV-2026-11-25-TOTALMENTE-GRATUITA

## Princípio
A arquitetura é dinâmica. PHASE_00–PHASE_05 são referências iniciais, não uma sequência obrigatória nem limite de fases. Consultar PROMPT_VIVO/EXECUTION_PROTOCOL.md e PHASE_CONTROL.md.

## Histórico de versões

### v1.0 — 2026-11-25 — Arquitetura inicial
PHASE_00_SCOPE; PHASE_01_LANDSCAPE; PHASE_02_DEMAND; PHASE_03_VALIDATION; PHASE_04_FEASIBILITY; PHASE_05_SYNTHESIS.

### v2.0 — 2026-11-25 — Governança adaptativa
Explicitada a autonomia para dividir, mesclar, reordenar, modificar, adicionar, pular ou reabrir fases, com histórico preservado.

### v3.0 — 2026-11-25 — Transição para PHASE_03_VALIDATION (PA-003)
PHASE_02 encerrada com PASS WITH GAPS por autorização do usuário. Lacunas transferidas à validação.

### v4.0 — 2026-11-25 — Transição para PHASE_04_FEASIBILITY (PA-004)
PHASE_03 encerrada para transição com PASS WITH GAPS; não havia prova de compra, recorrência ou disposição a pagar. Fase 04 foi planejada para fluxo de entrega, fontes, ferramentas gratuitas, qualidade, tempo, capacidade e economia unitária. A documentação criada não significa execução operacional concluída.

### v5.0 — 2026-11-25 — Controlador e subfase 03.1 (PA-005)
A auditoria identificou lacunas críticas em compra específica, comprador, canal sem leilão e recorrência. Criada PHASE_03_1_PURCHASE_EVIDENCE. PHASE_04 movida para QUEUED/NOT_STARTED; plano preservado, teste operacional ainda não executado. Evidências iniciais S056–S061. Gate 03.1: CONTINUE.

### v6.0 — 2026-11-25 — Bootstrap entre chats (PA-006)
Criados BOOTSTRAP.md, RESUME_PACKET.md e USER_INPUT_LOG.md para reconstrução de contexto e incorporação de feedback do usuário. Não altera escopo comercial nem evidência da pesquisa. Corrige divergência histórica em que a Fase 04 aparecia como "em andamento" apesar de estar aguardando execução.

## Estado atual confirmado
| Fase | Estado | Gate/observação |
|---|---|---|
| PHASE_00_SCOPE | Concluída | PASS WITH GAPS |
| PHASE_01_LANDSCAPE | Concluída | PASS WITH GAPS |
| PHASE_02_DEMAND | Encerrada para transição | PASS WITH GAPS; lacunas preservadas |
| PHASE_03_VALIDATION | Encerrada para transição | PASS WITH GAPS; sem compra/recorrência comprovada |
| PHASE_03.1_PURCHASE_EVIDENCE | IN_PROGRESS | CONTINUE; evidência de compra específica, canal e recorrência ainda insuficientes |
| PHASE_04_FEASIBILITY | QUEUED / NOT_STARTED | Plano e documentos preparatórios existem; nenhum teste operacional foi executado |
| PHASE_05_SYNTHESIS | Planejada/adaptável | Reavaliar após fases anteriores |

## PA-006 — Registro da decisão
**Motivo:** usuário solicitou retomada entre chats com contexto completo, incluindo identidade do projeto, execução, pesquisa/build atual, fases, evidências e trabalho anterior; também esclareceu que comentários durante a conversa podem influenciar a continuação.

**Mudança:** protocolo obrigatório de bootstrap, pacote canônico de retomada e log de entradas do usuário. O controlador continua decidindo a ação mínima útil quando o usuário disser "próxima/continua".

**Arquivos:** PROMPT_VIVO/BOOTSTRAP.md; PROMPT_VIVO/MASTER_PROMPT.md; PROMPT_VIVO/MEMORY_AND_HANDOFF.md; RESUME_PACKET.md; USER_INPUT_LOG.md; PHASE_ARCHITECTURE.md.

## Regra de atualização
Toda mudança futura deve registrar motivo, arquivos afetados, dependências e impacto; sincronizar RUN_STATE, RESEARCH_PLAN, MEMORY_HANDOFF, RESUME_PACKET e operations/STATE. Não apagar histórico.
