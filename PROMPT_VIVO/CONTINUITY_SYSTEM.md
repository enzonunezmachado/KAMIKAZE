# CONTINUITY SYSTEM — Memória, histórico e retomada entre chats

**Versão:** 1.0  
**Projeto:** NEGÓCIO DIGITAL KAMIKAZE  
**Objetivo:** garantir que o trabalho sobreviva a limites de conversa, troca de chat ou troca de modelo, sem depender da memória interna do assistente.

## 1. Princípio fundamental

O repositório GitHub é a memória persistente e a fonte de continuidade do projeto. A conversa é uma sessão temporária de trabalho.

Nenhuma descoberta, decisão, correção, autorização, mudança de fase ou próxima ação importante pode existir somente no chat. O trabalho só é considerado documentado quando os arquivos foram atualizados e a gravação foi confirmada.

Este sistema não executa trabalho em segundo plano e não consegue salvar dados depois que uma sessão termina sem uma ferramenta/sessão ativa. Ele torna obrigatória a persistência durante o trabalho e antes de encerrar ou transferir a conversa.

## 2. Ponteiro canônico de trabalho atual

- `PROMPT_VIVO/CURRENT_WORK.md` é a fonte única para apontar a última linha/entrega substantivamente desenvolvida ou atualizada e a próxima ação de retomada.
- O ponteiro é distinto do estado da pesquisa principal: uma linha operacional recém-documentada pode ser o último trabalho realizado sem substituir a fase de pesquisa ainda ativa.
- `operations/STATE.md` continua identificando a execução ativa e suas restrições; `RUN_STATE.md` continua registrando o estado detalhado da execução.
- Em todo checkpoint relevante, atualizar `CURRENT_WORK.md` depois de determinar o que foi efetivamente concluído. Sincronizar os atalhos para apontarem a ele, em vez de manter cópias independentes do foco mais recente.
- Não atualizar o ponteiro apenas por edição incidental, criação de fase vazia ou mudança de data. Exigir trabalho substantivo e gravação confirmada.
- Se o trabalho mais recente não puder ser determinado, registrar `NEEDS_RECONCILIATION`; não adivinhar.

## 3. Arquitetura: quatro camadas

### Camada A — Estado canônico
- `operations/STATE.md`: ponteiro do projeto para a execução ativa, missão, estado comercial, recursos e restrições.
- `PROMPT_VIVO/runs/<RUN_ID>/RUN_STATE.md`: estado detalhado da execução e fase/subfase.
- `PHASE_CONTROL.md`: decisão de gate e ação permitida.
- `PHASE_ARCHITECTURE.md`: estrutura e dependências das fases.

### Camada B — Memória de trabalho
- `RESUME_PACKET.md`: pacote canônico e curto de retomada.
- `MEMORY_HANDOFF.md`: contexto ampliado e transferência.
- `RESEARCH_PLAN.md`: perguntas e método.
- `SOURCE_LEDGER.md`: fontes, datas, evidências e limitações.
- `FINDINGS.md`: achados consolidados.
- `OPEN_QUESTIONS.md`: lacunas e próximos estudos.
- `USER_INPUT_LOG.md`: decisões, correções, preferências e autorizações humanas.

### Camada C — Histórico de alterações
- `PROMPT_VIVO/SESSION_LOG.md`: histórico global, append-only, de sessões e alterações estruturais.
- `PROMPT_VIVO/runs/<RUN_ID>/SESSION_LOG.md`: histórico detalhado de cada execução.
- `PROMPT_VIVO/CHANGELOG.md`: mudanças no próprio Prompt Vivo, protocolos, templates e governança.

Os logs registram eventos e apontam para os arquivos alterados; não substituem o conteúdo atual desses arquivos. Não reescrever o histórico para apagar decisões anteriores. Correções são novos eventos que referenciam o evento corrigido.

### Camada D — Retomada simples
- `PROMPT_VIVO/NEXT_CHAT_PROMPT.md`: texto pronto para copiar e colar em um novo chat.
- `PROMPT_VIVO/BOOTSTRAP.md`: procedimento obrigatório que reconstrói o contexto e audita a consistência antes de agir.

## 4. Quando documentar

A documentação é atualizada em quatro momentos:

