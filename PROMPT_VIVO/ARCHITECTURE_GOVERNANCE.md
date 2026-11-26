# Governança da arquitetura documental e memória operacional

**Status:** NORMATIVO para novas alterações; migração gradual dos documentos existentes.  
**Escopo:** Prompt Vivo, execuções, conhecimento e operações do NEGÓCIO DIGITAL KAMIKAZE.  
**Objetivo:** garantir que cada arquivo tenha função real, seja descoberto pela IA e tenha regras claras de leitura, escrita, autoridade e atualização.

## 1. Princípios

1. **Um arquivo = uma responsabilidade primária.** Não criar documentos que apenas repetem outros.
2. **Índices antes de profundidade.** A IA começa pelo README da pasta e abre detalhes sob demanda.
3. **Fonte canônica por tipo de informação.** Resumos apontam para a fonte; não competem com ela.
4. **Estado atual separado de histórico.** Estado é compacto e substituível; logs são append-only.
5. **Human-in-the-loop.** O usuário controla prioridades, hipóteses subjetivas, aprovações e ações externas.
6. **Progressive disclosure.** Carregar o mínimo necessário para a tarefa, não o repositório inteiro.
7. **Verificação executável.** Regras objetivas devem ser verificadas por scripts/CI sempre que possível.
8. **Documentação proporcional.** Não criar arquivo, pasta, fase ou agente sem necessidade demonstrável.
9. **Rastreabilidade.** Toda conclusão importante aponta para evidência, decisão ou fonte canônica.
10. **Preservação de ideias.** Insights do usuário são registrados mesmo quando ainda não têm evidência; classificá-los como hipótese/ideia, não descartá-los.

## 2. Fontes canônicas — quem manda em quê

| Informação | Fonte canônica | Documentos derivados |
|---|---|---|
| Última entrega substantiva | `PROMPT_VIVO/CURRENT_WORK.md` | Atalhos e logs apontam para ela |
| Execução ativa, recursos e restrições do projeto | `operations/STATE.md` | README e handoff resumem |
| Estado da fase/execução | `runs/<RUN_ID>/RUN_STATE.md` | RESUME_PACKET aponta |
| Gate e próxima ação permitida | `runs/<RUN_ID>/PHASE_CONTROL.md` | RESUME_PACKET aponta |
| Estrutura/dependência das fases | `PHASE_ARCHITECTURE.md` | Plano e handoff referenciam |
| Evidência e proveniência | `SOURCE_LEDGER.md` + fonte original | FINDINGS e resumos citam IDs |
| Síntese de achados | `FINDINGS.md` | RESUME_PACKET extrai apenas o essencial |
| Decisões/autorizações humanas | `USER_INPUT_LOG.md` | Documentos operacionais implementam sem reescrever a decisão |
| Contexto ampliado de transferência | `MEMORY_HANDOFF.md` | RESUME_PACKET contém só o essencial |
| Último contexto para novo chat | `RESUME_PACKET.md` (derivado) | Não é fonte de verdade de fase/evidência |
| Histórico de sessões | Logs globais e da execução (append-only) | Não substituem estado atual |
| Mudanças na metodologia | `PROMPT_VIVO/CHANGELOG.md` | README/índices apontam |

Em conflito, não escolher pelo timestamp isolado. Usar a fonte canônica correspondente, examinar eventos e commits, registrar a reconciliação e corrigir os derivados. Se a fonte canônica estiver ausente ou inconclusiva, marcar BLOCKED/NEEDS_RECONCILIATION.

## 3. Protocolo obrigatório de leitura em árvore

A leitura segue a navegação por níveis:

1. Raiz: `AGENTS.md` → `README.md`.
2. Sistema: `PROMPT_VIVO/AGENTS.md` → `PROMPT_VIVO/README.md`.
3. Ponteiro e regras: `CURRENT_WORK.md` → este documento → `BOOTSTRAP.md`.
4. Execução: `operations/README.md` → `operations/STATE.md`.
5. Pasta de execução: `runs/README.md` → `runs/<RUN_ID>/README.md`.
6. Resumo da execução: `RESUME_PACKET.md`; em seguida ler RUN_STATE e PHASE_CONTROL para estado/gate canônicos.
7. Abrir plano, fontes, achados, fase, dossiês e templates somente quando necessários. Sempre ler o README da pasta antes de navegar para dentro dela.

Se um README de pasta estiver ausente, não presumir estrutura nem gravar vários arquivos às cegas. Primeiro criar/atualizar o índice daquela pasta, explicando escopo, ordem de leitura, regra de gravação e o que não deve ser salvo ali.

## 4. Regras de tamanho e granularidade

Não existe limite universal de linhas. Usar estes orçamentos como alertas operacionais:

| Classe | Faixa recomendada | Ação ao exceder |
|---|---:|---|
| README/índice | 30–120 linhas | Mover detalhes para documentos próprios |
| AGENTS/instruções de entrada | 40–140 linhas | Separar regras gerais de skills específicas |
| Estado canônico | 30–120 linhas | Mover histórico e explicações para registros |
| Resumo de retomada | 40–120 linhas | Manter somente o essencial e links |
| Método/protocolo | 80–250 linhas | Dividir por responsabilidade quando a navegação melhorar |
| Dossiê/relatório/registro | Variável | Dividir por entidade, fase ou lote quando ficar difícil de consultar |
| Histórico append-only | Sem teto fixo | Particionar por ano/execução quando busca e leitura piorarem |

