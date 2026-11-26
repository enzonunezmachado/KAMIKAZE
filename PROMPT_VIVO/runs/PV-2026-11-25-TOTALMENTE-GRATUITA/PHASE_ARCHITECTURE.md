# Arquitetura de fases — PV-2026-11-25-TOTALMENTE-GRATUITA

## Princípio
A arquitetura é dinâmica. PHASE_00–PHASE_05 são referências iniciais, não sequência obrigatória nem limite de fases. Consultar PROMPT_VIVO/EXECUTION_PROTOCOL.md e PHASE_CONTROL.md.

## Histórico
- **v1.0 — 25/11/2026:** arquitetura inicial PHASE_00–PHASE_05.
- **v2.0 — 25/11/2026:** governança adaptativa; permitir dividir, mesclar, reordenar, modificar, adicionar, pular e reabrir fases, preservando histórico.
- **v3.0 / PA-003:** PHASE_02 encerrada com PASS WITH GAPS por autorização do usuário; lacunas transferidas.
- **v4.0 / PA-004:** PHASE_03 encerrada para transição com PASS WITH GAPS; Fase 04 planejada, sem teste operacional.
- **v5.0 / PA-005:** auditoria encontrou lacunas críticas em compra, comprador, canal e recorrência; abriu PHASE_03.1. Fase 04 voltou a QUEUED/NOT_STARTED.
- **v6.0 / PA-006:** criados BOOTSTRAP.md, RESUME_PACKET.md e USER_INPUT_LOG.md para retomada entre chats e incorporação de feedback. Corrigida divergência em que Fase 04 aparecia como em andamento.

## Estado atual
| Fase | Estado | Gate |
|---|---|---|
| PHASE_00_SCOPE | Concluída | PASS WITH GAPS |
| PHASE_01_LANDSCAPE | Concluída | PASS WITH GAPS |
| PHASE_02_DEMAND | Encerrada para transição | PASS WITH GAPS |
| PHASE_03_VALIDATION | Encerrada para transição | PASS WITH GAPS; sem compra/recorrência comprovada |
| PHASE_03.1_PURCHASE_EVIDENCE | IN_PROGRESS | CONTINUE |
| PHASE_04_FEASIBILITY | QUEUED / NOT_STARTED | Nenhum teste operacional executado |
| PHASE_05_SYNTHESIS | Planejada/adaptável | Reavaliar |

## PA-007 — Segunda rodada de evidência em PHASE_03.1
**Data:** 25/11/2026.  
**Motivo:** aprofundar compra concluída, intenção de recorrência e demanda por monitoramento competitivo.

**Fontes novas:** S062–S066.
- S062: pedido Workana com intenção de repetir pesquisa de preços a cada 3–4 meses; comprador com 76 projetos pagos, mas pedido específico aberto.
- S063: pedido de análise competitiva documentada; comprador sem histórico de pagamentos.
- S064: 99Freelas, pesquisa de preços/estoque em pontos de venda, concluído parcialmente e com vencedor; trabalho de campo.
- S065: oferta VintePila de pesquisa/validação com zero vendas visíveis.
- S066: pedido Workana para SaaS de monitoramento de anúncios com IA, orçamento R$500–R$1.000; aberto, sem prova de contratação/assinantes.

**Decisão:** CONTINUE PHASE_03.1. Evidência melhorou para procura e necessidade recorrente declarada, mas não comprova venda repetida de relatório remoto competitivo, assinatura recorrente ou canal sem leilão. Fase 04 continua QUEUED/NOT_STARTED.

## Regra de atualização
Toda mudança futura deve registrar motivo, arquivos afetados, dependências e impacto; sincronizar RUN_STATE, RESEARCH_PLAN, MEMORY_HANDOFF, RESUME_PACKET, USER_INPUT_LOG e operations/STATE. Não apagar histórico.

## PA-008 — Terceira rodada: canais de aquisição e urgência
**Data:** 25/11/2026. **Fontes:** S067–S070.
- S067 mostra parceiros/pares e conversas setoriais como fontes de informação para PMEs, além de uso de consultoria.
- S068 reforça WhatsApp como canal operacional dominante em serviços, mas não prova aquisição nem autoriza mensagens não solicitadas.
- S069 documenta networking, rodadas e agentes B2B no programa subsidiado Move+ do Sebrae.
- S070 oferece referência de escopo profissional de pesquisa, sem comparação direta de preço.
**Decisão:** CONTINUE PHASE_03.1. Canais gerais de confiança são plausíveis; canal específico para vender benchmarking ainda não foi demonstrado. Fase 04 continua QUEUED/NOT_STARTED.