1. **Após cada lote relevante de pesquisa:** registrar fontes e achados antes de iniciar uma nova trilha.
2. **Após cada decisão:** registrar mudança de hipótese, prioridade, escopo, método, fase, gate ou restrição.
3. **Em checkpoints:** atualizar todos os arquivos de estado e retomada após uma unidade coerente de trabalho.
4. **Antes de encerrar, trocar de chat ou quando houver sinal de limite:** fazer checkpoint de transferência imediatamente.

Não é necessário criar commit por cada busca individual. Agrupar mudanças relacionadas em checkpoints, mas nunca deixar um lote de pesquisa significativo sem registro.

## 5. Protocolo obrigatório de checkpoint

Executar nesta ordem:

0. Determinar a última unidade substantiva concluída; atualizar `PROMPT_VIVO/CURRENT_WORK.md` e conferir se a próxima ação continua correta.
1. Registrar novas fontes em `SOURCE_LEDGER.md`, com ID único sequencial e o que a fonte prova/não prova.
2. Consolidar achados em `FINDINGS.md`, distinguindo observação, cálculo, inferência, hipótese e contraprova.
3. Atualizar `OPEN_QUESTIONS.md` e `VALIDATION_MATRIX.md` quando aplicável.
4. Atualizar instrução/checkpoint da fase e `PHASE_CONTROL.md`.
5. Atualizar `PHASE_ARCHITECTURE.md` e `RESEARCH_PLAN.md` se escopo, dependência ou sequência mudou.
6. Atualizar `USER_INPUT_LOG.md` para cada nova entrada humana que altere o trabalho.
7. Atualizar `RUN_STATE.md` com estado real, fase, gate, progresso, bloqueios e próxima ação concreta.
8. Atualizar `MEMORY_HANDOFF.md` com contexto suficiente para outra IA.
9. Atualizar `RESUME_PACKET.md` por último, para refletir os arquivos já sincronizados.
10. Atualizar `operations/STATE.md` com o ponteiro da execução e estado resumido, sem duplicar toda a pesquisa.
11. Acrescentar evento no log da execução e no log global; atualizar `PROMPT_VIVO/CHANGELOG.md` apenas quando o próprio sistema/instruções mudar.
12. Confirmar que todas as gravações foram aceitas pelo GitHub. Registrar commit SHA quando a ferramenta o fornecer.

Se não houver ferramenta de escrita, produzir os arquivos atualizados em conteúdo copiável e declarar que ainda não foram persistidos. Nunca afirmar que salvou sem confirmação.

## 6. Estrutura mínima de cada evento de sessão

Cada entrada nos logs deve incluir:
- ID do evento, único e crescente (ex.: `KAM-2026-11-26-001`);
- data;
- sessão/rodada;
- objetivo do trabalho;
- ações efetivamente executadas;
- descobertas e decisões;
- arquivos criados/alterados;
- estado/gate após a sessão;
- pendências e próxima ação;
- limitações, falhas e ações que não foram realizadas;
- commit SHA ou estado de persistência (CONFIRMADO / NÃO PERSISTIDO).

Não registrar somente “continuamos a pesquisa”. Escrever o que mudou e por que importa.

## 7. Protocolo de retomada em novo chat

Quando receber o texto de `NEXT_CHAT_PROMPT.md`:

1. Abrir o repositório e ler este sistema e `BOOTSTRAP.md`.
2. Ler `operations/STATE.md` para descobrir a execução ativa; não adivinhar pelo nome mais recente.
3. Ler `RESUME_PACKET.md` primeiro e depois os arquivos detalhados indicados.
4. Verificar datas, IDs de evento, commits e consistência entre estado, handoff, arquitetura e controlador.
5. Consultar o final dos logs para saber o que aconteceu na última sessão.
6. Comparar o estado do repositório com a conversa atual. A mensagem atual do usuário pode trazer nova prioridade ou correção; registrar antes de prosseguir.
7. Reconstituir internamente o contexto: missão, execução, pergunta ativa, fases, hipóteses, evidências, contraprovas, decisões, recursos, orçamento, proibições, pendências e próxima ação.
8. Executar auditoria de completude e escolher CONTINUE_PHASE, CREATE_SUBPHASE, REOPEN_PHASE, ADVANCE, SYNTHESIZE ou BLOCK conforme o controlador.
9. Continuar do próximo passo útil. Não repetir pesquisas já suficientes, não recomeçar do escopo e não pedir ao usuário dados já registrados.
10. Ao final do primeiro checkpoint no novo chat, registrar a retomada como novo evento de sessão.

