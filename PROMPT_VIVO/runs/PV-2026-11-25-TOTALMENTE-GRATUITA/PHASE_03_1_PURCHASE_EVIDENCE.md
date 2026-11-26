# PHASE 03.1 — Evidência de compra e canais sem leilão

**Execução:** PV-2026-11-25-TOTALMENTE-GRATUITA  
**Data de abertura:** 2026-11-25  
**Estado:** IN_PROGRESS  
**Gate:** CONTINUE — primeira coleta relevante, ainda insuficiente.

## Por que esta subfase existe
A Fase 03 foi encerrada para transição por autorização do usuário, mas a auditoria posterior constatou que não havia prova suficiente de compra concluída para o serviço de pesquisa, nem validação de comprador estreito, canal de aquisição ou recorrência. Como esses pontos podem alterar a decisão de negócio, não é correto avançar diretamente para teste de viabilidade como se a validação estivesse completa.

## Perguntas desta subfase
1. Encontramos ao menos um pedido de pesquisa de mercado com status concluído e freelancer vencedor?
2. Há evidência de vendas concluídas/reviews em serviços comparáveis, distinguindo categoria geral de serviço específico?
3. Quais preços são apenas anúncios e quais são transações/contratações concluídas?
4. Os pedidos exigem pesquisa pública ou coleta de dados pessoais/contato direto?
5. Que canais evitam leilões com dezenas de freelancers, sem recorrer a spam?
6. Existe sinal de demanda recorrente, e não apenas pedidos pontuais?
7. Qual é a menor oferta com escopo claro e risco de entrega controlado?

## Achados iniciais desta subfase
- Uma página de projeto 99Freelas para estudo de mercado de potenciais clientes de curso de inglês (publicado em 31/08/2026) aparece como Concluído e identifica freelancer vencedor. Orçamento aberto com valor mínimo de R$60, cinco propostas e sete interessados. É evidência mais forte de contratação concluída do que anúncios de serviço, embora não revele o valor final pago nem prove que o escopo foi entregue sem disputa posterior (S058).
- O projeto exigia 50 contatos pessoais/WhatsApp de potenciais clientes. Isso não deve ser copiado como oferta padrão: envolve dados pessoais e qualificação de pessoas, com risco de privacidade, base legal e precisão. A oportunidade mais segura pode estar em pesquisa de empresas/dados corporativos públicos, não em listas de indivíduos.
- VintePila mostra uma categoria com 50 serviços e alguns depoimentos de compradores da categoria, mas os depoimentos exibidos não identificam necessariamente compras de pesquisa de mercado. Não usar a avaliação geral da categoria como prova específica (S056).
- Dois serviços específicos de análise de concorrentes anunciam R$30–R$80 e R$100–R$200, mas exibem sem avaliações ainda; portanto, preço ofertado, não venda comprovada (S057, S059).
- A própria VintePila documenta reputação baseada em serviços concluídos, avaliações e métricas de entrega; a plataforma declara receita líquida de 80% para vendedor nos níveis descritos. Isso é dado da plataforma e deve ser confirmado nos termos vigentes antes de usar em economia unitária (S060).
- Não há ainda evidência de assinatura/recorrência para pequenos negócios brasileiros que paguem por monitoramento competitivo; software pago existente comprova oferta de ferramentas, não demanda do segmento-alvo (S055, S061).

## Contraprovas e limites
- Um projeto concluído é uma evidência de compra, mas um caso isolado não mede tamanho de mercado nem repetição.
- A categoria tem muitos anúncios, mas anúncios sem avaliações não comprovam procura.
- Serviços de pesquisa podem ser vendidos por preço muito baixo, pressionando margem e confiança.
- Plataformas de propostas continuam fora da estratégia preferida do usuário.
- Não há autorização para publicar anúncio, enviar proposta, contatar compradores ou entrevistar pessoas.

## Próximas tarefas
1. Investigar pedidos concluídos adicionais com vencedor e orçamento/valor final, preferencialmente escopos de análise competitiva, pesquisa de produto e inteligência comercial.
2. Verificar se existe evidência específica de reviews/vendas para serviços comparáveis, não apenas avaliações da categoria.
3. Buscar sinais de aquisição por indicação, parceria, conteúdo demonstrativo e demanda inbound; estimar esforço sem executar contato.
4. Separar serviços de pesquisa pública de atividades de coleta de dados pessoais ou cliente oculto.
5. Avaliar se a recorrência é uma necessidade do cliente ou apenas uma hipótese sugerida pelo fornecedor.
6. Atualizar a matriz e decidir se a subfase pode ser encerrada ou precisa de 3.2.

