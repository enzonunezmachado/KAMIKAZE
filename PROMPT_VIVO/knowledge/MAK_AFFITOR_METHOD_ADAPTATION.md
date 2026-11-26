# Estudo de referência — Affitor affiliate-skills e adaptação ao Motor de Aquisição Kamikaze

**Data da auditoria:** 26/11/2026  
**Repositório estudado:** https://github.com/Affitor/affiliate-skills  
**Versão declarada:** 1.2.1  
**Licença declarada:** MIT  
**Decisão:** aproveitar arquitetura e métodos; não importar nem instalar o projeto.

## 1. Objetivo e escopo

Este documento registra uma leitura de arquitetura, instruções e implementação do Affitor/affiliate-skills. O propósito não é copiar o produto nem presumir que suas promessas comerciais funcionam. É identificar princípios que aumentem a qualidade do Kamikaze: pesquisa melhor, conteúdo realmente útil, distribuição disciplinada, relações duradouras, medição e melhoria contínua.

Foram examinados:
- README, QUICKSTART, SKILL.md, CLAUDE.md, bootstrap e documentação de fonte da verdade;
- mapa de funil, mapa do flywheel e estratégia de distribuição;
- protocolo de feedback, disclosure de afiliados, regras de plataforma, frameworks de oferta e provedores de dados sociais;
- registry e evals;
- package.json e implementação do cliente de API, CLI, servidor e cache;
- habilidades individuais de pesquisa/verificação, tendências, ângulos, briefs, conteúdo social, repurposing, landing pages, email, analytics, compliance, funnel planning e self-improvement.

A árvore consultada continha 53 arquivos SKILL.md e 53 entradas no registry. A versão declarada em VERSION era 1.2.1.

## 2. O que o Affitor realmente oferece

O Affitor organiza habilidades de IA em oito estágios:
1. Research — pesquisar programas, produtos, nichos, concorrentes e conteúdo.
2. Content — criar conteúdo social adaptado ao canal.
3. Blog/SEO — conteúdo de busca e autoridade temática.
4. Landing — páginas e ofertas.
5. Distribution — hubs, email e distribuição.
6. Analytics — rastrear cliques, conversões e desempenho.
7. Automation — reaproveitar e automatizar tarefas repetitivas.
8. Meta — planejar funil, verificar compliance e aprender com resultados.

A ideia central é modular: cada habilidade recebe entradas explícitas, executa uma tarefa delimitada e entrega uma saída estruturada para a próxima. O flywheel conecta analytics de volta à pesquisa. Portanto, o sistema não deveria apenas produzir posts: deveria aprender com a resposta do mercado.

## 3. Padrões que agregam valor ao Kamikaze

### 3.1 Pesquisar antes de produzir
Antes de escrever, estudar:
- problema e linguagem usados pelo público;
- perguntas reais e objeções;
- conteúdos que já existem e formatos usados;
- lacunas de informação e segmentos pouco atendidos;
- canais onde o público está ativo;
- sinais de intenção, não apenas alcance.

Cada evidência deve conter fonte, data, contexto e tipo: dado observado, relato, hipótese ou estimativa. Não inventar métricas ausentes.

### 3.2 Verificar ofertas na fonte primária
Diretórios afiliados são índices para descobrir candidatos, não autoridades finais. Antes de recomendar ou divulgar um produto, confirmar:
- existência e qualidade do produto;
- público adequado e problema resolvido;
- preço e condições atuais;
- comissão, tipo e duração;
- atribuição/cookie, regras de tráfego e restrições;
- elegibilidade, aprovação, mínimo e prazo de saque;
- reembolso, chargeback, suporte e reputação;
- alternativas e limitações.

Cada condição deve ter fonte primária ou ser marcada como não confirmada. Comissão alta não compensa produto ruim ou inadequado.

### 3.3 Criar brief antes de criar conteúdo
O brief mínimo deve conter:
- público e situação concreta;
- problema/trigger;
- resultado desejado;
- dúvidas e objeções reais;
- alternativas que o público já usa;
- fontes e provas disponíveis;
- ângulo editorial;
- canal/formato;
- CTA adequado ao nível de consciência;
- disclosure comercial, se houver afiliação;
- afirmações que não podem ser feitas por falta de prova.

### 3.4 Escolher ângulos por adequação, não por adivinhação
Gerar alternativas específicas (tutorial, demonstração, comparação, história, explicação, checklist, resposta a pergunta, análise honesta de limites). Comparar relevância, evidência, diferenciação, adequação à plataforma, capacidade de produzir e custo de tempo. Sem dados suficientes, usar ranking qualitativo e declarar incerteza; não inventar score preciso.

