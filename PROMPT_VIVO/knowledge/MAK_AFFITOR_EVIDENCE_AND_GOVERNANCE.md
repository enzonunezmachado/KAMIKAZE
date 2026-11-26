# Affitor — auditoria de evidências, métricas e adaptação brasileira

**Projeto consumidor:** NEGÓCIO DIGITAL KAMIKAZE  
**Repositório auditado:** https://github.com/Affitor/affiliate-skills  
**Snapshot auditado:** branch `main`, árvore Git `f4cb063a0ee83b1b9e5167e396ab46cc9123dadc`  
**Data da auditoria:** 2026-11-26  
**Escopo:** contagem e canonização das skills; integridade das métricas; heurísticas de plataforma; evidência dos estudos de caso; disclosure e conformidade brasileira; claims de urgência, bônus e garantias.  
**Método:** leitura de README, registry, changelog, fonte de geração do registry, testes, avaliações, referências compartilhadas e skills selecionadas. Leitura das fontes oficiais brasileiras e das políticas de plataforma. Nenhuma instalação ou execução do repositório foi feita.

> Esta auditoria é uma avaliação documental e operacional, não parecer jurídico, auditoria de resultados comerciais nem certificação do Affitor.

---

## 1. Contagem real de skills: 50, 52 ou 53?

### Resultado do snapshot

A árvore recursiva de `main` contém exatamente **53 arquivos canônicos `SKILL.md` sob `skills/*/*/SKILL.md`**, distribuídos por oito estágios. O `registry.json` contém 53 entradas. Após normalizar o campo `path` do registry para `path/SKILL.md`, a comparação encontrou:

- arquivos de skill ausentes do registry: **0**;
- entradas do registry sem arquivo correspondente: **0**;
- caminhos duplicados no registry: **0**;
- divergência entre contagem de arquivos canônicos e registry: **0**.

| Estágio | Skills |
|---|---:|
| research | 11 |
| content | 7 |
| blog | 7 |
| landing | 8 |
| distribution | 4 |
| analytics | 5 |
| automation | 5 |
| meta | 6 |
| **Total** | **53** |

### Por que aparecem três números?

- **50:** o `CHANGELOG.md` registra que a versão 1.2.0, em 03/04/2026, atualizou README e registry com 50 skills. É um número histórico, válido para aquela versão, não para o snapshot atual.
- **52:** o README atual ainda anuncia “52 AI-powered skills”, “52 skills” no título da seção, e o QUICKSTART também usa 52. É documentação pública desatualizada em relação ao catálogo atual.
- **53:** é a contagem reproduzível da árvore atual e do `registry.json` no snapshot auditado.

O root `SKILL.md` (`affiliate-check`) e `template/SKILL.md` não foram incluídos na contagem de skills catalogadas: o primeiro é a skill/entrada de integração do repositório, e o segundo é um modelo, não uma skill de estágio. A contagem operacional deve ser definida explicitamente como arquivos `skills/<stage>/<slug>/SKILL.md`, não como qualquer arquivo com esse nome no repositório.

### Fonte da verdade e prevenção de drift

O próprio `docs/AGENT-SOURCE-OF-TRUTH.md` diz que os arquivos individuais são canônicos para comportamento, o `registry.json` é o catálogo machine-readable, e README/QUICKSTART são resumos derivados. O script `scripts/generate-registry.js` varre `skills/{stage}/{skill}/SKILL.md` e gera o registry. O teste `tests/test-registry-invariants.ts` compara contagem, paths, estágio, slug, existência dos arquivos e frontmatter.

**Regra Kamikaze:** sempre que citar a quantidade de skills, registrar snapshot/commit e método de contagem. Nunca misturar skills catalogadas, root integration skill, templates, exemplos e ferramentas. A fonte atual é 53, até nova verificação; não editar o projeto de terceiros.

---

## 2. Skills antigas, ponteiros de compatibilidade e versões canônicas

O caso comprovado mais claro é `affiliate-program-search`:

