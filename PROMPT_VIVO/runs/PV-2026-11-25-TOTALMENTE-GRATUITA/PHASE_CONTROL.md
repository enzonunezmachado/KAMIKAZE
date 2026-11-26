
# Controlador adaptativo de fases — execução Kamikaze

**Versão:** 1.1  
**Escopo:** esta execução; modelo reutilizável para futuras runs.

## Regra de interação
Quando o usuário disser "próxima", "continua", "vai", "pode avançar" ou equivalente, interpretar como autorização para continuar o trabalho — não como obrigação de trocar o número da fase nem como aprovação automática de um gate factual.
Comentários, correções e preferências expressos antes de "próxima" também devem ser incorporados: classificar impacto, registrar em USER_INPUT_LOG.md e reavaliar escopo, método, critérios e arquitetura.

## Retomada entre chats
Em novo chat, executar PROMPT_VIVO/BOOTSTRAP.md e ler RESUME_PACKET.md antes dos detalhes. Reconstruir projeto, execução, pesquisa/build atual, fase, evidências, decisões, restrições e próxima ação. Não pedir que o usuário repita o contexto documentado. Não alegar certeza total; apontar arquivos ausentes ou contraditórios.

## Ciclo obrigatório antes de cada transição
1. **Recarregar:** ler RUN_STATE, RESUME_PACKET, arquitetura, plano, checkpoint atual, instrução da fase, fontes, achados, perguntas abertas e entregáveis existentes.
2. **Incorporar feedback:** verificar mensagens recentes do usuário; registrar no USER_INPUT_LOG e atualizar arquivos afetados.
3. **Auditar completude:** comparar objetivo/perguntas da fase com evidências, qualidade, contraprovas e entregáveis.
4. **Classificar:** avaliar cada requisito como RESPONDIDO, PARCIAL, NÃO RESPONDIDO, BLOQUEADO ou NÃO APLICÁVEL.
5. **Escolher a ação mínima útil:** CONTINUE_PHASE, CREATE_SUBPHASE, REOPEN_PHASE, ADVANCE, SYNTHESIZE ou BLOCK.
6. **Registrar decisão:** motivo, evidências, lacunas, dependências, impacto de cotas, entregáveis e próximo gate.
7. **Sincronizar memória:** PHASE_ARCHITECTURE, RUN_STATE, RESEARCH_PLAN, MEMORY_HANDOFF, RESUME_PACKET, USER_INPUT_LOG, STATE e checkpoint afetado.
8. **Executar a ação escolhida:** não ficar apenas anunciando o plano.

## Estados de gate
- PASS: requisitos essenciais atendidos; lacunas residuais não mudam a decisão.
- PASS_WITH_GAPS: pode prosseguir com limitações explicitadas e transferidas.
- CONTINUE: falta trabalho que pode ser feito agora; não avançar.
- FAIL: evidência/viabilidade contradiz a hipótese ou o padrão mínimo.
- BLOCKED: dependência externa ou aprovação necessária.

## Regras de integridade
- Autorização para "próxima" não transforma hipótese em fato nem compra em venda.
- Não encerrar fase apenas porque foi criado o arquivo da fase seguinte.
- Não repetir pesquisa já suficiente; aprofundar apenas onde a resposta pode mudar a decisão.
- Uma fase pode ter subfases ilimitadas, sem criar burocracia.
- Fases paralelas são permitidas quando não dependem uma da outra; registrar dependências.
- Nunca apagar histórico; registrar reabertura, divisão, mescla ou encerramento.
- Não abordar clientes, publicar, enviar propostas, contratar, comprar, assinar ou fazer deploy sem autorização humana explícita.

## Formato de decisão ao usuário
Informar em poucas linhas: fase auditada, decisão (continuar/subfase/avançar), motivo principal, o que foi executado, estado do repositório e próximo passo. Evitar pedir que o usuário escolha a numeração; a IA administra a arquitetura e explica a decisão.

## Aplicação atual
A auditoria identificou que PHASE_03_VALIDATION foi encerrada para transição antes de responder questões críticas. PHASE_04_FEASIBILITY existe como plano, mas nenhum teste operacional foi executado. PHASE_03_1_PURCHASE_EVIDENCE permanece ativa. Na segunda rodada, S062–S066 acrescentaram evidência parcial de execução, intenção de compra e recorrência declarada, mas não comprovaram venda de relatório remoto competitivo nem canal sem leilão. Portanto, gate CONTINUE; PHASE_04 fica QUEUED/NOT_STARTED.



## Atualização após Rodada 5 (S076–S086)
A auditoria encontrou evidência geral de busca e indicação, mas não conversão específica para pesquisa; alta concorrência em serviços operacionais; e bloqueios de elegibilidade aos 16 anos em plataformas importantes. Antes de considerar piloto, investigar rota legal de recebimento/contrato, participação de responsável adulto, parceria supervisionada e prova demonstrável de capacidade. Manter PHASE_03.1 em CONTINUE; PHASE_04 QUEUED/NOT_STARTED. Não abordar, publicar ou enviar proposta.


## Atualização após Rodada 7 (S101–S104)
A investigação de plataformas de tarefas para IA encontrou Prolific (Brasil elegível, porém waitlist e até 22 dias de aprovação) e Outlier (pagamento semanal, mas vaga PT-BR encontrada exigia coding expertise). Esses modelos não resolvem automaticamente a meta imediata. Manter PHASE_03.1 em CONTINUE; PHASE_04 QUEUED/NOT_STARTED. Nenhuma conta/candidatura ou contato foi realizado.
