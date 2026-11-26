# Histórico de evolução — Prompt Vivo

## 2026-11-25 — Criação da arquitetura inicial

### Motivo
O usuário definiu a necessidade de um sistema de prompts e arquivos Markdown interligados, capaz de conduzir pesquisas em várias etapas, registrar resultados, criar novas instruções especializadas, melhorar seus próprios métodos e permitir continuidade entre chats sem reconstruir o processo manualmente.

### Estrutura criada
- README e arquitetura da pasta.
- CORE com princípios e hierarquia.
- MASTER_PROMPT para inicialização e retomada.
- Protocolo de execução e checkpoints.
- Método de pesquisa profunda.
- Padrão de evidências.
- Quality Gate.
- Protocolo de autoaperfeiçoamento.
- Memória e transferência entre chats.
- Template de execução.
- Seis fases reutilizáveis: escopo, cenário, demanda, validação, viabilidade e síntese.

### Decisões de arquitetura
- Cada pesquisa concreta terá uma pasta própria em `runs/`.
- O conhecimento reutilizável ficará separado dos dados específicos de cada execução.
- A IA poderá melhorar instruções e criar módulos, com níveis de mudança e aprovação para alterações centrais.
- A documentação será a memória persistente; o chat é uma sessão temporária.
- A estrutura deve ser adaptável a diferentes temas, sem pré-selecionar um modelo de negócio.

### Limitações reconhecidas
O Prompt Vivo não cria memória automática fora dos arquivos, não garante que todo chat tenha acesso ao GitHub e não executa trabalho entre sessões sem uma ferramenta que permita isso. A retomada depende de a IA conseguir ler os arquivos e salvar as alterações.

## Regra para novas entradas
Adicionar novas mudanças no topo, com data, motivo, arquivos afetados, impacto e forma de verificar se a melhoria funcionou.
