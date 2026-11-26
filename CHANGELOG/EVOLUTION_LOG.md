# Histórico de evolução — Negócio Digital Kamikaze

Este documento registra mudanças de direção, correções e decisões para preservar a continuidade do projeto. Ele não é uma lista de tarefas nem substitui o estado operacional.

## 2026-11-25 — Recalibração da identidade e do escopo

### Motivo

Ao revisar a estratégia, o usuário esclareceu que o Kamikaze não deve escolher um negócio com base em sua atividade pessoal ou em familiaridade circunstancial. A hipótese de assistência técnica de celulares foi uma inferência indevida e não representa a proposta definida.

A intenção original é construir uma operação digital ampla, modular e de baixo custo para pesquisar como pessoas e empresas usam IA e outros recursos digitais, encontrar oportunidades comerciais em diferentes mercados, validar procura e pagamento, produzir soluções e vender.

### Mudanças realizadas

- Atualizado o nome de trabalho de Projeto Sem Nome para **Negócio Digital Kamikaze** nos documentos centrais e referências operacionais.
- Atualizado o README para apresentar o Kamikaze como uma operação de descoberta, validação, produção, distribuição e comercialização — não como um negócio de nicho já escolhido.
- Reescrito o brief para incluir pesquisa de usos comerciais atuais de IA, e-commerce/dropshipping, produtos digitais, serviços, freelancing, automações/agentes, conteúdo curto e outros modelos.
- Atualizada a missão imediata para buscar **R$ 150 efetivamente recebidos até 06/12/2026**, com investimento inicial de R$ 0.
- Removida do banco de oportunidades a hipótese **“Orçamento que não esfria”**, direcionada a assistências técnicas de celulares.
- Excluído o experimento comercial que dependia dessa hipótese.
- Excluída a lista de assistências técnicas locais criada para entrevistas.
- Atualizado o estado operacional para registrar que nenhuma oportunidade foi escolhida e que a próxima fase é pesquisa ampla e comparativa.
- Atualizadas as orientações de skills e quickstart para refletir o escopo amplo e o nome atual.
- Preservadas pesquisas exploratórias anteriores como material de referência; elas não constituem decisões nem oportunidades aprovadas.

### O que esta mudança significa

O Kamikaze não é, por definição, dropshipping, assistência técnica, SaaS, agência, canal de conteúdo ou qualquer outro modelo isolado. Essas possibilidades só podem avançar depois de pesquisa e validação.

O histórico pessoal do responsável não deve determinar o mercado escolhido. A seleção deve ser guiada por evidências, comprador alcançável, viabilidade de entrega, custos, riscos e possibilidade real de receber.

### Estado após a mudança

- Oportunidade escolhida: nenhuma.
- Experimento comercial ativo: nenhum.
- Receita recebida: R$ 0.
- Despesas: R$ 0.
- Meta imediata: R$ 150 até 06/12/2026.
- Próximo movimento: retomar pesquisa ampla, incluindo usos comerciais de IA e diferentes modelos de monetização, comparar evidências e então definir um teste comercial prioritário.

## Como manter este histórico

Adicionar uma nova seção no topo sempre que houver uma mudança relevante de identidade, escopo, meta, critérios, estratégia ou decisão. Registrar o motivo, os arquivos alterados, o que foi removido/preservado e o novo estado. Não apagar decisões antigas deste histórico; corrigir o rumo com uma nova entrada.


## 2026-11-25 — Criação do sistema Prompt Vivo

### Motivo
O usuário propôs uma estrutura viva de arquivos Markdown que instrui a IA a conduzir pesquisas profundas em etapas, registrar resultados, atualizar os próprios prompts, criar especializações e retomar trabalhos em novos chats.

### Alterações
- Criada a pasta `PROMPT_VIVO/` com README, CORE, Master Prompt, protocolo de execução, método de pesquisa, padrão de evidências, Quality Gate, autoaperfeiçoamento, memória/transferência e template.
- Criadas seis fases de pesquisa reutilizáveis, de definição de escopo à síntese e decisão.
- Criadas pastas-base para execuções, conhecimento especializado e templates.
- Integrado o sistema à documentação principal do Kamikaze e ao estado operacional.

### Princípios definidos
- Cada execução tem memória própria e checkpoints persistentes.
- A IA pode melhorar métodos e criar módulos especializados, mas mudanças na arquitetura central e no escopo exigem aprovação.
- A pesquisa deve ser rastreável, ampla, crítica e baseada em evidências.
- A documentação permite continuidade entre chats, desde que o próximo chat consiga acessar os arquivos.

### Estado
Arquitetura inicial criada. Ainda falta executar um ciclo real de pesquisa com o Prompt Vivo para avaliar a eficácia e ajustar o sistema com base no uso.


## 2026-11-25 — Primeira execução Prompt Vivo: TOTALMENTE GRATUITA

### Motivo
Iniciar o primeiro teste real do Prompt Vivo com pesquisa ampla de oportunidades digitais e monetização com IA, sob exigência explícita de custo zero e controle de cotas.

### Alterações
- Criada a execução PV-2026-11-25-TOTALMENTE-GRATUITA em PROMPT_VIVO/runs/.
- Criados estado, plano, ledger de fontes, achados, perguntas abertas, handoff e síntese inicial.
- Criada política específica de orçamento de recursos: 60% de uso planejado, 30% de reserva de recuperação e 10% de incerteza, com checkpoints e fallback sem burlar limites.
- Atualizado o índice de execuções e o estado operacional.

### Estado
Primeiro lote exploratório concluído; PHASE_01_LANDSCAPE continua em andamento. Nenhuma oportunidade aprovada.