- O registry o descreve como **“Compatibility pointer”** e direciona para `find-and-verify-affiliate-program`.
- O README ainda apresenta os dois como se fossem duas ferramentas autônomas para tarefas distintas.
- O changelog 1.2.1 (19/10/2026) registra explicitamente que a descoberta de programas foi incorporada ao fluxo MCP-first de `find-and-verify-affiliate-program`, mantendo `affiliate-program-search` como ponteiro de compatibilidade naquela release.

Isso não é uma skill removida do filesystem; é uma entrada preservada para compatibilidade, enquanto o fluxo de trabalho atual é canônico em outra skill. Logo, não se deve interpretar cada pasta como capacidade independente nem somar uma skill ponteiro como se fosse uma funcionalidade nova.

A auditoria confirma também que a fonte do repositório declara hierarquia documental: skill individual e referências locais > README/QUICKSTART; referências compartilhadas > resumos; registry + arquivos reais > contagens promocionais. O `CHANGELOG` fornece o contexto histórico da migração.

**Regra Kamikaze:** manter um catálogo de capacidades com estado `canonical`, `compatibility_pointer`, `deprecated`, `experimental` ou `template`. Um ponteiro de compatibilidade deve declarar destino e motivo. A contagem de capacidades principais deve poder ser separada da contagem de arquivos físicos.

---

## 3. Métricas de conteúdo: dado observado, proxy e estimativa

### O que a implementação documental propõe

A skill `trending-content-scout` combina duas modalidades:

1. **API mode:** tenta obter estatísticas estruturadas das APIs/provedores configurados.
2. **web_search fallback:** extrai título, autor e contagens aproximadas de snippets/resultados de busca, ou apenas sinais de visibilidade quando não há métricas estruturadas.

A fórmula proposta para um `engagement_score` é:

`(likes × 2 + comments × 3 + shares × 5) / max(views, 1) × 1000`

A própria skill orienta estimar shares no YouTube como `comments × 0.5` quando não disponíveis e, no fallback de busca, usar views como sinal de ranking e marcar o score como estimado. A referência `social-data-providers.md` reconhece que shares não estão disponíveis em algumas APIs e podem ser estimados por razão de engajamento.

### Problemas metodológicos

- Os pesos 2, 3 e 5 são escolhas internas do modelo, não coeficientes validados como relação universal entre likes, comentários, compartilhamentos e valor comercial.
- A estimativa `shares = comments × 0.5` não é observação; não deve ser apresentada como contagem real.
- Views de plataformas distintas não são equivalentes: definições, superfícies, duração, reprodução automática, janela de contagem e distribuição variam.
- Snippets de busca podem estar desatualizados, arredondados, incompletos ou sem contexto temporal.
- Uma amostra dos “top resultados” encontrada por busca não é amostra aleatória do mercado. Há viés de seleção, personalização, idioma, região, ranking e indexação.
- Médias de um pequeno conjunto de posts são sensíveis a outliers. Mediana, intervalo, tamanho da amostra e distribuição são mais informativos.
- “Top 10%” exige amostra e regra de percentil explícitas; não pode ser extrapolado de uma busca parcial.
- Engajamento não prova intenção de compra, conversão, receita ou qualidade do público.

A skill `content-angle-ranker` também produz pontuações subjetivas: usa pesos como engagement prediction 30%, creator fit 15% e critérios de competição/plataforma, e oferece defaults genéricos quando os dados são limitados. São úteis como estrutura de discussão, mas não são um modelo estatístico calibrado. A própria skill reconhece que, com dados limitados, os scores podem usar padrões gerais da plataforma.

### Taxonomia obrigatória de evidência

Cada campo do MAK deve receber um rótulo:

