# Quickstart — stack gratuita de agentes

Este guia é para quando houver acesso ao computador Windows. Nada aqui foi instalado ou testado nesta pesquisa.

## 1. Primeiro candidato: Antigravity

Documentação e download: https://antigravity.google/download

PowerShell:
```powershell
irm https://antigravity.google/cli/install.ps1 | iex
agy --version
```

Ou instale o aplicativo desktop pelo site oficial.

1. Entre com uma conta Google pessoal.
2. Confira o plano e o saldo/cota em `/usage` ou no painel de uso.
3. Abra o repositório PROJETO-SEM-NOME como workspace.
4. Confirme que confia na pasta antes de permitir indexação e execução.
5. Verifique se a skill `.agents/skills/zero-cost-opportunity-ops/SKILL.md` foi reconhecida.
6. Comece com uma tarefa pequena e delimitada; não iniciar com cinco agentes.

## 2. Como usar o Swarm sem desperdiçar cota

Exemplo de tarefa:
```text
/swarm
Pesquise independentemente três áreas diferentes: (1) pequenos negócios,
(2) hobbies/artesanato e (3) profissionais autônomos. Cada agente deve
entregar até cinco fontes primárias, resumo da dor, alternativa atual,
sinal comercial e contraprova. Não criar produtos nem contatar ninguém.
Salvar cada resultado em arquivo separado em research/. O agente coordenador
deve deduplicar e verificar links antes de sintetizar. Não inventar dados.
```

Comece com 2 ou 3 agentes. Não usar 5–10 por padrão. Se o trabalho for simples, pedir ao agente principal para executar sem subagentes.

## 3. Conectar Reddit Research MCP

Projeto: https://github.com/dialog-tools/reddit-research-mcp

O README declara servidor hospedado gratuito, sem credenciais Reddit, mas exige cliente MCP compatível e OAuth do serviço.

Antigravity suporta MCP. A forma exata de cadastrar o endpoint deve seguir a versão atual da documentação de Antigravity e o fluxo de autenticação do servidor. Endpoint anunciado: `https://mcp.dialog.tools/mcp`.

Não compartilhar cookies, tokens ou senhas. Não presumir que o app ChatGPT Android seja um cliente MCP.

## 4. Testar Pain Miner

Projeto: https://github.com/AdvancingTitans/pain-miner

Em terminal com Python 3.10+:
```bash
git clone https://github.com/AdvancingTitans/pain-miner.git
cd pain-miner
python3 scripts/pain_miner.py diagnose --out pain-diagnose.json
```

Só se o diagnóstico indicar fontes utilizáveis, rodar lote pequeno:
```bash
python3 scripts/pain_miner.py run \
  --target "recurring practical problems across small business, hobbies and professional communities" \
  --hours 720 \
  --min-score 10 \
  --min-comments 3 \
  --profile-communities \
  --fetch-comments \
  --analyze \
  --out pain-run.json
```

Gerar relatório:
```bash
python3 scripts/pain_miner.py render-report --input pain-run.json --out pain-report.md
```

Se aparecer `INSUFFICIENT_EVIDENCE`, não forçar uma oportunidade. Se uma fonte retornar 403/429, parar de insistir e registrar indisponibilidade.

## 5. Ferramentas para não instalar agora

- Ollama: exige memória local; referência oficial é 8 GB disponíveis para 7B. Evitar no computador de 4 GB.
- OpenHands: agente de programação que precisa de modelo forte e ambiente; local não significa leve.
- Dify/Flowise: builders úteis quando já existe caso de uso, mas exigem instalação/servidor/modelo.
- n8n: Community Edition pode ser self-hosted gratuitamente, mas exige manutenção e a licença limita revenda como serviço de workflow.
- CrewAI/LangGraph/smolagents: frameworks para desenvolver nossos próprios agentes; não são um produto pronto nem incluem inferência gratuita ilimitada.

## 6. Primeiro experimento do sistema

Objetivo: avaliar se o sistema encontra problemas e compradores melhor do que uma pesquisa manual simples.

- Escolher três nichos muito diferentes.
- Coletar até 10 threads por nicho.
- Abrir e ler fontes originais.
- Deduplicar autores e posts.
- Identificar pelo menos uma contraprova por problema promissor.
- Pesquisar alternativas e preços.
- Gerar no máximo três oportunidades candidatas.
- Escolher uma oferta manual para testar com compradores reais.
- Não construir software antes de receber sinal comercial.

## 7. Segurança e limites

- Revisar diffs antes de aceitar mudanças.
- Não executar scripts desconhecidos sem ler o código.
- Não versionar tokens/chaves.
- Não permitir envio automático de mensagens ou publicações.
- Não gastar nem contratar nada sem autorização explícita.
- Não contornar bloqueios de fontes.
- Confirmar a cota e o modelo disponíveis antes de tarefas longas.
