# CURRENT WORK — Ponteiro canônico de continuidade

**Atualizado:** 27/11/2026  
**Função:** identificar a última entrega substantiva e a próxima ação de retomada.

## Última entrega substantiva

### Correção da publicação do portfólio

- Adicionado `.github/workflows/deploy-pages.yml`: build MkDocs com `--strict`, upload exclusivo de `portfolio_site/site/` e deploy com GitHub Pages Actions.
- O workflow foi persistido no commit `05f6cb7c8662d7144350c142089b53709fd40779`.
- Pré-requisito administrativo: Settings → Pages → Source = GitHub Actions. A ferramenta GitHub disponível não oferece alteração dessa configuração de Pages; o usuário precisa selecionar essa origem se ainda estiver como branch.
- Deploy confirmado: workflow `45938486917` concluiu com sucesso no commit `a402a89`; o conteúdo do portfólio foi publicado pelo GitHub Pages Actions. Alterações posteriores de documentação não alteraram as fontes do site.

- Linha: padrão reutilizável de desenvolvimento web do NEGÓCIO DIGITAL KAMIKAZE.
- Entrega: módulo `web/` com guia de desenvolvimento para IA, template HTML inicial, CSS dark reutilizável, JavaScript progressivo e integração dos assets ao build MkDocs.
- Complemento solicitado em 27/11: `web/AI_PROMPT_SCRIPTS.md` reúne regras de design sintetizadas e seis playbooks curtos para delimitar, criar direção visual, construir, auditar, corrigir e fechar tarefas. O índice `web/README.md` orienta leitura seletiva; não é necessário carregar/colar todos os roteiros.
- Commits confirmados: `028c19f` (playbooks), `835ef29` (índice) e `4495215` (changelog).
- Arquivos principais: `web/README.md`, `web/AI_WEB_DEVELOPMENT_GUIDE.md`, `web/templates/starter.html`, `portfolio_site/docs/assets/kamikaze-base.css`, `portfolio_site/docs/assets/kamikaze.js`, `mkdocs.yml`.
- Regra persistente: ao criar/revisar qualquer site, ler o índice e o guia em `web/`; tema escuro Kamikaze é o padrão, com HTML semântico, CSS separado, JS vanilla, responsividade e acessibilidade.
- Persistência: commits individuais confirmados no GitHub em 27/11/2026.
- Validação documental recuperada: workflow `45939953007` passou no commit `70ec82b`, incluindo validador documental, build `mkdocs build --strict` e markdownlint. Deploy do portfólio também passou no workflow `45939795049` (commit `2932ad2`). A aparência ainda não foi inspecionada em navegador/captura.

## Prioridade operacional preservada

A frente comercial de primeira venda continua prioritária. A criação desta base web foi uma solicitação explícita do usuário, mas não substitui nem valida a operação comercial.

- Meta financeira: receber pelo menos R$140 até 08/12/2026.
- Orçamento operacional autorizado: R$0.
- Estado comercial: nenhum contato, conversa, proposta, contratação ou receita recebida.

## Próxima ação

1. Retomar a revisão individual dos candidatos do lote 001 e confirmar presença digital, menu atual de serviços/preços e possível lacuna real.
2. Selecionar somente negócios com oportunidade observável; não presumir que não encontrar um menu significa que ele não existe.
3. Preparar uma abordagem individual e específica para aprovação do usuário.
4. Após autorização, iniciar um pequeno teste de aquisição; registrar respostas e sinais comerciais.
5. Validar o build MkDocs e revisar visualmente o portfólio usando a nova base CSS/JS quando isso não desviar a prioridade comercial e houver ambiente de navegador disponível.

## Oferta em teste

- Segmento inicial: barbearias, salões e estúdios independentes de beleza em Embu das Artes e entorno.
- Serviço: organizar até 25 serviços/preços em um PDF simples pronto para WhatsApp e uma planilha editável.
- Preço experimental: R$149, 50% para iniciar e 50% na entrega.
- Prazo proposto: até 2 dias úteis após receber todos os dados.
- A oferta e o preço são hipóteses; não há demanda validada.
- Não construir site, sistema de agendamento, CRM, automação ou pacote recorrente antes de uma venda.

## Pesquisa e arquitetura anteriores

- Execução preservada: PV-2026-11-25-TOTALMENTE-GRATUITA.
- Foco de pesquisa anteriormente registrado: PHASE_03.5_ACQUISITION_ENGINE_AND_AFFILIATE_VALIDATION.
- A pesquisa exploratória fica subordinada à operação de primeira venda. Não avançar novas fases, criar módulos ou alterar gates sem necessidade concreta.
- Company Solutions permanece disponível como infraestrutura de análise, mas não é necessário ativar seu processo completo para este teste.

## Regra de atualização

Atualizar este ponteiro após uma entrega substantiva confirmada. Sincronizar os documentos operacionais correspondentes. Não inferir trabalho concluído por timestamp. Não existe execução em segundo plano.

## Auditoria de consistência do repositório — em andamento

- Árvore GitHub consultada no commit inicial da auditoria: 135 arquivos versionados, sem truncamento.
- Falhas confirmadas: caminho incorreto para `CONTINUITY_SYSTEM.md` e caminhos relativos ambíguos no BOOTSTRAP; link para demonstração inexistente em `operations/FIRST_SALE/README.md`; tabela Markdown malformada em `PROMPT_VIVO/README.md`; meta antiga R$150/06-12 ainda aparecia em brief e skills; CI documental falhava por ponteiro de última entrega divergente e por lint Markdown.
- Correções iniciais persistidas: BOOTSTRAP, README do Prompt Vivo, oferta/índice da Primeira Venda, estado TOML, brief, skills, RUN_STATE/RESUME_PACKET e `scripts/validate_docs.py` ampliado para incluir links da Primeira Venda.
- CI documental: PASS em `45939953007`; após a correção de layout, novo workflow `45940140564` também passou em validação, MkDocs strict e markdownlint.
- Portfólio: `.km-main` agora é wrapper full-width sem padding; `.rst-content` é o único container central com max-width/padding, alinhado ao header/footer. O validador `scripts/validate_portfolio_build.py` verifica assets, shell, largura total, eixo dos containers, breakpoint mobile e reduced motion.
- Deploy da correção: workflow `45940140491` PASS (build, validador de shell/assets, upload e deploy). A inspeção visual real ainda não foi concluída; não declarar alinhamento visual confirmado sem navegador/captura.
- Privacidade: o repositório é público e arquivos operacionais/históricos contêm contexto pessoal e financeiro. Valores financeiros pessoais foram retirados de cópias atuais em dois arquivos, mas continuam no histórico Git. Não reescrever histórico nem migrar a memória sem decisão do usuário.
