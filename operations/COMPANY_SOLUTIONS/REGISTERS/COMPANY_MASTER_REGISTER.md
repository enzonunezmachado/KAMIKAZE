# Registro Mestre de Empresas

**Fonte canônica de identidade e histórico resumido.** Uma linha por empresa, mesmo que apareça em múltiplas pesquisas, lotes, verticais ou cidades.

| Company ID | Nome comercial | Cidade/UF | Setor | Domínio/perfil oficial | Primeiro lote | Última revisão | Prioridade atual | Research status | Contact status | Sales status | Reavaliação elegível? | Dossiê |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | Nenhuma empresa registrada | — | — | — | — | — | — | — | — | — | — | — |

## Regras
- ID: `CO-YYYY-NNNN`, sequencial e permanente. Nunca reutilizar IDs.
- Antes de inserir, deduplicar por domínio, nome + localidade, telefone comercial validado e perfis oficiais. Empresas com filiais devem ter regra consistente: unidade/local distinto só recebe ID próprio se a oportunidade e decisão de compra forem realmente independentes.
- Guardar somente dados empresariais necessários. Evitar dados pessoais de funcionários/proprietários.
- O registro mestre não substitui o histórico do lote nem o dossiê. É um índice compacto.
- Se a empresa reaparecer, atualizar o mesmo registro e abrir reavaliação vinculada; não contá-la como empresa nova.
- Marcar "não reavaliar" quando houver opt-out, recusa definitiva, pedido de exclusão ou bloqueio legítimo.
- A coluna "prioridade atual" não apaga ranking histórico. Cada lote preserva seu snapshot.

## Critérios de identidade
1. Mesmo site/domínio oficial: provável duplicata.
2. Mesmo nome e endereço/município: revisar como provável duplicata.
3. Mesmo telefone público: sinal adicional, não prova isolada.
4. Franquias/unidades: separar apenas quando gestão, necessidade e decisão de compra forem distintas.
5. Nome parecido sem confirmação: manter como candidato não resolvido; não fundir por suposição.

## Valores controlados
- Research status: DISCOVERED, SCREENED, RANKED, HOLD, DISQUALIFIED, REASSESSMENT.
- Contact status: NOT_ELIGIBLE, PERMISSION_NEEDED, PERMISSION_REQUESTED, PERMISSION_GRANTED, CONTACTED, NO_RESPONSE, DECLINED, DO_NOT_CONTACT.
- Sales status: NOT_APPROACHED, QUALIFICATION, PROPOSAL, NEGOTIATION, WON, LOST, NOT_A_FIT.
- Reavaliação: YES, CONDITIONAL, NO.
