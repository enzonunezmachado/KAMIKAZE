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
