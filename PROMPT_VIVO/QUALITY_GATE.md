# Quality Gate — Auditoria de qualidade e prontidão para decisão

Aplicar ao final de cada fase, antes da síntese e antes de decidir entre continuar pesquisando ou iniciar um experimento.

## A. Cobertura
- O objetivo da fase foi atendido?
- As perguntas críticas foram respondidas?
- Foram exploradas fontes e perspectivas diversas?
- Há áreas importantes ignoradas?

## B. Qualidade das fontes
- As fontes originais foram abertas quando possível?
- Datas e contexto estão claros?
- Há fontes independentes ou apenas cópias?
- Existem conflitos de interesse?
- A informação está atualizada o suficiente?

## C. Raciocínio
- Fatos estão separados de inferências e hipóteses?
- A conclusão excede a evidência?
- Há contraprovas?
- Foram consideradas explicações alternativas?
- Dados ausentes estão sendo tratados como desconhecidos, não como zero?

## D. Relevância
- O achado altera uma decisão ou responde a uma pergunta?
- Há detalhe suficiente para agir?
- Há conteúdo redundante que pode ser removido?
- O próximo passo está definido?

## E. Reprodutibilidade
- Outra IA consegue entender o que foi feito?
- Fontes, consultas importantes, datas e limitações estão registradas?
- O estado da execução foi atualizado?
- A continuidade pode ocorrer em outro chat?

## F. Prontidão para experimento

A pesquisa não deve continuar indefinidamente tentando provar algo que só o comportamento real de compradores pode responder. Avaliar:

1. **Comprador:** existe um segmento ou perfil de comprador identificável?
2. **Problema:** há evidência observável de uma dor, desejo ou tarefa relevante?
3. **Comportamento econômico:** há evidência de pagamento na categoria ou em solução adjacente? Distinguir isso de compra da oferta específica.
4. **Alternativas:** concorrentes e substitutos estão mapeados o suficiente para formular um diferencial testável?
5. **Canal:** existe ao menos um caminho legítimo e plausível para alcançar participantes?
6. **Entrega:** é possível demonstrar ou cumprir a promessa com capacidade e recursos disponíveis?
7. **Risco:** privacidade, termos, segurança, reputação e custos estão dentro de limites aceitáveis?
8. **Experimento:** existe uma hipótese clara, teste mínimo, métrica, critério de sucesso e critério de interrupção?

### Regra de parada da pesquisa
- Continuar pesquisando quando um fato externo não conhecido puder mudar a decisão, a segurança, a elegibilidade, o custo ou o desenho do teste.
- Parar a pesquisa de uma pergunta quando consultas adicionais repetirem evidência, não reduzirem incerteza decisiva ou tiverem baixo valor de informação.
- Quando a incerteza central for disposição a pagar, conversão, retenção ou comportamento real, reconhecer que pesquisa pública não substitui experimento.
- Se houver prontidão e o teste for barato, reversível, ético e autorizado, preferir o menor experimento capaz de responder à pergunta.
- Se o teste exigir contato, publicação, cadastro, despesa ou compromisso externo, obter autorização explícita antes de executá-lo.
- Não inventar uma probabilidade de sucesso como “60%” sem base histórica calibrada. Usar níveis de evidência, prontidão e risco; score heurístico não é probabilidade estatística.

### Cartão mínimo de experimento
Registrar:
- hipótese falsificável;
- comprador e contexto;
- oferta/entrega e preço, quando aplicável;
- canal e forma de recrutamento;
- amostra ou janela mínima justificada;
- métrica principal e sinais secundários;
- critério de sucesso e de interrupção;
- custo, risco e autorização necessária;
- resultado observado e limitações.

## G. Resultado do gate

Registrar:
- **PASS:** fase adequada para avançar.
- **PASS WITH GAPS:** pode avançar, mas lacunas precisam ser carregadas.
- **REWORK:** falha importante exige correção.
- **BLOCKED:** depende de acesso ou decisão humana.
- **READY_TO_TEST:** pesquisa suficiente para formular e executar experimento mínimo autorizado.
- **RESEARCH_MORE:** falta informação externa decisiva.
- **NOT_WORTH_TESTING:** evidência/risco/valor não justifica teste no contexto atual.

Nunca marcar PASS apenas para concluir mais rápido. Também não manter pesquisa aberta apenas para evitar a incerteza de testar.
