# Scripts — Ferramentas de validação

Esta pasta contém scripts executáveis de apoio à qualidade documental e à operação do repositório.

## Validador atual
- `validate_docs.py`: verifica arquivos obrigatórios, limites de tamanho, links locais selecionados e sincronização entre `operations/state.toml` e snapshots Markdown.
- Dependências: biblioteca padrão do Python 3.11+ (CI usa Python 3.12).

## Como executar
Na raiz do repositório:

```bash
python scripts/validate_docs.py
```

## Regras
- Scripts devem ser determinísticos, seguros e sem efeitos colaterais não documentados.
- Não incluir tokens, senhas ou dados pessoais.
- Não alterar arquivos automaticamente sem uma opção explícita e documentada.
- Atualizar este README quando novos scripts forem adicionados.
