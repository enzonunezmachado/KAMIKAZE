# CURRENT WORK — Ponteiro automático de continuidade

**Última atualização:** 2026-11-26
**Regra:** este arquivo é o primeiro ponteiro para identificar o trabalho mais recentemente desenvolvido/atualizado no Kamikaze. Não inferir o foco apenas pelo número da fase ou pelo nome mais recente de arquivo.

## Último trabalho desenvolvido
- **Linha:** Motor de Diagnóstico e Soluções Empresariais
- **Local:** `operations/COMPANY_SOLUTIONS/`
- **Última entrega:** estrutura documental para lotes de 20 empresas, ranking, registro mestre, dossiês, contatos/supressão, projetos, contratos recorrentes e financeiro.
- **Estado:** DOCUMENTADO / NÃO ATIVADO.
- **O que NÃO aconteceu:** nenhum lote foi pesquisado, nenhuma empresa cadastrada/contatada, nenhuma proposta enviada, nenhum projeto/contrato/implantação ou gasto realizado.
- **Referência:** `operations/COMPANY_SOLUTIONS/README.md` e `CONTROL_TOWER.md`.

## Linha de pesquisa principal ainda ativa
- **Execução:** `PV-2026-11-25-TOTALMENTE-GRATUITA`
- **Foco:** pesquisa ampla de oportunidades digitais e monetização com IA; frentes PHASE_03.1–03.5 permanecem com lacunas e estados que precisam ser reconciliados.
- **PHASE_04_FEASIBILITY:** QUEUED / NOT_STARTED; não iniciar sem gate factual e autorização apropriada.
- **Orçamento operacional:** R$0.
- **Meta contextual:** buscar R$150 recebidos até 06/12/2026; objetivo, não garantia.

## Próxima ação obrigatória ao retomar
1. Auditar os registros mais recentes em `PROMPT_VIVO/SESSION_LOG.md` e no log da execução.
2. Reconciliar os estados divergentes entre `operations/STATE.md`, `RUN_STATE.md`, `PHASE_CONTROL.md` e `RESUME_PACKET.md`, usando eventos confirmados e o trabalho mais recente como evidência.
3. Atualizar este ponteiro e todos os resumos/atalhos dependentes no mesmo checkpoint.
4. Só então continuar a pesquisa ou ativar a linha empresarial, conforme a decisão registrada e autorização do usuário.

## Regra de atualização automática operacional
Este é o ponteiro canônico. Em toda unidade relevante de trabalho, a IA responsável pelo checkpoint deve:
1. identificar qual linha/artefato foi efetivamente mais recentemente desenvolvido ou atualizado;
2. atualizar este arquivo com entrega, estado, evidências, limites e próxima ação;
3. sincronizar os arquivos de entrada (BOOTSTRAP, NEXT_CHAT_PROMPT e operations/STATE) para apontarem para este arquivo, sem manter cópias independentes do foco atual;
4. atualizar RUN_STATE/RESUME_PACKET quando o estado da execução mudar;
5. confirmar a gravação no GitHub antes de declarar a atualização concluída.

**Importante:** o ponteiro não muda só porque um arquivo foi tocado, nem porque uma fase foi criada. Só muda após trabalho substantivo confirmado. A atualização ocorre no checkpoint da sessão ativa; não existe execução em segundo plano nem atualização após o chat terminar.
