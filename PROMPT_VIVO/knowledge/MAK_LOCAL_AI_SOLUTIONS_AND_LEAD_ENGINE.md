# MAK — Soluções digitais locais, prospecção e motor de leads

**Data:** 26/11/2026  
**Estado:** linha de pesquisa paralela documentada; não aprovada como execução comercial.  
**Objetivo:** identificar pequenos negócios na região, diagnosticar maturidade digital e oferecer soluções tecnológicas/IA proporcionais, com implantação competitiva e manutenção recorrente. Primeiro cliente e cases reais são os objetivos iniciais; não prometer resultados que ainda não foram medidos.

## 1. Hipótese comercial

Uma operação solo assistida por IA pode produzir sites, cardápios, páginas, formulários, sistemas leves e automações com custo/tempo de implementação menor que uma agência tradicional. O modelo possível:
- implantação com preço inicial competitivo;
- mensalidade fixa para hospedagem compatível com uso comercial, manutenção, pequenas atualizações, monitoramento e suporte delimitado;
- extras cobrados separadamente;
- componentes reutilizáveis por segmento, mas personalização real para cada cliente.

A vantagem não é simplesmente “fazer barato com IA”; é entregar rápido, com escopo claro, comunicação simples e manutenção confiável.

## 2. Princípio de diagnóstico: adequação à maturidade

Não presumir que todo pequeno negócio precisa de app, chatbot ou CRM. Avaliar sinais públicos e confirmar em conversa:

| Nível | Sinais possíveis | Primeira solução proporcional |
|---|---|---|
| 0 — presença básica | Ficha incompleta, telefone, pouca informação pública, sem canal digital claro | Perfil/contato, página simples de apresentação, horários, localização e CTA |
| 1 — social/WhatsApp | Instagram ou WhatsApp, mas sem catálogo/cardápio organizado | Link único, catálogo/cardápio responsivo, botão WhatsApp, formulário simples |
| 2 — operação digital inicial | Cardápio/link de pedido, mas conteúdo desatualizado, fluxo confuso ou dependência de atendimento manual | Site leve, menu organizado, FAQ, captura de pedidos/solicitações, mensagens preparadas |
| 3 — operação estruturada | Site, redes, pedidos, equipe, agenda ou vários serviços | Automação específica, painel leve, integração autorizada, relatórios ou workflow |
| 4 — operação avançada | Processos e sistemas já existentes, equipe e dados | Diagnóstico aprofundado; integração sob medida, nunca propor sem entender sistemas e segurança |

Nível é hipótese de trabalho, não julgamento de qualidade do empresário. Ausência de site não significa falta de CNPJ, orçamento ou interesse. CNPJ não é um proxy confiável de maturidade digital. Não inventar problemas; validar com o responsável.

## 3. Oferta inicial por vertical

### Pizzaria / restaurante
- Cardápio digital responsivo com categorias, tamanhos, adicionais, preços e observações.
- Botões de pedido via WhatsApp (pedido é confirmado pela equipe; não fingir integração automática).
- Página com horário, endereço, área de entrega, meios de pagamento e perguntas frequentes.
- Link curto/QR code para balcão, embalagem e redes sociais.
- Atualização mensal do cardápio e horários.
- Evolução opcional: formulário de pedido, painel de pedidos ou integração oficial com plataforma, somente após validar necessidade e custo.

### Barbearia / salão
- Página de serviços e preços, localização e profissionais.
- Solicitação de horário via WhatsApp ou formulário.
- Perguntas frequentes, políticas de atraso/cancelamento e link para agenda existente.
- Evolução: lembretes ou agenda integrada com consentimento e ferramentas autorizadas.

### Oficina / assistência / prestador
- Página de serviços, regiões atendidas, fotos autorizadas, formulário de orçamento e CTA.
- Checklist de triagem; não coletar dados desnecessários.
- Painel simples de solicitações somente se houver volume/processo que justifique.

