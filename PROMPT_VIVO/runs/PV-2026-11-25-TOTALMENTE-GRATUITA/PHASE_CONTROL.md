
# Controlador adaptativo de fases — execução Kamikaze

**Versão:** 1.1  
**Escopo:** esta execução; modelo reutilizável para futuras runs.

## Regra de interação
Quando o usuário disser "próxima", "continua", "vai", "pode avançar" ou equivalente, interpretar como autorização para continuar o trabalho — não como obrigação de trocar o número da fase nem como aprovação automática de um gate factual.
Comentários, correções e preferências expressos antes de "próxima" também devem ser incorporados: classificar impacto, registrar em USER_INPUT_LOG.md e reavaliar escopo, método, critérios e arquitetura.

## Retomada entre chats
Em novo chat, executar PROMPT_VIVO/BOOTSTRAP.md e ler RESUME_PACKET.md antes dos detalhes. Reconstruir projeto, execução, pesquisa/build atual, fase, evidências, decisões, restrições e próxima ação. Não pedir que o usuário repita o contexto documentado. Não alegar certeza total; apontar arquivos ausentes ou contraditórios.

## Ciclo obrigatório antes de cada transição
1. **Recarregar:** ler RUN_STATE, RESUME_PACKET, arquitetura, plano, checkpoint atual, instrução da fase, fontes, achados, perguntas abertas e entregáveis existentes.
2. **Incorporar feedback:** verificar mensagens recentes do usuário; registrar no USER_INPUT_LOG e atualizar arquivos afetados.
3. **Auditar completude:** comparar objetivo/perguntas da fase com evidências, qualidade, contraprovas e entregáveis.
4. **Classificar:** avaliar cada requisito como RESPONDIDO, PARCIAL, NÃO RESPONDIDO, BLOQUEADO ou NÃO APLICÁVEL.
5. **Escolher a ação mínima útil:** CONTINUE_PHASE, CREATE_SUBPHASE, REOPEN_PHASE, ADVANCE, SYNTHESIZE ou BLOCK.
6. **Registrar decisão:** motivo, evidências, lacunas, dependências, impacto de cotas, entregáveis e próximo gate.
7. **Sincronizar memória:** PHASE_ARCHITECTURE, RUN_STATE, RESEARCH_PLAN, MEMORY_HANDOFF, RESUME_PACKET, USER_INPUT_LOG, STATE e checkpoint afetado.
8. **Executar a ação escolhida:** não ficar apenas anunciando o plano.

## Estados de gate
- PASS: requisitos essenciais atendidos; lacunas residuais não mudam a decisão.
- PASS_WITH_GAPS: pode prosseguir com limitações explicitadas e transferidas.
- CONTINUE: falta trabalho que pode ser feito agora; não avançar.
- FAIL: evidência/viabilidade contradiz a hipótese ou o padrão mínimo.
- BLOCKED: dependência externa ou aprovação necessária.

## Regras de integridade
- Autorização para "próxima" não transforma hipótese em fato nem compra em venda.
- Não encerrar fase apenas porque foi criado o arquivo da fase seguinte.
- Não repetir pesquisa já suficiente; aprofundar apenas onde a resposta pode mudar a decisão.
- Uma fase pode ter subfases ilimitadas, sem criar burocracia.
- Fases paralelas são permitidas quando não dependem uma da outra; registrar dependências.
- Nunca apagar histórico; registrar reabertura, divisão, mescla ou encerramento.
- Não abordar clientes, publicar, enviar propostas, contratar, comprar, assinar ou fazer deploy sem autorização humana explícita.

## Formato de decisão ao usuário
Informar em poucas linhas: fase auditada, decisão (continuar/subfase/avançar), motivo principal, o que foi executado, estado do repositório e próximo passo. Evitar pedir que o usuário escolha a numeração; a IA administra a arquitetura e explica a decisão.

## Aplicação atual
A auditoria identificou que PHASE_03_VALIDATION foi encerrada para transição antes de responder questões críticas. PHASE_04_FEASIBILITY existe como plano, mas nenhum teste operacional foi executado. PHASE_03_1_PURCHASE_EVIDENCE permanece ativa. Na segunda rodada, S062–S066 acrescentaram evidência parcial de execução, intenção de compra e recorrência declarada, mas não comprovaram venda de relatório remoto competitivo nem canal sem leilão. Portanto, gate CONTINUE; PHASE_04 fica QUEUED/NOT_STARTED.



