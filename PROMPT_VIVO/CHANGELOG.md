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


## 2026-11-25 — Primeiro teste real: TOTALMENTE GRATUITA

- Criada execução PV-2026-11-25-TOTALMENTE-GRATUITA.
- Registrados plano, fontes, achados, questões abertas, handoff e síntese em elaboração.
- Criada política de cotas com reserva explícita e fallback permitido; percentual de 90% definido como meta de confiabilidade a medir, não promessa.
- O primeiro lote identificou hipóteses em serviços operacionais de dados/documentos/conteúdo, riscos de automação genérica, custos de dropshipping e taxas de marketplaces.
- Próxima iteração: aprofundar procura brasileira e verificar caminhos de aquisição/pagamento.

## 2026-11-25 — Governança adaptativa de fases

### Motivo
O usuário esclareceu que o Prompt Vivo precisa administrar dinamicamente a quantidade e a estrutura das fases: concluir uma fase sem inventar novas quando desnecessárias, mas também criar, modificar, dividir, mesclar, reordenar, pular ou reabrir fases quando a pesquisa exigir.

### Diagnóstico
O protocolo anterior permitia aprofundar, encerrar linhas e pesquisar em paralelo, mas não definia explicitamente o ciclo de vida completo das fases nem a obrigação de sincronizar o plano e o estado quando a arquitetura mudasse.

### Alterações
- Adicionada seção obrigatória de arquitetura adaptativa ao EXECUTION_PROTOCOL.md.
- Atualizado README para deixar claro que PHASE_00–PHASE_05 são modelos, não limite fixo.
- Toda run deverá manter PHASE_ARCHITECTURE.md para registrar decisões e versões da sequência.

### Governança
Ajustes locais na execução são permitidos dentro do escopo aprovado; mudanças no protocolo/CORE seguem aprovação humana. Esta alteração central foi autorizada pelo pedido explícito do usuário.

### Teste
Aplicar imediatamente na execução PV-2026-11-25-TOTALMENTE-GRATUITA ao iniciar PHASE_02_DEMAND.


## 2026-11-26 — Sistema de continuidade e histórico entre chats

### Motivo
O usuário pediu um mecanismo permanente para documentar atualizações do Kamikaze e recuperar contexto quando o limite de uma conversa acabar, permitindo abrir outro chat e continuar a pesquisa sem recontar o histórico.

### Diagnóstico
Já existiam BOOTSTRAP, RESUME_PACKET, RUN_STATE e MEMORY_HANDOFF, inspirados no mecanismo do NEXUS. Porém, faltava um log cronológico padronizado de sessões, um prompt de retomada pronto para copiar e um protocolo explícito de sincronização e confirmação de escrita. Também foram encontrados trechos com referências malformadas no BOOTSTRAP.

### Alterações
- Criado `CONTINUITY_SYSTEM.md` com camadas de estado, memória, histórico e retomada; protocolo de checkpoint; reconciliação de divergências; checklist de integridade.
- Criado `NEXT_CHAT_PROMPT.md` para copiar e colar em novo chat.
- Criados logs append-only global e por execução: `SESSION_LOG.md`.
- Reescrito `BOOTSTRAP.md` para corrigir referências, carregar o sistema, auditar estado e continuar.
- Atualizados MASTER_PROMPT, EXECUTION_PROTOCOL, MEMORY_AND_HANDOFF e README.
- Sincronizados operations/STATE e arquivos da execução ativa; registrada a entrada do usuário.

### Limites
O mecanismo não trabalha em segundo plano nem salva após a conversa terminar. Checkpoints devem ser feitos enquanto a sessão está ativa e dependem de acesso confirmado ao GitHub. O novo chat precisa ter acesso ao repositório.

### Verificação
Confirmar a existência dos arquivos e a leitura das atualizações no GitHub. A retomada futura deve testar o texto de NEXT_CHAT_PROMPT e verificar que não repete pesquisas concluídas.


## 2026-11-26 — acionador persistente de tráfego pago
- Criado `knowledge/PAID_TRAFFIC_MODULE_ACTIVATION.md` com protocolo de ativação por intenção explícita + confirmação, arquitetura modular, etapas/gates, skills, repositórios, compliance, segurança financeira e handoff esperado.
- Ampliado catálogo open source com 49 skills de marketing-skills e repositórios oficiais/auxiliares Google Ads, Meta Ads, MCP, n8n, reporting e Meridian.
- Atualizados `knowledge/README.md`, `BOOTSTRAP.md`, `NEXT_CHAT_PROMPT.md` e `CONTINUITY_SYSTEM.md` para descoberta de acionadores dormentes em novos chats.
- Nenhuma integração, instalação, campanha ou gasto autorizado/executado.


## 2026-11-26 — pesquisa de construção com IA e ferramentas gratuitas
- Criado `knowledge/MAK_ZERO_COST_AI_BUILD_CASES.md` com casos, arquitetura, custos declarados e restrições dos planos gratuitos.
- Criado suplemento de fontes S436–S450: `runs/PV-2026-11-25-TOTALMENTE-GRATUITA/SOURCE_LEDGER_SUPPLEMENT_S436_S450.md`.
- Atualizados PHASE_03.5, FINDINGS, RUN_STATE, RESUME_PACKET, USER_INPUT_LOG, logs e operations/STATE.
- Nenhuma ferramenta foi instalada ou executada; nenhum app, conta, deploy ou gasto foi realizado.