### Loja de bairro
- Catálogo leve, produtos/serviços principais, horário e localização.
- Link para consulta de disponibilidade pelo WhatsApp.
- Não construir e-commerce/estoque/ERP se um catálogo simples resolver.

### Clínica/saúde
- Linha de maior cautela: dados de saúde são sensíveis. Começar apenas por site institucional, informações públicas, agendamento com fornecedor adequado e formulário mínimo. Não criar chatbot que coleta sintomas/prontuários nem manipular dados clínicos sem requisitos, contratos e controles especializados.

## 4. Modelo comercial e manutenção

Preços ainda são HIPÓTESES para testar, não benchmark de mercado nem tabela aprovada:
- **Página essencial:** implantação experimental R$300–600; manutenção R$59–99/mês.
- **Cardápio/catálogo + WhatsApp:** implantação experimental R$450–900; manutenção R$79–149/mês.
- **Automação ou painel específico:** orçamento após diagnóstico e protótipo; não precificar como pacote simples.
- Domínio, e-mail, serviços de terceiros, taxas, APIs e integrações pagas são custos separados, transparentes e preferencialmente pagos diretamente pelo cliente.
- Cliente deve ser titular de domínio, contas, dados e ativos; conceder acesso mínimo necessário.
- Mensalidade não pode ser “taxa vaga”: definir SLA razoável, backup quando aplicável, atualizações de conteúdo com limite, monitoramento e suporte em horário acordado.
- Definir o que não está incluído: novas páginas grandes, redesign, funcionalidades, cadastro massivo, anúncios, custos de API, suporte emergencial e alterações ilimitadas.
- Cobrar implantação e mensalidade separadamente; contrato simples com escopo, prazo, propriedade, renovação, cancelamento, responsabilidade por conteúdo e proteção de dados.
- Não oferecer hospedagem comercial em plano free que proíba uso comercial (ex.: Vercel Hobby). Revalidar termos e custos de cada serviço.

## 5. Motor de leads local

### Fontes
1. Google Maps para descoberta manual por categoria e bairro; observar ficha, telefone comercial, site, links, fotos e presença digital.
2. Diretórios locais como Solutudo e Taboao.org, confirmando atualidade em fonte do próprio negócio.
3. Instagram/Facebook oficiais, Linktree e cardápios/sistemas de pedido linkados pela própria empresa.
4. Site e domínio do negócio; busca Google pelo nome e telefone.
5. Indicações de clientes e parceiros, com introdução consentida.

### Restrição crítica — Google Maps
Não criar scraper, crawler, extensão, robô, extração em massa nem exportar para CRM uma base de nomes, endereços, telefones ou avaliações extraída do Google Maps. Termos do Google Maps Platform proíbem exportar/copiar conteúdo do Maps para fora dos serviços; Places API também tem restrições de armazenamento e extração. Usar Maps manualmente como interface de descoberta e verificar dados por fontes independentes/publicadas pelo próprio negócio. Se um fluxo automatizado for necessário, obter dados de diretórios/fontes com licença e termos que permitam o uso, ou usar API e armazenar apenas o que os termos autorizam. Não treinar IA com conteúdo do Maps.

### Ficha mínima de lead
- Nome comercial e categoria.
- Fonte e URL pública.
- Telefone comercial geral, somente quando publicado para contato.
- Bairro/cidade.
- Site/link de pedidos/redes oficiais encontrados.
- Sinais observados, data da verificação e confiança.
- Hipótese de melhoria e pacote compatível.
- Canal de contato apropriado e status de permissão/opt-out.
- Nunca inferir proprietário, dados privados, CPF, telefone pessoal ou situação cadastral sem fonte legítima.

### Lead score (0–100; heurístico)
- Dor observável e específica: 0–25.
- Adequação entre dor e pacote simples: 0–20.
- Sinais de operação/atividade recente: 0–15.
- Contato comercial público e apropriado: 0–10.
- Capacidade provável de absorver a solução (sem inferir renda pessoal): 0–10.
- Evidência de interesse/abertura ao contato: 0–20.
Score baixo ou informação desconhecida não deve ser mascarado. Não pontuar com base em aparência, endereço residencial ou suposições socioeconômicas.

