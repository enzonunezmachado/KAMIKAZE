# Autoaperfeiçoamento controlado do Prompt Vivo

## 1. Objetivo

Permitir que a IA desenvolva instruções melhores, novos métodos e módulos especializados a partir do que aprende, sem comprometer consistência, segurança ou rastreabilidade.

## 2. O que a IA pode melhorar

- perguntas de pesquisa;
- estratégia de busca e seleção de fontes;
- critérios de comparação;
- modelos de registro;
- organização de fases;
- checklists e gates;
- instruções de especialização por domínio;
- ferramentas e fluxos de trabalho;
- métodos para reduzir repetição e melhorar continuidade.

## 3. Gatilhos de melhoria

Propor melhoria quando:
- uma fase falha repetidamente pelo mesmo motivo;
- uma fonte ou mecanismo novo melhora a cobertura;
- uma execução revela dimensão crítica ausente;
- o método produz ruído ou duplicação;
- uma técnica aumenta verificabilidade ou reduz custo;
- um domínio exige conhecimento e protocolo próprios.

## 4. Processo obrigatório

1. **Observar:** descrever o problema ou oportunidade de melhoria com exemplo real.
2. **Diagnosticar:** explicar por que a estrutura atual não atende.
3. **Propor:** definir mudança mínima, arquivos afetados e benefício esperado.
4. **Verificar:** checar conflitos com CORE, evidência, segurança e escopo.
5. **Aplicar:** atualizar os arquivos quando a mudança for segura, coerente e autorizada pelo escopo do trabalho.
6. **Registrar:** adicionar entrada em `CHANGELOG.md`.
7. **Testar:** indicar em qual próxima execução a melhoria será avaliada.
8. **Reverter ou ajustar:** se a mudança piorar o resultado, registrar e corrigir.

## 5. Níveis de mudança

- **Nível 1 — Ajuste local:** melhorar instrução de uma fase ou arquivo de execução. Pode ser aplicado durante o trabalho.
- **Nível 2 — Módulo reutilizável:** criar método, template ou conhecimento especializado. Pode ser criado quando houver utilidade clara; registrar no changelog.
- **Nível 3 — Arquitetura central:** alterar CORE, hierarquia, salvaguardas ou protocolo central. Não fazer silenciosamente. Apresentar justificativa e pedir confirmação do usuário antes de aplicar.
- **Nível 4 — Mudança de escopo do Kamikaze:** exige decisão explícita do usuário e atualização dos documentos centrais do projeto.

## 6. Não fazer

- Não criar prompts só para parecer mais sofisticado.
- Não multiplicar fases sem ganho claro.
- Não reescrever instruções centrais por preferência estilística.
- Não remover salvaguardas para acelerar pesquisa.
- Não promover uma descoberta isolada a conhecimento universal.
- Não apagar versões antigas ou histórico.
- Não declarar que ficou especialista apenas por ter produzido muitos arquivos.

## 7. Especialização por domínio

Quando uma execução revelar que um domínio merece aprofundamento:
1. criar pasta em `knowledge/<DOMINIO>/`;
2. registrar conceitos, glossário, atores, métricas, modelos, fontes de referência e riscos;
3. separar fatos duradouros de dados temporais;
4. criar protocolo especializado apenas quando a complexidade justificar;
5. registrar data de revisão e lacunas;
6. referenciar o módulo a partir da execução, sem duplicar tudo.

A especialização significa possuir uma base organizada e atualizável, não conhecimento perfeito ou acesso ilimitado.