## Atualização após Rodada 5 (S076–S086)
A auditoria encontrou evidência geral de busca e indicação, mas não conversão específica para pesquisa; alta concorrência em serviços operacionais. A análise pessoal de bloqueios de menoridade estava baseada em premissa incorreta: o usuário tem 18 anos. Reavaliar plataformas sob a idade correta; não exigir responsável adulto por menoridade. Investigar demonstração prática de competência sem presumir incapacidade por falta de histórico. Manter PHASE_03.1 em CONTINUE; PHASE_04 QUEUED/NOT_STARTED. Não abordar, publicar ou enviar proposta.


## Atualização após Rodada 7 (S101–S104)
A investigação de plataformas de tarefas para IA encontrou Prolific (Brasil elegível, porém waitlist e até 22 dias de aprovação) e Outlier (pagamento semanal, mas vaga PT-BR encontrada exigia coding expertise). Esses modelos não resolvem automaticamente a meta imediata. Manter PHASE_03.1 em CONTINUE; PHASE_04 QUEUED/NOT_STARTED. Nenhuma conta/candidatura ou contato foi realizado.


## Atualização do controlador — Rodada 8 (S105–S115)
A auditoria identificou divergências entre indexadores e status oficial: YPAI está fechada; OpenTrain não paga freelancers no Brasil; CSL tem um projeto anunciado com janela inicial já passada e possível futuro lote; Babel não confirma taxa/eligibilidade local e exclui explicitamente o Brasil em outra vaga; pesquisa Lionbridge exige dispositivo não Android. A vaga Fera está recente, mas sem remuneração/volume.
**Decisão:** CONTINUE_PHASE. A próxima ação é verificar oportunidade atual de novo lote CSL, condições de consentimento e pagamento, pagamento/volume Lionbridge e termos locais Babel; paralelamente, avaliar o escopo e remuneração da vaga Fera sem contatar o anunciante. Não iniciar Fase 04 nem realizar candidaturas/contatos sem aprovação.


## Atualização do controlador — Rodada 9 (S116–S119)
A pesquisa encontrou RWS Search Evaluator (até US$6/h, sem experiência prévia, mas inglês fluente e 5h/semana), TELUS (US$5/h estimados, inglês profissional e residência 3–5 anos), Welo Junior Quality Coordinator (20h/semana, inglês forte, remuneração não divulgada) e Clickworker (pagamento semanal, mas método e registro no Brasil variam por conta). A próxima decisão exige verificar inglês real, residência e disponibilidade do usuário, além de confirmar pagamento e carga. Não presumir esses requisitos. Manter CONTINUE_PHASE e PHASE_04 QUEUED/NOT_STARTED; nenhuma candidatura ou conta criada.

## Atualização do controlador — Rodada 10 (S120–S124)
OneForma Freya surge como hipótese mais promissora para tarefa remota PT-BR: US$6 por hora de áudio, sem experiência/diploma, lotes semanais e pagamento quinzenal por ciclo com mínimo US$25. O volume é variável, o trabalho é por hora de áudio e o locale/método Brasil precisa confirmação na conta. TSMG QC tem treinamento e pagamento por trabalho validado, mas sem taxa/ciclo público. YPAI tem status contraditório/fechado nas páginas oficiais.
**Decisão:** CONTINUE_PHASE. Próximo passo: aprofundar OneForma (método brasileiro, taxa confirmada no locale, qualificação, prazo de aprovação e produtividade de iniciante) e TSMG (taxa e pagamento). PHASE_04 continua QUEUED/NOT_STARTED. Nenhuma conta, candidatura, formulário ou contato foi realizado.

