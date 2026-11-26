# Controlador adaptativo de fases — execução Kamikaze

**Versão:** 1.0  
**Escopo:** esta execução; modelo reutilizável para futuras runs.

## Regra de interação
Quando o usuário disser "próxima", "continua", "vai", "pode avançar" ou equivalente, interpretar como autorização para continuar o trabalho — não como obrigação de trocar o número da fase nem como aprovação automática de um gate factual.

## Ciclo obrigatório antes de cada transição
1. **Recarregar:** ler RUN_STATE, arquitetura, plano, checkpoint atual, fontes, achados, perguntas abertas e entregáveis existentes.
2. **Auditar completude:** comparar objetivo/perguntas da fase com evidências, qualidade, contraprovas e entregáveis.
3. **Classificar:** avaliar cada requisito como RESPONDIDO, PARCIAL, NÃO RESPONDIDO, BLOQUEADO ou NÃO APLICÁVEL.
4. **Escolher a ação mínima útil:**
   - CONTINUE_PHASE: manter a fase atual se trabalho essencial ainda cabe nela.
   - CREATE_SUBPHASE: criar 3.1, 3.2 etc. quando a lacuna for relevante e tiver método/entregável próprio.
   - REOPEN_PHASE: reabrir fase encerrada se nova evidência comprometer sua conclusão.
   - ADVANCE: iniciar a próxima fase apenas quando as dependências críticas estiverem suficientemente tratadas ou explicitamente transferidas.
   - SYNTHESIZE: consolidar quando pesquisa adicional não altera decisão.
   - BLOCK: parar se faltar decisão, permissão ou acesso indispensável.
5. **Registrar decisão:** motivo, evidências, lacunas, dependências, impacto de cotas, entregáveis e próximo gate.
6. **Sincronizar memória:** PHASE_ARCHITECTURE, RUN_STATE, RESEARCH_PLAN, MEMORY_HANDOFF, STATE e checkpoint afetado.
7. **Executar a ação escolhida:** não ficar apenas anunciando o plano.

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
Em cada resposta, informar em poucas linhas: fase auditada, decisão (continuar/subfase/avançar), motivo principal, o que foi executado, estado do repositório e próximo passo. Evitar pedir que o usuário escolha a numeração; a IA administra a arquitetura e explica a decisão.

## Aplicação atual
A auditoria identificou que PHASE_03_VALIDATION foi encerrada para transição antes de responder questões críticas (compra comprovada, comprador estreito, canal e recorrência). PHASE_04_FEASIBILITY existia como plano, mas ainda não tinha teste operacional. Portanto, abrir PHASE_03_1_PURCHASE_EVIDENCE para fechar parcialmente as lacunas mais decisivas antes de executar a Fase 04. A Fase 04 fica planejada/aguardando, não concluída.