### 3.5 Conteúdo nativo e conteúdo-mãe
Uma pesquisa profunda pode gerar uma peça principal e derivados. Porém, cada versão precisa respeitar o canal:
- vídeo curto: demonstração/gancho rápido e informação visual;
- Instagram: reels, stories, carrossel e perfil coerentes;
- YouTube: tutorial, teste, comparação e busca;
- Reddit/comunidades: resposta útil, conversa e regras locais;
- LinkedIn: experiência, processo e aprendizagem profissional;
- Pinterest/blog: conteúdo pesquisável e durável.

Não publicar o mesmo texto em todos os lugares. Não transformar volume de posts em objetivo independente. Uma peça útil e bem distribuída vale mais que dezenas de variações vazias.

### 3.6 Distribuição é um trabalho próprio
Criar conteúdo não é o mesmo que colocá-lo diante do público certo. Para cada peça, registrar:
- canal e comunidade;
- formato e tópico;
- segmento;
- CTA;
- URL/código de origem;
- data e tempo gasto;
- regras verificadas;
- estado: rascunho, revisado, autorizado, publicado, medido.

A distribuição inclui busca, feed, comunidades, conversas relevantes, parcerias e indicações. Cada canal tem seu próprio contexto e suas próprias regras.

### 3.7 Medição por etapas
Separar:
- exposição: alcance/views;
- atenção: retenção/watch time;
- interesse: visitas ao perfil, follows, saves, comentários e perguntas;
- intenção: cliques, consultas, pedidos de detalhes;
- conversão: compra aprovada;
- economia: comissão líquida, reembolso, chargeback e payout;
- relacionamento: retorno, compartilhamento, introdução, recompra e lembrança.

Views e seguidores são indicadores antecedentes legítimos quando contextualizados por tempo, origem e qualidade. Não são vendas. Comparar taxas apenas com denominador, janela temporal e amostra. Não comparar números brutos de plataformas diferentes como se fossem equivalentes.

### 3.8 Retrospectiva e feedback
Depois de cada ciclo, perguntar:
- O que esperávamos?
- O que ocorreu?
- Em qual etapa houve avanço ou perda?
- Qual evidência sustenta o diagnóstico?
- O problema foi público, oferta, conteúdo, canal, confiança, CTA, checkout ou payout?
- Qual única mudança é mais informativa testar agora?

Registrar também resultados negativos, falhas de fonte, ausência de dados, erros de cálculo e premissas que não se confirmaram. Não transformar uma campanha pequena em regra universal.

## 4. A extensão própria do MAK: relacionamento e memória de marca

O funil tradicional tende a terminar em conversão e retenção. O MAK acrescenta um caminho relacional de longo prazo:

**Descoberta → interação útil → valor percebido → boa experiência → conexão consentida → presença relevante → lembrança futura → retorno, indicação ou compra.**

Uma pessoa pode não comprar, não indicar e não seguir no primeiro contato, e ainda assim sair com uma impressão positiva. Isso é um resultado relacional possível, não uma venda atribuída.

### Cinco resultados possíveis de uma conexão
1. Compra imediata.
2. Introdução/indicação voluntária imediata.
3. Lembrança futura e recomendação espontânea.
4. Necessidade própria futura que faz a pessoa voltar.
5. Acompanhamento e distribuição de conteúdo, fortalecendo a relação.

### Protocolo de relacionamento
1. Escolher pessoas porque conhecem/atendem o público, não apenas porque possuem muitos contatos.
2. Pedir permissão antes de apresentar a solução.
3. Explicar com honestidade quem somos, o que estamos construindo, para quem serve e o que não resolve.
4. Entregar uma contribuição útil mesmo se não houver compra.
5. Ouvir feedback e registrar objeções sem tentar vencer toda objeção.
6. Se fizer sentido, convidar a acompanhar um canal social; nunca condicionar ajuda a follow.
7. Se não houver fit, perguntar sem pressão se a pessoa conhece alguém que poderia se beneficiar.
8. Preferir introdução voluntária ou mensagem encaminhável; não pedir/armazenar dados de terceiros sem consentimento.
9. Informar claramente quando um link gera comissão.
10. Agradecer independentemente do resultado; não usar culpa, falsa urgência ou follow-up insistente.

