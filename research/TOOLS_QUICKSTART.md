# Como testar as ferramentas pesquisadas

Este guia evita instalar tudo. Comece pelo Pain Miner e só adicione o MCP se o ambiente suportar.

## Opção 1 — Pain Miner (primeiro teste recomendado)

Projeto: https://github.com/AdvancingTitans/pain-miner

Pré-requisitos: Python 3.10+ e internet. O README do projeto declara coleta pública padrão sem conta/API key do Reddit. Isso não garante que todos os endpoints estejam acessíveis em toda rede.

### Baixar
```bash
git clone https://github.com/AdvancingTitans/pain-miner.git
cd pain-miner
```

### Diagnosticar fontes antes de coletar
```bash
python3 scripts/pain_miner.py diagnose --out pain-diagnose.json
```

Se Reddit estiver bloqueado, não insistir em loop. Registrar a falha e usar as fontes alternativas suportadas.

### Rodar um primeiro lote exploratório
```bash
python3 scripts/pain_miner.py run \
  --target "people with recurring unsolved practical problems across hobby, professional, consumer and creator communities" \
  --hours 720 \
  --min-score 10 \
  --min-comments 3 \
  --profile-communities \
  --fetch-comments \
  --analyze \
  --out pain-run.json
```

Observação: o Pain Miner tem foco em Reddit, Hacker News e V2EX. O parâmetro de alvo amplo não transforma o script em um crawler universal. A saída deve ser lida e revisada; não aceitar scores automaticamente.

### Gerar relatório
```bash
python3 scripts/pain_miner.py render-report --input pain-run.json --out pain-report.md
```

Se houver `INSUFFICIENT_EVIDENCE`, respeitar o resultado. Não preencher o relatório com hipóteses como se fossem descobertas.

## Opção 2 — Reddit Research MCP

Projeto: https://github.com/dialog-tools/reddit-research-mcp

O README oferece conexão MCP hospedada e declara uso standalone gratuito. Requer cliente MCP compatível e autenticação OAuth do serviço. O servidor é ferramenta de coleta e consulta, não o analista completo.

Exemplos do README para clientes compatíveis:

Claude Code:
```bash
claude mcp add --scope local --transport http dialog-mcp https://mcp.dialog.tools/mcp
```

Codex CLI:
```bash
codex mcp add dialog-mcp npx -y mcp-remote https://mcp.dialog.tools/mcp --auth-timeout 120 --allow-http
```

Gemini CLI:
```bash
gemini mcp add dialog-mcp npx -y mcp-remote https://mcp.dialog.tools/mcp --auth-timeout 120 --allow-http
```

Antes de conectar, revisar a documentação atual e permissões do cliente. Não compartilhar senha, cookie ou token no chat. Não presumir que o app ChatGPT para Android aceite esse MCP diretamente.

## Opção 3 — Trend Opportunity Radar

Projeto: https://github.com/datou202307-design/trend-opportunity-radar

Instalação documentada:
```bash
npx skills add datou202307-design/trend-opportunity-radar -g
```

É uma skill de pesquisa por plataforma. A coleta real pode exigir adaptadores ou MCP de terceiros. O projeto é melhor como referência para relatórios com amostragem, fontes, contraprovas e trilha de evidências do que como primeiro setup.

## Nossa skill local

Arquivo neste repositório: `.agents/skills/market-opportunity-scout/SKILL.md`.

Ela foi escrita para este projeto e amplia o escopo além de SaaS/tecnologia: serviços manuais, conteúdo, curadoria, intermediação, produtos digitais e outras formas de negócio. Também exige classificar sinais comerciais S0–S4, procurar contraprovas e manter a memória em arquivos Markdown.

Para um agente que leia Agent Skills, copie a pasta `market-opportunity-scout` para o diretório de skills suportado por esse agente. Se o agente não suporta skills, envie o conteúdo de SKILL.md como instrução de trabalho ou peça que ele leia o arquivo no GitHub.

## Teste de qualidade antes de confiar

Compare o resultado da pesquisa manual e do Pain Miner no mesmo lote. Registre:
- número de comunidades descobertas e realmente consultadas;
- quantidade de threads abertas e comentários lidos;
- quantidade de autores independentes;
- fontes válidas e links quebrados;
- duplicatas;
- achados irrelevantes;
- sinais S0–S4 identificados corretamente;
- concorrentes e preços encontrados;
- contraprovas;
- oportunidades que sobreviveram à revisão humana.

Não usar quantidade de ideias, nota de oportunidade, views ou upvotes como métrica de sucesso. A métrica final é encontrar problemas com compradores acessíveis e validar interesse comercial real.