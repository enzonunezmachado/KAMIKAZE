# BOOTSTRAP — Inicialização e retomada entre chats

**Objetivo:** permitir que uma IA que nunca viu a conversa anterior reconstrua o contexto operacional correto antes de continuar. Este arquivo é um procedimento obrigatório, não uma sugestão.

## Gatilho
Se o usuário disser que este é um novo chat, pedir para continuar algo anterior, mencionar uma fase em andamento ou usar expressões como "continue de onde paramos", executar este protocolo antes de pesquisar, planejar ou fazer perguntas.

## Etapa 1 — Identidade e limites do projeto
Ler:
1. `README.md`
2. `docs/BRIEF.md`
3. `operations/STATE.md`
4. `operations/AVAILABLE_RESOURCES.md`
5. `PROMPT_VIVO/README.md`
6. `PROMPT_VIVO/CORE.md`
7. `PROMPT_VIVO/EXECUTION_PROTOCOL.md`
8. `PROMPT_VIVO/MEMORY_AND_HANDOFF.md)
9. `PROMPT_VIVO/MASTER_PROMPT.md`

Não presumir que o nome de uma pasta ou o último número de fase descreve sozinho o trabalho.

## Etapa 2 — Descobrir qual trabalho está ativo
1. Identificar o RUN_ID apontado por `operations/STATE.md`.
2. Ler, nessa execução, `RESUME_PACKET.md` primeiro.
3. Ler `RUN_STATE.md`, `PHASE_ARCHITECTURE.md`, `PHASE_CONTROL.md), `RESEARCH_PLAN.md), `MEMORY_HANDOFF.md) e o checkpoint da fase ativa.
4. Ler a instrução completa da fase ativa.
5. Consultar `SOURCE_LEDGER.md`, `FINDINGS.md), `OPEN_QUESTIONS.md), matrizes e entregáveis indicados pelo pacote de retomada.
6. Se dois arquivos divergirem, não escolher silenciosamente: comparar datas/versões, priorizar o registro mais recente e explícito, registrar a divergência e corrigir os arquivos dependentes antes de prosseguir.

## Etapa 3 — Reconstruir o contexto completo
Antes de agir, formular internamente um mapa que identifique:
- projeto e objetivo comercial/operacional maior;
- execução ativa (ID, título, escopo e motivo de existir);
- pesquisa específica em andamento e a pergunta principal que ela tenta responder;
- hipóteses incluídas, excluídas e ainda não escolhidas;
- fase/subfase ativa, seu gate, dependências e critérios de saída;
- o que já foi feito, com evidências e fontes;
- o que foi tentado e falhou;
- decisões e preferências expressas pelo usuário;
- recursos, orçamento, prazos e restrições;
- ações proibidas sem aprovação;
- lacunas que realmente podem mudar a decisão;
- próxima ação concreta e menor passo útil.

Não dizer que possui "certeza total". Declarar contexto reconstruído a partir dos arquivos, apontar divergências e distinguir fato, inferência e hipótese.

## Etapa 4 — Integrar a conversa atual e feedback do usuário
O repositório é a memória durável; a conversa atual é uma camada de entrada adicional.
1. Capturar comentários, correções, novas preferências, rejeições, prioridades e autorizações explícitas do usuário.
2. Interpretar feedback como possível alteração de escopo, critérios, método, prioridade ou gate — não apenas como comentário social.
3. Comparar cada entrada com decisões anteriores. Se houver conflito, preservar o histórico e registrar a decisão mais recente, sem apagar a anterior.
4. Atualizar `USER_INPUT_LOG.md` com data, conteúdo resumido, impacto, arquivos afetados e status (APLICADO, INCORPORADO AO PLANO, SEM IMPACTO, AGUARDA APROVAÇÃO).
5. Não transformar um pedido de "próxima/continua" em autorização para ações externas, gastos ou aprovação factual de um gate.
6. Não pedir ao usuário para repetir informação já presente nos arquivos ou na conversa.

## Etapa 5 — Auditoria antes de continuar
Executar `PHASE_CONTROL.md`. Verificar:
- completude real da fase atual;
- evidências e contraprovas;
- entregáveis faltantes;
- pesquisas redundantes;
- mudanças trazidas pelo usuário;
- cotas/limites e margem;
- consistência entre estado, arquitetura, plano, checkpoint e handoff.

Escolher e executar a ação mínima útil: CONTINUE_PHASE, CREATE_SUBPHASE, REOPEN_PHASE, ADVANCE, SYNTHESIZE ou BLOCK.

## Etapa 6 — Trabalho e persistência
Depois da decisão:
- executar pesquisa/análise real, não apenas anunciar tarefas;
- registrar cada fonte e o que ela prova/não prova;
- atualizar achados, perguntas, matriz, arquitetura e checkpoint;
- sincronizar `RUN_STATE.md`, `RESEARCH_PLAN.md`, `MEMORY_HANDOFF.md), `RESUME_PACKET.md) e `operations/STATE.md);
- atualizar o `USER_INPUT_LOG.md);
- salvar mudanças no GitHub e só declarar persistência após confirmação.

## Etapa 7 — Resposta ao usuário
Começar com uma confirmação concisa do contexto reconstruído: projeto, execução, pergunta da pesquisa, fase e estado. Depois informar o que foi auditado e efetivamente executado, decisão de fase, achados, lacunas e próxima ação. Não despejar todos os arquivos se não for necessário.

## Limites
Este protocolo melhora a continuidade, mas não garante onisciência: a IA só pode reconstruir o que foi registrado e está acessível. Se arquivos essenciais estiverem ausentes, contraditórios ou inacessíveis, dizer exatamente o que falta. Nunca inventar contexto.
