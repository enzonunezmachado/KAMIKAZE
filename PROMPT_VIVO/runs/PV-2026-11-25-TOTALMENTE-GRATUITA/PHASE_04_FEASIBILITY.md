# PHASE 04 — Viabilidade operacional e econômica

**Execução:** PV-2026-11-25-TOTALMENTE-GRATUITA  
**Início:** 2026-11-25  
**Estado:** IN_PROGRESS  
**Gate inicial:** não avaliado.

## Pergunta central
Uma ou mais hipóteses sobreviventes podem ser entregues com qualidade, segurança, custo monetário inicial zero, ferramentas acessíveis e economia unitária plausível — sem construir software prematuramente?

## Hipóteses sob avaliação
A. **Serviço de inteligência comercial delimitada:** pesquisa de mercado/concorrentes para responder uma pergunta concreta de negócio, com fontes, datas, comparações, limites e recomendação.
B. **Produto recorrente assistido por IA:** monitoramento de mudanças competitivas e relatórios periódicos, inicialmente operado manualmente como concierge; não construir plataforma ainda.
C. **Comparador secundário:** planilhas padronizadas e rápidas, apenas se houver distribuição e pagamento claros; não competir em leilões de propostas nem produzir amostras não pagas.

## Princípios
- Capital autorizado: R$0. Nenhum trial que converta automaticamente, cartão cadastrado, API paga, anúncio ou assinatura.
- A fase deve separar viabilidade técnica, operacional, comercial e econômica. Uma hipótese pode ser tecnicamente possível e comercialmente inviável.
- Ferramentas com cotas opacas não podem ser dependência crítica. Toda etapa crítica precisa de fallback manual.
- Nenhuma promessa de pesquisa literalmente infinita. Definir universo, fontes, frequência, limites e data de atualização.
- Não coletar dados privados, burlar paywalls, violar termos ou fazer scraping proibido.
- IA auxilia descoberta e síntese; toda afirmação material precisa de fonte verificável e revisão humana.
- Não enviar mensagens, propostas, publicar demonstrações ou abordar leads sem aprovação humana.
- Não construir software antes de validar uso repetido e pagamento.

## Plano de trabalho
1. Mapear o fluxo ponta a ponta de um estudo de inteligência comercial, do briefing à entrega.
2. Definir escopo mínimo que produza decisão útil sem prometer estudo profissional abrangente.
3. Identificar fontes públicas estáveis por tipo de sinal e limites de cobertura.
4. Desenhar fluxo de coleta, registro, verificação, síntese e revisão.
5. Fazer teste interno com um caso público e medir tempo, erros, retrabalho e rastreabilidade; não usar como case comercial sem autorização.
6. Estimar capacidade por semana, preço mínimo, custos variáveis e taxas de pagamento — separar fatos confirmados de estimativas.
7. Avaliar a recorrência: o que muda, com qual frequência, qual ação o cliente toma e por que não basta uma checagem mensal/manual.
8. Comparar serviço pontual, concierge recorrente e planilhas rápidas.
9. Definir critérios de parar, simplificar, pivotar ou seguir para um piloto.

## Entregáveis
- PHASE_04_FEASIBILITY_CHECKPOINT.md
- DELIVERY_WORKFLOW.md
- UNIT_ECONOMICS.md
- TOOL_STACK_AUDIT.md
- atualizar VALIDATION_MATRIX.md, RUN_STATE.md, RESEARCH_PLAN.md e MEMORY_HANDOFF.md.

## Critérios de saída
PASS: existe fluxo testado, fontes verificáveis, capacidade mensurada, custo inicial zero e economia plausível; incertezas comerciais explicitadas.
PASS WITH GAPS: execução parece possível, mas persistem incertezas que podem ser testadas em piloto controlado.
FAIL: dependência paga, coleta instável/ilegítima, qualidade insuficiente, esforço incompatível ou economia unitária inviável.

## Restrições de interpretação
PASS nesta fase não significa demanda ou vendas comprovadas. Se a viabilidade técnica for aprovada e a disposição a pagar continuar desconhecida, recomendar piloto apenas após aprovação humana, sem registrar receita antecipada.