## 8. Resolução de divergências

Não existe um arquivo isolado que possa sobrepor silenciosamente todos os outros.

- Para descobrir qual execução está ativa: `operations/STATE.md`.
- Para saber o que fazer agora: `PHASE_CONTROL.md` + `RUN_STATE.md`, auditados contra a arquitetura e o plano.
- Para reconstruir o contexto: `RESUME_PACKET.md` + `MEMORY_HANDOFF.md`.
- Para histórico de mudanças: `SESSION_LOG.md` e `CHANGELOG.md`.
- Para fatos e evidências: `SOURCE_LEDGER.md` + fontes originais; o resumo nunca substitui a fonte.
- Para decisões humanas: `USER_INPUT_LOG.md`, respeitando a decisão mais recente sem apagar o histórico.

Se dois arquivos divergirem:
1. identificar qual é o mais recente e se a atualização foi confirmada;
2. conferir os logs e os commits;
3. conferir se a divergência é factual, temporal ou apenas de granularidade;
4. não escolher silenciosamente;
5. registrar a reconciliação como evento;
6. sincronizar os arquivos dependentes antes de iniciar uma nova linha de pesquisa.

Se a fonte de verdade não puder ser determinada, marcar BLOCKED e pedir apenas a informação realmente indispensável.

## 9. Regras de economia de contexto

- O `RESUME_PACKET.md` deve ser curto o bastante para leitura rápida, mas apontar para detalhes.
- O `MEMORY_HANDOFF.md` guarda contexto ampliado, não cópia integral do Source Ledger.
- O `SESSION_LOG.md` é cronológico e conciso; não duplicar relatórios.
- Não carregar indiscriminadamente todos os arquivos do repositório; seguir os links do pacote e buscar detalhes conforme necessário.
- Manter um bloco “PRÓXIMA AÇÃO EXATA” com verbo, objeto, fonte/arquivo e critério de conclusão.
- Quando o contexto estiver perto do limite, interromper novas pesquisas, persistir o checkpoint e preparar a transferência.

## 10. Comportamento ao receber “continua”, “próxima” ou equivalente

Não perguntar qual fase vem depois. Executar bootstrap/auditoria, incorporar o feedback recente, escolher a menor ação útil e continuar. “Continua” não significa avançar automaticamente uma fase, nem autoriza contato externo, publicação, gasto, cadastro, contratação ou deploy.

## 11. Checklist de integridade

- [ ] Execução ativa identificada pelo estado operacional.
- [ ] RESUME_PACKET atualizado e coerente.
- [ ] RUN_STATE, PHASE_CONTROL e arquitetura coerentes.
- [ ] Fontes e achados persistidos.
- [ ] Feedback humano registrado.
- [ ] Pendências e próxima ação específicas.
- [ ] Logs global e da execução atualizados.
- [ ] Nenhuma ação não autorizada foi executada.
- [ ] Escrita confirmada ou limitação declarada.
- [ ] NEXT_CHAT_PROMPT continua válido e não depende de contexto oculto.

**Regra final:** a sessão só está pronta para transferência quando outra IA, sem acesso ao chat anterior, consegue identificar o que estamos fazendo, por que estamos fazendo, o que já foi demonstrado, o que ainda falta e qual é a próxima ação — sem pedir ao usuário que reconte a história.


## 12. Módulos dormentes e acionadores de ativação
O índice `PROMPT_VIVO/knowledge/README.md` pode apontar módulos futuros com estado DORMANT e seus documentos de acionamento. Durante o bootstrap, compare a mensagem atual do usuário com esses acionadores. Quando houver intenção clara:
1. ler integralmente o documento do acionador;
2. apresentar escopo, etapas, riscos, recursos, custos e entregáveis;
3. solicitar a confirmação expressamente definida;
4. respeitar gates adicionais por ação (contas, integrações, publicações, gastos);
5. registrar a ativação e atualizar estado/logs.
Não ativar por menções exploratórias, perguntas gerais ou pesquisa sem pedido de implementação.
