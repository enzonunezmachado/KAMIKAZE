# Registro de Contatos, Permissões e Supressão

Este registro controla a autorização e o histórico de cada tentativa. Nunca usar uma lista de empresas como autorização automática para enviar mensagens.

| Contact Event ID | Company ID | Data | Canal | Tipo de evento | Permissão/evidência | Resultado | Próxima ação | Opt-out? | Fonte/dossiê |
|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | Nenhum evento registrado | — | — | — | — | — |

## Tipos de evento
- CHANNEL_RESEARCHED: canal público localizado, sem contato.
- PERMISSION_REQUESTED: pedido de autorização para encaminhar apresentação.
- PERMISSION_GRANTED: consentimento registrado, com canal, escopo e data.
- PERMISSION_DENIED: autorização negada.
- INTRODUCTION_RECEIVED: apresentação por terceiro consentida.
- MESSAGE_SENT: mensagem enviada pelo operador, com data e conteúdo/versão arquivada.
- RESPONSE_RECEIVED: resposta recebida.
- FOLLOW_UP_SENT: follow-up permitido e dentro da cadência aprovada.
- OPT_OUT: pessoa/empresa pediu para não receber novos contatos.
- WRONG_CONTACT: canal/destinatário incorreto.
- BOUNCED_OR_INVALID: endereço ou canal inválido.

## Regras de cadência e decisão
- Registrar tentativas individualmente, sem mensagens em massa.
- Sem resposta não significa rejeição. Após a cadência previamente aprovada e limitada, classificar como NO_RESPONSE e pausar. Não insistir indefinidamente.
- Uma recusa clara encerra a abordagem daquela oferta. Registrar DECLINED; reabrir somente se a própria empresa voltar ou houver convite explícito para contato sobre outra necessidade.
- Pedido de não contato/opt-out: marcar DO_NOT_CONTACT e bloquear novas abordagens promocionais. Não reativar por simples mudança de lote.
- Permissão deve ser específica ao canal e finalidade; número público não equivale a opt-in para WhatsApp.
- Guardar apenas evidência mínima de permissão e contato. Restringir acesso; não armazenar conversas completas ou dados pessoais desnecessários.
- Se um contato for feito por e-mail, telefone, formulário ou outro canal, respeitar as regras próprias do canal e a legislação aplicável.
