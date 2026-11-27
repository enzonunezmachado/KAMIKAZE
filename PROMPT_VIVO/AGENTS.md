# AGENTS — Prompt Vivo

**Leitura obrigatória:** `README.md`, `ARCHITECTURE_GOVERNANCE.md` e `BOOTSTRAP.md` antes de operar o Prompt Vivo. O estado e a próxima ação vêm de `operations/state.toml` e das fontes canônicas da frente ativa; `CURRENT_WORK.md` está obsoleto.

## Protocolo

- `CURRENT_WORK.md` aponta a última entrega substantiva, não necessariamente a fase de pesquisa ativa.
- `operations/STATE.md` identifica o RUN_ID e restrições do projeto.
- `runs/<RUN_ID>/RUN_STATE.md` é a fonte canônica do estado da execução e da fase atual.
- `runs/<RUN_ID>/PHASE_CONTROL.md` é a fonte canônica da decisão de gate e da próxima ação permitida.
- `RESUME_PACKET.md` é resumo derivado para retomada; nunca pode contradizer RUN_STATE/PHASE_CONTROL e não substitui os originais.
- `MEMORY_HANDOFF.md` contém contexto ampliado; não é estado operacional.
- `SESSION_LOG.md` é append-only; correções são novos eventos.
- `SOURCE_LEDGER.md` registra fontes; `FINDINGS.md` registra síntese; nenhuma síntese substitui a fonte original.

## Antes de criar ou editar

1. Leia o README da pasta de destino.
2. Confirme que o arquivo tem função única e não duplica uma fonte canônica.
3. Mantenha arquivos de entrada concisos; mova detalhes para documentos especializados e referencie-os.
4. Atualize índices e links de navegação quando a estrutura mudar.
5. Atualize o estado estruturado apenas quando prioridade, estado ou próxima ação mudar; não mantenha ponteiro manual de última entrega.
6. Execute o validador documental e corrija falhas relevantes.

## Execução prática

- Toda tarefa deve estar ligada a uma decisão, risco ou resultado concreto.
- Defina pergunta de decisão, evidência suficiente, timebox e ação seguinte antes de pesquisar.
- Quando a informação já basta para um teste barato, reversível e autorizado, pare de pesquisar e teste.
- Não manter iniciativas artificialmente IN_PROGRESS: escolher CONTINUE, TEST, HOLD, KILL ou ESCALATE, com critério de sucesso e condição de parada.
- Não criar módulos, agentes, documentos ou workflows quando uma ação menor produzir o mesmo valor.
- Distinguir atividade, ativo produzido, sinal de mercado, intenção comercial, contratação, faturamento, caixa e retenção.
- Dizer ao usuário quando estamos dando voltas, quando é hora de agir e quando uma hipótese deve ser estacionada ou abandonada.

## Controle humano

O usuário define prioridades e aprova decisões subjetivas. Não descarte insights humanos por não aparecerem na pesquisa inicial. A IA pode pesquisar, estruturar, comparar, criticar e executar tarefas delimitadas; deve expor incertezas e pedir aprovação para decisões irreversíveis ou externas.