| Classe | Significado | Exemplo |
|---|---|---|
| OBSERVED_PLATFORM | Métrica lida diretamente em painel/API oficial ou página pública identificada | views exibidas em vídeo |
| OBSERVED_THIRD_PARTY | Dado fornecido por fornecedor externo; registrar fornecedor e método | estimativa de tráfego Similarweb |
| SEARCH_SNIPPET | Valor extraído de snippet, potencialmente incompleto/defasado | contagem aproximada em resultado de busca |
| CALCULATED | Cálculo determinístico sobre dados observados | taxa de comentário = comentários/views |
| ESTIMATED | Valor inferido por regra ou aproximação | shares estimados a partir de comentários |
| HEURISTIC | Regra qualitativa ou pontuação de julgamento | “comparativos tendem a funcionar” |
| HYPOTHESIS | Suposição a testar | “este ângulo pode atrair compradores” |
| UNKNOWN | Dado ausente | cliques não fornecidos |

Nunca preencher campo ausente com zero sem dizer que zero significa “medido e igual a zero”. Ausente é `null/unknown`, não zero.

### Protocolo de medição recomendado ao Kamikaze

Para cada publicação/peça, registrar plataforma, URL/ID, formato, tema, data/hora, data da captura, idade da publicação no momento da captura, origem do dado, contagens brutas, público/segmento, CTA, cliques, leads, compras, receita, reembolsos e esforço. Calcular taxas apenas quando numerador e denominador forem observados na mesma janela e com definições compatíveis.

- Separar alcance/impressões de visualizações e reproduções.
- Guardar snapshot em tempos definidos (ex.: 24h, 7d, 30d) quando for possível; não comparar um post de 2 horas com um de 3 semanas.
- Comparar posts dentro da mesma plataforma, formato, objetivo e janela.
- Exibir `n`, mediana, quartis ou faixa; evitar apenas média.
- Marcar amostras pequenas como exploratórias.
- Separar métricas antecedentes (views, visitas, follows, saves) de intenção (cliques, perguntas, conversas) e resultado (compras, comissão líquida, payout).
- Não usar “engagement score” como sinônimo de potencial de venda.

---

## 4. Regras de plataformas: políticas oficiais versus heurísticas

O arquivo `shared/references/platform-rules.md` contém conselhos como “LinkedIn suprime posts com links externos”, “comentários são o melhor lugar para link”, “comparações convertem melhor”, “contas Reddit com menos de 30 dias/baixo karma são sinalizadas”, e associações entre plataforma e perfil de comprador. Essas afirmações podem ser hipóteses úteis, mas não são políticas oficiais universais nem garantias de alcance/conversão.

### Classificação

- **POLICY:** regra publicada pela própria plataforma, vinculada a URL, data de consulta, região e escopo.
- **OBSERVED_PATTERN:** padrão observado em amostra delimitada; requer amostra, janela e método.
- **HEURISTIC:** recomendação operacional que pode funcionar em alguns contextos.
- **HYPOTHESIS:** hipótese ainda não testada no canal/segmento do projeto.
- **ANECNOTE:** relato individual; não generalizar.

Exemplo: “Reddit exige transparência e algumas comunidades proíbem autopromoção” deve ser dividido em regra geral da plataforma e regra específica de cada subreddit. A recomendação de construir karma antes de divulgar é heurística; nunca justifica participação disfarçada ou promoção que viole as regras da comunidade.

**Regra Kamikaze:** não afirmar que um link no corpo reduz alcance, que um formato é “o melhor”, ou que determinada plataforma favorece uma oferta sem evidência atual e específica. Testar variações quando permitido, medir resultados e revisar a política oficial antes de cada campanha. As políticas mudam e podem variar por país, conta, produto, formato e tipo de relação comercial.

---

## 5. Estudos de caso numéricos: o que está e não está demonstrado

O arquivo `shared/references/case-studies.md` apresenta três casos com números detalhados:

- HeyGen/LinkedIn: cerca de US$2.400/mês, 3 meses, 2,3% clique-para-trial e 18% trial-para-pago.
- Semrush/SEO: cerca de US$3.000/mês, 6 meses, 4,1% clique-para-trial.
- Webflow/X: cerca de US$1.800/mês, 2 meses até primeira comissão significativa, 1,8% clique-para-cadastro.

