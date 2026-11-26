# PROMPT VIVO — Sistema de instruções e conhecimento evolutivo

**Versão:** 1.0  
**Criado em:** 25/11/2026  
**Projeto proprietário:** Negócio Digital Kamikaze

## 1. O que é

O **Prompt Vivo** é um sistema modular de instruções, protocolos, métodos, memória de execução, evidências e conhecimento especializado. Ele permite que uma IA conduza trabalhos complexos em etapas, consulte instruções específicas, registre descobertas, identifique lacunas, atualize os próprios materiais operacionais e retome o trabalho em outro chat.

Não é apenas uma biblioteca de prompts. É uma estrutura de trabalho evolutiva.

O sistema deve melhorar por meio de:
- pesquisa real e consulta a fontes;
- comparação de métodos e ferramentas;
- registro de evidências e incertezas;
- avaliação crítica dos próprios resultados;
- identificação de novas perguntas e linhas de investigação;
- atualização controlada de instruções, modelos e conhecimento;
- continuidade entre chats e sessões.

## 2. O que o Prompt Vivo deve entregar

Ao final de uma execução, deve existir um conjunto rastreável de:
1. objetivo e escopo definidos;
2. plano de pesquisa;
3. fontes consultadas e evidências registradas;
4. análises e comparações;
5. hipóteses confirmadas, enfraquecidas ou rejeitadas;
6. lacunas e perguntas ainda abertas;
7. conclusões proporcionais às evidências;
8. oportunidades ou caminhos recomendados, quando houver base;
9. próximos passos executáveis;
10. melhorias propostas para o próprio Prompt Vivo.

## 3. Arquitetura da pasta

| Arquivo/pasta | Função |
|---|---|
| `CORE.md` | Identidade, princípios permanentes, limites e comportamento esperado |
| `MASTER_PROMPT.md` | Prompt inicial para iniciar ou retomar uma execução |
| `EXECUTION_PROTOCOL.md` | Regras de condução, etapas, checkpoints e continuidade |
| `RESEARCH_METHOD.md` | Método de pesquisa profunda, busca, triangulação e análise |
| `EVIDENCE_STANDARD.md` | Padrão para fontes, evidências, alegações e confiança |
| `QUALITY_GATE.md` | Auditoria de qualidade antes de concluir uma fase |
| `SELF_IMPROVEMENT.md` | Como a IA pode revisar e evoluir este próprio sistema |
| `MEMORY_AND_HANDOFF.md` | Memória, retomada em outro chat e transferência de contexto |
| `RUN_TEMPLATE.md` | Modelo para registrar uma execução |
| `PHASES/PHASE_00_SCOPE.md` | Definição do problema e do escopo |
| `PHASES/PHASE_01_LANDSCAPE.md` | Mapeamento amplo do mercado/tema |
| `PHASES/PHASE_02_DEMAND.md` | Mineração de problemas, necessidades e sinais de demanda |
| `PHASES/PHASE_03_VALIDATION.md` | Validação, concorrência, alternativas e contraprovas |
| `PHASES/PHASE_04_FEASIBILITY.md` | Viabilidade, modelos, custos, riscos e capacidade |
| `PHASES/PHASE_05_SYNTHESIS.md` | Síntese, decisão, plano de ação e próximos ciclos |
| `runs/` | Execuções concretas, cada uma com sua própria memória e resultados |
| `knowledge/` | Conhecimento especializado reutilizável e validado por tema |
| `templates/` | Modelos auxiliares para registros e análises |

## 4. Como funciona

1. O usuário apresenta um objetivo ou pede uma pesquisa.
2. A IA lê este README, CORE, MASTER_PROMPT e protocolo.
3. A IA cria ou identifica uma execução em `runs/`.
4. A execução percorre uma arquitetura de fases adaptativa: pode avançar, aprofundar, dividir, mesclar, reordenar, modificar, adicionar, pular ou reabrir fases conforme evidências e gates. PHASE_00–PHASE_05 são modelos iniciais, não limite fixo. Toda alteração é registrada em PHASE_ARCHITECTURE.md na execução, e os arquivos de estado/plano/handoff são sincronizados.
5. Cada fase consulta fontes e registra resultados nos arquivos da execução.
6. A IA atualiza o estado da execução e indica a próxima ação.
7. Ao descobrir método, ferramenta, conceito ou pergunta relevante, avalia se deve atualizar o conhecimento reutilizável.
8. Ao identificar melhoria no sistema, registra proposta e impacto; aplica mudanças seguras e compatíveis, preservando histórico.
9. A síntese final separa fatos, evidências, inferências, hipóteses e recomendações.

## 5. Como iniciar

No novo chat, forneça o link do repositório e use o conteúdo de `MASTER_PROMPT.md`. Se o objetivo já estiver definido, inclua-o no pedido. A IA deve ler os documentos centrais e a execução ativa antes de perguntar novamente o que já está documentado.

## 6. Regras invioláveis

- O Prompt Vivo apoia o Kamikaze; não escolhe um negócio por preferência ou conveniência pessoal.
- Não inventar fontes, dados, citações, preços, resultados ou capacidades de ferramentas.
- Não transformar relato isolado em verdade de mercado.
- Não confundir atividade de pesquisa com validação comercial.
- Não declarar venda, receita ou interesse de compra sem evidência.
- Não executar ações externas, publicar, abordar pessoas, contratar, pagar, fazer deploy ou alterar contas sem autorização humana explícita.
- Não apagar evidências negativas nem histórico de decisões.
- Não alterar princípios centrais silenciosamente.
- Não criar arquivos redundantes sem função clara.
- Não preencher lacunas com suposições ocultas.
- O limite real de contexto, ferramentas, acesso e tempo deve ser respeitado.

## 7. Relação com o Kamikaze

O Prompt Vivo é uma infraestrutura metodológica do Kamikaze, não um negócio independente. Seu trabalho é aumentar a qualidade e a continuidade de pesquisa e execução. A meta comercial e as restrições vigentes permanecem nos documentos centrais do Kamikaze, especialmente `docs/BRIEF.md` e `operations/STATE.md`.

## 8. Regra de evolução

O sistema deve evoluir quando houver evidência de que uma instrução, método, ferramenta ou estrutura pode melhorar resultados. Toda mudança relevante deve ser registrada em `CHANGELOG.md`, com motivo, arquivos afetados, benefício esperado e possíveis efeitos colaterais.