### Memória de marca não é spam
A presença contínua deve justificar a atenção: conteúdo útil, progresso verdadeiro, respostas, demonstrações e atualizações. A pessoa deve poder silenciar, deixar de seguir ou encerrar contato sem pressão. Não usar grupos como listas de prospecção.

### Registro mínimo e respeitoso
Para uma conexão, registrar apenas o necessário:
- identificador/nome público ou apelido;
- canal e contexto do encontro;
- valor/conteúdo entregue;
- permissão para contato/seguimento;
- preferência de canal;
- próximo passo solicitado pela própria pessoa;
- introdução consentida, se houver;
- origem de eventual oportunidade.

Não registrar dados sensíveis nem contatos de terceiros sem base/consentimento. Definir retenção e exclusão conforme finalidade e obrigações aplicáveis.

## 5. Arquitetura proposta do Motor de Aquisição Kamikaze

O MAK deve ser composto por módulos leves e reutilizáveis, não por um agente autônomo que publica e envia mensagens sozinho.

| Módulo MAK | Função | Saída operacional |
|---|---|---|
| 01. Audience & Problem Research | Encontrar público, problemas, gatilhos, linguagem e objeções | Mapa de público e evidências |
| 02. Offer Intelligence | Descobrir e verificar produtos/serviços/afiliações | Ficha de oferta e confiança |
| 03. Channel Intelligence | Mapear canais, comunidades, formatos e regras | Mapa de distribuição |
| 04. Content Intelligence | Observar padrões, concorrentes, perguntas e lacunas | Brief e ângulos priorizados |
| 05. Content Studio | Produzir peça-mãe e adaptações nativas | Rascunhos revisáveis |
| 06. Relationship Network | Construir relações, memória de marca e introduções consentidas | Registro de conexões e próximos passos |
| 07. Distribution Desk | Organizar calendário e publicação autorizada | Fila de conteúdo aprovado |
| 08. Measurement | Acompanhar exposição, atenção, interesse, intenção, venda e relacionamento | Painel/registro por canal |
| 09. Learning Loop | Diagnosticar e escolher a próxima experiência | Retrospectiva e hipótese seguinte |
| 10. Compliance & Quality Gate | Verificar alegações, disclosure, direitos, privacidade e regras | PASS / WARN / FAIL |

### Flywheel MAK
Pesquisa de público/oferta → ângulo → conteúdo → distribuição → atenção/interesse/intenção → compra e/ou relacionamento → métricas e feedback → pesquisa atualizada.

Duas saídas são igualmente válidas:
- **Commercial loop:** interesse → intenção → compra → payout/retenção.
- **Relationship loop:** valor → confiança → conexão → lembrança → retorno/introdução/compra futura.

A relação pode amadurecer sem ser forçada para o loop comercial.

## 6. Operação com IA: automatizar preparação, não autonomia social

Padrão operacional recomendado:
1. IA pesquisa e organiza fontes.
2. IA prepara brief e rascunhos.
3. Humano verifica fatos, tom, adequação, disclosure e direitos.
4. Humano autoriza a publicação/contato.
5. Conteúdo é publicado manualmente ou por ferramenta oficialmente permitida, após autorização.
6. Resultados são registrados.
7. IA analisa e sugere a próxima melhoria.

Não permitir:
- auto-DM, spam, scraping ou coleta de contatos em massa;
- postagem sem revisão/autorização;
- comentários fingindo ser clientes;
- depoimentos ou experiências inventadas;
- automação por navegador que viole termos;
- uso de APIs pagas ou quotas desconhecidas sem aprovação;
- alterações no NEXUS ou dependência de quota do AI Studio sem confirmação.

## 7. Auditoria crítica do Affitor: limites e alertas

- Contagens em README/CLAUDE/bootstrap divergem (50, 52 e 53); a árvore e registry consultados tinham 53 habilidades.
- O registry declara geração em 19/10/2026, enquanto VERSION marca 1.2.1; conferir a fonte real e não assumir sincronização perfeita.
- `affiliate-program-search` é uma ponte de compatibilidade; o fluxo canônico é `find-and-verify-affiliate-program`. Não reutilizar o antigo score como verdade ou score oficial.
- O scout social usa fallback de busca web e, quando faltam métricas, algumas fórmulas/proxies são frágeis. Não inferir shares, impressões ou engagement comparável.
- Regras de plataforma são heurísticas, não política oficial permanente. Verificar as regras atuais de cada plataforma e comunidade antes de publicar.
- A referência FTC é dos EUA. Para o Brasil, complementar com CDC, CONAR, LGPD e regras locais; a referência do repo não é aconselhamento jurídico brasileiro.
- Frameworks de oferta podem sugerir bônus, garantia e urgência. Só prometer o que existe e pode ser entregue; sem escassez, prazo, depoimento, autoridade ou ROI fabricados.
- Os estudos de caso numéricos não têm comprovação independente suficiente no próprio repositório; o próprio documento de case studies indica que não há resultados comunitários verificados. Não usá-los como benchmark.
- Linguagem como “viral”, “3x potencial” ou ROI alto é aspiracional, não garantia.
- O CLI depende de Bun e API externa OpenAffiliate; pode ajudar a consultar candidatos, mas não comprova termos nem qualidade. Não é necessário para o MAK inicial.
- Evals podem carregar expectativas legadas de scoring e precisam ser lidos junto das skills canônicas.

