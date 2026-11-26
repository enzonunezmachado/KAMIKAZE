# BOOTSTRAP — Inicialização e retomada entre chats

**Obrigatório** sempre que a conversa for nova, o usuário pedir continuidade, mencionar trabalho anterior ou disser “continua/próxima”.

## 0. Carregar o sistema de continuidade
Leia primeiro:
1. `PROMPT_VIVO/CONTINUITY_SYSTEM.md`
2. `PROMPT_VIVO/MASTER_PROMPT.md`
3. `PROMPT_VIVO/EXECUTION_PROTOCOL.md`
4. `PROMPT_VIVO/MEMORY_AND_HANDOFF.md`

## 1. Identificar a execução ativa
1. Leia `README.md`, `operations/STATE.md`, `operations/AVAILABLE_RESOURCES.md` e `PROMPT_VIVO/README.md`.
2. Use `operations/STATE.md` como ponteiro para descobrir o RUN_ID ativo; não adivinhe pelo nome mais recente.
3. Leia `PROMPT_VIVO/runs/<RUN_ID>/RESUME_PACKET.md` primeiro.
4. Leia o `SESSION_LOG.md` global e o da execução; confira os eventos mais recentes e a persistência.
5. Leia `RUN_STATE.md`, `PHASE_ARCHITECTURE.md`, `PHASE_CONTROL.md`, `RESEARCH_PLAN.md`, `MEMORY_HANDOFF.md`, `USER_INPUT_LOG.md` e o checkpoint/instrução da fase ativa.

## 2. Reconstruir o contexto
Identifique:
- missão do projeto e meta contextual;
- execução, escopo e pergunta central;
- linhas de pesquisa ativas, em pausa, encerradas ou rejeitadas;
- fase/subfase, gate, dependências e critério de saída;
- o que já foi feito e o que as evidências realmente provam/não provam;
- fontes, contraprovas, tentativas malsucedidas e perguntas abertas;
- decisões e preferências humanas;
- recursos, orçamento, prazos e restrições;
- ações que exigem autorização explícita;
- próxima ação concreta.

Não alegue certeza total. Diferencie fato documentado, inferência e hipótese.

## 3. Auditar divergências e completude
Compare data, eventos e estado entre operations/STATE, RUN_STATE, PHASE_CONTROL, PHASE_ARCHITECTURE, RESUME_PACKET, MEMORY_HANDOFF e SESSION_LOG.
- Se houver divergência, identificar origem e versão mais recente confirmada.
- Não escolher silenciosamente.
- Registrar reconciliação como novo evento e sincronizar arquivos dependentes.
- Se não for possível determinar o estado com segurança, marcar BLOCKED e perguntar somente o indispensável.

Executar o controlador adaptativo e decidir: CONTINUE_PHASE, CREATE_SUBPHASE, REOPEN_PHASE, ADVANCE, SYNTHESIZE ou BLOCK. Não avançar só porque uma fase seguinte existe ou porque acabou o chat.

## 4. Incorporar a conversa atual
A mensagem atual do usuário é uma nova camada de entrada. Capturar correções, novas ideias, preferências, prioridades, rejeições e autorizações; comparar com decisões anteriores; registrar em USER_INPUT_LOG.md e atualizar os arquivos afetados. Preservar histórico, sem apagar decisões antigas.

## 5. Continuar o trabalho
- Executar a próxima ação de pesquisa/análise autorizada.
- Não reiniciar a pesquisa nem repetir trabalho válido.
- Não perguntar ao usuário o que já está documentado.
- Entregar resultados consolidados, com fontes, limites, contraprovas e decisão.
- Não realizar ações externas sem autorização.

## 6. Checkpoint obrigatório
Após cada lote relevante e antes de encerrar/transferir:
1. atualizar SOURCE_LEDGER, FINDINGS, OPEN_QUESTIONS e matrizes;
2. atualizar checkpoint/instrução da fase, PHASE_CONTROL e PHASE_ARCHITECTURE quando aplicável;
3. atualizar USER_INPUT_LOG;
4. sincronizar RUN_STATE, MEMORY_HANDOFF e RESUME_PACKET;
5. sincronizar operations/STATE;
6. acrescentar SESSION_LOG da execução e global;
7. atualizar CHANGELOG quando o próprio Prompt Vivo mudar;
8. confirmar as gravações no GitHub e registrar commit SHA quando disponível.

Se não houver escrita disponível, entregar conteúdo copiável e declarar NÃO PERSISTIDO. Nunca alegar que salvou sem confirmação.

## 7. Resposta de retomada
Informar brevemente projeto, execução, pergunta ativa, fase/gate, divergências resolvidas, trabalho que será continuado e próxima ação. Não despejar todo o repositório.

**Limite:** este protocolo não executa trabalho em segundo plano. Ele permite retomada confiável com base nos registros persistidos e acessíveis.