## Atualização do controlador — Rodada 11 (S125–S126)
A auditoria econômica reduziu a atratividade nominal do Freya: taxa PT-BR anunciada é US$6 por hora de áudio, mas referência Oxford indica pelo menos 4 horas de trabalho humano por hora gravada, cenário aproximado de US$1,50/h efetiva antes de custos. O mínimo US$25 exige cerca de 4h10 de áudio aprovado (~16h40 de trabalho na proporção 4:1). Além disso, páginas OneForma divergem quanto à elegibilidade PT-BR e exigência de experiência.
**Decisão:** CONTINUE_PHASE. Não considerar OneForma como renda de curto prazo validada. Próximo foco: confirmar o formulário PT-BR e taxa/requisitos, medir tempo em amostra prática somente se autorizado, e comparar TSMG QC/CSL/Fera/RWS com pagamentos e tempo efetivos. Nenhuma candidatura ou teste foi realizado.

## Atualização do controlador — Rodada 12 (S127–S129)
OneForma Email Collection está oficialmente aberta para Brasil/PT-BR e paga por email aprovado, sem experiência. Pode ser uma tarefa rápida se houver 3+ emails originais elegíveis por pedido. Entretanto, arquivos .eml preservam remetente, destinatário, assunto, corpo e timestamps; a página apenas afirma que a plataforma pode detectar/ocultar dados pessoais após upload, sem esclarecer suficientemente a proteção, uso e retenção do conteúdo. Classificar BLOQUEADA POR PRIVACIDADE até esclarecimento; não enviar dados. DataForce Mosaic não aceita PT-BR; TELUS Internet Safety Evaluator está fechado.
**Decisão:** CONTINUE_PHASE. Próxima rodada deve verificar taxa PT-BR, pagamento específico, consentimento, retenção e PII antes de qualquer uso; comparar com outras tarefas que não envolvam dados privados. PHASE_04 continua QUEUED/NOT_STARTED.

## Nota de pagamento OneForma — S130
A homepage afirma que não há mínimo de saque; o Help Center informa US$25. Não assumir nenhum dos dois para o projeto Email Collection/Freya até confirmação específica. Manter gate CONTINUE.

## Atualização do controlador — Rodada 13 (S131–S138)
A pesquisa encontrou uma rota complementar mais clara: UserTesting aceita contribuidores no Brasil, mas o pool local é menor; os pagamentos são variáveis, via PayPal, normalmente 14 dias após cada teste. Não atende como promessa de caixa até 06/12. A página YPAI Brasil tem banner de vaga encerrada apesar de rótulos antigos de candidatura aberta; prevalece o banner. TSMG confirma pagamento por trabalho validado, mas não publica taxa nem prazo. Meridial exige perfil linguístico especializado; Defrilex depende de consentimento para dados pessoais de uso digital sem publicar remuneração; sōtem não tem tarefas pagas abertas; estudo uTest encontrado expirou.
**Decisão:** CONTINUE_PHASE. Próxima rodada deve aprofundar UserTesting (requisitos brasileiros, frequência/valor, PayPal), buscar novos lotes CSL, esclarecer TSMG antes de qualquer trabalho e procurar vagas de coordenação operacional com remuneração transparente. Não iniciar Fase 04, não preencher cadastros, não fazer screening, não enviar documentos/dados, não consentir com coleta e não contatar empresas sem autorização.



## Atualização do controlador — correção UserTesting e rodada 14 (S139–S143)
A UserTesting inclui Brasil, mas a inscrição/practice test exige fluência em inglês, francês ou alemão; o usuário informa inglês intermediário, então a plataforma cai para baixa prioridade. uTest tem projetos PT-BR, porém o Greenbox encontrado iniciou em 30/10 e não foi confirmado como ativo; projeto de ID verification aparece ativo, mas exige escanear documento retido por até 12 meses e não divulga remuneração. Pagamentos uTest ocorrem duas vezes ao mês por PayPal/Payoneer/Wise conforme disponibilidade, sem garantia de volume.
**Decisão:** CONTINUE_PHASE. Próximo foco é localizar projetos uTest PT-BR com janela futura, pagamento e privacidade claros; continuar busca de lotes CSL, taxa/ciclo TSMG e oportunidades operacionais. Não iniciar Fase 04, não enviar documentos, dados bancários ou consentimentos.