Porém, o próprio documento afirma **“No community results yet”** na seção de resultados comunitários. Não há, junto a esses três casos, identidade verificável do afiliado, URL de campanha, analytics, dashboard da rede, período de atribuição, comprovante de payout, método de cálculo, custos, reembolsos ou corroboração independente. Portanto, os números são **claims de caso sem documentação de origem suficiente no repositório**. Não podem ser usados como benchmarks comprovados nem como expectativa de resultado.

O README contém uma demonstração “zero to first commission” com amostras como 47 vídeos, engagement 35.2, mediana 18K views e top 10% em 85K; o próprio formato é uma demonstração ilustrativa, não um relatório de execução auditado. Evals testam se uma resposta contém padrões textuais e critérios de formato; não provam que a estratégia gera vendas.

### Escala de confiança para casos

- **C0 — ilustração:** números de exemplo/demonstração, sem fonte.
- **C1 — autorrelato:** autor identificável relata resultado, sem documentação verificável.
- **C2 — evidência observável parcial:** post, painel ou página pública permite confirmar parte dos números.
- **C3 — corroboração independente:** fonte independente confirma identidade, campanha e resultado relevante.
- **C4 — evidência primária auditável:** export/dashboard de rede, registros de atribuição e pagamento, com período, custos e reembolsos reconciliáveis.

Os três casos no `case-studies.md` devem ser tratados como **C0/C1 não classificável com segurança** até que o mantenedor apresente as fontes primárias. A seção “Community-Verified Results” vazia não corrobora esses casos.

### Campos mínimos de um caso futuro

Produto e programa; afiliado ou identificador anonimizado; plataforma; links/peças; datas; impressões/views; cliques únicos; trials/leads; vendas aprovadas; comissão bruta; estornos/reembolsos; comissão líquida; payout recebido; investimento/custos; horas de trabalho; janela de atribuição; fonte de cada número; consentimento para publicação; limitações e resultados negativos. Marcar claramente o que foi revisado e por quem. “Verified” não deve significar apenas que o texto parece plausível.

---

## 6. Disclosure e conformidade: adaptação ao Brasil

A referência atual `shared/references/ftc-compliance.md` é explicitamente centrada na FTC e usa `#ad` como exemplo genérico. A FTC é autoridade norte-americana; seu material pode servir como referência comparativa, mas **não é a fonte normativa principal para uma campanha dirigida ao consumidor brasileiro**.

### Fontes brasileiras prioritárias

1. **Código de Defesa do Consumidor — Lei 8.078/1990**
   - Art. 30: informação/publicidade suficientemente precisa vincula o fornecedor e integra o contrato.
   - Art. 31: oferta deve trazer informação correta, clara, precisa, ostensiva e em português, incluindo características, preço, garantia, prazos e origem.
   - Art. 36: publicidade deve ser identificável fácil e imediatamente; o parágrafo único exige sustentação factual/técnica/científica das mensagens.
   - Art. 37: proíbe publicidade enganosa ou abusiva; omitir dado essencial também pode caracterizar enganosidade.
   - Art. 38: o ônus de provar veracidade/correção da publicidade é de quem a patrocina.
2. **Decreto 7.962/2013 (comércio eletrônico):** exige informações claras sobre produto, serviço e fornecedor, atendimento facilitado e respeito ao direito de arrependimento; o art. 2º lista informações que devem estar em destaque e fácil visualização nos meios eletrônicos de oferta/contratação.
3. **CONAR — Código Brasileiro de Autorregulamentação Publicitária e Guia de Marketing e Publicidade por Influenciadores Digitais.** A página do CONAR atualizada em 26/05/2026 informa nova versão diagramada do guia, com vigência a partir de 01/06/2026, tratando identificação, transparência, testemunhais genuínos, restrições setoriais, crianças/adolescentes e IA.
4. **Políticas das plataformas:** são obrigações contratuais adicionais, não substitutos da lei brasileira.

### Orientação prática conservadora para afiliados