## 6. Contato, LGPD e WhatsApp

- Telefone publicado não significa consentimento para disparo de WhatsApp.
- Política do WhatsApp Business exige que a pessoa espere a comunicação e recomenda/prevê opt-in para mensagens/calls; não usar lista fria para disparos, automação ou follow-up em massa.
- Preferir: visita presencial respeitosa em horário apropriado; ligação breve ao número comercial para perguntar quem cuida de tecnologia/marketing e se aceita receber uma apresentação; e-mail comercial publicado; formulário oficial; networking/indicação. Se o responsável autorizar, enviar a apresentação no canal e formato acordados.
- Uma mensagem inicial por canal apropriado deve identificar o remetente, explicar a razão concreta, origem do contato, oferecer saída simples e não insistir após recusa. Não contornar bloqueios nem alternar canais para perseguir a pessoa.
- Dados de pessoa física (MEI, nome de responsável, celular pessoal, e-mail nominal) podem ser dados pessoais mesmo em contexto empresarial. Dado público continua sujeito à LGPD.
- Legítimo interesse não é autorização genérica para qualquer prospecção: documentar finalidade, necessidade, expectativa razoável, balanceamento, salvaguardas e opt-out; não usar dados sensíveis. Consultar o guia ANPD e obter orientação jurídica se escalar a operação.
- Nenhuma mensagem, ligação, visita ou contato foi feito nesta pesquisa.

## 7. Pilotos locais observados — Taboão da Serra

O diretório Solutudo lista 62 empresas na categoria pizzarias em Taboão da Serra. As páginas individuais exibem contatos e endereços, mas alguns registros podem estar desatualizados. Isso demonstra volume potencial de pesquisa, não 62 leads qualificados.

### Lista exploratória (não contactar sem validação)
| Negócio | Telefone listado | Endereço | Observação inicial |
|---|---|---|---|
| Pizzaria e Pastelaria Dinomarkis | (11) 95155-2170 | R. Enaura Maria da Conceição, 275, Jardim Silvio Sampaio | Página de diretório não mostra site/WhatsApp direto no conteúdo; precisa verificar canal atual e operação. |
| Bonaiute Pizzaria | (11) 4701-9292 | R. Dr. Carlos Siqueira Neto, 177, Parque Pinheiros | Diretório lista telefone e endereço; presença digital atual ainda não auditada. |
| Banana Pizzaria 1000 Graus | (11) 94100-0342 | R. Miguel Jorge, 183, Jardim Guaciara | Diretório lista telefone e endereço; presença digital atual ainda não auditada. |
| Pizzaria Souza Taboão | (11) 95957-4283 | R. Piracicaba, 204, Arraial Paulista | Diretório lista telefone e endereço; presença digital atual ainda não auditada. |
| Pizzaria Laroc | (11) 4701-9899 | Av. Dr. José Maciel, 622, Jardim Maria Rosa | Diretório lista telefone e endereço; presença digital atual ainda não auditada. |
| Pizzaria União Taboão | (11) 94741-9225 | R. Caroba, 444, Jardim Record | Diretório local aponta Instagram; site/cardápio não identificado nessa página. |
| Pizzaria Jardim Salete | Há divergência: Solutudo lista (11) 4138-3452 e Taboao.org lista (11) 98573-2935 | Solutudo: Av. Balbina Rodrigues de Borba, 738; Taboao.org: nº 760 | Não usar telefone/endereço até confirmar diretamente. |

**Importante:** estes são candidatos para auditoria, não recomendações de abordagem nem afirmações de que não possuem site. O diretório pode estar desatualizado. A presença de telefone não autoriza mensagem fria.