## PA-009 — Quarta rodada: contratação concluída e pesquisa recorrente
**Data:** 25/11/2026. **Fontes:** S071–S075.
- S071: pesquisa de preços de catálogo com 44 vinhos, concluída e vencedora identificada; concorrência alta.
- S072: pricing estratégico de 6–8 SKUs, concluído e vencedor; requer especialização, NDA e tratamento cuidadoso de tributação.
- S073: cliente espião mensal, histórico de pagamento do comprador e recorrência declarada; status contraditório, não contar como concluído.
- S074: curadoria de fornecedores/produtos para e-commerce, concluída; continuidade apenas potencial.
- S075: pesquisa de tendências três vezes por semana, concluída; duração e renovação não conhecidas.
**Decisão:** CONTINUE PHASE_03.1. Compra de pesquisa aplicada a decisões/rotinas está bem demonstrada, mas canais sem leilão, recompra e adequação de habilidade ainda faltam. PHASE_04 permanece QUEUED/NOT_STARTED.



## PA-010 — Quinta rodada: canal, capacidade de iniciante e elegibilidade
**Data:** 25/11/2026. **Fontes:** S076–S086.
- Google e survey local indicam busca/networking/indicação como caminhos gerais, mas não comprovam conversão para pesquisa competitiva; jornada de compra B2B pode levar ~2 meses.
- Tarefas operacionais de e-commerce têm demanda aparente, mas pedidos recentes exibem 132–181 propostas e exigem prática; conteúdo genérico com IA está comoditizado.
- Workana e Upwork exigem 18 anos; Fiverr permite menor somente via conta de responsável e supervisão. Brasil: 16–17 relativamente incapaz para certos atos; MEI 16–18 requer emancipação. Elegibilidade/recebimento requerem rota legal e adulto responsável quando aplicável.
**Decisão:** CONTINUE PHASE_03.1. Abrir perguntas específicas sobre rota legal de recebimento, parceria supervisionada, canais de confiança e demonstração de competência. PHASE_04 continua QUEUED/NOT_STARTED.


## PA-011 — correção de idade e ampliação da investigação para trabalho de bastidores
**Data:** 25/11/2026  
**Motivo:** o usuário corrigiu a idade atual para 18 anos (não 16) e esclareceu que possui capacidade/disposição para aprender e desempenhar o necessário; a ausência de experiência profissional não deve ser tratada como incapacidade.

**Mudanças:**
- Invalidar como restrição pessoal as conclusões da rodada 5 baseadas em menoridade.
- Manter fontes S081–S084 como referências históricas/gerais, mas reavaliar elegibilidade pessoal com 18 anos.
- Adicionar S087–S100 sobre elegibilidade, pagamentos, tarefas documentais, trabalho operacional de agência, white-label e tarefas de áudio para IA.
- Ampliar a comparação para duas trilhas: apoio operacional/orquestração de conteúdo e tarefas pontuais de dados/voz para IA.
- Manter PHASE_03.1 em CONTINUE; nenhuma oportunidade aprovada, candidatura ou contato realizado.
- Sincronizar RUN_STATE, RESEARCH_PLAN, MEMORY_HANDOFF, RESUME_PACKET, USER_INPUT_LOG, checkpoint, FINDINGS, SOURCE_LEDGER, OPEN_QUESTIONS, VALIDATION_MATRIX e operations/STATE.

**Impacto no gate:** nenhuma fase é encerrada. PHASE_04 permanece QUEUED/NOT_STARTED.


## PA-012 — plataformas de microtarefas e avaliação de IA
**Data:** 25/11/2026  
**Motivo:** ampliar a comparação de renda de entrada com projetos de voz, microestudos e avaliação de IA, distinguindo disponibilidade de conta, alocação de tarefas e pagamento.
**Fontes:** S101–S104.
- Prolific aceita residentes no Brasil com mais de 18 anos, mas usa waitlist e estudos podem levar até 22 dias para aprovação.
- Outlier tem pagamento semanal, mas a vaga localizada para português brasileiro exigia conhecimento de programação.
**Decisão:** manter PHASE_03.1 em CONTINUE. Nenhuma plataforma garante acesso/receita imediata; não criar conta ou candidatura sem decisão do usuário.


