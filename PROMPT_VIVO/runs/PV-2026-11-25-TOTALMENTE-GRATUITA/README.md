# Execução PV-2026-11-25-TOTALMENTE-GRATUITA

**Objetivo:** pesquisar oportunidades digitais e caminhos de monetização com IA, recursos gratuitos e sem audiência prévia, preservando o orçamento operacional de R$0.

## Ordem de leitura
1. [Pacote de retomada](RESUME_PACKET.md) — resumo curto; não é fonte canônica de estado.
2. [Estado da execução](RUN_STATE.md) — fonte canônica da fase e do progresso.
3. [Controle de fases](PHASE_CONTROL.md) — gate e próxima ação permitida.
4. [Arquitetura das fases](PHASE_ARCHITECTURE.md) e [plano](RESEARCH_PLAN.md).
5. [Fontes](SOURCE_LEDGER.md), [achados](FINDINGS.md), [perguntas abertas](OPEN_QUESTIONS.md) e matriz.
6. Abrir checkpoints e pesquisas especializadas conforme a fase ativa.

## Regras de gravação
- Fonte original e metadados entram em SOURCE_LEDGER; síntese entra em FINDINGS.
- Não misturar intenção, anúncio, contratação, pagamento e recompra.
- Resultado negativo e contraprova devem ser preservados.
- USER_INPUT_LOG registra correções, ideias, decisões e autorizações do usuário.
- SESSION_LOG é append-only.
- RESUME_PACKET deve permanecer curto e derivado de RUN_STATE/PHASE_CONTROL.
- Não iniciar PHASE_04, contato, publicação, candidatura, compra ou gasto sem gate e autorização correspondentes.