### Exemplos que mostram maturidade diferente
- Paiva Pizzas tem Linktree com Instagram, pedido online Saipos, WhatsApp e telefone fixo: não vender “um site” sem descobrir o que está faltando. Talvez nem seja lead prioritário.
- Skina da Pizza tem página de pedidos WABiz: não propor cardápio digital redundante; investigar se a plataforma resolve o problema atual.
- Pizzaria Bom Sucesso aparece com Linktree, WhatsApp e iFood: solução deve ser diferenciada, não mais um link genérico.

## 8. Portfólio de demonstração

Construir até três demos próprias, usando negócios fictícios e dados inventados claramente rotulados como demonstração:
1. **Pizzaria:** cardápio responsivo, categorias/adicionais, botão WhatsApp com mensagem pré-preenchida, horários e entrega.
2. **Barbearia:** serviços, preços fictícios, profissionais, solicitação de horário e FAQ.
3. **Prestador/oficina:** serviços, região atendida, formulário de orçamento e galeria demonstrativa.

Cada demo precisa mostrar:
- problema e público-alvo;
- antes/depois hipotético, sem inventar resultado real;
- funcionalidades incluídas e excluídas;
- versão mobile;
- velocidade, acessibilidade e testes básicos;
- como o cliente altera conteúdo;
- custo de operação e limites;
- termo “projeto demonstrativo — não é cliente real”.

Não construir três produtos enormes. Reutilizar componentes e mudar identidade, conteúdo e fluxo. Só transformar demo em case real após autorização e entrega a cliente; pedir autorização para publicar nome, imagens e métricas.

## 9. Processo operacional assistido por IA

1. Descobrir negócio em fonte permitida.
2. Conferir site, redes, pedidos, ficha, conteúdo e sinais atuais manualmente.
3. IA recebe apenas dados públicos pertinentes e produz diagnóstico preliminar com evidências e incertezas.
4. Humano confirma se a dor é real e se o negócio é adequado.
5. Criar mini-proposta de uma página com uma melhoria específica, escopo, prazo, preço e manutenção.
6. Contatar somente por canal apropriado; pedir permissão para enviar apresentação quando necessário.
7. Se houver interesse, fazer conversa de descoberta e confirmar processo atual antes de fechar escopo.
8. Construir protótipo com dados fictícios; aprovar antes de usar dados/contas do cliente.
9. Contrato, pagamento e autorização; implantação em contas do cliente ou com titularidade clara.
10. Handoff, treinamento, suporte, manutenção e revisão mensal.

IA pode resumir presença digital, gerar protótipos, preparar textos, construir código e testes. Não deve inventar problemas, publicar, enviar mensagens, acessar contas ou assumir compromissos sem revisão/aprovação humana.

## 10. Experimento inicial proposto — não iniciado

- Selecionar 10 negócios de uma única vertical e área.
- Verificar manualmente cada negócio e registrar evidência/fonte.
- Escolher 3 com dor clara e pacote proporcional.
- Criar 1 demo genérica antes da abordagem, não um app personalizado completo sem contrato.
- Buscar conversa consentida e validar problema/preço.
- Métricas: negócios auditados, dores confirmadas, permissões para apresentação, reuniões, propostas, fechamentos, valor de implantação, mensalidade, horas de entrega e custos reais.
- Critério de sucesso inicial: 1 cliente pagante e entrega satisfatória; não usar número de mensagens como substituto de venda.
- Sem bulk outreach, scraping, anúncio pago ou ferramenta paga.

## 11. Próximas pesquisas
- Auditar 10 negócios em Taboão/Embu com site, Instagram, pedidos e contato atual, evitando inferências.
- Comparar plataformas de cardápio/pedido e construtores de site, incluindo custos, termos comerciais, exportabilidade e dependência do fornecedor.
- Validar faixa de preço local com evidência de concorrentes e entrevistas consentidas.
- Avaliar stack gratuita comercialmente permitida e domínio pago diretamente pelo cliente.
- Pesquisar contratos, escopo de manutenção, backups, LGPD e responsabilidade.
- Reavaliar vertical: pizzarias são uma hipótese inicial, não nicho decidido.