Quando houver link com comissão, pagamento, produto recebido, desconto, convite, benefício ou outra relação material:
- identificar a natureza comercial de forma clara, ostensiva e próxima da recomendação/link, desde a primeira exposição relevante;
- preferir linguagem em português simples: **“Publicidade — este é um link de afiliado. Se você comprar por ele, posso receber uma comissão, sem custo adicional para você.”**
- adaptar a frase à realidade: se recebeu produto gratuitamente, dizer isso; se é parceria paga, dizer isso; se é comissão apenas quando há compra, não sugerir pagamento fixo;
- não depender apenas de uma página institucional, de uma hashtag ambígua, de texto escondido no rodapé ou de uma ferramenta nativa se a relação não ficar clara ao consumidor;
- em vídeo, deixar a informação visível e/ou audível de forma adequada ao formato, não apenas em descrição que pode não ser vista;
- manter registro do produto, termos, comissão, afirmações e fontes que sustentam a recomendação;
- não afirmar experiência pessoal que não ocorreu; separar “testei” de “pesquisei/documentei”;
- quando houver dúvida sobre produto regulado/restrito, público vulnerável ou claim de saúde/finanças, bloquear a campanha e exigir análise específica antes de publicar.

### Regras específicas de plataforma verificadas nesta auditoria

- **TikTok:** a Central de Ajuda em português determina ativar a configuração de divulgação de conteúdo ao promover a própria empresa ou produto/serviço de terceiro em troca de pagamento ou outro incentivo. O TikTok rotula conteúdo promocional próprio ou parceria paga; a plataforma pode remover/restringir posts sem divulgação apropriada. A documentação também diz que a configuração, por si, não altera a distribuição no feed.
- **Instagram/Meta:** materiais oficiais do Instagram para empresas dizem que conteúdo de marca em troca de valor — dinheiro, presentes ou descontos — deve usar o rótulo “Parceria paga”. Isso é regra de plataforma para conteúdo de marca; a identificação textual clara continua importante para cumprir o CDC/CONAR e esclarecer a comissão de afiliado.
- **YouTube:** a auditoria não encontrou nesta rodada fonte oficial atual suficientemente específica para fixar uma regra universal de disclosure de link afiliado em todas as superfícies. Não copiar automaticamente a regra FTC de “primeiros 30 segundos” como lei brasileira. Verificar a política atual de promoções pagas do YouTube e usar divulgação clara na própria peça, descrição e/ou ferramenta nativa conforme o tipo de relação.

Os critérios da Secom/PR para publicidade institucional e Midiacad não devem ser automaticamente generalizados para todo afiliado privado; são úteis como referência adicional, mas têm escopo próprio.

### Limite jurídico

Este módulo estabelece controles operacionais conservadores e fontes para consulta; não determina responsabilidade jurídica em casos concretos. Para ofertas reguladas, campanhas de grande alcance, contratos complexos ou dúvidas materiais, consultar profissional habilitado.

---

## 7. Urgência, escassez, bônus, garantias e claims de conversão

As referências `offer-frameworks.md` e skills `grand-slam-offer`, `bonus-stack-builder` e `guarantee-generator` contêm boas salvaguardas (bônus entregáveis, garantia limitada ao que o afiliado controla, rejeição de falsa urgência), mas também recomendações e números que não devem ser repetidos como fatos:

- “bonuses are the #1 differentiator” e “bonus stacks increase conversion rates by 2–5x”;
- bônus avaliados em 3–10x o preço do produto ou total percebido maior que o produto;
- “guarantee increases conversion rates by 15–30%”;
- bônus de 200–400% higher conversion, hero bonus can double conversions;
- sugerir limitar bônus no tempo, usar exclusividade ou criar “only through my link”;
- garantias de resultado/satisfação e claims como “I'll help you get your first campaign in 48 hours”.

Essas percentagens aparecem sem fonte, desenho de experimento, amostra, segmento, intervalo de confiança ou resultados publicados no repositório. São **claims não corroborados**. O uso de valor percebido artificial também pode enganar: não atribuir preço fictício a material gratuito, não chamar algo de exclusivo se não for exclusivo, não inflar o valor de um bônus e não prometer suporte que não será prestado.

### Política Kamikaze de oferta