## PA-013 — validação de disponibilidade e meios de pagamento no Brasil
**Data:** 25/11/2026  
**Motivo:** resultados de busca mostraram vagas de IA com taxas atraentes, mas status e pagamentos precisavam de confirmação nas páginas oficiais.
**Mudanças:**
- YPAI Data/Voice: páginas abertas oficialmente indicam vaga fechada, apesar de snippets/indexadores dizerem “Applications open”.
- CSL: projeto de R$200 por participante tem janela inicial passada (7–8/11), com possibilidade de futuros lotes; adicionada análise de consentimento e pagamento.
- OpenTrain: pagamentos a freelancers no Brasil indisponíveis; bloqueia a plataforma independentemente das taxas dos anúncios.
- Babel: separar taxa EUA/Canadá de taxa potencial no Brasil; uma vaga de voice actor exclui residentes no Brasil.
- Lionbridge: survey de US$10 exige smartphone não Android; incompatível com dispositivo conhecido.
- Fera: vaga recente atualizada como oportunidade de coordenação com remuneração/volume não divulgados.
**Decisão:** manter PHASE_03.1 em CONTINUE; nenhuma fase encerrada e nenhum contato/candidatura. PHASE_04 permanece QUEUED/NOT_STARTED.


## PA-014 — plataformas de avaliação e coordenação de qualidade
**Data:** 25/11/2026  
**Motivo:** investigar oportunidades remotas com instruções, critérios de qualidade e pagamento por tarefa, incluindo trabalho de avaliador e suporte de coordenação.
**Fontes:** S116–S119.
- RWS Search Evaluator: até US$6/h, Brasil, sem experiência obrigatória, mas inglês fluente e mínimo de horas; PayPal/banco, ciclo não confirmado.
- TELUS: cerca de US$5/h estimados, mas inglês profissional, residência de 3–5 anos e pagamento variável por tarefa.
- Clickworker: pagamentos semanais e mínimos publicados, mas disponibilidade de método/registro no Brasil é individual.
- Welo Junior Quality Coordinator: coordenação de QA 20h/semana, inglês forte, dedicação exclusiva e remuneração não divulgada.
**Decisão:** manter PHASE_03.1 em CONTINUE. Não iniciar candidatura nem assumir inglês, elegibilidade ou recebimento sem confirmação.

## PA-015 — validação de transcrição PT-BR e QC de áudio
**Data:** 25/11/2026  
**Motivo:** encontrar trabalho remoto em português nativo com tarefa delimitada, baixa exigência de experiência e pagamento verificável no Brasil.
**Fontes:** S120–S124.
- OneForma Freya lista PT-BR aberto, US$6 por hora de áudio, sem experiência/diploma; batches semanais first-come-first-served; pagamento duas vezes ao mês, mínimo US$25, PayPal/Payoneer conforme conta.
- TSMG QC Specialist oferece revisão de transcrições com treinamento, pagamento por trabalho validado, mas taxa/ciclo desconhecidos.
- YPAI tem discrepância entre resultados de busca e páginas oficiais abertas; vagas remotas brasileiras não devem ser contadas como ativas sem confirmação.
**Decisão:** manter PHASE_03.1 CONTINUE; aprofundar taxa/locale, saque Brasil, tempo de qualificação e produtividade real OneForma; não iniciar candidatura sem autorização.

## PA-016 — auditoria de remuneração efetiva e elegibilidade OneForma
**Data:** 25/11/2026  
**Motivo:** a taxa de US$6 por hora de áudio não equivale à hora trabalhada e as páginas OneForma divergem sobre países/requisitos.
**Fontes:** S125–S126.
- Oxford estima mínimo de 4h de trabalho humano por 1h de áudio claro; no cenário Freya de US$6/h de áudio, isso equivale a ~US$1,50/h efetiva antes de custos.
- O mínimo de US$25 exige ~4h10 de áudio aprovado, aproximadamente 16h40 de trabalho no cenário 4:1.
- Freya v2 lista PT-BR e ausência de experiência obrigatória, mas página de projeto de transcrição exige experiência e lista apenas cinco países; página pt_BR abriu conteúdo inconsistente.
**Decisão:** manter CONTINUE; não aprovar Freya como renda imediata até confirmar elegibilidade e produtividade.

## PA-017 — microtarefas de coleta de emails e proteção de dados pessoais
**Data:** 25/11/2026  
**Motivo:** surgiu projeto OneForma aberto no Brasil com pagamento por email aprovado, mas envolve arquivos .eml originais com dados pessoais.
**Fontes:** S127–S129.
- OneForma Email Collection aceita Brasil/PT-BR, sem experiência, 18+, paga por email aprovado; exige 3+ emails originais do mesmo pedido de produto físico entregue.
- Valor por email PT-BR não publicado. Pagamento do projeto não explicitamente confirmado sob calendário geral.
- Arquivos originais mantêm remetente/destinatário/assunto/corpo/data; a plataforma apenas diz que pode ocultar dados pessoais no upload. Retenção/uso/mascaramento específicos não estão claros.
- DataForce Mosaic não aceita PT-BR nos idiomas listados; TELUS Internet Safety Evaluator está fechado.
**Decisão:** manter CONTINUE; tratar a hipótese de emails como BLOQUEADA POR PRIVACIDADE até esclarecer masking, acesso, uso e retenção. Não enviar emails, anexos ou dados.


