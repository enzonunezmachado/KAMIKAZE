# MASTER PROMPT — Iniciar ou retomar o Prompt Vivo

> Este é o ponto de entrada para uma IA. Leia e siga os arquivos referenciados antes de executar.

## Regra zero — novo chat / retomada
Se esta for uma conversa nova, ou o usuário pedir continuidade de trabalho anterior, **leia e execute integralmente `PROMPT_VIVO/BOOTSTRAP.md` antes de qualquer ação**. Não basta ler apenas o resumo: o pacote de retomada aponta os arquivos de detalhe que definem a execução real. Reconstrua projeto, execução, pesquisa atual, fase, evidências, decisões, recursos, restrições e próximo passo. Não alegue certeza total; declare divergências ou lacunas.

O repositório é a memória durável, mas mensagens do usuário na conversa atual também são entradas operacionais. Capture correções, comentários, novas preferências e prioridades em `USER_INPUT_LOG.md`; avalie se alteram escopo, método, critérios ou arquitetura antes de continuar. "Próxima/continua" autoriza continuidade, não avanço automático de fase nem ações externas.

## Instrução principal

Você está trabalhando no projeto **Negócio Digital Kamikaze** e deve utilizar o sistema **Prompt Vivo** deste repositório como ambiente operacional de pesquisa e evolução.

Repositório: https://github.com/enzonunezmachado/KAMIKAZE  
Pasta: `PROMPT_VIVO/`

### Etapa A — Carregar o contexto
Para retomada, siga BOOTSTRAP.md. Para uma execução nova, leia nesta ordem:
1. `README.md` do repositório;
2. `docs/BRIEF.md`;
3. `operations/STATE.md`;
4. `operations/AVAILABLE_RESOURCES.md`;
5. `PROMPT_VIVO/README.md`;
6. `PROMPT_VIVO/CORE.md`;
7. `PROMPT_VIVO/EXECUTION_PROTOCOL.md`;
8. `PROMPT_VIVO/RESEARCH_METHOD.md`;
9. `PROMPT_VIVO/EVIDENCE_STANDARD.md`;
10. `PROMPT_VIVO/QUALITY_GATE.md`;
11. `PROMPT_VIVO/SELF_IMPROVEMENT.md`;
12. `PROMPT_VIVO/MEMORY_AND_HANDOFF.md`;
13. arquivos da execução ativa em `PROMPT_VIVO/runs/`, se houver;
14. arquivos de pesquisa anteriores que sejam relevantes para a decisão atual.

Não leia indiscriminadamente todo o repositório se isso não agregar à tarefa. Faça busca direcionada por materiais existentes para evitar repetição.

### Etapa B — Identificar a intenção
Determine se o usuário quer:
- iniciar uma nova pesquisa/execução;
- continuar uma execução existente;
- reexecutar uma fase;
- auditar resultados;
- especializar o sistema em um domínio;
- atualizar os métodos do Prompt Vivo;
- encerrar e sintetizar uma execução.

Se houver execução ativa compatível, retome-a. Não crie outra execução para o mesmo objetivo sem motivo. Se o objetivo estiver ausente e for indispensável, faça uma única pergunta objetiva.

### Etapa C — Criar/retomar a execução
Para nova execução:
- atribua identificador curto e estável;
- crie pasta em `PROMPT_VIVO/runs/<ID>/`;
- use `RUN_TEMPLATE.md`;
- crie RUN_STATE, RESEARCH_PLAN, SOURCE_LEDGER, FINDINGS, OPEN_QUESTIONS e FINAL_SYNTHESIS;
- adapte as fases ao objetivo, sem remover verificações críticas.

Para execução existente:
- ler RESUME_PACKET, RUN_STATE, PHASE_ARCHITECTURE, PHASE_CONTROL, RESEARCH_PLAN, MEMORY_HANDOFF, USER_INPUT_LOG e checkpoint atual;
- abrir a instrução completa da fase e os artefatos relevantes;
- resolver divergências de estado explicitamente;
- identificar a próxima ação concreta e continuar sem reiniciar trabalho válido.

### Etapa D — Executar
Siga `EXECUTION_PROTOCOL.md` e as fases relevantes em `PHASES/`. A pesquisa deve usar mecanismos adequados ao tema: mecanismos de busca distintos, páginas primárias, documentação oficial, marketplaces, bibliotecas de anúncios quando acessíveis, comunidades e fóruns originais, avaliações, catálogos, bases públicas e entrevistas apenas quando autorizadas.

Não limite a pesquisa a um único site, mecanismo ou tipo de fonte. Não finja acesso a fontes fechadas. Registre indisponibilidade e substitutos.

### Etapa E — Atualizar a memória
Ao terminar cada fase ou checkpoint:
- atualizar RUN_STATE;
- registrar fontes em SOURCE_LEDGER;
- consolidar achados em FINDINGS;
- atualizar OPEN_QUESTIONS;
- atualizar plano e próxima ação;
- atualizar USER_INPUT_LOG quando houver nova entrada relevante;
- atualizar RESUME_PACKET e MEMORY_HANDOFF;
- sincronizar PHASE_ARCHITECTURE e operations/STATE;
- salvar no repositório quando houver acesso autorizado e ferramenta disponível.

Não deixar a única cópia de uma descoberta importante no chat.

### Etapa F — Evoluir o próprio Prompt Vivo
Observe perguntas faltantes, fontes melhores, métodos de validação, erros recorrentes e formatos de registro. Aplique SELF_IMPROVEMENT.md. Não altere CORE, hierarquia, salvaguardas ou princípios de evidência silenciosamente. Registre propostas e impactos.

### Etapa G — Resposta ao usuário
Informe objetivamente:
- contexto reconstruído (projeto, execução e pesquisa ativa);
- o que foi efetivamente executado;
- principais descobertas sustentadas;
- limitações e lacunas;
- fase atual e decisão do controlador;
- arquivos criados/atualizados;
- próxima ação.

Não afirmar que a execução foi salva no GitHub sem confirmação da operação. Se não houver acesso de escrita, entregar o conteúdo e indicar o que precisa ser salvo.

## Pedido/objetivo desta execução
O objetivo específico será fornecido pelo usuário na mensagem que acompanha este Master Prompt. Se o usuário já o definiu na conversa, use o contexto existente sem perguntar novamente.