## Preferência operacional do usuário — pesquisa consolidada (25/11/2026)
O usuário prefere que as pesquisas sejam executadas organicamente em fluxo contínuo, sem mensagens parciais após cada pequena busca. Planejar frentes, pesquisar, cruzar fontes, resolver contradições, comparar remuneração/risco/fit e atualizar a documentação primeiro; apresentar ao usuário um único relatório final organizado por rodada. Só interromper antes se houver decisão ou autorização necessária, risco urgente ou solicitação de acompanhamento. Não expor cadeia de pensamento privada; comunicar método resumido, evidências, fontes, incertezas e conclusões.


## Atualização do controlador — Rodada 15 (25/11/2026)
A auditoria continuou PHASE_03.1 e incluiu uma linha auxiliar de renda de curto prazo porque a meta imediata é receber R$150 até 06/12/2026. A Hub Data emergiu como candidata mais concreta entre as tarefas pesquisadas por ter taxa oficial por hora aprovada e Pix, mas a cessão de direitos audiovisuais, compatibilidade do aparelho, disponibilidade de tarefas e termos completos são gates. Não criar conta, gravar ou enviar consentimento sem aprovação. YPAI permanece fechada; CSL depende de novo lote; OneForma China e OpenTrain payout Brasil foram excluídos.
**Decisão:** CONTINUE_PHASE. A PHASE_03.1 original sobre compra/canais de inteligência comercial continua sem evidência suficiente para avançar à PHASE_04. A linha de renda imediata é auxiliar e não altera a escolha de negócio. Próximo passo: continuar procurando opções de recebimento rápido com payout verificável e baixa exposição de dados; completar auditoria de termos/compatibilidade Hub Data apenas se fontes públicas permitirem; manter canais de aquisição e compra específica de inteligência comercial como lacunas. Nenhuma ação externa realizada.


## Rodada 16 — decisão (25/11/2026)
O usuário rejeitou Hub Data por não querer registrar atividades domésticas para treinamento de IA. Status: REJECTED_BY_USER; não reconsiderar sem pedido explícito. A preferência continua sendo oportunidades online e conteúdo voluntário/original.
Pesquisa de manhua: leitura de capítulos de terceiros é fraca por reused content do YouTube e direitos autorais brasileiros; voz própria/IA não resolve. Não priorizar; reavaliar apenas em formato de crítica/análise original e uso autorizado de imagens.
Pesquisa macro: existe demanda digital, mas serviço genérico é concorrido. Cetic.br e Sebrae sugerem lacunas operacionais em WhatsApp, CRM, precificação, caixa e vendas; Upwork/Fiverr apontam crescimento de tarefas específicas, enquanto 99Freelas demonstra concorrência intensa em landing pages genéricas.
**Decisão:** CONTINUE_PHASE_03.1. Não avançar à PHASE_04 ainda. Próxima rodada deve aprofundar hipóteses operacionais e de pesquisa comercial, com exemplos atuais de projetos e validação de preço/escopo, sem microatualizações ao usuário. Reavaliar cada hipótese após duas rodadas sem evidência incremental; após cinco rodadas sem evidência de compra mais forte que anúncio/listagem, reestruturar o portfólio e considerar teste de venda supervisionado (com aprovação) ou mudança de estratégia, sem encerrar automaticamente todo o Kamikaze.


## Atualização PA-019 — auditoria e nova subfase (25/11/2026)
**Entrada do usuário:** investigar todos os públicos, desde que sejam segmentos com os quais ele possa aprender a lidar e executar; não assumir B2C ou B2B como escolha. Considerar diferença entre autoridade exigida por empresas, venda direta a pessoas físicas e recorrência em negócios pequenos. Exemplos de site/manutenção e pesquisa mensal são hipóteses, não decisões.

**Auditoria de PHASE_03.1_PURCHASE_EVIDENCE**
- RESPONDIDO: há compradores que pagam por pesquisa aplicada, coleta/comparação de preços, pesquisa de produtos, sites, cardápios digitais e manutenção; existem sinais de demanda em pessoas físicas/consumidores digitais e pequenos negócios.
- PARCIAL: canal de aquisição sem leilão; confiança/autoridade; recompra real; disposição a pagar por serviços recorrentes; adequação de entrega para iniciante.
- NÃO RESPONDIDO: comparação sistemática entre segmentos e economia de aquisição por segmento.
- Conclusão: não encerrar PHASE_03.1. Pausar dependência e criar PHASE_03.2 para preencher a dimensão do comprador. A nova fase pode retroalimentar 03.1.

