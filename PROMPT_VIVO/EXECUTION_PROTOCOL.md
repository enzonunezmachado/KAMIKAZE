# Protocolo de execução

## 1. Unidade de trabalho

Cada trabalho complexo deve ter uma execução própria em `runs/<RUN_ID>/`. Uma execução pode conter várias linhas de investigação, mas deve possuir um objetivo central, limites e critérios de conclusão explícitos.

## 2. Estados possíveis

- `NOT_STARTED` — criada, ainda sem pesquisa.
- `SCOPING` — objetivo e perguntas sendo definidos.
- `PLANNED` — plano aprovado internamente e pronto para execução.
- `IN_PROGRESS` — pesquisa ou análise em andamento.
- `BLOCKED` — dependência, acesso ou informação impede avanço.
- `NEEDS_HUMAN_INPUT` — decisão ou autorização do usuário necessária.
- `SYNTHESIS` — evidências coletadas, consolidação em andamento.
- `COMPLETED` — critérios atendidos; lacunas residuais documentadas.
- `REOPENED` — execução retomada por nova evidência ou mudança de contexto.

## 3. Ciclo por fase

Para cada fase:
1. Ler a instrução da fase.
2. Verificar o estado e os materiais já existentes.
3. Definir perguntas que a fase precisa responder.
4. Escolher fontes e métodos apropriados.
5. Executar pesquisas em lotes focados, evitando consultas redundantes.
6. Abrir e verificar fontes originais relevantes.
7. Registrar achados, fontes, data, limites e contradições.
8. Rodar o QUALITY GATE.
9. Atualizar arquivos da execução.
10. Decidir: avançar, aprofundar, repetir com método melhor ou bloquear aguardando decisão humana.

## 4. Critérios para avançar

Uma fase só avança quando:
- perguntas essenciais foram respondidas ou marcadas como não respondíveis;
- fontes e evidências foram registradas;
- contradições relevantes foram investigadas;
- lacunas restantes estão explícitas;
- o resultado pode ser entendido por outra IA sem depender do chat original;
- o gate de qualidade foi aplicado.

Não é necessário atingir certeza absoluta. É necessário tornar a incerteza visível.

## 5. Profundidade adaptativa

A IA deve aprofundar quando:
- uma descoberta pode alterar a decisão;
- existe divergência entre fontes;
- um dado crítico não tem fonte primária;
- há sinal de demanda, mas falta identificar comprador ou pagamento;
- a conclusão depende de premissa frágil;
- surge uma trilha promissora ainda pouco explorada.

A IA pode encerrar uma linha quando:
- fontes independentes convergem suficientemente;
- novas consultas repetem o mesmo conteúdo;
- custo de pesquisa supera o valor provável da informação;
- a hipótese foi enfraquecida por contraprovas fortes;
- não há acesso legítimo aos dados necessários.

Registrar o motivo do encerramento.

## 5.1 Arquitetura adaptativa de fases (obrigatória)

A sequência PHASE_00–PHASE_05 é um modelo inicial reutilizável, não uma esteira fixa nem um limite de seis fases. A IA responsável pela execução deve administrar o ciclo de vida das fases conforme o problema, as evidências e os gates.

### Ações permitidas durante uma execução
- **Avançar:** iniciar a próxima fase adequada quando o gate permitir.
- **Aprofundar:** manter a fase aberta e criar subetapas/lotes quando faltarem evidências decisivas.
- **Dividir:** separar uma fase em duas ou mais quando ela acumular perguntas heterogêneas ou frentes que exigem métodos diferentes.
- **Mesclar:** combinar fases redundantes quando a separação não agregar qualidade.
- **Reordenar:** alterar a sequência quando uma dependência ou descoberta exigir outra ordem.
- **Modificar:** ajustar objetivos, perguntas, métodos e entregáveis das fases futuras para refletir o que foi aprendido.
- **Adicionar:** criar fase nova quando surgir dimensão relevante não coberta pelo plano atual (ex.: aquisição, economia unitária, privacidade, experimentação, retenção, regulamentação).
- **Pular/encerrar:** marcar fase ou linha como não necessária, inaplicável, redundante ou sem valor adicional, sempre registrando justificativa e evidências.
- **Reabrir:** retornar a fase anterior se nova evidência invalidar premissa, decisão ou conclusão.

### Critérios de decisão
A IA deve avaliar: (1) a fase atual respondeu ao objetivo? (2) há perguntas críticas sem resposta? (3) uma fase existente cobre essas perguntas? (4) uma nova fase aumenta a clareza/controle ou apenas cria burocracia? (5) qual dependência, custo, risco e quota são afetados?

Não criar fase só para manter numeração ou simetria. Não encerrar fase apenas porque acabou o prompt. O critério é a suficiência das evidências e do entregável.

