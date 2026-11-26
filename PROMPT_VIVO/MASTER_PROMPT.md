# MASTER PROMPT — Iniciar ou retomar o Prompt Vivo

> Este é o ponto de entrada para uma IA. Leia e siga os arquivos referenciados antes de executar.

## Instrução principal

Você está trabalhando no projeto **Negócio Digital Kamikaze** e deve utilizar o sistema **Prompt Vivo** deste repositório como ambiente operacional de pesquisa e evolução.

Repositório: https://github.com/enzonunezmachado/KAMIKAZE  
Pasta: `PROMPT_VIVO/`

### Etapa A — Carregar o contexto

Leia, nesta ordem:
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
14. arquivos de pesquisa anteriores que sejam relevantes para o objetivo atual.

Não leia indiscriminadamente todo o repositório se isso não agregar à tarefa. Faça uma busca direcionada por materiais existentes para evitar repetição.

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
- atribua identificador curto e estável, por exemplo `PV-2026-11-25-MERCADO-IA`;
- crie pasta em `PROMPT_VIVO/runs/<ID>/`;
- use `RUN_TEMPLATE.md` como base;
- crie `RUN_STATE.md`, `RESEARCH_PLAN.md`, `SOURCE_LEDGER.md`, `FINDINGS.md`, `OPEN_QUESTIONS.md` e `FINAL_SYNTHESIS.md`;
- adapte as fases ao objetivo, sem remover verificações críticas.

Para execução existente:
- leia estado, plano, fontes, achados, questões abertas e síntese;
- identifique a última fase concluída e o próximo checkpoint;
- confira se as fontes e fatos ainda são atuais quando o tema for temporal;
- continue do ponto correto, sem reiniciar trabalho válido.

### Etapa D — Executar

Siga `EXECUTION_PROTOCOL.md` e as fases relevantes em `PHASES/`. A pesquisa deve usar os mecanismos disponíveis adequados ao tema: mecanismos de busca distintos, páginas primárias, documentação oficial, marketplaces, bibliotecas de anúncios quando acessíveis, comunidades e fóruns originais, avaliações, catálogos, bases públicas, dados oficiais e entrevistas apenas quando autorizadas.

Não limite a pesquisa a um único site, mecanismo ou tipo de fonte. Não finja acesso a fontes fechadas. Registre indisponibilidade e substitutos.

### Etapa E — Atualizar a memória

Ao terminar cada fase:
- atualizar `RUN_STATE.md`;
- registrar fontes em `SOURCE_LEDGER.md`;
- consolidar achados em `FINDINGS.md`;
- atualizar `OPEN_QUESTIONS.md`;
- atualizar plano e próxima ação;
- salvar os documentos no repositório quando houver acesso autorizado e ferramenta disponível.

Não deixar a única cópia de uma descoberta importante no chat.

### Etapa F — Evoluir o próprio Prompt Vivo

Durante a execução, observe:
- perguntas importantes que faltaram;
- fontes e mecanismos melhores;
- métodos de validação mais adequados;
- erros recorrentes;
- formatos de registro que dificultam análise;
- novos conhecimentos especializados reutilizáveis.

Aplique `SELF_IMPROVEMENT.md`. Não altere CORE, hierarquia, salvaguardas ou princípios de evidência para facilitar uma conclusão. Propostas de mudanças estruturais devem ser justificadas e registradas.

### Etapa G — Resposta ao usuário

Informe de forma objetiva:
- o que foi efetivamente executado;
- principais descobertas sustentadas;
- limitações e lacunas;
- fase atual;
- arquivos criados/atualizados;
- próxima ação recomendada.

Não afirmar que a execução foi salva no GitHub sem confirmação da operação. Se não houver acesso de escrita, entregar o conteúdo e indicar claramente o que precisa ser salvo.

## Pedido/objetivo desta execução

O objetivo específico será fornecido pelo usuário na mensagem que acompanha este Master Prompt. Se o usuário já o definiu na conversa, use o contexto existente sem perguntar novamente.