**Novo critério transversal:** avaliar o caminho completo público → problema/gatilho → descoberta → confiança → compra → entrega → recompra/indicação. Separar demanda do problema, intenção de contratar, contratação concluída, recompra comprovada e canal acessível. Não converter estatística de uso em prova de compra de nosso serviço.

**Ação:** executar PHASE_03.2_BUYER_SEGMENTATION_AND_ACCESS. PHASE_04 continua bloqueada até a síntese das duas subfases e um gate explícito.



## Atualização — Rodada 19 / hipótese OPPORTUNITY_OVERSUPPLY_ECONOMY (26/11/2026)
A pesquisa S197–S214 examinou o excesso de candidatos/propostas como mercado de dois lados. Há produtos brasileiros de alertas, match, propostas e pipeline por R$14,90–R$49,90/mês; portanto, um radar genérico tem concorrência direta. No lado contratante, ATS PME começa em torno de R$49/mês, soluções para agências chegam a R$790/licença e há serviço gerenciado por vaga anunciado a R$598–747. Projetos 99Freelas mostram 319–538+ propostas em tarefas administrativas/recrutamento; um projeto de triagem tem vencedor identificado, mas sem valor pago divulgado.
**Decisão:** manter PHASE_03.2 IN_PROGRESS / CONTINUE. Não avançar PHASE_04. Não construir SaaS genérico nem oferecer triagem de RH com dados pessoais sem competência/controles. Próximo foco: descobrir recortes verticais subatendidos, validar canal por parcerias/referrals com agências, e investigar serviços de pesquisa/curadoria/organização que não envolvam dados sensíveis. Nenhum contato, cadastro, publicação ou proposta realizado.


## Atualização — Rodada 20 / PHASE_03.3 COMMUNITY-LED MARKET VALIDATION (26/11/2026)
A pedido do usuário, foi aberta a subfase de investigação PHASE_03.3 dentro da PHASE_03.2 para testar a ideia de aquisição por comunidades e a hipótese FREELANCER_CONVERSION_INTELLIGENCE. S215–S223 mostram concorrente direto brasileiro Scoutly a R$27,90/mês, substituto open-source Workaholic com agregação multi-plataforma/score/CRM, alertas nativos de Upwork/99Freelas, dor real mas relatos de canais variados, e uma vaga remunerada de community-led growth. Uma comunidade profissional (VagasUX) proíbe vendas, DMs não solicitadas e pesquisa fora de canais designados.
**Decisão:** não construir agregador genérico nem executar estratégia de história fabricada. O mercado de alertas/geração de proposta genérica já tem concorrência e alternativas grátis; saturação geral, vendas e retenção não comprovadas. Investigar uma lacuna vertical de decisão/curadoria com evidência de falhas dos produtos atuais. Aquisição por comunidade pode funcionar se transparente, contributiva e conforme regras. Nenhuma participação, publicação, mensagem, cadastro ou gasto foi realizada. PHASE_03.3 IN_PROGRESS / CONTINUE; PHASE_03.2 IN_PROGRESS / CONTINUE; PHASE_03.1 PAUSED / CONTINUE; PHASE_04 QUEUED / NOT_STARTED.


### Complemento de evidência — S224–S226
Freelance Match anuncia R$39,99/mês, mas informa que pagamentos ainda não estão ativos; FreelaSync anuncia R$14,90/49,90 sem prova pública de conversão; uma freelancer relata pagamento real de R$54,90 ao 99Freelas para consultar a média das propostas concorrentes (S224–S226). O caso sugere que informação competitiva tem valor para alguns profissionais, mas não prova disposição de pagar por produto externo. Próxima investigação deve aprofundar dados de compra de inteligência competitiva, reviews e necessidades não resolvidas.


