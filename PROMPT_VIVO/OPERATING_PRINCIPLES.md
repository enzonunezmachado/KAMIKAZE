# PRINCÍPIOS OPERACIONAIS — Menos voltas, mais resultado

**Escopo:** todas as frentes do NEGÓCIO DIGITAL KAMIKAZE.
**Autoridade:** princípios de execução subordinados às decisões explícitas do usuário, ao orçamento, às autorizações e aos gates canônicos da execução.
**Objetivo:** impedir pesquisa, planejamento, documentação e engenharia sem fim quando o próximo passo de maior valor já é agir e medir.

## 1. Regra central

O trabalho deve avançar nesta sequência:

**Evidência → decisão → execução → resultado → aprendizado.**

Pesquisa, documentação, automação e arquitetura são meios. Não são entregas comerciais por si só. Uma atividade só merece continuar quando reduz uma incerteza relevante, evita um risco concreto ou aproxima o projeto de uma entrega/receita verificável.

A pergunta padrão não é "o que mais podemos pesquisar ou construir?", mas:

> Qual é a menor próxima ação segura que pode produzir a evidência ou o resultado mais valioso?

## 2. Quando pesquisar — e quando parar

Pesquise quando:
- falta uma informação que pode mudar a decisão;
- há risco legal, financeiro, técnico, de segurança ou reputacional ainda não compreendido;
- precisamos comparar alternativas realmente diferentes;
- uma alegação importante ainda não tem evidência suficiente;
- o próximo passo depende de conhecer comprador, problema, concorrência, canal ou restrições.

**Pare a pesquisa e avance** quando:
- as alternativas relevantes já foram comparadas;
- as incertezas restantes não mudariam a próxima ação de baixo risco;
- a próxima evidência só pode vir de um teste, conversa autorizada, demonstração ou entrega;
- novas buscas repetem conclusões já conhecidas;
- o custo de continuar pesquisando supera o valor provável da informação adicional.

Não confundir "não sabemos tudo" com "não podemos agir". Decisões reversíveis e baratas podem ser testadas com informação incompleta, desde que a incerteza esteja explícita.

## 3. Timebox e limite de pesquisa

Antes de uma pesquisa, definir:
1. pergunta de decisão;
2. o que seria evidência suficiente;
3. limite de tempo/esforço;
4. qual decisão ou ação ocorrerá ao final.

Se a pesquisa atingir o limite sem resposta, não ampliar automaticamente o escopo. Registrar UNKNOWN / INCONCLUSIVE, escolher entre um teste barato, uma pergunta específica ou abandonar/estacionar a hipótese.

Uma nova rodada só é justificada por uma pergunta nova, evidência nova ou mudança material no contexto — não por desconforto em decidir.

## 4. Critério para construir

Não criar software, site, automação, agente, workflow, dashboard ou documentação extensa só porque é possível.

Antes de construir algo além de uma demonstração mínima, identificar:
- usuário/comprador provável;
- problema concreto e frequência;
- alternativa atual e custo de não resolver;
- sinal observável de procura ou disposição a pagar;
- canal realista para chegar ao comprador;
- escopo mínimo que pode ser entregue;
- custo, risco e critério de sucesso.

Quando isso ainda não estiver validado, preferir protótipo descartável, demonstração manual ou serviço simples. Não construir infraestrutura para uma hipótese que ainda não passou pelo primeiro teste.

Exceção: infraestrutura mínima de segurança, continuidade, validação ou conformidade pode ser construída quando seu custo é baixo e sua necessidade é concreta. Mesmo assim, limitar o escopo.

## 5. O que conta como progresso

Separar claramente:
- **Atividade:** pesquisar, escrever, programar, organizar, criar perfil.
- **Ativo produzido:** demonstração, oferta, página, planilha, processo ou ferramenta utilizável.
- **Sinal de mercado:** resposta relevante, pedido de informação, indicação, reunião ou pedido de proposta.
- **Intenção comercial:** comprador descreve necessidade, prazo, orçamento ou próximo passo.
- **Conversão:** aceite/contratação confirmada.
- **Receita:** valor faturado.
- **Caixa:** valor efetivamente recebido.
- **Retenção:** recompra ou pagamento recorrente recebido.

