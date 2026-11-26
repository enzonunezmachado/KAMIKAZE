# Método de Ranking e Seleção — versão 1.0

## Objetivo
Comparar 20 empresas com critérios consistentes e selecionar aquelas que combinam chance plausível de contratação, valor empresarial, viabilidade de entrega e risco aceitável.

**Os scores são heurísticas de priorização, não probabilidades estatísticas.** Não escrever "86% de chance de fechar" quando o score é 86/100.

## Gate zero — elegibilidade
Antes da pontuação, verificar:
- empresa e identidade suficientemente confirmadas;
- atividade atual razoavelmente confirmada;
- não está em lista de supressão;
- não é duplicata;
- oportunidade pode ser investigada por fontes permitidas;
- nenhuma restrição evidente torna contato/proposta inadequados.

Se falhar, marcar HOLD ou DISQUALIFIED e explicar. Não forçar score.

## Score A — Conversion Fit (0–100)
| Critério | Peso | Pergunta |
|---|---:|---|
| Dor/oportunidade observável | 25 | Há evidência pública concreta de uma lacuna? |
| Benefício empresarial compreensível | 20 | A solução pode economizar tempo, reduzir perdas, organizar operação ou melhorar experiência? |
| Adequação da solução | 15 | A proposta é específica e não redundante? |
| Sinais de prioridade/trigger | 10 | Há evidência recente de mudança, reclamação recorrente ou necessidade ativa? |
| Acesso ao decisor/canal apropriado | 10 | Existe canal empresarial legítimo e caminho para pedir permissão? |
| Capacidade aparente de adoção | 10 | A empresa possui processo/equipe/canal que permita usar a solução? |
| Credibilidade e timing | 10 | Podemos demonstrar competência e apresentar no momento/contexto adequado? |

## Score B — Business Value Fit (0–100)
| Critério | Peso |
|---|---:|
| Impacto operacional/econômico plausível | 25 |
| Valor percebido e clareza do retorno | 20 |
| Potencial de recorrência legítima | 15 |
| Reutilização de componentes sem customização excessiva | 10 |
| Capacidade de pagamento inferida com evidência não invasiva | 10 |
| Baixo custo e tempo de entrega | 10 |
| Potencial de case autorizado e aprendizado | 10 |

O potencial de pagamento é apenas hipótese e nunca deve ser inferido de dados pessoais, aparência, endereço residencial ou atributos sensíveis.

## Evidência e confiança
Cada critério recebe nota de 0–5 e uma justificativa curta. Anexar URL/fonte, data de acesso e o trecho/observação que sustenta a avaliação. Classificar confiança:
- HIGH: fontes oficiais/primárias e evidência direta, recente e coerente.
- MEDIUM: múltiplos sinais independentes, mas parte inferencial.
- LOW: informação escassa, antiga, conflitante ou baseada em uma única fonte.
- UNKNOWN: não foi possível verificar.

Registrar também contraevidência e soluções concorrentes já utilizadas. Dado ausente é UNKNOWN, não nota neutra disfarçada.

## Completude e incerteza
- Coverage: proporção de critérios com evidência suficiente.
- Confidence: qualidade/independência/atualidade das fontes.
- Um score alto com coverage baixo não autoriza contato prioritário.
- Ranking deve mostrar score, coverage e confidence lado a lado.
- Quando houver conflito, reduzir confiança e abrir pergunta; não escolher a informação mais conveniente.

## Priorização combinada
Ordenação padrão: primeiro gates; depois Conversion Fit; em seguida Business Value Fit; desempate por maior confiança/coverage e menor esforço/risco. Não esconder scores individuais dentro de uma média opaca.

Recomendação:
- PRIORITY_A: alto fit de conversão e valor, confiança pelo menos MEDIUM.
- PRIORITY_B: potencial interessante, mas exige confirmação ou protótipo limitado.
- HOLD: dados insuficientes, timing ruim ou dor ainda hipotética.
- DO_NOT_APPROACH: risco, canal inadequado, opt-out ou recusa aplicável.
- DISQUALIFIED: duplicata, empresa inativa, identidade não confirmada ou oportunidade sem sentido.

A quantidade de empresas contatadas não é meta. Um lote pode legitimamente terminar sem contato.

## Decisão de prototipagem
- DEMO_CONCEPT: protótipo genérico com dados fictícios, sem alegar personalização real.
- COMPANY_INSPIRED_DEMO: demonstração inspirada em sinais públicos, sem usar marca/conteúdo protegido nem sugerir parceria.
- FUNCTIONAL_PROTOTYPE: somente se pequeno, seguro, sem dados reais e dentro do orçamento de tempo aprovado.
- FULL_BUILD: apenas após requisitos, aceite comercial, escopo, preço, autorização e gate técnico.

Antes de qualquer construção, estimar horas, dependências, dados, risco, teste, manutenção e valor de aprendizagem. Se exceder limite definido para demo, reduzir escopo ou não construir.

## Calibração futura
Após volume suficiente, comparar score com resultados observados: permissão, resposta, reunião, proposta, fechamento e recebimento. Avaliar precisão por faixa, falsos positivos, falsos negativos e vieses de seleção. Não recalibrar pesos com amostra minúscula nem alegar previsão estatística sem base.