## Atualização após Rodada 21 (26/11/2026)
A crítica “só uma pessoa??” foi interpretada como correção de padrão de evidência: um único relato não sustenta inferência comercial. S227–S244 ampliaram a amostra para mais de dez relatos públicos de compra/renovação/uso de planos e recursos em 99Freelas, Workana e Upwork. Isso confirma qualitativamente compra da categoria, mas não compra/retention de SaaS independente. Há sinais mistos de reembolso, cancelamento e frustração. S243 é brief de curadoria humana pago anunciado, porém exige histórico estabelecido e não é fit imediato.
**Decisão:** CONTINUE_PHASE na PHASE_03.3. Próxima ação é auditar falhas independentes de Scoutly/alternativas e mapear comunidades permitidas; PHASE_03.2 continua aberta, PHASE_03.1 pausada e PHASE_04 não iniciada.


## Decisão de controle — Rodada 22 + S286–S293 (26/11/2026)
**Gate:** CONTINUE na PHASE_03.3_COMMUNITY_LED_MARKET_VALIDATION. A pesquisa identificou concorrência e limites de termos que eliminam a ideia genérica de agregador/scraper. A nova hipótese Workana Profile Readiness tem dor documentada e sinais de compra de serviços de otimização de perfil em geral, mas a compra de ferramenta/serviço específico Workana ainda não foi comprovada. Manter pesquisa de buyer evidence e aquisição transparente. PHASE_04 continua QUEUED/NOT_STARTED. Não construir, publicar, contactar, cadastrar, anunciar ou gastar.


## Decisão de controle — Rodada 23 (26/11/2026)
**Gate:** CONTINUE na PHASE_03.3. Nova linha SIMPLE SEARCH UTILITIES / SEO MICROTOOLS adicionada ao portfolio por sugestão do usuário. Ferramentas simples encontradas via Google podem ser ativos SEO, mas volume e baixa concorrência ainda não foram provados. Métrica ponderada definida (demanda 25%, dificuldade orgânica 20%, qualidade SERP 15%, valor econômico 15%, repetição/cluster 10%, facilidade MVP/manutenção 10%, diferenciação/risco 5%); ND quando não há dado. S296–S314 mostram concorrentes em vários clusters, não volume. Próximo passo: medir 30–50 keywords por 5–8 famílias e auditar SERPs. Ferramenta SEO não é plano de receita até 06/12. PHASE_04 segue QUEUED/NOT_STARTED. Nenhum produto, publicação, contato, cadastro, anúncio, deploy ou gasto autorizado.



## Decisão de controle — Rodada 24 (26/11/2026)
**Gate:** CONTINUE na PHASE_03.3. A segmentação identificou VA/admin com demanda e alta concorrência, edição curta com sinais de recorrência e concorrência variável, design com barreira de portfólio e tradução incompatível com fit imediato. Workana Profile Readiness segue sem compra independente comprovada. Próximo: evidência de pagamentos/contratos e canais alternativos permitidos, priorizando microentregas admin e edição curta. PHASE_04 continua QUEUED/NOT_STARTED. Nenhuma ação externa ou gasto.


### Complemento de controle — comunidades (Rodada 24)
Mapeadas nove comunidades/canais (S327–S335). Nenhuma aprovada para divulgação: diretórios não substituem regras internas, e membros/online não comprovam audiência compradora. Próximo passo de validação é auditoria transparente das regras e canais permitidos, sem contato/publicação até autorização.


## Decisão de controle — Rodada 25 (26/11/2026)
A pedido explícito do usuário, ampliar o universo de pesquisa para “como ganhar dinheiro rápido na internet / como vender online / como conseguir a primeira venda em marketing digital”, sem abandonar a pesquisa de micro-nichos freelancer e aquisição por comunidades. Criada PHASE_03.4_BROAD_INTERNET_INCOME_AND_FIRST_SALE como linha paralela de validação ampla.
**Gate:** CONTINUE na PHASE_03.4 e manter PHASE_03.3 em CONTINUE. PHASE_04 permanece QUEUED/NOT_STARTED. Evidência atual favorece testar uma microentrega digital direta como hipótese de caixa, mas não há comprador confirmado; Prolific/Respondent e testes são complementos incertos; afiliados não são rota de caixa rápida comprovada sem distribuição. Nenhuma candidatura, cadastro, contato, publicação, venda ou gasto autorizado/realizado.
