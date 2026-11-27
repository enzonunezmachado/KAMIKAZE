# Estado operacional — Kamikaze

**Atualizado:** 27/11/2026  
**Fonte canônica:** [state.toml](state.toml)

## Prioridade e próxima ação
- **Execução ativa:** `FIRST_SALE_PILOT` — gate `TEST` (`IN_PROGRESS`).
- **Frente prioritária:** `local_business_low_digital_presence`.
- **Próxima ação:** validar atividade recente e canais próprios dos três melhores candidatos do lote 001; se não houver evidência incremental, encerrar descoberta e rever a oferta. Não contatar.
- **Critério de sucesso:** encontrar candidatos únicos com baixa presença digital comprovada e uma necessidade plausível que caiba na nossa capacidade; separar fatos, inferências e desconhecidos.
- **Parada:** 20 candidatos triados ou duas rodadas sem evidência incremental. Não ampliar pesquisa por inércia.

## Frentes
- **Primeira Venda:** ACTIVE / TEST. A oferta de menu PDF + planilha por R$150 é apenas uma hipótese; adaptar somente após identificar necessidade real. Fonte: [README](FIRST_SALE/README.md).
- **Company Solutions:** RESEARCH-ONLY / NOT ACTIVATED. Usar os critérios mínimos de deduplicação/diagnóstico, sem ativar o sistema completo. Fonte: [README](COMPANY_SOLUTIONS/README.md).
- **Portfólio web:** secundário/manutenção. Não construir demonstração genérica antes de identificar comprador e problema. Fonte: [guia web](../web/README.md).

## Situação financeira e limites
- Meta histórica de curto prazo: receber R$150 até 08/12/2026; não há receita recebida.
- Orçamento autorizado: R$0.
- Contatos, propostas, clientes e vendas: nenhum confirmado nesta operação.
- Não contatar, publicar, cadastrar, gastar, contratar, fazer deploy ou assumir compromissos externos sem autorização específica.

## Pesquisa local — lote 001\n- Sete pistas exploratórias em HOLD: Ateliê Sônia Dantas, Ateliê da Tucca/Ateliê (R. Frutal), Chaveiro Pinheirinho, Assistência Técnica Refrigeração & Vendas, Ateliê Sra Costura, Ateliê de Costura Márcia e Chaveiro e Eletricista Cristiano.\n- Nenhuma está qualificada; faltam confirmação direta/recente de atividade, lacuna com impacto e validação do responsável. Nenhum contato foi feito.\n- Relatório: [lote 001](../research/2026-11-27-low-digital-presence-batch-001.md).\n\n## Execução de pesquisa anterior
- RUN_ID preservado: `PV-2026-11-25-TOTALMENTE-GRATUITA`.
- Fases 03.1–03.5: PAUSED / RESEARCH PARKED; PHASE_04: QUEUED / NOT_STARTED.
- A prioridade atual é a pesquisa comercial local definida em `[work]` no state.toml, não a retomada automática das fases antigas.

## Retomada
1. Ler `operations/state.toml` e seguir `work.primary_stream` / `work.next_action`.
2. Ler o README da frente indicada e sua fonte de estado/deduplicação.
3. Para a execução de pesquisa histórica, ler RUN_STATE e PHASE_CONTROL; não reabrir fases pausadas sem decisão explícita.
4. Atualizar state.toml somente quando prioridade, estado ou próxima ação mudar; não manter ponteiro de última entrega.