- **PA-018 — 25/11/2026:** acrescentada linha auxiliar de investigação de renda imediata por tarefas remuneradas/AI data collection, sem alterar o objetivo central nem promover essas plataformas a negócio Kamikaze. Motivo: missão imediata de R$150 até 06/12 e as rodadas 13–15 já estavam investigando esse tipo de canal. Dependências: payout verificável, elegibilidade Brasil, disponibilidade real, prazo de aprovação, privacidade e capacidade. PHASE_03.1 continua ativa; PHASE_04 não inicia por causa desta linha auxiliar. Entregáveis: S144–S153, findings e perguntas abertas.


## PA-019 — criação da PHASE_03.2_BUYER_SEGMENTATION_AND_ACCESS (25/11/2026)
**Motivo:** o usuário pediu revisão de fase e ampliação explícita da pesquisa para todos os públicos que possam ser atendidos com capacidade aprendida: pessoas físicas, profissionais independentes, microempreendedores/pequenos negócios e empresas estruturadas. A pesquisa anterior analisava sobretudo o que vender, sem segmentar adequadamente quem compra, barreira de confiança, capacidade de pagamento, canal e adequação de iniciante.

**Auditoria da PHASE_03.1:** S056–S075 comprovam compras pontuais e alguns sinais de recorrência pretendida em pesquisa comercial, mas não demonstram recompra efetiva nem canal de aquisição previsível sem marketplace. S157–S174 e S175–S185 ampliam sinais macro e exemplos de contratação, mas não fecham a questão do comprador acessível. Portanto, PHASE_03.1 não passa; fica PAUSED/DEPENDENCY enquanto a subfase de segmentação produz a camada ausente.

**Nova subfase:** PHASE_03.2_BUYER_SEGMENTATION_AND_ACCESS — IN_PROGRESS / CONTINUE.
Escopo: comparar B2C, profissionais independentes, micro/pequenos negócios e empresas estruturadas; identificar problemas, gatilhos, capacidade/disposição de pagamento, confiança/autoridade, canais de aquisição, competição, ticket, recorrência e acessibilidade operacional. Considerar serviços, produtos digitais, conteúdo, ferramentas e modelos híbridos; não pré-selecionar pesquisa de mercado ou criação de sites.

**Regra:** "todos os públicos" significa investigar todos os segmentos, não tentar vender tudo a todos ao mesmo tempo. A seleção posterior será baseada em evidência e no melhor caminho de execução, não em preferência prévia.

**Decisão de fase:** PHASE_04_FEASIBILITY permanece QUEUED/NOT_STARTED. Nenhum negócio, nicho ou oferta aprovado; nenhuma ação externa autorizada.


## PA-020 — Rodada 18: profissionais independentes e comprador intermediário
**Data:** 25/11/2026. **Fontes:** S186–S196.
- Briefs de assistente virtual e apoio operacional demonstram demanda, mas concorrência extrema em marketplace.
- Agências aparecem como compradoras intermediárias de execução/organização, com possibilidade de fee mensal; escopos exigem ferramentas, comunicação, prazos e às vezes formalização.
- PMEs não devem ser tratadas como compradoras fáceis: pesquisa Serasa indica cautela na expansão de equipe e baixa intenção de contratação flexível.
- Confiança e prova são transversais; porte maior formaliza mais o processo.
**Decisão:** manter PHASE_03.2 CONTINUE. Investigar canais não leilão e microentregas operacionais demonstráveis; não aprovar agência/segmento sem evidência de aquisição e margem.


## Atualização PA-020 — PHASE_03.3 e Rodada 21 (26/11/2026)
- PHASE_03.3_COMMUNITY_LED_MARKET_VALIDATION foi criada como subfase da PHASE_03.2; continua IN_PROGRESS / CONTINUE.
- PHASE_03.2 permanece IN_PROGRESS / CONTINUE; PHASE_03.1 está PAUSED / CONTINUE; PHASE_04 está QUEUED / NOT_STARTED.
- Rodada 21 ampliou evidência de compra de recursos/plataformas para freelancers (S227–S244), mas não provou compra/retention de SaaS independente.
- Nenhuma alteração no CORE, protocolo central ou salvaguardas.