## Critério de saída
PASS: múltiplas evidências independentes de compra/contratação comparável e canal plausível; recorrência classificada honestamente.
PASS WITH GAPS: evidência limitada, mas suficiente para desenhar um teste pequeno e seguro.
CONTINUE: lacunas críticas ainda pesquisáveis.
FAIL: demanda/compras insuficientes ou economics incompatíveis.
BLOCKED: dados necessários não estão publicamente disponíveis ou dependem de autorização.



## Rodada 5 — canais, barreira de entrada e elegibilidade (25/11/2026)
**Fontes:** S076–S086; detalhes completos no SOURCE_LEDGER.md e FINDINGS.md.
- Google B2B indica busca (65%) e networking (61%) entre MEIs, mas jornada média de compra de cerca de dois meses; não atende como garantia à meta imediata.
- Survey exploratória de freelancers em SP aponta indicação (46,6%), plataformas (33,8%) e redes sociais (19,6%); amostra de 96 respostas, concentrada em Vila Mariana/Pinheiros. Portfólio e avaliações influenciam confiança.
- Sebrae aponta operação digital concentrada em uma pessoa e rotinas de catálogo/indicadores; porém, serviços de cadastro de catálogo têm 132–181 propostas em exemplos recentes, mostrando competição extrema.
- IA genérica em conteúdo já é comum; tarefas simples podem estar comoditizadas.
- Nota histórica de elegibilidade: as fontes S081–S084 registram regras gerais para menores, mas a conclusão de bloqueio pessoal está superada. O usuário tem **18 anos**; reavaliar Workana/Upwork/Fiverr sob os termos atuais e não aplicar restrições de menoridade.
- O melhor caminho de confiança sem leilão é, em tese, indicação + demonstração pública transparente + escopo pequeno; ainda não existe prova de conversão para o serviço pesquisado.
**Gate:** CONTINUE. Necessário investigar rota legal de recebimento, responsável adulto, parcerias supervisionadas e demonstração de competência. PHASE_04 permanece QUEUED/NOT_STARTED. Nenhuma ação externa.
\n\n## Correção de perfil do operador — 25/11/2026\nO usuário tem **18 anos**, não 16. Informações gerais sobre termos de plataformas e legislação permanecem como fontes, mas conclusões que tratavam o usuário como menor estão superadas. O usuário afirma ter capacidade e disposição para aprender e desempenhar o necessário. Avaliar oportunidades por tarefas e requisitos concretos, sem presumir incapacidade por ausência de experiência profissional. Manter transparência sobre histórico e credenciais.

## Rodada 8 — status operacional e pagamento Brasil (S105–S115)
YPAI Data/Voice: vaga fechada nas páginas oficiais, apesar de resultados de busca desatualizados (S105). CSL: projeto de conversa R$200 por participante, mas prioridade inicial 7–8/11/2026 já passou; possível lote futuro, sem garantia; confirmar autorização, finalidade, uso/retenção da voz e prazo de pagamento (S106–S107). OpenTrain: pagamento a freelancers no Brasil indisponível, logo excluir suas vagas anunciadas de alta remuneração (S108–S111). Babel: Conversation Partner anuncia pagamento semanal, mas taxa US$17,50 é EUA/Canadá e a taxa/elegibilidade no Brasil não estão confirmadas; Voice Actor exclui residentes no Brasil (S112–S113). Lionbridge survey US$10 exige smartphone não Android, incompatível; áudio PT-BR US$10/h permanece sem volume/calendário (S114). Fera: vaga recente de coordenação de conteúdo, PJ, mensal fixo sem valor divulgado, disponibilidade sob demanda e contato com clientes (S115). Gate CONTINUE; nenhuma ação externa.

## Rodada 12 — OneForma Email Collection e bloqueio de privacidade (S127–S129)
OneForma Online Shopping Email Collection está aberta para Brasil/PT-BR, sem experiência e paga por email aprovado; exige 3+ mensagens .eml originais do mesmo pedido de produto físico entregue desde 2024. Valor por email no Brasil não publicado. Os arquivos precisam manter remetente, destinatário, assunto, corpo e timestamp originais. A plataforma diz que pode detectar/ocultar dados pessoais após upload, mas não esclarece suficientemente proteção, acesso, uso e retenção do conteúdo. Classificar BLOQUEADA POR PRIVACIDADE; não enviar nenhum email. DataForce Mosaic não aceita PT-BR; TELUS Internet Safety Evaluator está fechado. Gate CONTINUE.