**Urgência/escassez:** só usar quando houver limite real, verificável e explicado (prazo contratual, estoque real, número real de vagas ou capacidade de atendimento). Não reiniciar contagem regressiva, não inventar “últimas vagas”, não usar prazo falso e não ocultar que a oferta continuará disponível.

**Bônus:** cada bônus deve existir, ter escopo, formato, prazo de entrega, elegibilidade e responsável definidos. “Exclusivo” apenas se a exclusividade puder ser demonstrada. Não atribuir valor monetário sem base real de preço comparável ou histórico de venda. Não criar bônus apenas para inflar a oferta.

**Garantia:** separar a garantia oficial do produtor da promessa adicional do afiliado. Não alterar, ampliar ou prometer reembolso em nome do produtor. Uma promessa própria só pode cobrir algo sob controle do afiliado, com capacidade, condições, prazo e procedimento claros; não garantir renda, aprovação, resultado comercial ou desempenho de terceiro. Se não houver capacidade para cumprir, não oferecer garantia adicional.

**Claims de resultado:** toda afirmação objetiva precisa de evidência adequada, representativa e contextualizada. Informar condições, período, amostra e limitações. Um caso individual não representa resultado típico. Nunca usar projeções como resultados realizados.

**Regra de bloqueio:** sem prova de prazo/escassez, sem oferta urgente; sem ativo/entrega, sem bônus; sem capacidade e termos claros, sem garantia; sem fonte e contexto, sem percentual de conversão/ganho.

---

## 8. O que o Kamikaze deve aproveitar e o que deve rejeitar

### Aproveitar
- arquitetura modular e outputs estruturados;
- encadeamento de pesquisa → decisão → produção → distribuição → mensuração → aprendizado;
- verificação de termos na fonte primária do produtor;
- separação entre dados brutos e recomendação;
- qualidade editorial e revisão humana;
- feedback de erros e retrospectivas;
- compliance como gate pré-publicação;
- registro explícito de incerteza e origem dos dados.

### Adaptar
- scoring de ângulos como ferramenta de priorização, nunca previsão de sucesso;
- benchmark de conteúdo com coorte comparável e janela definida;
- recomendações de canal como hipóteses locais a testar;
- disclosure FTC para um módulo brasileiro centrado em CDC, CONAR, Decreto 7.962/2013 e políticas da plataforma;
- casos de sucesso como exemplos até que tenham evidência primária.

### Não adotar sem validação
- previsões de conversão e renda derivadas de benchmarks não documentados;
- claims de 2–5x, 15–30% ou 200–400% sem estudo rastreável;
- regras universais de algoritmo/alcance;
- métricas calculadas com dados estimados apresentadas como observadas;
- falsa exclusividade, escassez, urgência, garantia ou experiência pessoal;
- automação que viole termos, privacidade ou regras de comunidade.

---

## 9. Checklist de auditoria para cada campanha MAK

1. Oferta e termos atuais confirmados em fonte oficial? Data e URL registradas?
2. Público, problema e alternativa foram identificados sem assumir fit?
3. Todo dado tem fonte, data, método e classe de evidência?
4. Views, seguidores, cliques, leads, vendas e payout estão separados?
5. Comparações usam a mesma plataforma, formato, janela e denominador?
6. Recomendações de algoritmo estão rotuladas como heurística/hipótese?
7. Caso de sucesso tem nível de confiança e evidência proporcional ao claim?
8. Comissão/benefício foi divulgado em português, de forma imediata e clara?
9. Ferramentas de disclosure da plataforma foram ativadas quando exigidas?
10. Claims, depoimentos e comparações têm sustentação verificável?
11. Bônus existem e podem ser entregues? Exclusividade e valor são reais?
12. Prazo/escassez é verdadeiro e auditável?
13. Garantia está sob controle do responsável e possui termos claros?
14. Política atual da plataforma e regras da comunidade foram verificadas?
15. Há aprovação humana antes de publicar, contatar ou gastar?

## 10. Fontes primárias e referências