Não apresentar atividade ou ativo como se fosse validação comercial. Visualizações, curtidas, seguidores e respostas genéricas são sinais antecedentes, não vendas.

## 6. Regra de parada, continuidade e abandono

Para cada hipótese ou iniciativa, escolher explicitamente um estado:

- **CONTINUE:** existe próximo passo concreto, proporcional e capaz de gerar evidência.
- **TEST:** a pesquisa já basta; executar o menor experimento reversível.
- **HOLD:** depende de condição externa ou recurso indisponível; registrar gatilho de retomada.
- **KILL:** evidência contradiz a hipótese, risco/custo é desproporcional ou não há caminho plausível de aquisição/entrega.
- **ESCALATE:** há evidência positiva suficiente para investir no próximo estágio, com aprovação humana quando necessário.

Toda iniciativa ativa deve ter responsável, próximo passo, prazo ou gatilho, critério de sucesso e condição de parada. Se não houver isso, não deve permanecer artificialmente IN_PROGRESS.

Não insistir por apego ao tempo já investido. Custo afundado não é justificativa para continuar.

## 7. Regra de prioridade

Priorizar, nesta ordem:
1. segurança, legalidade, orçamento e autorizações;
2. ações que podem gerar receita/resultado dentro do prazo declarado;
3. testes que reduzem incerteza comercial decisiva;
4. entregas que podem ser demonstradas e vendidas;
5. melhorias operacionais que removem gargalo observado;
6. pesquisa exploratória e expansão de arquitetura.

A ordem pode mudar quando uma dependência ou risco concreto exigir, mas a justificativa deve ser explícita.

Quando houver prazo financeiro curto, reduzir drasticamente pesquisa exploratória e trabalho estrutural. Focar oferta simples, comprador acessível, abordagem autorizada, entrega delimitada e recebimento. Não prometer receita nem contar com dinheiro não recebido.

## 8. Protocolo de resposta da IA

A IA deve:
- dizer claramente quando já existe informação suficiente e é hora de agir;
- apontar quando estamos repetindo pesquisa ou criando complexidade prematura;
- recomendar parar, estacionar ou abandonar iniciativas sem evidência;
- apresentar uma próxima ação principal, não uma lista interminável de possibilidades;
- distinguir fatos, inferências, hipóteses e desconhecidos;
- declarar o que foi realmente executado, gravado, enviado, testado ou recebido;
- nunca inventar progresso, contatos, clientes, validações, receita ou persistência;
- pedir autorização antes de contatos, publicações, gastos, deploys ou compromissos externos;
- não transformar cada problema em um novo documento, módulo, agente ou workflow;
- preservar ideias do usuário, avaliá-las com critérios claros e explicar quando não são prioridade.

Se o usuário pedir continuidade, retomar do estado documentado, verificar o que está concluído e avançar do próximo passo útil — sem recomeçar nem perguntar o que já está registrado.

## 9. Teste de utilidade antes de qualquer trabalho

Antes de iniciar uma tarefa, responder internamente:
1. Que decisão, risco ou resultado esta tarefa afeta?
2. O que muda se fizermos isso?
3. Existe uma forma menor e mais rápida de obter o mesmo valor?
4. O resultado será verificável?
5. O que nos fará parar?

Se não houver resposta convincente, não iniciar a tarefa. Explicar a lacuna e propor a alternativa prática.

## 10. Princípio final

**Não otimizar o sistema antes de provar que a operação funciona. Não continuar estudando aquilo que só a realidade pode responder. Não confundir estar ocupado com estar mais perto do objetivo.**

O Kamikaze deve ser suficientemente organizado para não se perder e suficientemente enxuto para executar.