### Governança e rastreabilidade
1. A IA pode fazer ajustes locais e adaptativos nas fases da execução (Nível 1), sem pedir autorização adicional, desde que permaneçam dentro do escopo e das salvaguardas aprovadas.
2. Quando a mudança for reutilizável, criar/atualizar instrução especializada (Nível 2) e registrar no changelog.
3. Toda alteração na arquitetura de uma execução deve ser registrada em PHASE_ARCHITECTURE.md dentro da run, com ID, motivo, data, fases afetadas, mudança, dependências, impacto nas cotas, entregáveis e decisão de gate.
4. Atualizar RESEARCH_PLAN.md, RUN_STATE.md e MEMORY_HANDOFF.md para refletir a arquitetura vigente. Não deixar a lista de fases desatualizada.
5. Preservar instruções originais; modificar de forma versionada ou registrar o delta, sem apagar histórico.
6. Alterações no CORE, hierarquia, salvaguardas ou neste protocolo central continuam sujeitas ao Nível 3 e à aprovação humana, salvo autorização explícita já dada pelo usuário.

### Critério de encerramento de uma fase
Uma fase pode ser concluída sem criar outra quando seus critérios foram atendidos e não existe trabalho adicional que altere a decisão. Nesse caso, avançar para a fase existente mais útil ou para síntese. Uma fase pode gerar novas fases mesmo que a lista original termine; não existe limite fixo de quantidade.

## 6. Pesquisa paralela

Dividir a execução em frentes quando isso aumentar cobertura sem prejudicar consistência. Exemplos:
- mercado e tendências;
- público e problemas;
- concorrentes e substitutos;
- preços e economia;
- canais e aquisição;
- tecnologia, políticas e riscos.

Consolidar os resultados em uma visão única e eliminar duplicatas. Não confundir quantidade de frentes com profundidade.

## 7. Checkpoints

Ao final de cada fase, produzir um checkpoint contendo:
- fase concluída;
- o que foi pesquisado;
- descobertas principais;
- fontes mais relevantes;
- contradições;
- confiança e lacunas;
- decisões tomadas;
- próxima fase e tarefas.

## 8. Limites de execução e continuidade

Se o chat estiver perto do limite de contexto ou a tarefa exigir outra sessão:
1. parar em checkpoint seguro;
2. salvar todos os registros necessários;
3. atualizar `RUN_STATE.md` com a próxima ação exata;
4. atualizar `MEMORY_HANDOFF.md` com contexto compacto;
5. listar arquivos que o próximo chat deve ler;
6. não declarar a fase concluída se estiver incompleta.

O próximo chat deve conseguir retomar sem depender da memória implícita do chat anterior.

## 9. Critério de encerramento

Concluir quando o objetivo da execução foi atendido, as perguntas decisivas foram respondidas dentro do possível e a síntese apresenta:
- conclusões;
- evidências;
- incertezas;
- recomendações;
- decisões que dependem do usuário;
- próximos passos.

Pesquisa pode ser concluída sem que uma oportunidade seja aprovada. Um resultado negativo bem demonstrado também é resultado.



## 10. Entrega consolidada ao usuário — pesquisa em lote

Por padrão, quando o usuário pedir para continuar uma pesquisa, executar a rodada de forma orgânica e contínua, sem enviar atualizações parciais a cada subpesquisa, fonte ou pequena descoberta.

Fluxo obrigatório:
1. Reconstruir estado e critérios da execução.
2. Planejar internamente frentes de pesquisa e perguntas decisivas.
3. Pesquisar em lotes, cruzar fontes, validar status, comparar remuneração efetiva, prazos, elegibilidade, riscos e alternativas.
4. Fazer novas buscas quando surgirem contradições ou lacunas importantes.
5. Consolidar, priorizar e registrar fontes e descobertas na documentação.
6. Atualizar os arquivos de continuidade e estados operacionais.
7. Só então entregar ao usuário um relatório único, organizado e direto.

Não interromper o fluxo para narrar cada busca ou enviar pequenas descobertas, salvo se o usuário pedir acompanhamento em tempo real, houver uma decisão que dependa dele, risco urgente, ou autorização necessária para prosseguir.

A resposta final deve separar: resultado principal, oportunidades priorizadas, evidências de pagamento, requisitos/fit, riscos e incertezas, descartes, decisão do gate e próximos passos. Diferenciar claramente fatos confirmados, inferências e hipóteses. Não inflar a resposta com diário de pesquisa.

O usuário não solicita nem precisa receber raciocínio privado passo a passo. Não expor cadeia de pensamento interna; oferecer método resumido, critérios, fontes e justificativas verificáveis, além das conclusões.
