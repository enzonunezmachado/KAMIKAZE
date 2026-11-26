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

### v2.0 — 2026-11-25 — Aplicação da governança adaptativa
**Motivo:** o usuário autorizou explicitar que o Prompt Vivo pode administrar o número e a ordem das fases, criando ou alterando etapas quando necessário, sem multiplicar fases por formalidade.

**Decisões atuais:**
| Fase | Estado | Gate/observação |
|---|---|---|
| PHASE_00_SCOPE | Concluída | PASS WITH GAPS; escopo e restrições registrados |
| PHASE_01_LANDSCAPE | Concluída | PASS WITH GAPS; mapa inicial suficiente para minerar demanda |
| PHASE_02_DEMAND | Em andamento | Primeiro lote encontrou sete clusters; faltam canais diretos, preço líquido, prazo e capacidade de entrega |
| PHASE_03_VALIDATION | Planejada | Só será adaptada após entender quais clusters têm sinal mais forte |
| PHASE_04_FEASIBILITY | Planejada | Pode ser dividida se custos, aquisição e capacidade exigirem análises distintas |
| PHASE_05_SYNTHESIS | Planejada | Pode ocorrer antes ou depois de fases adicionais conforme evidência |

## Registro de alterações
| ID | Data | Ação | Justificativa | Impacto |
|---|---|---|---|---|
| PA-001 | 2026-11-25 | PHASE_01 marcada PASS WITH GAPS e PHASE_02 iniciada | O landscape inicial já mapeou os modelos principais; pedidos concretos agora agregam mais valor | Avanço sem repetir pesquisa ampla |
| PA-002 | 2026-11-25 | Nenhuma fase adicional criada | Os sete clusters ainda cabem na mineração de demanda; não há evidência de que uma fase separada melhore o trabalho | Evita burocracia; reavaliar no gate da Fase 02 |

## Regra de atualização
Toda mudança futura deve acrescentar linha ao histórico e atualizar RESEARCH_PLAN.md, RUN_STATE.md e MEMORY_HANDOFF.md. Não apagar fases ou registros anteriores; marcar como skipped, merged, retired ou reopened com justificativa.