### Repositório Affitor
- README: https://github.com/Affitor/affiliate-skills/blob/main/README.md
- Registry: https://github.com/Affitor/affiliate-skills/blob/main/registry.json
- Changelog: https://github.com/Affitor/affiliate-skills/blob/main/CHANGELOG.md
- Source of truth: https://github.com/Affitor/affiliate-skills/blob/main/docs/AGENT-SOURCE-OF-TRUTH.md
- Registry generator: https://github.com/Affitor/affiliate-skills/blob/main/scripts/generate-registry.js
- Registry invariant tests: https://github.com/Affitor/affiliate-skills/blob/main/tests/test-registry-invariants.ts
- Trending content scout: https://github.com/Affitor/affiliate-skills/blob/main/skills/research/trending-content-scout/SKILL.md
- Content angle ranker: https://github.com/Affitor/affiliate-skills/blob/main/skills/research/content-angle-ranker/SKILL.md
- Platform rules: https://github.com/Affitor/affiliate-skills/blob/main/shared/references/platform-rules.md
- Social data providers: https://github.com/Affitor/affiliate-skills/blob/main/shared/references/social-data-providers.md
- Case studies: https://github.com/Affitor/affiliate-skills/blob/main/shared/references/case-studies.md
- FTC compliance: https://github.com/Affitor/affiliate-skills/blob/main/shared/references/ftc-compliance.md
- Offer frameworks: https://github.com/Affitor/affiliate-skills/blob/main/shared/references/offer-frameworks.md
- Compliance checker: https://github.com/Affitor/affiliate-skills/blob/main/skills/meta/compliance-checker/SKILL.md
- Bonus stack builder: https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/bonus-stack-builder/SKILL.md
- Guarantee generator: https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/guarantee-generator/SKILL.md
- Grand slam offer: https://github.com/Affitor/affiliate-skills/blob/main/skills/landing/grand-slam-offer/SKILL.md

### Brasil — legislação, autorregulação e plataforma
- CDC, Lei 8.078/1990 (arts. 30, 31, 36, 37 e 38): https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- Decreto 7.962/2013 (comércio eletrônico): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm
- CONAR — códigos: https://www.conar.org.br/codigos
- CONAR — atualização do Guia de Marketing e Publicidade por Influenciadores Digitais (26/05/2026; vigência 01/06/2026): https://www.conar.org.br/noticias/guia-de-marketing-e-publicidade-por-influenciadores-digitais
- TikTok — promover marca, produto ou serviço (Central de Ajuda pt-BR): https://support.tiktok.com/pt_BR/business-and-creator/creator-and-business-accounts/promoting-a-brand-product-or-service
- Instagram/Meta — transparência em parcerias: https://pt-br.facebook.com/business/news/instagram/tools-to-disclose-instagram-partnerships/
- Instagram/Meta — colaboração com criadores e parceria paga: https://pt-br.facebook.com/business/instagram/collaborate-with-creators
- Secom — identificação de conteúdo publicitário (escopo de publicidade institucional/criadores contratados): https://www.gov.br/secom/pt-br/assuntos/publicidade/meios/internet/identificacao-de-conteudo-publicitario
- FTC — Endorsement Guides (referência comparativa dos EUA, não substitui normas brasileiras): https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking

---

## 11. Limitações e próximos passos

- Snapshot é da branch `main` e do tree SHA indicado; o repositório pode mudar depois desta auditoria.
- O conteúdo foi lido via GitHub; os testes do repositório não foram executados.
- Não foi feita auditoria de todas as 53 skills linha a linha; a análise aprofundada concentrou-se nas áreas diretamente ligadas às sete ressalvas solicitadas.
- Não foi possível confirmar externamente os três estudos de caso numéricos.
- Não foi realizada consulta jurídica individualizada.
- Não foram publicadas campanhas nem realizados testes de marketing.

**Decisão para o Kamikaze:** incorporar este documento como política metodológica do MAK. A próxima atualização da arquitetura deve aplicar as classes de evidência, níveis de confiança, disclosure brasileiro e gates de oferta aos workflows de pesquisa, conteúdo, distribuição, relacionamento e mensuração. Não importar nem executar o Affitor; adaptar apenas os métodos aprovados.