## 8. O que incorporar no Prompt Vivo agora

1. Modularizar a execução em módulos com input/output e handoffs claros.
2. Criar padrão de brief de conteúdo baseado em evidência.
3. Tornar verificação de oferta em fonte primária obrigatória.
4. Tornar análise de canal/comunidade anterior à distribuição.
5. Separar rascunho, revisão, aprovação, publicação e mensuração.
6. Criar tracking consistente por conteúdo/canal/CTA.
7. Criar retrospectiva com diagnóstico e próxima hipótese.
8. Adicionar relacionamento/memória de marca como trilha independente de conversão.
9. Adotar feedback estruturado para falhas e dados ausentes.
10. Manter gates de compliance, privacidade, copyright e autorização humana.

## 9. Prioridade e limites atuais

A meta de R$150 recebidos até 06/12/2026 continua separada da construção de um motor de médio prazo. Afiliação pode ter prazos de aprovação, reembolso e payout incompatíveis com o prazo imediato. O MAK não está validado até existirem experiências e resultados observados.

Nenhuma ferramenta foi instalada, nenhum código foi executado/importado, nenhuma conta afiliada foi criada, nenhum conteúdo foi publicado e nenhum contato foi realizado nesta auditoria.

## 10. Fontes primárias examinadas

- https://github.com/Affitor/affiliate-skills
- https://github.com/Affitor/affiliate-skills/blob/main/README.md
- https://github.com/Affitor/affiliate-skills/blob/main/QUICKSTART.md
- https://github.com/Affitor/affiliate-skills/blob/main/CLAUDE.md
- https://github.com/Affitor/affiliate-skills/blob/main/docs/AGENT-SOURCE-OF-TRUTH.md
- https://github.com/Affitor/affiliate-skills/blob/main/docs/affiliate-funnel-overview.md
- https://github.com/Affitor/affiliate-skills/blob/main/shared/references/flywheel-connections.md
- https://github.com/Affitor/affiliate-skills/blob/main/shared/references/feedback-protocol.md
- https://github.com/Affitor/affiliate-skills/blob/main/shared/references/ftc-compliance.md
- https://github.com/Affitor/affiliate-skills/blob/main/shared/references/platform-rules.md
- https://github.com/Affitor/affiliate-skills/blob/main/shared/references/offer-frameworks.md
- https://github.com/Affitor/affiliate-skills/blob/main/shared/references/social-data-providers.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/research/find-and-verify-affiliate-program/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/research/trending-content-scout/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/research/content-angle-ranker/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/funnel-planner/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/compliance-checker/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/self-improver/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/content/content-pillar-atomizer/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/content/reddit-post-writer/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/content/tiktok-script-writer/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/automation/content-repurposer/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/distribution/email-drip-sequence/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/analytics/conversion-tracker/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/analytics/performance-report/SKILL.md
- https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/landing-page-creator/SKILL.md


## Retificação e aprofundamento da auditoria (2026-11-26)
A contagem anunciada neste estudo deve ser lida junto da auditoria posterior [MAK_AFFITOR_EVIDENCE_AND_GOVERNANCE.md](MAK_AFFITOR_EVIDENCE_AND_GOVERNANCE.md). O snapshot atual auditado da branch main (tree SHA `f4cb063a0ee83b1b9e5167e396ab46cc9123dadc`) contém 53 skills canônicas e 53 entradas de registry. O README/QUICKSTART anunciam 52, enquanto o changelog registra 50 para a release 1.2.0; esses dois números são documentação histórica/desatualizada, não a contagem atual. A auditoria também detalha proxies de métricas, heurísticas, casos não corroborados, disclosure brasileiro e controles de oferta. Em caso de divergência, usar o documento de governança mais recente.
