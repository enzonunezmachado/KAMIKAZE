# Estado operacional — Kamikaze

**Última atualização:** 25/11/2026  
**Fase:** PHASE_03_1_PURCHASE_EVIDENCE — evidência de compra e canais sem leilão  
**Meta imediata:** receber pelo menos R$ 150 até 06/12/2026  
**Capital inicial:** R$ 0  
**Receita recebida no Kamikaze:** R$ 0  
**Despesas:** R$ 0  
**Oportunidade escolhida:** nenhuma  
**Experimento comercial ativo:** nenhum

## Missão atual
Pesquisar e comparar oportunidades digitais de diferentes categorias, identificar uma oportunidade executável e testar uma oferta comercial real dentro da janela imediata. O foco não é transformar uma atividade pessoal em negócio por conveniência.

## Direção confirmada
- Kamikaze é uma operação ampla de pesquisa, validação, produção e comercialização digital.
- Não há nicho, produto ou modelo de negócio escolhido antecipadamente.
- Investigar usos comerciais de IA, e-commerce/dropshipping, produtos digitais, serviços, pesquisa, automações, conteúdo e outros modelos.
- Pesquisa de mercado/concorrência é hipótese prioritária em investigação, não escolha definitiva.
- O usuário autorizou um controlador adaptativo: toda solicitação de continuidade exige auditoria de completude; não avançar mecanicamente.
- Comentários, correções e novas preferências do usuário podem alterar a pesquisa e a próxima ação; registrar em USER_INPUT_LOG.md.
- Para novo chat, executar PROMPT_VIVO/BOOTSTRAP.md e ler RESUME_PACKET.md antes de continuar.
- PHASE_03.1 está em andamento porque a Fase 03 deixou lacunas críticas. PHASE_04_FEASIBILITY permanece QUEUED/NOT_STARTED, não executada.
- Investigar serviço pontual e sistema de monitoramento recorrente assistido por IA; não prometer pesquisa literalmente infinita nem construir antes de validar uso e pagamento.
- Dropshipping e conteúdo gerado com IA continuam hipóteses a investigar criticamente.
- Não priorizar leilões de propostas com muitos freelancers disputando um comprador. Planilhas rápidas ficam como comparador secundário, não como estratégia de volume sem comprador.
- Não desenvolver software ou infraestrutura antes de existir justificativa comercial.
- Não pagar ferramentas, APIs, hospedagem ou anúncios sem autorização explícita.
- Não presumir acesso a planos pagos ou agentes ilimitados.
- NEXUS e ATLAS permanecem projetos separados.

## Recursos operacionais
- Inventário: [operations/AVAILABLE_RESOURCES.md](AVAILABLE_RESOURCES.md).
- Notebook principal com 8 GB RAM; tablet e celular auxiliares.
- Maquininha configurada e testada; taxas/prazos devem ser verificados antes de precificar.
- Priorizar ferramentas web leves, gratuitas e com fallback manual.
- Equipamentos de assistência técnica não definem o escopo do Kamikaze.

## Prompt Vivo
- Arquitetura: [PROMPT_VIVO/README.md](../PROMPT_VIVO/README.md).
- Master Prompt: [PROMPT_VIVO/MASTER_PROMPT.md](../PROMPT_VIVO/MASTER_PROMPT.md).
- Bootstrap: [PROMPT_VIVO/BOOTSTRAP.md](../PROMPT_VIVO/BOOTSTRAP.md).
- Execução ativa: [PV-2026-11-25-TOTALMENTE-GRATUITA](../PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/RESUME_PACKET.md).

## Estado da execução
- PHASE_00_SCOPE: PASS WITH GAPS.
- PHASE_01_LANDSCAPE: PASS WITH GAPS.
- PHASE_02_DEMAND: encerrada para transição, PASS WITH GAPS.
- PHASE_03_VALIDATION: encerrada para transição, PASS WITH GAPS; sem compra/recorrência comprovada.
- PHASE_03.1_PURCHASE_EVIDENCE: IN_PROGRESS, gate CONTINUE.
- PHASE_04_FEASIBILITY: QUEUED/NOT_STARTED; plano existe, mas teste operacional não foi executado.
- Arquitetura: [PHASE_ARCHITECTURE.md](../PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/PHASE_ARCHITECTURE.md).
- Matriz: [VALIDATION_MATRIX.md](../PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/VALIDATION_MATRIX.md).
- Viabilidade: [PHASE_04_FEASIBILITY.md](../PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/PHASE_04_FEASIBILITY.md), apenas planejamento.
- Política de cotas: RESOURCE_BUDGET_POLICY.md; quota permanece opaca.

## Próximos passos
1. Continuar pesquisa de compra comprovada e canal sem leilão.
2. Desenhar fluxo de entrega e relatório mínimo apenas quando validação justificar.
3. Auditar ferramentas/fontes gratuitas e fallback.
4. Executar teste interno com dados públicos e medir tempo/qualidade.
5. Estimar economia unitária, capacidade e taxas.
6. Avaliar se recorrência justifica cobrança.
7. Só então decidir se um piloto comercial merece ser proposto; abordagem externa exige aprovação humana.

## Aprovações e segurança
- Nenhuma oportunidade ou abordagem externa aprovada.
- Nenhum cliente foi contatado, nenhuma venda e nenhum gasto.
- Mensagens externas, publicações, compras, assinaturas, deploys e ações irreversíveis exigem aprovação humana.
- Não contar curtidas, visualizações, seguidores ou elogios como receita.

## Registro de decisões
| Data | Decisão | Motivo |
|---|---|---|
| 25/11/2026 | Identidade Negócio Digital Kamikaze | Nome definitivo do projeto |
| 25/11/2026 | Retirar hipótese comercial pré-selecionada | Pesquisa ampla antes de escolher modelo |
| 25/11/2026 | Meta R$150 até 06/12/2026 | Meta financeira definida pelo usuário |
| 25/11/2026 | Pesquisa ampla de modelos digitais e IA | Evitar nicho prematuro |
| 25/11/2026 | Arquitetura adaptativa | Criar/alterar fases conforme evidência |
| 25/11/2026 | PHASE_02 encerrada com PASS WITH GAPS | Usuário autorizou transição à validação |
| 25/11/2026 | PHASE_03 encerrada com PASS WITH GAPS | Usuário autorizou transição; auditoria posterior identificou lacunas críticas |
| 25/11/2026 | Criar controlador adaptativo e PHASE_03.1 | Auditoria de completude antes de cada transição |
| 25/11/2026 | Criar bootstrap entre chats e pacote de retomada | Garantir reconstrução explícita de contexto e incorporação de feedback |
