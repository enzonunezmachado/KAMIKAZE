# Política de orçamento de recursos — TOTALMENTE GRATUITA

## 1. Custo zero
Orçamento autorizado: R$0. Não cadastrar cartão para desbloquear uso, ativar billing, iniciar trial com conversão automática ou consumir créditos que possam gerar cobrança. Não usar API paga como fallback. Taxas variáveis inevitáveis após venda devem ser informadas, calculadas no preço e aprovadas antes de ofertar. Trial temporário e crédito promocional não contam como solução totalmente gratuita.

## 2. Auditoria obrigatória por ferramenta
Registrar plano/região; cota e unidade; janela de renovação; rate limits (RPM/RPD/TPM), concorrência e tamanho máximo; cotas compartilhadas; painel e horário de reset; termos comerciais, privacidade, retenção e treinamento; restrições; comportamento ao atingir limite; alternativa manual e alternativa tecnológica. Se número não for público: marcar QUOTA OPACA e não depender dela para etapa crítica.

## 3. Reserva conservadora
Para cada cota numérica conhecida, planejar consumo máximo de 60% da cota disponível no período; reservar 30% para correções/repetições/falhas e 10% para incerteza. Aplicar a cada janela diária/semanal e também à cota mensal agregada. Prevalece a cota mais restritiva. Não gastar toda a cota na exploração. Dividir orçamento por fase e medir consumo real.

## 4. Controle
Criar RESOURCE_USAGE_LOG.md quando houver cota mensurável. Registrar data, ferramenta, recurso, consumo antes/depois, tarefa, saldo, reset e fonte. Checkpoint ao atingir 50% do orçamento de execução. Pausar chamadas não essenciais em 60%. Não ultrapassar 70% da cota publicada/confirmada sem replanejamento. Não iniciar lote grande sem estimativa e limite de parada. Evitar repetir consultas; resumir contexto; usar método manual quando suficiente.

## 5. Meta de confiabilidade de 90%
90% é meta de planejamento, não garantia estatística. Não há base para prometer 90% sem histórico de consumo e falhas. Aproximar alta confiabilidade por: unidades pequenas; estimativa pessimista; reserva de 40%; teste-piloto; dois caminhos alternativos independentes para etapa crítica (um manual/offline sempre que possível); salvar no GitHub após cada fase; entregar versão mínima antes de pesquisa extra; nunca deixar síntese depender de uma única quota. Após três ciclos comparáveis, calcular taxa observada e intervalo de incerteza, informando amostra.

## 6. Fallback sem abuso
Alternar apenas entre serviços gratuitos legítimos e dentro dos termos. Não criar contas múltiplas, identidades falsas, chaves rotativas ou automações para burlar limites. Se quota acabar, parar, registrar, aguardar reset ou migrar para alternativa permitida. Pesquisa manual com fontes públicas e documentos locais é fallback. API gratuita com rate limit desconhecido nunca deve ser gargalo.

## 7. Dependência
A = essencial, B = aceleradora, C = conveniência. Ferramenta A exige quota compreendida e fallback comprovado. B/C com quota opaca podem ser usadas sem depender delas. Stack principal exige custo total zero, disponibilidade no Brasil, limites compreendidos, termos compatíveis, proteção de dados, exportação e fallback.
