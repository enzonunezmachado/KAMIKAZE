# Prompt Vivo — sistema de instruções, pesquisa e continuidade

O Prompt Vivo é a infraestrutura metodológica do Kamikaze. Organiza instruções, métodos, evidências, conhecimento reutilizável, execução por fases e continuidade entre sessões. Não é apenas uma coleção de prompts.

## Entrada obrigatória

1. [AGENTS.md](AGENTS.md) — instruções para agentes que reconhecem o padrão.
2. [operations/state.toml](../operations/state.toml) — estado estruturado e próxima ação prioritária.
3. [ARCHITECTURE_GOVERNANCE.md](ARCHITECTURE_GOVERNANCE.md) — autoridade, função dos arquivos, navegação, tamanho e gravação.
4. [BOOTSTRAP.md](BOOTSTRAP.md) — procedimento obrigatório de retomada.
5. [CONTINUITY_SYSTEM.md](CONTINUITY_SYSTEM.md) — fontes canônicas e checkpoint.
6. [MASTER_PROMPT.md](MASTER_PROMPT.md) — inicialização da pesquisa.
7. [EXECUTION_PROTOCOL.md](EXECUTION_PROTOCOL.md) — condução e checkpoints.

## Arquivos centrais

| Arquivo | Responsabilidade |
| --- | --- |
| `CORE.md` | Identidade, princípios e limites permanentes |
| `OPERATING_PRINCIPLES.md` | Regras práticas para decidir, pesquisar, executar, priorizar e parar sem ciclos improdutivos |
| `MASTER_PROMPT.md` | Entrada para nova execução |
| `EXECUTION_PROTOCOL.md` | Processo de trabalho e checkpoints |
| `RESEARCH_METHOD.md` | Pesquisa, triangulação e contraprovas |
| `EVIDENCE_STANDARD.md` | Proveniência, qualidade e classificação de evidências |
| `QUALITY_GATE.md` | Critérios de auditoria antes de concluir fases |
| `SELF_IMPROVEMENT.md` | Evolução controlada do método |
| `MEMORY_AND_HANDOFF.md` | Transferência ampliada de contexto |
| `NEXT_CHAT_PROMPT.md` | Texto pronto para iniciar novo chat |
| `SESSION_LOG.md` | Histórico global append-only |
| `CHANGELOG.md` | Mudanças na metodologia e estrutura do Prompt Vivo |

## Estrutura de pastas

- [`runs/`](runs/README.md): execuções independentes por RUN_ID. Ler o README de cada execução antes de abrir arquivos internos.
- [`knowledge/`](knowledge/README.md): conhecimento especializado reutilizável, com fontes e validade.
- [`PHASES/`](PHASES/): modelos de fase reutilizáveis.
- [`templates/`](templates/): modelos vazios; não armazenar registros reais.
- [`operations/`](../operations/README.md): estado e operação comercial; não confundir com a memória de pesquisa.

## Como a memória funciona

- Estado atual não é histórico.
- `operations/state.toml` define a frente prioritária e a próxima ação; cada frente mantém seus próprios detalhes na fonte operacional correspondente.
- state.toml registra estado estruturado; RUN_STATE e PHASE_CONTROL descrevem execução e gate.
- RESUME_PACKET é resumo curto derivado; MEMORY_HANDOFF guarda contexto ampliado.
- SESSION_LOG é append-only; correções entram como eventos novos.
- SOURCE_LEDGER guarda proveniência; FINDINGS guarda síntese; fonte original permanece necessária.
- Conhecimento de uma execução só migra para knowledge após revisão de reutilização e validade.

## Leitura progressiva e regras

Antes de entrar em uma pasta, leia seu README. Abra documentos detalhados sob demanda; não carregue tudo automaticamente. Cada arquivo deve ter uma função, leitor, gatilho de atualização e regra de gravação claros. Não criar documentos redundantes nem duplicar estado.

As regras normativas estão em [ARCHITECTURE_GOVERNANCE.md](ARCHITECTURE_GOVERNANCE.md). Instruções para agentes compatíveis estão em [AGENTS.md](AGENTS.md).

## Validação

O repositório usa [scripts/validate_docs.py](../scripts/validate_docs.py) para verificar estrutura, tamanhos, links selecionados e sincronização de estado. GitHub Actions executa a validação, o build MkDocs e o lint Markdown em push/PR. A CI não avalia verdade semântica, qualidade de hipótese ou autorização humana.

## Limites

O GitHub preserva documentos versionados; não executa trabalho em segundo plano nem garante que toda IA leia automaticamente o repositório. AGENTS.md depende do suporte da ferramenta; em outras interfaces, executar BOOTSTRAP explicitamente.
