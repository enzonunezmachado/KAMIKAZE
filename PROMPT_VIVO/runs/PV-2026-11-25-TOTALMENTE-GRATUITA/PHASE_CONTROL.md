
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
A auditoria encontrou evidência geral de busca e indicação, mas não conversão específica para pesquisa; alta concorrência em serviços operacionais. A análise pessoal de bloqueios de menoridade estava baseada em premissa incorreta: o usuário tem 18 anos. Reavaliar plataformas sob a idade correta; não exigir responsável adulto por menoridade. Investigar demonstração prática de competência sem presumir incapacidade por falta de histórico. Manter PHASE_03.1 em CONTINUE; PHASE_04 QUEUED/NOT_STARTED. Não abordar, publicar ou enviar proposta.


## Atualização após Rodada 7 (S101–S104)
A investigação de plataformas de tarefas para IA encontrou Prolific (Brasil elegível, porém waitlist e até 22 dias de aprovação) e Outlier (pagamento semanal, mas vaga PT-BR encontrada exigia coding expertise). Esses modelos não resolvem automaticamente a meta imediata. Manter PHASE_03.1 em CONTINUE; PHASE_04 QUEUED/NOT_STARTED. Nenhuma conta/candidatura ou contato foi realizado.


## Atualização do controlador — Rodada 8 (S105–S115)
A auditoria identificou divergências entre indexadores e status oficial: YPAI está fechada; OpenTrain não paga freelancers no Brasil; CSL tem um projeto anunciado com janela inicial já passada e possível futuro lote; Babel não confirma taxa/eligibilidade local e exclui explicitamente o Brasil em outra vaga; pesquisa Lionbridge exige dispositivo não Android. A vaga Fera está recente, mas sem remuneração/volume.
**Decisão:** CONTINUE_PHASE. A próxima ação é verificar oportunidade atual de novo lote CSL, condições de consentimento e pagamento, pagamento/volume Lionbridge e termos locais Babel; paralelamente, avaliar o escopo e remuneração da vaga Fera sem contatar o anunciante. Não iniciar Fase 04 nem realizar candidaturas/contatos sem aprovação.


## Atualização do controlador — Rodada 9 (S116–S119)
A pesquisa encontrou RWS Search Evaluator (até US$6/h, sem experiência prévia, mas inglês fluente e 5h/semana), TELUS (US$5/h estimados, inglês profissional e residência 3–5 anos), Welo Junior Quality Coordinator (20h/semana, inglês forte, remuneração não divulgada) e Clickworker (pagamento semanal, mas método e registro no Brasil variam por conta). A próxima decisão exige verificar inglês real, residência e disponibilidade do usuário, além de confirmar pagamento e carga. Não presumir esses requisitos. Manter CONTINUE_PHASE e PHASE_04 QUEUED/NOT_STARTED; nenhuma candidatura ou conta criada.

## Atualização do controlador — Rodada 10 (S120–S124)
OneForma Freya surge como hipótese mais promissora para tarefa remota PT-BR: US$6 por hora de áudio, sem experiência/diploma, lotes semanais e pagamento quinzenal por ciclo com mínimo US$25. O volume é variável, o trabalho é por hora de áudio e o locale/método Brasil precisa confirmação na conta. TSMG QC tem treinamento e pagamento por trabalho validado, mas sem taxa/ciclo público. YPAI tem status contraditório/fechado nas páginas oficiais.
**Decisão:** CONTINUE_PHASE. Próximo passo: aprofundar OneForma (método brasileiro, taxa confirmada no locale, qualificação, prazo de aprovação e produtividade de iniciante) e TSMG (taxa e pagamento). PHASE_04 continua QUEUED/NOT_STARTED. Nenhuma conta, candidatura, formulário ou contato foi realizado.