Essas faixas são heurísticas internas, não leis. Não fragmentar texto coeso só para cumprir contagem. Acima do orçamento, registrar justificativa ou refatorar.

## 5. Classificação documental inspirada em Diátaxis

Ao criar documentação técnica, identificar sua finalidade:
- **Tutorial:** ensina alguém a realizar uma primeira tarefa.
- **How-to / guia prático:** resolve uma tarefa específica.
- **Referência:** descreve campos, interfaces, regras, comandos e contratos.
- **Explicação:** registra conceitos, contexto e justificativas.

Um documento pode conter mais de um tipo em pequena escala, mas seu propósito primário deve estar claro. Não misturar tutorial com referência extensa nem esconder decisões em guias de execução.

## 6. Ciclo de vida de um documento

Antes de criar, responder:
- Qual problema este arquivo resolve?
- Quem precisa lê-lo e em qual momento?
- Qual fonte ele consulta e qual informação é sua responsabilidade?
- Quem/qual processo o atualiza e em que gatilho?
- O que deve ser salvo aqui e o que deve ficar em outro lugar?
- Como evitar cópia divergente?
- Como validar sua integridade?

Estados: PROPOSED → ACTIVE → DEPRECATED → ARCHIVED. Um documento só deve ser arquivado após atualizar links e preservar seu destino histórico.

## 7. Regras de escrita e sincronização

- README de pasta: propósito, escopo, ordem de leitura, conteúdo permitido/proibido, arquivos filhos e regra de atualização.
- Estado: sobrescrever o estado atual; não acumular diário.
- Log: acrescentar evento; não reescrever eventos antigos.
- Índice: lista e aponta; não duplica conteúdo.
- Template: estrutura vazia reutilizável; não registrar dados reais nele.
- Dossiê: fatos e evidências de uma entidade específica.
- Run: decisões e resultados de uma execução; não contaminar conhecimento permanente sem revisão.
- Knowledge: conhecimento reutilizável, com data, proveniência, limitações e validade temporal.
- Portfolio: somente materiais aprovados para divulgação; demos fictícias devem ser rotuladas e não insinuar clientes/cases reais.
- Checkpoint: atualizar somente documentos afetados; não editar arquivos por rotina se o conteúdo não mudou.
- Não marcar tarefa concluída sem artefato e verificação correspondentes.

## 8. Controle de tamanho e validação

O script `scripts/validate_docs.py` verifica presença de arquivos de entrada, README em diretórios operacionais, limites de tamanho dos documentos de retomada e referências locais selecionadas. GitHub Actions executa o script e o lint Markdown em push/pull request.

A CI verifica propriedades objetivas; não entende semântica de pesquisa, verdade de evidências, qualidade de uma ideia ou autorização humana. Revisão humana/IA continua necessária para esses critérios.

## 9. Como atualizar a própria arquitetura

Quando surgir uma nova necessidade:
1. capturar o insight do usuário sem apagá-lo;
2. identificar quais documentos/fluxos são afetados;
3. pesquisar padrões e alternativas quando necessário;
4. comparar custo de complexidade com benefício operacional;
5. propor ou aplicar somente o escopo autorizado;
6. atualizar índices, AGENTS, validator e histórico;
7. executar validação e registrar limitações.

**Não criar mais documentação como resposta automática a todo problema documental. Primeiro tentar corrigir a responsabilidade e a navegação existentes.**

## 10. Referências externas e decisões de adaptação

- [GitHub Spec Kit](https://github.github.com/spec-kit/): adotar constituição/princípios, artefatos por etapa, clarificação, tarefas dependenciadas, análise de consistência e convergência. Não importar o fluxo inteiro para pesquisa comercial sem adaptar.
- [BMAD Method](https://www.bmadcode.com/method): estudar papéis especializados, workflows, entregáveis e gates. Usar especialistas para tarefas delimitadas; não multiplicar agentes em exploração subjetiva sem benefício demonstrado.
- [AGENTS.md](https://agents.md/): usar instruções hierárquicas e específicas por pasta onde a ferramenta reconheça o padrão.
- [LangChain Deep Agents — Memory](https://docs.langchain.com/oss/python/deepagents/memory): adotar memória em arquivos, skills sob demanda e separação entre contexto curto e conhecimento persistente. Não presumir que qualquer IA terá filesystem ou memória automática.
- [Diátaxis](https://diataxis.fr/): classificar documentação por tutorial, how-to, referência e explicação.

O objetivo é adaptar princípios úteis ao fluxo Kamikaze, não migrar cegamente para um framework nem criar dependência de ferramenta específica.

### Limite de enforcement
AGENTS.md orienta somente ferramentas que reconhecem o padrão ou que receberam instrução para lê-lo. BOOTSTRAP é obrigatório no fluxo de retomada, mas não pode forçar uma interface externa a ler arquivos por conta própria. GitHub Actions executa código real no runner após push/PR; não executa prompts nem chama uma IA automaticamente. A CI pode detectar falhas e produzir um check vermelho. **Sem branch protection/ruleset exigindo esse check, um push direto para main ainda pode ser aceito mesmo com a CI falhando.** A configuração de branch protection não foi alterada nesta rodada; requer ação administrativa no GitHub.
