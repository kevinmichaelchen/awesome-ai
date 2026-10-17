# Awesome AI

A personal, categorized index of 468 AI projects I've starred: agent frameworks, coding agents, skills, sandboxes, memory and retrieval, tools, and models. Each section is sorted by GitHub stars.

_Last generated 2026-10-17. Star counts are a snapshot._

## Contents

- [Agent frameworks & assistants](#agent-frameworks--assistants) (82)
  - [Agent frameworks & SDKs](#agent-frameworks--sdks) (17)
  - [Personal & team assistant agents](#personal--team-assistant-agents) (39)
  - [Multi-agent collaboration & simulation](#multi-agent-collaboration--simulation) (12)
  - [Domain & research agents](#domain--research-agents) (6)
  - [Agent evals, benchmarks & training](#agent-evals-benchmarks--training) (8)
- [Coding agents](#coding-agents) (114)
  - [Coding agent CLIs & harness cores](#coding-agent-clis--harness-cores) (13)
  - [Agent IDEs & desktop workbenches (ADEs)](#agent-ides--desktop-workbenches-ades) (21)
  - [Parallel agent orchestration](#parallel-agent-orchestration) (14)
  - [Remote & mobile agent clients](#remote--mobile-agent-clients) (10)
  - [Autonomous loops & background agents](#autonomous-loops--background-agents) (15)
  - [Harness plugins, hooks & config](#harness-plugins-hooks--config) (21)
  - [Agent task tracking & planning](#agent-task-tracking--planning) (8)
  - [Agent sessions, usage & observability](#agent-sessions-usage--observability) (12)
- [Agent skills](#agent-skills) (44)
  - [Skill collections & packs](#skill-collections--packs) (12)
  - [Visual & media output skills](#visual--media-output-skills) (14)
  - [Behavior, writing & workflow skills](#behavior-writing--workflow-skills) (12)
  - [Skill specs, registries & testing](#skill-specs-registries--testing) (6)
- [Agent sandboxes & execution](#agent-sandboxes--execution) (30)
  - [Agent VM & container sandboxes](#agent-vm--container-sandboxes) (19)
  - [Code interpreters & language sandboxes](#code-interpreters--language-sandboxes) (7)
  - [Agent workspaces & virtual filesystems](#agent-workspaces--virtual-filesystems) (4)
- [Agent memory, context & retrieval](#agent-memory-context--retrieval) (58)
  - [Agent memory systems](#agent-memory-systems) (19)
  - [Code intelligence for agents](#code-intelligence-for-agents) (11)
  - [RAG, knowledge graphs & context layers](#rag-knowledge-graphs--context-layers) (14)
  - [Semantic & hybrid search](#semantic--hybrid-search) (6)
  - [Token & context-window optimization](#token--context-window-optimization) (8)
- [Agent tools & integrations](#agent-tools--integrations) (47)
  - [MCP platforms & tool plumbing](#mcp-platforms--tool-plumbing) (7)
  - [Service connectors (MCP servers, API CLIs & clients)](#service-connectors-mcp-servers-api-clis--clients) (10)
  - [Browser & computer-use automation](#browser--computer-use-automation) (14)
  - [Web crawling & scraping](#web-crawling--scraping) (9)
  - [Document parsing, OCR & extraction](#document-parsing-ocr--extraction) (7)
- [Models, inference & LLM access](#models-inference--llm-access) (93)
  - [LLM inference engines & serving](#llm-inference-engines--serving) (16)
  - [Local model runners & desktop AI](#local-model-runners--desktop-ai) (8)
  - [ML frameworks, training & fine-tuning](#ml-frameworks-training--fine-tuning) (9)
  - [Open model releases & research code](#open-model-releases--research-code) (5)
  - [Speech, voice & dictation](#speech-voice--dictation) (26)
  - [Vision, video & image models](#vision-video--image-models) (8)
  - [LLM gateways, routers & model catalogs](#llm-gateways-routers--model-catalogs) (15)
  - [LLM app utilities & typed AI functions](#llm-app-utilities--typed-ai-functions) (6)

## Agent frameworks & assistants

### Agent frameworks & SDKs

Libraries, SDKs and runtimes for building agents in TypeScript, Python, Rust, Go and Elixir, including Effect-based and Cloudflare-based options.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [agno-agi/agno](https://github.com/agno-agi/agno) | 42.8k | 2022-05-04 | Python framework and runtime for agent platforms: build agents with the SDK, serve them with the AgentOS runtime, and manage them through the AgentOS web UI. |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | 30.4k | 2025-07-27 | Opinionated, model-agnostic agent harness from LangChain that runs out of the box, with planning, sub-agents and filesystem tools. Any piece can be overridden or replaced. |
| [mastra-ai/mastra](https://github.com/mastra-ai/mastra) | 28.9k | 2024-08-06 | TypeScript framework for building AI applications and agents, distributed as the @mastra/core package. Backed by Y Combinator (W25). |
| [withastro/flue](https://github.com/withastro/flue) | 8.5k | 2026-02-07 | TypeScript framework for programmable agent harnesses, for building autonomous agents that run in sandboxes, in the style of Claude Code and Codex. |
| [cloudflare/agents](https://github.com/cloudflare/agents) | 5.8k | 2025-01-29 | SDK for building agents as persistent, stateful execution environments on Cloudflare Durable Objects, where each agent has its own state, storage and lifecycle. |
| [agentjido/jido](https://github.com/agentjido/jido) | 1.9k | 2024-12-16 | Elixir framework for autonomous agents and dynamic multi-agent workflows, built around distributed, supervised behavior on the BEAM. |
| [rivet-dev/agents](https://github.com/rivet-dev/agents) | 1.6k | 2026-01-25 | Rivet's agent infrastructure that runs agents such as Pi as durable Rivet Actors with memory that survives restarts, plus a sandbox adapter package. |
| [openclaw/lobster](https://github.com/openclaw/lobster) | 1.3k | 2026-01-18 | OpenClaw-native workflow shell with typed, JSON-first pipelines and approval gates that turns skills and tools into composable, repeatable automations OpenClaw can call in one step. |
| [charmbracelet/fantasy](https://github.com/charmbracelet/fantasy) | 1k | 2025-08-15 | Go library for building AI agents with tools, giving multiple providers and models one API. Programs compile to native binaries. |
| [liveloveapp/hashbrown](https://github.com/liveloveapp/hashbrown) | 728 | 2025-03-26 | Headless TypeScript framework for AI chat and agents in React or Angular apps. The model renders your components and calls your tools in the browser, with any provider. |
| [clavia-labs/tardigrade](https://github.com/clavia-labs/tardigrade) | 425 | 2026-08-13 | TypeScript framework on Effect for composable agents built around an immutable event log, taking a functional approach to state and effects inspired by Elm and Jotai. APIs still changing. |
| [a-agmon/rs-graph-llm](https://github.com/a-agmon/rs-graph-llm) | 382 | 2025-06-10 | Type-safe Rust framework (graph-flow) for stateful, resumable agent workflows, modeled on LangGraph's graph execution engine. |
| [humanlayer/fold](https://github.com/humanlayer/fold) | 167 | 2026-07-01 | Effect-native, provider-agnostic TypeScript agent core with an optional coding agent, CLI and TUI. Supports subagents, RLM-style orchestration and subscription-backed providers such as Codex and Grok. |
| [yielded-dev/agent](https://github.com/yielded-dev/agent) | 164 | 2026-07-29 | TypeScript toolkit built on Effect and Effect AI for durable agent Threads. Define schemas, instructions and tools, and the runtime runs the model/tool loop and can retain accepted work across restarts. |
| [SouthBridgeAI/hankweave-runtime](https://github.com/SouthBridgeAI/hankweave-runtime) | 159 | 2026-01-21 | Single-threaded, headless-first runtime for long-horizon data agents, designed around maintainability and repairability. Run with bunx hankweave. |
| [stukennedy/honi](https://github.com/stukennedy/honi) | 46 | 2026-03-04 | Lightweight framework for AI agents on Cloudflare Workers, combining Hono routing, Durable Objects for state and the AI SDK. Pitched as Mastra for Cloudflare deployments. |
| [leostera/agents](https://github.com/leostera/agents) | 33 | 2026-02-25 | Rust toolkit for typed agent systems: LLM sessions, tools, context and storage, plus an evals crate with graded trajectories, a cargo-evals runner and an embeddable JavaScript codemode. |

### Personal & team assistant agents

Personal and team assistant agents, from always-on chat-app bots and self-hosted agent servers to desktop coworker apps, many in the OpenClaw family.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 49.1k | 2026-02-01 | Ultra-lightweight self-hosted personal AI agent framework in Python with a web UI, tools, memory, MCP, scheduled automation and chat-app integrations. |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | 33.6k | 2025-08-07 | Open-source desktop cowork app with a built-in agent that also fronts Claude Code, Codex, OpenClaw and 20+ other CLI agents. Offers remote access and 24/7 automation. |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | 33k | 2026-02-13 | Single Rust binary agent runtime for personal assistants, connecting to about 20 LLM providers and 30+ chat channels. Runs on any OS. |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 31k | 2026-01-31 | Lightweight OpenClaw alternative that runs each agent in its own container on Anthropic's Agents SDK, connecting to WhatsApp, Telegram, Slack, Discord and Gmail with memory and scheduled jobs. |
| [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | 30.1k | 2026-02-04 | Lightweight personal AI assistant written in Go that targets cheap hardware, with a claimed footprint of about 10MB RAM on $10 boards and millisecond boot. |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | 18.2k | 2026-02-24 | Open-source agent operating system written in Rust and shipped as a single binary across 14 crates, for running autonomous agents. Pre-1.0 with breaking changes between minor versions. |
| [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | 18k | 2025-01-13 | Open-source desktop AI coworker that indexes your work into a knowledge graph and uses it to act, with built-in email, notes and whiteboard surfaces. Works solo or with a team. |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent) | 15.6k | 2025-07-29 | Open-source local cowork desktop app with AI agents, positioned as a free alternative to Claude Cowork and Codex. |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | 12.7k | 2026-02-03 | Agent OS in Rust from NEAR AI, built as a personal AI assistant with emphasis on privacy, security and extensibility. |
| [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | 11.5k | 2026-04-15 | Cloudflare's internal AI productivity workspace, built on Workers, for creating documents, building apps and running agents with company context and systems. |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 9.9k | 2026-01-27 | Experimental proof of concept for running the OpenClaw personal assistant (formerly Moltbot/Clawdbot) inside a Cloudflare Sandbox on Workers. Not officially supported. |
| [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | 8.1k | 2026-02-16 | Autonomous personal AI assistant runtime written in Zig, aimed at small size and speed. Part of a Null ecosystem with a setup UI (nullhub), orchestrator and observability tools. |
| [osaurus-ai/osaurus](https://github.com/osaurus-ai/osaurus) | 8.1k | 2025-08-17 | Native macOS harness for AI agents written in Swift, with any model, persistent memory, autonomous execution and cryptographic identity. Runs fully offline. |
| [memovai/mimiclaw](https://github.com/memovai/mimiclaw) | 5.8k | 2026-02-04 | C firmware that turns a $5 ESP32-S3 board into a personal AI assistant, reached over Telegram. Runs with no Linux or Node.js on the device. |
| [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | 4.8k | 2025-07-23 | Self-hostable AI chat client from the Thunderbird team that lets users choose their own models and keep their data. Early-stage and aimed at enterprise customers. |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | 3.6k | 2026-02-09 | Multi-agent, multi-team assistant that runs 24/7 across Discord, WhatsApp and Telegram, where agents with isolated workspaces hand off work to teammates. Aimed at one-person companies. |
| [cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent) | 3.4k | 2026-04-20 | Always-on personal agent defined by a user-written soul, with permission-gated tools, token budgets and local memory, reachable from the CLI or Telegram. |
| [moltis-org/moltis](https://github.com/moltis-org/moltis) | 2.9k | 2026-01-29 | Self-hosted personal agent server in Rust shipped as one binary, with sandboxed execution, multiple LLM providers, voice, memory, MCP tools and Telegram, WhatsApp, Discord and Teams integrations. |
| [felinics/Memoh](https://github.com/felinics/Memoh) | 2.7k | 2026-01-12 | Open-source multi-agent platform in Go that gives each agent its own always-on cloud computer with desktop, browser, network and long-term memory. Can also host coding agents such as Claude Code. |
| [spacedriveapp/spacebot](https://github.com/spacedriveapp/spacebot) | 2.4k | 2026-02-11 | Multi-threaded agent harness built to serve teams, communities and companies on Discord, Slack, Telegram and Twitch, written in Rust. A hosted one-click option is available at spacebot.sh. |
| [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) | 2k | 2026-01-28 | Web dashboard for OpenClaw: connect to a Gateway, view agents, chat, manage approvals and configure jobs from one interface. |
| [langchain-ai/openwork](https://github.com/langchain-ai/openwork) | 1.5k | 2026-01-13 | Desktop interface for deepagentsjs agents, giving them filesystem and shell access, distributed on npm. |
| [OpenBMB/EdgeClaw](https://github.com/OpenBMB/EdgeClaw) | 1.2k | 2026-02-13 | Edge-cloud collaborative personal assistant built on OpenClaw, adding Claude Code-style features. Aims to balance security, cost and efficiency between local and cloud models. |
| [okou-ai/okou](https://github.com/okou-ai/okou) | 1.2k | 2025-11-14 | Slack-based AI teammate you assign to a role. It connects to the tools a team already uses and does work across marketing, sales, engineering and operations. |
| [supermemoryai/company-brain](https://github.com/supermemoryai/company-brain) | 1k | 2026-09-25 | Slack teammate, previously a paid product and now open source, that remembers what a team says and can perform tasks. Self-hosted on Cloudflare. |
| [pocketpaw/pocketpaw](https://github.com/pocketpaw/pocketpaw) | 891 | 2026-02-02 | Self-hosted personal AI agent with a native desktop app and web dashboard, reachable over Discord, Slack, WhatsApp and Telegram. Supports Anthropic, OpenAI or Ollama. Beta. |
| [qhkm/zeptoclaw](https://github.com/qhkm/zeptoclaw) | 651 | 2026-02-12 | Single Rust binary for running personal AI agents locally, at the edge or on a VPS, with tools, memory, channels, providers and sandboxed autonomy built in. |
| [dominant-strategies/entropic](https://github.com/dominant-strategies/entropic) | 296 | 2026-01-31 | Local-first Tauri desktop AI workspace that runs OpenClaw in a hardened local runtime. Source builds default to a local-only profile with hosted features disabled. |
| [arsumbris/arsumbris](https://github.com/arsumbris/arsumbris) | 265 | 2026-09-13 | macOS-only agent-native IDE for typed knowledge, where types, skills, tools and UI components live together in composable repos that can depend on each other. Early alpha. |
| [zscole/gru](https://github.com/zscole/gru) | 216 | 2026-01-16 | Self-hosted Python service that runs autonomous task agents controlled from Telegram, Discord or Slack. Agents learn user patterns and keep memory across tasks. |
| [iii-experimental/agentos](https://github.com/iii-experimental/agentos) | 162 | 2026-03-01 | Agent OS made of 65 narrow Rust worker binaries, one per domain, that register Functions and Triggers on the iii engine, and which the project describes as self-evolving. |
| [hunvreus/heypi](https://github.com/hunvreus/heypi) | 159 | 2026-05-11 | Connects one Pi agent to Slack, Discord, Telegram, local apps or webhooks as a team chat agent, adding routing, runtime isolation, approvals, memory, schedules and audit records. |
| [Michaelliv/mercury](https://github.com/Michaelliv/mercury) (archived) | 143 | 2026-02-26 | Personal assistant for WhatsApp, Slack and Discord that runs pi as a sandboxed subprocess and deploys as a single Docker container. |
| [yoheinakajima/babyagi3](https://github.com/yoheinakajima/babyagi3) | 130 | 2026-01-28 | Minimal personal agent configured once and driven by natural language to remember things, research, send emails, schedule tasks and learn new skills. Can get expensive with many automations. |
| [Compound-inc/rift](https://github.com/Compound-inc/rift) | 124 | 2025-08-29 | Self-hostable AI chat platform for teams, built on Bun and TanStack, with branching chats and multi-provider support, focused on responsiveness while preserving native provider behavior. |
| [Consensys/c0](https://github.com/Consensys/c0) | 105 | 2026-08-02 | Open-source organizational AI platform deployable to Cloudflare in one step, with its own agent harness for company tools and context. The README points to the SolZero fork for new projects. |
| [letta-ai/letta-oss-ui](https://github.com/letta-ai/letta-oss-ui) | 85 | 2026-01-28 | Open-source demo desktop app on the Letta Agent SDK where you point a stateful agent at a folder, describe a task and watch it work, with memory kept across chats. |
| [idodekerobo/draft](https://github.com/idodekerobo/draft) | 47 | 2026-05-26 | Shared workspace that collects a team's decisions, context and activity into a company brain, which connected agents read through MCP or a local CLI. |
| [millionco/pookie](https://github.com/millionco/pookie) | 42 | 2026-05-05 | Slack bot that answers by searching your Slack, and can also generate images, run Python on attached files, search the web and call MCP tools. A managed version is offered. |

### Multi-agent collaboration & simulation

Platforms, protocols and simulations where many agents or agents and humans collaborate, share work or interact socially.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 103.5k | 2026-03-02 | Node.js server and React dashboard for orchestrating a team of AI agents, with goals, tasks and cost tracking. Positioned as the company around agents like OpenClaw. |
| [block/buzz](https://github.com/block/buzz) | 36.1k | 2026-03-06 | Self-hostable workspace on a relay you own where humans and AI agents share rooms in communities. Written in Rust under Apache 2.0. |
| [camel-ai/oasis](https://github.com/camel-ai/oasis) | 5.3k | 2024-11-13 | Open social-media simulation framework from CAMEL-AI that can run up to one million LLM agents interacting with each other, for studying social behavior. |
| [openagents-org/openagents](https://github.com/openagents-org/openagents) | 4.2k | 2025-03-10 | Open-source workspace where multiple AI agents connect and collaborate, with an agent launcher on npm and a Python package. No account required. |
| [hyperspaceai/agi](https://github.com/hyperspaceai/agi) | 2.1k | 2026-03-08 | Experimental peer-to-peer network where autonomous agents run experiments, gossip findings to peers and push results to this repository, joinable from a browser or CLI. |
| [klawsh/klaw.sh](https://github.com/klawsh/klaw.sh) | 634 | 2026-02-15 | Go CLI that works like kubectl for AI agents: deploy, monitor, isolate and scale fleets of business agents from one binary, with Slack control. |
| [rllm-org/hive](https://github.com/rllm-org/hive) | 217 | 2026-03-14 | Open-source platform where agents collaborate on a shared artifact: each task is a repo plus eval script, agents work in isolated forks, runs are tracked by git SHA, and results go on a leaderboard. |
| [pass-agent/loomkin](https://github.com/pass-agent/loomkin) | 181 | 2026-02-28 | Elixir/OTP platform where AI agents form teams, spawn specialists, share discoveries, review each other's work and vote, with persistent memory and a live mission-control UI. |
| [Intelligent-Internet/CommonGround](https://github.com/Intelligent-Internet/CommonGround) | 153 | 2026-02-16 | Python and PostgreSQL kernel that provides a durable shared work layer for human-agent and multi-agent collaboration, exposed over an HTTP API. |
| [Weber-GeoML/Choir](https://github.com/Weber-GeoML/Choir) | 116 | 2026-09-21 | Open protocol for distributed multi-agent autoformalization: an orchestrator turns a large Lean or Isabelle formalization plan into GitHub tasks that contributors claim and work with their own agents. |
| [warpdotdev/oz-workspace](https://github.com/warpdotdev/oz-workspace) | 72 | 2026-02-13 | Sample app for Warp's Oz API: chat rooms where assigned agents collaborate in real time over SSE, @mention each other, create Kanban tasks and produce artifacts such as PRs. |
| [zscole/matrix-agents](https://github.com/zscole/matrix-agents) | 19 | 2026-02-05 | Shell-based coordination of AI agents running on different machines through your own Matrix server, avoiding cloud services and third-party platforms. |

### Domain & research agents

Agents specialized for a field such as financial research, deep research reports, data science and automated R&D.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 98.1k | 2026-03-06 | Setup in which AI agents autonomously run research experiments on single-GPU nanochat training, iterating on training code without a human in the loop. |
| [virattt/dexter](https://github.com/virattt/dexter) | 27.7k | 2025-10-14 | Autonomous financial research agent that uses task planning, self-reflection and real-time market data. Described as Claude Code built for financial research. |
| [microsoft/RD-Agent](https://github.com/microsoft/RD-Agent) | 15k | 2024-04-03 | Microsoft framework that automates data-driven R&D, with agents proposing and implementing experiments such as model and factor development. Has a tech report, live demo and papers. |
| [ValueCell-ai/valuecell](https://github.com/ValueCell-ai/valuecell) | 11k | 2025-09-01 | Community-driven multi-agent platform for financial applications, covering stock research, market analysis and trading, including A-share deep research. A hosted version exists. |
| [business-science/ai-data-science-team](https://github.com/business-science/ai-data-science-team) | 5.5k | 2024-12-11 | Python library of specialized agents for data loading, cleaning, visualization and modeling, plus AI Pipeline Studio, an app that records work as a visual, reproducible pipeline. Beta. |
| [Nutlope/open-deep-research](https://github.com/Nutlope/open-deep-research) | 435 | 2025-05-29 | Next.js web app that plans searches and writes sourced research reports using open-source LLMs on Together.ai. Uses Clerk for auth and Drizzle with Neon for storage. |

### Agent evals, benchmarks & training

Benchmarks, trajectory analysis, user simulators and training or evolution frameworks for measuring and improving agents.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | 18.7k | 2025-06-18 | Lightweight reinforcement learning framework of about 3,500 lines for training agents with their real harnesses. Refactored in v1.0. |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 8.6k | 2026-02-15 | Benchmark and leaderboard where OpenClaw-style agents act as coworkers across 44+ professions, ranked by income, cost and quality on real-life tasks. |
| [aiming-lab/SkillRL](https://github.com/aiming-lab/SkillRL) | 1k | 2026-02-08 | NeurIPS 2026 research code for training agents with recursive skill-augmented reinforcement learning, discovering skills automatically from experience. Includes SFT data generation. |
| [imbue-ai/darwinian_evolver](https://github.com/imbue-ai/darwinian_evolver) | 533 | 2026-02-02 | Lightweight framework that evolves code and prompts: it keeps a population of solutions, selects parents, mutates them with LLMs and scores the offspring each iteration. |
| [arklexai/arksim](https://github.com/arklexai/arksim) | 233 | 2026-02-27 | Simulates multi-turn user conversations with an AI agent to surface failures such as misread intent that only appear mid-conversation, before the agent reaches production. |
| [MaxBittker/runebench](https://github.com/MaxBittker/runebench) | 132 | 2026-02-26 | Benchmark suite that scores AI coding agents on long-horizon RuneScape tasks. Agents write TypeScript against an 8x-speed emulated game server via rs-sdk. |
| [AR-FORUM/hodoscope](https://github.com/AR-FORUM/hodoscope) | 121 | 2026-02-19 | Python tool for unsupervised, human-in-the-loop analysis of agent trajectories: summarizes, embeds and visualizes actions to find patterns across models. Reads common eval formats via LiteLLM. |
| [zou-group/humanlm](https://github.com/zou-group/humanlm) | 93 | 2026-02-11 | Stanford research code for training language models to simulate specific users by aligning to their latent states rather than imitating their responses. |

## Coding agents

### Coding agent CLIs & harness cores

Terminal coding agents and harness cores that read and edit code and run commands, including forks and agents tuned for open or local models.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 251.9k | 2026-08-13 | Open-source agent harness from DeepSeek AI (`dsh`), built on an everything-is-a-plugin architecture powered by the Cordis framework. |
| [openai/codex](https://github.com/openai/codex) | 129.6k | 2025-04-13 | OpenAI's coding agent that runs locally in the terminal, also available as an IDE extension and desktop app. |
| [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 68.6k | 2023-07-14 | Rust coding agent tuned for low-cost open models such as Kimi and GLM, with a Codex-like interface and provider-recommended harness reimplementations. |
| [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | 22.1k | 2026-05-08 | Open-source Rust coding and research agent for long-running work, built around a Recursive Language Model (RLM) approach to context and designed to improve itself. |
| [just-every/code](https://github.com/just-every/code) | 4k | 2025-08-10 | Community fork of the Codex CLI that adds browser integration, multi-agent orchestration across OpenAI, Claude and Gemini, theming and reasoning controls while staying compatible with upstream. |
| [batrachianai/toad](https://github.com/batrachianai/toad) | 3.5k | 2025-07-17 | Python terminal interface that wraps coding agents such as Claude, Gemini, Codex and OpenHands behind one unified UI. |
| [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | 3.2k | 2026-02-11 | Agent harness that combines mechanical detection of dead code, duplication and complexity with subjective LLM review to guide a coding agent in systematically improving codebase quality. |
| [Dicklesworthstone/pi_agent_rust](https://github.com/Dicklesworthstone/pi_agent_rust) | 1.9k | 2026-02-02 | Rust terminal coding agent CLI with no unsafe code, positioned as a fast-starting alternative to managed-runtime agents. |
| [Twigpine/zero](https://github.com/Twigpine/zero) | 1.7k | 2026-05-28 | Go terminal coding agent that inspects repositories, edits files, runs commands and keeps durable local sessions, with a user-chosen model and permission level. |
| [tontinton/maki](https://github.com/tontinton/maki) | 1.2k | 2026-02-13 | Rust coding agent designed to use few context tokens, extendable with Neovim-style Lua plugins. |
| [EuniAI/Prometheus](https://github.com/EuniAI/Prometheus) | 1.1k | 2024-10-14 | Python agent platform that builds a knowledge graph of a codebase and uses it to reason about, understand and repair issues through autonomous code agents. |
| [walter-grace/mac-code](https://github.com/walter-grace/mac-code) | 1k | 2026-03-23 | Claude-Code-style terminal agent that runs large local models on Apple Silicon Macs by paging weights from flash, targeting models that do not fit in RAM. |
| [Effectful-Tech/clanka](https://github.com/Effectful-Tech/clanka) | 112 | 2026-03-07 | TypeScript CLI coding agent from Effectful that defaults to Codex subscription auth for OpenAI and supports API keys and custom endpoints. |

### Agent IDEs & desktop workbenches (ADEs)

Desktop, native and web workbenches where a human drives one or many coding agents with terminals, diffs and worktrees in a single window.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [stablyai/orca](https://github.com/stablyai/orca) | 95k | 2026-03-17 | Agentic development environment for running Codex, Claude Code, OpenCode or Pi side-by-side, each in its own worktree, with desktop, mobile companion and remote runtime. |
| [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | 28.2k | 2026-01-28 | Ghostty-based macOS terminal with vertical tabs and notifications designed for running multiple AI coding agents. |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 28.1k | 2026-02-08 | Agent harness control surface for controlling coding agents on your machine from Electron desktop, web and iOS/Android mobile apps. |
| [slopus/happy](https://github.com/slopus/happy) | 24.2k | 2025-07-18 | Open-source app for orchestrating Claude, Codex and Grok in one place, reusing existing vendor subscriptions and each vendor's own prompts and tools. |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | 21.2k | 2025-10-13 | Open-source agentic development environment for desktop, mobile, web and CLI that manages Claude Code, Codex, Copilot, OpenCode and other agents alongside editor, terminals, diffs and a browser. |
| [superset-sh/superset](https://github.com/superset-sh/superset) | 15.3k | 2025-10-21 | Agentic IDE for running many CLI coding agents such as Claude Code and Codex in parallel with terminals, code review and browser previews, using the user's own subscriptions. |
| [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | 13.3k | 2026-02-13 | Go tool for planning, running and supervising teams of coding agents from planning to merge, supporting Claude Code, Codex and many other harnesses across desktop, web, mobile and cloud. |
| [openchamber/openchamber](https://github.com/openchamber/openchamber) | 11.7k | 2025-09-11 | Open-source workspace built on the OpenCode agent for running and reviewing agent work, usable from desktop and remotely. |
| [generalaction/emdash](https://github.com/generalaction/emdash) | 6k | 2025-08-28 | Open-source agentic development environment for running multiple coding agents in parallel with any provider. |
| [get-bb/bb](https://github.com/get-bb/bb) | 4.4k | 2026-02-24 | Agentic IDE that can control, customize and automate itself, driven through a desktop app, web app, CLI or HTTP API, with work organized into followable threads. |
| [Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor) | 4.3k | 2026-01-11 | Tauri app for orchestrating multiple Codex agents across local workspaces, with a project sidebar and conversation view backed by the Codex app-server protocol. |
| [zeronsh/zeron](https://github.com/zeronsh/zeron) | 3.3k | 2026-07-20 | Native control plane for running Claude Code, Codex, Cursor, Devin and other coding agents from a desktop app, local by default with optional multi-device sync. |
| [hardbeat920/monocode](https://github.com/hardbeat920/monocode) | 3.1k | 2026-08-20 | GUI for coding agents that runs any installed and logged-in CLI such as Claude Code, Codex, Cursor, OpenCode or Devin, with tabs as sessions and a composer as the input. |
| [collabs-inc/collab-public](https://github.com/collabs-inc/collab-public) | 3.1k | 2026-03-15 | Early-stage desktop environment that places agent terminals, context files and running code on an infinite canvas. |
| [coder/xum](https://github.com/coder/xum) | 2.1k | 2025-09-17 | Desktop app (renamed from Mux) for isolated, parallel agentic development, acting as a coding agent multiplexer. |
| [penso/herdr-gpui](https://github.com/penso/herdr-gpui) | 1.5k | 2026-09-20 | Native Rust/GPUI client for macOS, Linux and Windows that connects to a local Herdr daemon to show terminal sessions, workspaces, Git worktrees and agent activity. |
| [penso/arbor](https://github.com/penso/arbor) | 836 | 2026-03-04 | Native Rust desktop app built on GPUI for agentic coding, combining Git worktrees, terminals and diffs in one window. |
| [missuo/herdrm](https://github.com/missuo/herdrm) | 762 | 2026-08-19 | Native macOS console for herdr that shows Claude Code, Codex, Gemini, Grok and OpenCode sessions across the Mac and SSH hosts, with full-fidelity TUI access to each. |
| [owengretzinger/constellagent](https://github.com/owengretzinger/constellagent) | 217 | 2026-02-10 | macOS desktop app for running multiple AI agents in parallel, each with its own terminal, Monaco editor and isolated git worktree in a single window. |
| [scarce/axel](https://github.com/scarce/axel) | 208 | 2026-01-29 | Native macOS app, paired with a Rust CLI, that presents a task list while orchestrating many AI agents across tmux panes, Ghostty-based terminals and git worktrees. |
| [longsurf-ai/endo](https://github.com/longsurf-ai/endo) | 93 | 2026-10-14 | Desktop chat app described as a Higher Order Harness that composes agents running on existing subscriptions into workflows under a single unified interface. |

### Parallel agent orchestration

CLI, TUI and tmux layers that spawn, multiplex and coordinate several coding agents, with worktree isolation and inter-agent messaging.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [herdrdev/herdr](https://github.com/herdrdev/herdr) | 44.5k | 2026-03-27 | Rust runtime and terminal multiplexer for coding agents that keeps terminals running in a background server so work continues after the client closes or an SSH connection drops. |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | 18.4k | 2025-12-16 | Go workspace manager that coordinates multiple coding agents such as Claude Code, Copilot, Codex and Gemini on different tasks, with persistent work tracking. |
| [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | 8.5k | 2026-03-17 | TypeScript library that runs coding agents in isolated sandboxes via a single `sandcastle.run()` call, with configurable branch strategies and merging commits back; provider-agnostic. |
| [agent-of-empires/agent-of-empires](https://github.com/agent-of-empires/agent-of-empires) | 3.4k | 2026-01-09 | Session manager for AI coding agents on Linux and macOS that runs agents in parallel across branches with persistent sessions, controllable from a TUI or a browser. |
| [standardagents/dmux](https://github.com/standardagents/dmux) | 1.8k | 2025-08-20 | Multiplexer that runs multiple AI coding agents in tmux panes, each in its own isolated git worktree, for parallel branching and merging. |
| [nrslib/takt](https://github.com/nrslib/takt) | 1.4k | 2026-01-25 | CLI that defines multi-agent coding workflows in YAML (planning, implementation, review, fix loops, human checkpoints), running them in isolated worktrees with traceable logs. |
| [Ataraxy-Labs/opensessions](https://github.com/Ataraxy-Labs/opensessions) | 1.2k | 2026-03-19 | Rust tmux sidebar that tracks Amp, Claude Code, Codex and OpenCode sessions with per-thread markers, live state and a local HTTP API. |
| [AgentWorkforce/relay](https://github.com/AgentWorkforce/relay) | 885 | 2025-12-17 | TypeScript infrastructure for coding agents aimed at teams, so agents belonging to different teammates can communicate and share work instead of relying on copy-pasting. |
| [joelhooks/swarm-tools](https://github.com/joelhooks/swarm-tools) | 747 | 2025-12-08 | OpenCode plugin for multi-agent swarm coordination that decomposes tasks, runs agents in parallel, tracks agent issues and learns from past outcomes so work survives context loss. |
| [poteto/noodle](https://github.com/poteto/noodle) | 497 | 2026-02-22 | Go tool for orchestrating coding agents through skills. |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | 459 | 2025-12-10 | Named Tmux Manager: a Go binary that turns tmux into a control plane for multiple coding agents, with a TUI command palette, safety policies, Agent Mail coordination and a local REST/WebSocket API. |
| [kingbootoshi/codex-orchestrator](https://github.com/kingbootoshi/codex-orchestrator) | 355 | 2026-01-17 | Claude Code plugin and CLI that spawns OpenAI Codex agents in tmux sessions, monitors their progress, sends mid-task follow-ups and captures results. |
| [regenrek/peky](https://github.com/regenrek/peky) | 150 | 2025-11-23 | Go TUI that puts Claude Code, Codex CLI, pi, opencode and other terminal agents into a single app so parallel agents across projects stay organized. |
| [larstalian/tincan](https://github.com/larstalian/tincan) | 12 | 2026-10-11 | Peer-to-peer, serverless Rust binary that lets teammates' coding agents see who is working on what across machines and message each other directly into open sessions. |

### Remote & mobile agent clients

Clients for controlling coding agents from a phone, browser or chat app such as Discord or Telegram.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [0xSero/litter](https://github.com/0xSero/litter) | 2.5k | 2026-02-21 | Native iOS and Android client for Codex and Local Studio that connects to local or remote servers to manage sessions and run agentic coding workflows from a phone. |
| [remorses/kimaki](https://github.com/remorses/kimaki) | 1.4k | 2025-09-02 | Collaborative agent orchestrator that exposes OpenCode through Discord, mapping each channel to a project and each thread to a coding session. |
| [AltanS/collie](https://github.com/AltanS/collie) | 1.4k | 2026-06-28 | Self-hosted PWA that serves as a mobile client for Herdr, with experimental tmux and zellij support, for driving Claude Code, Pi, Codex and OpenCode from a phone with push alerts. |
| [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) | 1.1k | 2026-09-17 | Browser and phone client for herdr that offers chat and live terminal views of each agent pane, remote PCs over SSH, and web push alerts. |
| [hosenur/portal](https://github.com/hosenur/portal) | 812 | 2025-12-09 | Mobile-first web UI for OpenCode with Git integration, an in-browser terminal and isolated workspaces; a personal project unaffiliated with the OpenCode or SST teams. |
| [eriklangille/clauntty](https://github.com/eriklangille/clauntty) | 398 | 2025-12-22 | iOS SSH terminal with persistent sessions, GPU-accelerated rendering and native Claude Code support, keeping sessions alive when the app backgrounds. |
| [antirez/tgterm](https://github.com/antirez/tgterm) | 225 | 2026-02-03 | C program that exposes macOS terminals over Telegram so developers can send instructions to coding agents and observe results while away from the keyboard. |
| [joelhooks/opencode-vibe](https://github.com/joelhooks/opencode-vibe) | 180 | 2025-12-27 | Next.js 16 rebuild of the OpenCode web app with streaming chat, SSE sync and React Server Components; built on a canary release of Next.js. |
| [Rigos0/superturtle](https://github.com/Rigos0/superturtle) | 123 | 2026-02-25 | Autonomous coding agent controlled from Telegram by text or voice message, which works on the user's own machine using Codex and Claude Code. |
| [alexknowshtml/cord](https://github.com/alexknowshtml/cord) | 68 | 2026-01-25 | Discord harness for Claude Code that maps each conversation to a Discord thread and connects outbound, so no ports need to be exposed. |

### Autonomous loops & background agents

Systems that run coding agents unattended, including Ralph loops, issue-to-PR pipelines, background agents and software factories.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [openai/symphony](https://github.com/openai/symphony) | 27.7k | 2026-02-26 | Elixir service that monitors a project board such as Linear and turns work items into isolated autonomous implementation runs, so teams manage tasks instead of supervising agents. |
| [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | 11k | 2025-05-21 | Asynchronous open-source coding agent built on LangChain Deep Agents that investigates a codebase, implements and validates changes, opens pull requests, and monitors CI and review feedback. |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | 6.3k | 2026-05-31 | Local-first control plane with a durable state kernel that keeps goals, decisions and evidence across sessions for long-horizon agents running on Codex, Claude Code and other runtimes. |
| [ColeMurray/background-agents](https://github.com/ColeMurray/background-agents) | 3.4k | 2026-01-25 | Open-Inspect, a hosted background coding agent system inspired by Ramp's Inspect, that works on tasks in the background and is self-deployable. |
| [subsy/ralph-tui](https://github.com/subsy/ralph-tui) | 2.5k | 2026-01-11 | Terminal UI that orchestrates AI coding agents through a task list autonomously in a Ralph-style loop. |
| [fabro-sh/fabro](https://github.com/fabro-sh/fabro) | 1.7k | 2026-03-13 | Open-source workflow engine where the development process is defined as a graph that agents execute, with human intervention only at chosen points. |
| [marcus/nightshift](https://github.com/marcus/nightshift) | 1.1k | 2026-02-05 | Go tool that spends leftover Claude or Codex subscription budget to open pull requests on its own, which the user can accept or discard. |
| [iannuttall/ralph](https://github.com/iannuttall/ralph) (archived) | 951 | 2026-01-12 | Minimal file-based autonomous coding loop that starts each iteration fresh, using a JSON PRD plus git as memory and committing one story at a time. |
| [miantiao-me/cloud-code](https://github.com/miantiao-me/cloud-code) | 561 | 2026-01-25 | TypeScript project that runs OpenCode inside Cloudflare Workers and Containers to provide a dedicated cloud-hosted coding agent. |
| [snarktank/compound-product](https://github.com/snarktank/compound-product) | 543 | 2026-01-22 | Shell-based system that reads a product's daily performance reports, picks the top actionable priority, plans it, and implements the fix autonomously with an AI agent. |
| [terragon-labs/terragon-oss](https://github.com/terragon-labs/terragon-oss) | 261 | 2026-01-16 | Open-source snapshot of Terragon, a shut-down service that delegated work to Claude Code, Codex and other coding CLIs running as background agents in the cloud; provided as-is. |
| [rohunj/claude-build-workflow](https://github.com/rohunj/claude-build-workflow) | 231 | 2026-01-18 | Shell workflow for Claude Code that interviews the user (BMAD method), writes a PRD with user stories, designs the build, and then builds the app autonomously. |
| [tim-smart/lalph](https://github.com/tim-smart/lalph) | 134 | 2026-01-12 | TypeScript orchestrator that pulls work from an issue source such as GitHub Issues or Linear, runs a chosen CLI agent per project with configurable concurrency and review agent, and syncs task state. |
| [eduardolat/clancy](https://github.com/eduardolat/clancy) | 119 | 2026-01-18 | Go orchestrator for Ralph Wiggum loops that reruns agents such as opencode or Claude Code until a success criterion is met or safety limits are reached. |
| [thruflo/wisp](https://github.com/thruflo/wisp) | 44 | 2026-01-16 | Go tool that runs a pure-bash Ralph loop for spec-driven development inside isolated Sprites (sprites.dev) using Claude, then opens pull requests via a GitHub token. |

### Harness plugins, hooks & config

Plugins, hooks, statuslines, notifications, personas and config tools that extend or configure an existing coding-agent harness.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 70.1k | 2025-12-03 | Plugin layer (OmO) for coding-agent harnesses that adds multi-model workflows triggered by a keyword, plus memory, CodeMode and subscription support. |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 34.3k | 2026-03-30 | Claude Code plugin that adds slash commands to run Codex reviews, including an adversarial review, and to delegate tasks to Codex from inside Claude Code. |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | 33.6k | 2026-02-02 | Layer on top of Codex CLI that adds hooks, agent teams, HUDs, prompts and workflows (OMX). |
| [PeonPing/peon-ping](https://github.com/PeonPing/peon-ping) | 5.1k | 2026-02-09 | Shell tool that plays Warcraft III Peon voice lines and shows overlay notifications when Claude Code, Codex or other agents finish or need permission; agents can also pick sounds via MCP. |
| [crafter-station/petdex](https://github.com/crafter-station/petdex) | 4.2k | 2026-05-02 | Public gallery of animated companion pets for Codex, Claude Code, OpenCode, Gemini CLI and other agents, with a web gallery and an npm CLI to browse, install and submit pets. |
| [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) | 3.9k | 2025-12-23 | Claude Code environment using hooks, ledgers and handoffs to maintain state across sessions, run MCP execution outside the context window, and orchestrate agents with isolated contexts. |
| [QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) | 3.1k | 2026-07-29 | Python plugins that add native multimodal capabilities for Qwen models to any agent harness. |
| [intellectronica/ruler](https://github.com/intellectronica/ruler) | 2.9k | 2025-05-20 | Tool that keeps one set of coding-agent instructions and distributes them to the configuration files of multiple AI coding assistants. |
| [davis7dotsh/my-pi-setup](https://github.com/davis7dotsh/my-pi-setup) | 1.1k | 2026-04-30 | Author's personal configuration for the pi agent, adding a theme, Firecrawl tools, a custom status bar, background terminals, subagents, workflows and an ask-user tool; offered as an example. |
| [jarrodwatts/claude-delegator](https://github.com/jarrodwatts/claude-delegator) (archived) | 1k | 2026-01-08 | Archived Claude Code plugin that delegated tasks to Codex and Gemini; it no longer works with current Codex because the `codex mcp-server` command it relied on was removed. |
| [iannuttall/dotagents](https://github.com/iannuttall/dotagents) | 710 | 2026-01-06 | Guided Bun CLI that maintains one canonical .agents folder holding hooks, commands, skills and AGENTS/CLAUDE.md files and wires it into multiple AI tools. |
| [neiii/bridle](https://github.com/neiii/bridle) | 440 | 2025-12-27 | Rust TUI and CLI configuration manager for agent harnesses such as Claude Code, OpenCode, Goose, Amp, Copilot CLI and Crush, handling profiles and installing skills, agents and commands. |
| [jarrodwatts/claude-stt](https://github.com/jarrodwatts/claude-stt) (archived) | 364 | 2026-01-13 | Archived Claude Code plugin for local speech-to-text dictation with a hold-to-talk hotkey; superseded by Claude Code's native /voice command. |
| [kommander/oc-plugin-vault-tec](https://github.com/kommander/oc-plugin-vault-tec) | 182 | 2026-03-28 | OpenCode plugin that gives the coding agent a Vault-Tec Overseer persona in the style of a RobCo terminal, themed around the Fallout vault experiments. |
| [ctoth/claudio](https://github.com/ctoth/claudio) | 117 | 2025-07-28 | Go hook-driven audio layer that maps events from Claude Code, Codex, Gemini CLI, Qwen Code, Copilot CLI and OpenCode to contextual sounds without blocking the agent. |
| [seth-schultz/orchestr8](https://github.com/seth-schultz/orchestr8) | 69 | 2025-10-31 | Claude Code extension that packages agents and workflows to make Claude act as a full software engineering team. |
| [NathanFlurry/herdr-plugin-jj-workspace](https://github.com/NathanFlurry/herdr-plugin-jj-workspace) | 48 | 2026-06-23 | Herdr plugin, written in Rust, that creates and removes Jujutsu (jj) workspaces as Herdr workspaces, opening tabs with Codex alongside a terminal. |
| [joelreymont/banjo](https://github.com/joelreymont/banjo) | 43 | 2025-12-24 | Zig implementation of an ACP adapter that runs Claude Code and Codex inside editors such as Zed. |
| [MatiousCorp/claude-tts](https://github.com/MatiousCorp/claude-tts) | 30 | 2026-03-03 | Claude Code plugin that speaks responses aloud through ElevenLabs, OpenAI, Google, Amazon Polly, Azure, Kitten or local system TTS on macOS, Linux and Windows. |
| [alp82/claude-statusline](https://github.com/alp82/claude-statusline) | 26 | 2026-07-21 | Single bash script for the Claude Code statusline showing directory, branch, model, context window, and 5-hour and 7-day rate-limit bars that compare usage against elapsed time. |
| [kevinmichaelchen/perplexity-opencode](https://github.com/kevinmichaelchen/perplexity-opencode) (archived) | 7 | 2026-01-15 | OpenCode plugin that detects web-search or research requests in a message and nudges the agent to use the Perplexity MCP server. |

### Agent task tracking & planning

Issue trackers, task graphs and plan stores designed for agents and humans to plan and track coding work.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [Dicklesworthstone/beads_viewer](https://github.com/Dicklesworthstone/beads_viewer) | 1.7k | 2025-11-26 | Keyboard-driven terminal interface for the Beads issue tracker with list, kanban and dependency-graph views, PageRank and critical-path insights, and a robot-mode JSON API. |
| [hmans/beans](https://github.com/hmans/beans) | 951 | 2025-12-06 | Go CLI flat-file issue tracker that stores issues alongside the code for use by humans and coding agents. |
| [asdecided/core](https://github.com/asdecided/core) | 299 | 2026-06-01 | Rust engine that keeps requirements, decisions and designs as typed Markdown in a repo, validates them, and serves relevant decisions to agents over read-only MCP without embeddings. |
| [govctl-org/govctl](https://github.com/govctl-org/govctl) | 273 | 2026-01-17 | Rust governance-as-code CLI that keeps RFCs, ADRs and work items in the repo and guards AI-assisted delivery with them. |
| [joshuadavidthomas/opencode-beads](https://github.com/joshuadavidthomas/opencode-beads) | 263 | 2025-12-11 | OpenCode plugin integrating the Beads issue tracker, intentionally kept small in scope because Beads changes quickly. |
| [joelreymont/dots](https://github.com/joelreymont/dots) | 123 | 2025-12-24 | Minimal task tracker that stores tasks as plain Markdown files in a `.dots/` directory, delivered as a tiny single native CLI with no database or server. |
| [instructa/planr](https://github.com/instructa/planr) | 74 | 2025-03-26 | Planning layer for agent-built products that keeps Markdown tasks and dependencies in a Git repo and shows what is ready, blocked or waiting, with a CLI, agent skill, plugins and a board. |
| [robertpitt/cycle](https://github.com/robertpitt/cycle) | 16 | 2026-06-10 | Local-first ticket system backed by a Git repository, storing tickets, comments, plans and reviews alongside the code so humans and agents share the same history. |

### Agent sessions, usage & observability

Tools that capture, replay, search or measure coding-agent sessions, covering token and cost usage, transcripts and links between prompts and commits.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [ccusage/ccusage](https://github.com/ccusage/ccusage) | 19k | 2025-05-29 | CLI that analyzes token usage and cost for coding-agent tools from their local data files, run via `npx ccusage`. |
| [entireio/cli](https://github.com/entireio/cli) | 5.2k | 2026-01-02 | Go CLI that hooks into Git to capture AI agent sessions and index them alongside commits, giving a searchable record of prompts, responses and files touched. |
| [git-ai-project/git-ai](https://github.com/git-ai-project/git-ai) | 2.8k | 2025-07-02 | Git extension that links every AI-generated line in a repo to the agent, model and prompts that produced it, so the intent survives past the commit. |
| [cosmtrek/mindwalk](https://github.com/cosmtrek/mindwalk) | 1.4k | 2026-07-09 | Go tool that replays coding-agent sessions on a 3D map of the codebase, showing which parts of the repo the agent explored and treated as relevant. |
| [specstoryai/getspecstory](https://github.com/specstoryai/getspecstory) | 1.4k | 2024-12-13 | Local-first extensions for AI IDEs and terminal agents that capture and index conversation history, with options to sync to the cloud and turn histories into reusable skills. |
| [waynesutton/opensync](https://github.com/waynesutton/opensync) | 410 | 2026-01-17 | Cloud-synced dashboards for OpenCode, Claude Code, Codex, Cursor and Factory Droid that track session activity, tool usage and token spend, with semantic search and eval dataset export. |
| [Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail) | 224 | 2025-07-12 | Rust token-usage and cost monitor that reads local session data for Claude Code, Codex, Gemini, Qwen Code, Cline, Copilot, OpenCode and other agents, with real-time tracking. |
| [robertoshimizu/session-graph](https://github.com/robertoshimizu/session-graph) | 114 | 2026-02-20 | Python pipeline that turns AI coding sessions from Claude Code, ChatGPT, DeepSeek, Grok and Warp into an RDF knowledge graph with a W3C ontology, Wikidata entity linking and SPARQL queries. |
| [ssreeni1/tracebase](https://github.com/ssreeni1/tracebase) | 79 | 2026-05-26 | Imports local Codex and Claude session transcripts, encrypts raw events at rest, and serves a searchable localhost dashboard plus MCP access for inspecting what an agent did. |
| [dadlerj/tin](https://github.com/dadlerj/tin) | 64 | 2025-12-30 | Version-control layer that treats AI coding conversations as first-class artifacts, permanently linked to the code they produced, in the manner of git. |
| [saint0x/tl](https://github.com/saint0x/tl) | 17 | 2026-01-02 | Rust version-control layer built on Jujutsu that records a checkpoint on every file change so any working state from an AI-assisted session can be restored. |
| [captainsafia/stitch](https://github.com/captainsafia/stitch) | 11 | 2025-12-28 | Tool for recording the intent behind code changes ("stitches") and binding it to git commits and diffs, forming an intent DAG that linear history cannot express. |

## Agent skills

### Skill collections & packs

Bundles of agent skills and plugins grouped around a theme or vendor, such as science, UI design, screenwriting, Rails or a particular API.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 52.1k | 2025-10-19 | Library of 177 agent skills plus 100+ scientific database integrations for biology, chemistry, medicine and drug discovery. Follows the Agent Skills standard for Claude Code, Cursor and Codex. |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | 25.6k | 2025-10-09 | Plugin of 36 skills for coding agents including Claude Code, Codex and Cursor, structured around a loop of brainstorm, plan, build, review and capture. |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 18.2k | 2025-12-21 | Open collection of agent skills on context engineering and harness engineering: curating context, designing agent operating loops and evaluating agent behavior. |
| [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | 13.7k | 2026-03-17 | MiniMax's pack of development skills for AI coding agents, giving structured guidance for frontend, fullstack, Android, iOS and shader work. Marked beta. |
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | 8k | 2026-07-10 | Collection of agent skills for building interfaces, covering UI, typography, color, accessibility, layout and product writing, based on the author's design engineering writing. |
| [CloudAI-X/threejs-skills](https://github.com/CloudAI-X/threejs-skills) | 3.6k | 2026-01-19 | Collection of Three.js skill files that give Claude Code API details, best practices and patterns for creating 3D elements and interactive experiences. |
| [jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) | 1.7k | 2026-09-06 | 26 agent skills for Claude Code and Codex covering screenwriting, television writing and dramaturgy, distilled from 47 craft books and 23 volumes of published scripts. |
| [rjs/shaping-skills](https://github.com/rjs/shaping-skills) (archived) | 1.4k | 2026-01-29 | Claude Code skills for Shape Up shaping and breadboarding adapted to work with an LLM. The author marks them obsolete since Opus 4.6. |
| [marckohlbrugge/37signals-skills](https://github.com/marckohlbrugge/37signals-skills) | 726 | 2025-12-17 | Unofficial agent skills and reference guide that teach coding assistants to write Rails the 37signals way, extracted from Fizzy, Campfire and over 100 of DHH's code reviews. |
| [kitlangton/skills](https://github.com/kitlangton/skills) | 350 | 2026-07-15 | Kit Langton's personal agent skills, mainly a guide to production TypeScript with Effect v4. |
| [perplexityai/api-platform-developers](https://github.com/perplexityai/api-platform-developers) | 81 | 2026-07-15 | Official Perplexity API Platform skills published as portable Agent Skills for Claude Code, Codex CLI and other clients. The repository doubles as a Claude Code plugin marketplace. |
| [lassejlv/skills](https://github.com/lassejlv/skills) | 67 | 2026-04-30 | Personal multi-skill repository of agent skills, with one directory per skill and scripts to validate and install them individually or all at once. |

### Visual & media output skills

Skills whose output is visual or media: diagrams, slides, illustrations, posters, SVGs and launch videos.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 98.3k | 2026-02-19 | Agent skills that push coding agents toward better frontend design through art direction, reference images and a browser check, to avoid generic AI-looking pages. |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | 30.8k | 2026-01-28 | Coding-agent skill, packaged as a Claude Code plugin, that creates HTML presentations from scratch or by converting PowerPoint files. SKILL.md is readable by other agents. |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | 16.4k | 2026-06-16 | Agent skill invoked as /brag that turns a finished project into a short shareable launch video, with music, motion and share copy, rendered through Hyperframes. |
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | 14.9k | 2026-10-08 | Agent skill that explains an idea by building it as an interactive isometric illustration of a machine or system, made of many small parts in SVG with optional WebGL and 3D effects. |
| [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | 12.6k | 2026-05-27 | Codex skill that generates hand-drawn 16:9 white-background illustrations for Chinese articles, using the Xiaohei character and sparse red, orange and blue annotations. |
| [tw93/Kami](https://github.com/tw93/Kami) | 12k | 2026-04-20 | Layout rules and templates that let AI agents export documents as PDF, PNG and editable PowerPoint, with eight built-in document templates and a landing page. |
| [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | 10.5k | 2026-02-16 | Agent skill that turns terminal-style explanations such as architecture, diff reviews, plan audits and recaps into self-contained styled HTML pages or slide decks instead of ASCII art. |
| [Cocoon-AI/architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) | 7.5k | 2025-12-22 | Claude skill that generates dark-themed system architecture diagrams from a plain description, output as standalone HTML/SVG files that open in any browser. |
| [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | 7.3k | 2026-07-12 | Codex skill that turns a theme, sentence, object or reference set into a sparse, paper-textured zine-style editorial poster, an image prompt or a reusable visual system. |
| [YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill](https://github.com/YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill) | 1.9k | 2026-01-21 | Skill for OpenClaw and Claude Code that searches a library of 10,000+ Nano Banana Pro (Gemini) image prompts by use case and can remix them, with sample images. |
| [inkboard/system-atlas](https://github.com/inkboard/system-atlas) | 438 | 2026-08-20 | Agent skill that turns an architecture discussion into an explorable isometric atlas, generated from one data file together with an interactive map and a SYSTEM.md. |
| [1weiho/cinematic-shot](https://github.com/1weiho/cinematic-shot) | 133 | 2026-10-13 | Agent skill for directing cinematic product-launch films built from hero shots, each a steep oblique close-up of real UI floating on a stage. |
| [fiberplane/bs](https://github.com/fiberplane/bs) | 5 | 2026-03-16 | Claude Code skill that writes plans as Markdown with directives for callouts, cards, labels, mermaid diagrams and file trees. The Fiberplane desktop app renders them in a consistent design. |
| [iannuttall/png2svg](https://github.com/iannuttall/png2svg) | 4 | 2026-07-25 | Agent-guided workflow that rebuilds PNG logos, icons and monograms as clean parametric SVGs by measuring the raster, fitting a model and scoring renders against the source. |

### Behavior, writing & workflow skills

Skills that shape agent behavior, writing style or working process, such as planning, spec writing, minimal code and plain language.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 165.8k | 2026-06-12 | Skill that nudges coding agents toward minimal code by writing less and reusing more. Its README reports benchmark gains in code size, time, cost and tokens in Claude Code. |
| [blader/humanizer](https://github.com/blader/humanizer) | 57.8k | 2026-01-18 | Agent skill that rewrites text to remove signs of AI-generated writing, based on Wikipedia's Signs of AI writing guide, without changing the meaning. |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 57.5k | 2026-05-13 | Skill that stops coding agents from burying the answer: output is action-first with numbered steps and no filler pleasantries. Install instructions are provided for several agent CLIs. |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 27.5k | 2026-01-03 | Skill and hooks that keep a Manus-style Markdown plan on disk, re-injected each turn and recoverable after /clear or compaction, with a completion gate. Works across Claude Code, Codex, Cursor and others. |
| [ast-grep/agent-skill](https://github.com/ast-grep/agent-skill) | 892 | 2025-11-16 | Claude Code plugin marketplace shipping an ast-grep skill that teaches agents to search code structurally using AST patterns rather than text matching. |
| [dmmulroy/cloudflare-skill](https://github.com/dmmulroy/cloudflare-skill) | 726 | 2026-01-12 | OpenCode skill bundling Cloudflare platform reference docs for LLM consumption, covering Workers, Pages, KV, D1, R2, Workers AI, Vectorize, networking, security and infrastructure-as-code. |
| [docwriter-org/plain-writing-skill](https://github.com/docwriter-org/plain-writing-skill) | 710 | 2026-06-15 | Agent skill with plain-text rules that make an AI agent write in a plain style and check its own output, plus evals and a revision view that shows what changed. |
| [zscole/adversarial-spec](https://github.com/zscole/adversarial-spec) | 556 | 2026-01-11 | Claude Code plugin that refines product specs by having multiple LLMs critique each other iteratively until they reach consensus, to catch gaps a single model would miss. |
| [zscole/model-hierarchy-skill](https://github.com/zscole/model-hierarchy-skill) | 346 | 2026-02-11 | OpenClaw skill that routes agent tasks to cheaper or stronger models by complexity, so routine work like file reads and formatting does not run on expensive models. |
| [LeoYeAI/teammate-skill](https://github.com/LeoYeAI/teammate-skill) | 258 | 2026-03-31 | Skill that distills a teammate into an agent work skill and a five-layer persona by collecting Slack, Teams and GitHub data. Works with Claude Code, OpenClaw and other AgentSkills agents. |
| [blader/schematic](https://github.com/blader/schematic) | 246 | 2026-02-15 | Claude Code and Codex skill that reverse-engineers a detailed product and technical specification from the implementation on a git branch. |
| [blader/theorist](https://github.com/blader/theorist) | 192 | 2026-02-28 | Codex and Claude skill that keeps a per-repo THEORY.MD at the repository root, recording the problem thesis, current system model, strategy rationale and open uncertainties. |

### Skill specs, registries & testing

Skill specs, package managers, registries, routers and testing tools for creating, validating and distributing agent skills.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | 26.2k | 2025-12-16 | Specification and documentation for the Agent Skills format: a skill is a folder containing a SKILL.md file with instructions that extend an agent's capabilities. |
| [tripleyak/SkillForge](https://github.com/tripleyak/SkillForge) | 910 | 2025-12-30 | Skill creator for Claude Code and Codex that builds skills through baseline-tested generation with per-skill regression evals, an ecosystem doctor and cross-runtime compilation. |
| [modiqo/skillspec](https://github.com/modiqo/skillspec) | 707 | 2026-06-19 | Rust CLI that turns SKILL.md files into structured, testable contracts, with a Doctor risk report, guided imports and proof that an agent followed the skill. |
| [skilld-dev/skilld](https://github.com/skilld-dev/skilld) | 327 | 2026-02-03 | Open-source, privacy-friendly CLI behind the skilld.dev registry, used to find, preview, run and watch Agent Skills. Offered as a skills.sh alternative for humans and agents. |
| [rosieskills/rosie](https://github.com/rosieskills/rosie) | 157 | 2026-01-24 | Cross-platform package manager for AI agent skills, written in Rust, with a lockfile and a typed JavaScript API. Installable via npm, Homebrew and other package managers. |
| [GodsBoy/jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router) | 29 | 2026-09-16 | Typed, confidence-aware router that picks agent skills using TypeSafe Jev. Reports 68 of 72 synthetic requests routed correctly versus 51 for a lexical baseline. |

## Agent sandboxes & execution

### Agent VM & container sandboxes

MicroVM, VM and container sandboxes for running agents or untrusted agent code, locally or hosted, plus tooling around them.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 15.9k | 2025-12-17 | Self-hosted sandbox runtime for AI agents that starts on Docker and deploys on Kubernetes behind one API for executing code, running commands, managing files and operating browsers or desktops. |
| [superradcompany/microsandbox](https://github.com/superradcompany/microsandbox) | 8.7k | 2024-10-03 | Local-first microVM runtime and library with hardware isolation for untrusted workloads such as agents, user code, plugins and CI jobs, with fork and snapshot support. |
| [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | 6.8k | 2025-12-18 | Embeddable, portable microVM runtime with branchable state for running agents locally in isolation; also usable for dev environments and local sandboxing. |
| [agent-infra/sandbox](https://github.com/agent-infra/sandbox) | 6.2k | 2025-08-06 | Single Docker container bundling browser, shell, file tools, Jupyter, MCP and VSCode Server as an all-in-one environment for AI agents. |
| [boxlite-ai/boxlite](https://github.com/boxlite-ai/boxlite) | 2.5k | 2025-12-07 | Embeddable hardware-isolated micro-VM that runs any OCI image and persists across turns, so agents keep installed packages and files; scales from a laptop to an agentic cloud. |
| [zerobootdev/zeroboot](https://github.com/zerobootdev/zeroboot) | 2.5k | 2026-03-15 | Firecracker-based VM sandboxes for AI agents that spawn in under a millisecond by forking a snapshot copy-on-write, with a README benchmark claiming roughly 265KB of memory per sandbox. |
| [earendil-works/gondolin](https://github.com/earendil-works/gondolin) | 2.3k | 2026-02-03 | Experimental local Linux micro-VM agent sandbox (QEMU by default) with a TypeScript control plane that programs network and filesystem access and injects secrets to limit exfiltration. |
| [CelestoAI/celesto](https://github.com/CelestoAI/celesto) | 1k | 2026-02-15 | Platform providing secure, persistent sandboxed computers for AI agents, including browser and computer use. |
| [trailofbits/coop](https://github.com/trailofbits/coop) | 785 | 2026-04-02 | Rust CLI from Trail of Bits that manages disposable VMs in which Claude Code, Codex and Grok Build run with full tool access (Docker, git, compilers). |
| [madarco/agentbox](https://github.com/madarco/agentbox) | 538 | 2026-05-12 | CLI that launches multiple coding agents in parallel sandboxed VMs with one command, on your machine, self-hosted or in the cloud, with iTerm2, cmux, tmux and herdr integrations. |
| [gominimal/minimal](https://github.com/gominimal/minimal) | 185 | 2025-08-13 | CLI that runs coding agents in isolated boxes on your own machine using user namespaces or VMs, with access limited to what a minimal.toml config grants. |
| [huggingface/hf-sandbox](https://github.com/huggingface/hf-sandbox) (archived) | 159 | 2026-04-27 | Modal-style sandbox API running code on Hugging Face Jobs; the prototype is being upstreamed as a Sandbox API and hf sandbox CLI in huggingface_hub 1.22.0. |
| [computesdk/benchmarks](https://github.com/computesdk/benchmarks) | 130 | 2026-02-18 | Reproducible, provider-neutral benchmarks of sandboxes, object storage, headless browsers and AI gateways, the infrastructure agents run on. All tests are automated. |
| [jasonkneen/Agent-Farm-CLI](https://github.com/jasonkneen/Agent-Farm-CLI) | 68 | 2026-07-08 | CLI (farm) that runs N isolated AI accounts on one Mac, each in its own Apple container VM with separate provider state for claude, codex, grok and gemini, avoiding shared Keychain collisions. |
| [noperator/membrane](https://github.com/noperator/membrane) | 66 | 2025-10-27 | Lightweight cross-platform sandbox for AI agents that is agent-agnostic and gives real-time visibility into everything the agent does, favouring a small, understandable design. |
| [madarco/agentbox-herdr-plugin](https://github.com/madarco/agentbox-herdr-plugin) | 34 | 2026-06-24 | herdr plugin for AgentBox adding a live overlay of your AgentBox sandbox VMs and shortcuts to start a box in the current project. |
| [aezell/sprite-galaxy](https://github.com/aezell/sprite-galaxy) | 23 | 2026-01-10 | Go terminal UI that shows a Fly.io Sprites network as animated nodes in a galaxy view, with real-time running and stopped status for managing sprites. |
| [jbellerb/sprite-hacks](https://github.com/jbellerb/sprite-hacks) | 13 | 2026-02-05 | Scripts and demos from experimenting with Fly Sprites, including a reverse sshfs mount of a local directory and a jj sprite-workspace alias. |
| [janwilmake/sandbox](https://github.com/janwilmake/sandbox) | 5 | 2026-03-24 | Experiment exposing a Cloudflare sandbox terminal as an agent tool, with the user logged into their own stripe, git, gh and wrangler and the sandbox sleeping when idle. |

### Code interpreters & language sandboxes

In-process and language-level sandboxes such as restricted interpreters, WASM isolates, library OSes and code-mode toolkits.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [pydantic/monty](https://github.com/pydantic/monty) | 8.7k | 2023-05-28 | Python interpreter written in Rust for running LLM-generated code, avoiding container latency and cost; the MIT-licensed OSS version targets Python 3.14 syntax. |
| [rivet-dev/agentos](https://github.com/rivet-dev/agentos) | 4.8k | 2024-02-07 | Embeddable Linux-compatible sandbox built on WebAssembly and V8 isolates that gives each agent files, processes, shell and networking in a lightweight OS, claiming faster cold starts than containers. |
| [microsoft/litebox](https://github.com/microsoft/litebox) | 3.2k | 2024-12-11 | Microsoft library OS focused on security that supports both kernel- and user-mode execution for sandboxing. APIs are still evolving. |
| [denoland/ronly](https://github.com/denoland/ronly) | 166 | 2026-03-24 | Linux shell sandbox from Deno that blocks destructive operations at the kernel level, using rootless user namespaces, so untrusted agents can inspect a system read-only. |
| [parcadei/ouros](https://github.com/parcadei/ouros) | 146 | 2026-02-17 | Stateful sandboxed Python runtime in Rust for multi-turn agent code execution, with the ability to fork execution paths, rewind mistakes and call external services without host access. |
| [penberg/chimera](https://github.com/penberg/chimera) | 136 | 2026-05-17 | Userspace sandbox written in Rust that confines untrusted code, such as commands run by coding agents, while still allowing mediated access to the host's files and tools. |
| [bgub/helm](https://github.com/bgub/helm) | 65 | 2026-02-26 | Typed TypeScript code-mode framework where agents call typed functions instead of parsing CLI stdout, with permission controls and tool search. |

### Agent workspaces & virtual filesystems

Copy-on-write workspaces and virtual filesystems that give agents cheap, isolated or API-backed file trees.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [anomalyco/rift](https://github.com/anomalyco/rift) | 1.3k | 2026-05-31 | Rust tool that creates instant copy-on-write workspace snapshots of a project, for coding agents and parallel work. Marked early software. |
| [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs) | 1.2k | 2026-03-29 | Go FUSE driver that mounts large git repos as working trees right away and hydrates file contents on demand, aimed at agents and sandboxes where startup time matters. Beta. |
| [antfu/ghfs](https://github.com/antfu/ghfs) | 276 | 2026-03-04 | Syncs open GitHub issues and pull requests into a local .ghfs directory for offline viewing and batch operations by humans and agents. README says work in progress. |
| [0xff-ai/omnifs](https://github.com/0xff-ai/omnifs) | 87 | 2026-04-12 | FUSE filesystem that projects external systems such as GitHub, DNS, arXiv, Linear, Kubernetes and SQLite as directories and files that agents can read with ls, cat and grep. |

## Agent memory, context & retrieval

### Agent memory systems

Persistent memory layers that carry facts and experience across agent sessions, harnesses and devices.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 101.3k | 2025-08-31 | Plugin that records what an agent does during sessions, compresses it with AI and injects relevant context into later sessions, supporting Claude Code, Codex, Gemini, OpenCode and others. |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 67.3k | 2023-06-20 | Memory layer for AI agents and apps that stores and retrieves long-term memories through an API, with a README-reported memory algorithm benchmarked on LoCoMo and LongMemEval. |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 40.2k | 2026-01-05 | Context database for agents that unifies memory, RAG knowledge and skills under a single virtual filesystem, with self-evolving context. |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 29.5k | 2026-04-07 | Team-level memory hub that turns conversations, docs and code into four shared assets (chat memory, skills, LLM wiki, code graph) governed and reused across agents and frameworks. |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | 17.2k | 2025-07-24 | LLM-, datastore- and framework-agnostic memory infrastructure that turns agent actions and conversations into structured persistent state, deployable on managed cloud, VPC or on-premises. |
| [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | 14.6k | 2025-07-29 | Agent-driven personal memory system that stores memory as a wiki shared across sessions, agents and devices. |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 11.9k | 2025-07-06 | Memory operating system for LLM agents offering persistent memory, hybrid retrieval and cross-task skill reuse, with a DeepSeek Harness integration and a local memory viewer. |
| [aiming-lab/SimpleMem](https://github.com/aiming-lab/SimpleMem) | 3.8k | 2026-01-01 | ICML 2026 lifelong memory system for LLM agents that stores, compresses and retrieves text and multimodal memories, usable through MCP or Python. |
| [agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta) | 3.5k | 2026-02-15 | Claude Code plugin that interviews you about how you work and generates a personalised Markdown knowledge system, including folder structure, context files, hooks, navigation maps and note templates. |
| [letta-ai/claude-subconscious](https://github.com/letta-ai/claude-subconscious) | 2.9k | 2026-01-14 | Demo built on the Letta Code SDK where a background Letta agent watches Claude Code sessions, builds memory and feeds guidance back. Not meant for production; Letta Code is the supported route. |
| [zilliztech/memsearch](https://github.com/zilliztech/memsearch) | 2.8k | 2026-02-09 | Cross-agent semantic memory layer for Claude Code, Codex and others, storing memories as Markdown indexed in Milvus, with optional remote reranking. |
| [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) | 1.8k | 2026-05-12 | Memory layer that captures session history across Claude Code, Cursor, Codex, OpenCode and 20+ other harnesses and distills workflows, corrections and debugging patterns into reusable knowledge. |
| [verygoodplugins/automem](https://github.com/verygoodplugins/automem) | 822 | 2025-09-16 | Graph and vector long-term memory service that lets Claude, Cursor, Codex and other assistants recall decisions, preferences and relationships across sessions. |
| [Dicklesworthstone/cass_memory_system](https://github.com/Dicklesworthstone/cass_memory_system) | 448 | 2025-12-07 | Procedural memory for coding agents that turns scattered session history into persistent cross-agent memory, with a JSON mode for agent use. |
| [jumbocontext/cli](https://github.com/jumbocontext/cli) | 278 | 2025-12-05 | CLI that stores project details once and gives Claude, Codex, Copilot and other coding agents persistent memory, session continuity and goal tracking. |
| [glommer/memelord](https://github.com/glommer/memelord) | 197 | 2026-02-17 | In-process per-project persistent memory for coding agents, built on Turso and refined with reinforcement signals, so agents keep project patterns and user corrections across sessions. |
| [Necmttn/ax](https://github.com/Necmttn/ax) | 117 | 2026-05-08 | Local-first tool that observes Claude Code and Codex sessions and turns repeated mistakes and discoveries into lessons injected into later runs, a retro loop for coding agents. |
| [nikita-rulenko/Helixir](https://github.com/nikita-rulenko/Helixir) | 88 | 2025-11-29 | Rust memory control plane that keeps one governed reasoning graph shared across Codex, Claude Code, Cursor and other MCP clients, with full-host and remote-agent deployment modes. |
| [thezpack/personal-context-layer](https://github.com/thezpack/personal-context-layer) | 1 | 2026-07-08 | Local-first MCP server that keeps a live model of your schedule, sleep and cognitive load and hands it to connected AI sessions so they can adapt length and tone. |

### Code intelligence for agents

Indexes, graphs and fetchers that give coding agents structured knowledge of a codebase, its docs or its dependencies.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 74.3k | 2026-01-18 | Pre-indexed local code knowledge graph that auto-syncs on code changes and serves Claude Code, Codex, Gemini, Cursor, OpenCode and other agents, aiming for fewer tokens and tool calls. |
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | 32.2k | 2026-02-26 | Local Tree-sitter code knowledge graph served over MCP and CLI so AI coding tools read only the code relevant to a change during review, with published context-reduction benchmarks. |
| [sentrux/sentrux](https://github.com/sentrux/sentrux) | 3.3k | 2026-03-11 | Pure-Rust architectural sensor, also an MCP server, that scores code quality in real time so AI agents get a feedback loop on structural changes. |
| [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc) | 3k | 2026-01-06 | Rust CLI that fetches and caches source code for packages from npm, PyPI, crates.io and GitHub, returning the cached path so coding agents can read dependency internals. |
| [redhat-et/ripwire](https://github.com/redhat-et/ripwire) | 2.5k | 2026-07-29 | Zero-dependency C++23 CLI and MCP server that gives coding agents a ranked map of a repo (signatures, call graph) and afterwards checks blast radius, tests to run and quality deltas. |
| [justrach/codedb](https://github.com/justrach/codedb) | 1.4k | 2026-03-03 | Zig code intelligence server exposing MCP tools for tree, outline, symbol, search, read, edit, dependency and snapshot queries, including remote GitHub repos. |
| [JordanCoin/codemap](https://github.com/JordanCoin/codemap) | 701 | 2025-11-24 | Go CLI that resolves real imports, reports what breaks if a file changes and flags what it could not resolve, giving coding agents structural context at session start via codemap setup. |
| [glommer/codemogger](https://github.com/glommer/codemogger) | 347 | 2026-02-24 | Code indexing library and MCP server that chunks source by tree-sitter units, embeds them locally and stores vector and full-text indexes in one SQLite file per codebase, with no server or API keys. |
| [iannuttall/librarian](https://github.com/iannuttall/librarian) | 100 | 2026-01-04 | Local CLI that fetches and indexes developer documentation from GitHub repos and public websites so coding agents can search current docs instead of guessing. Needs Bun at runtime. |
| [joelhooks/pi-ast-grep](https://github.com/joelhooks/pi-ast-grep) | 27 | 2026-06-23 | Package for the pi coding agent that exposes ast-grep outline and structural search as agent tools, pinning a specific ast-grep CLI version. |
| [siliconjungle/-shapeshift-labs-loom](https://github.com/siliconjungle/-shapeshift-labs-loom) | 13 | 2026-06-10 | Project-level CLI that creates a .loom workspace, scans source into a content-addressed semantic graph and coordinates agent swarms, with Frontier language tooling. |

### RAG, knowledge graphs & context layers

RAG pipelines, GraphRAG, knowledge-graph extraction and context layers that turn documents and data into retrievable knowledge.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 39.2k | 2025-04-01 | Vectorless RAG that builds a tree-structured index of a document and has an LLM reason over it to retrieve context, with no vector database or chunking. |
| [getzep/graphiti](https://github.com/getzep/graphiti) | 31.9k | 2024-08-08 | Python framework from Zep for building real-time temporal knowledge graphs that track how facts change over time, for use by AI agents. |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | 14.1k | 2025-06-25 | Python framework that ingests enterprise data into context graphs and knowledge graphs, with graph analytics, causal reasoning and provenance for auditable AI systems. |
| [StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN) | 13k | 2025-06-09 | Local, private RAG engine for personal data that uses a very small vector index, claiming 97% storage savings; accompanies an MLSys 2026 paper. |
| [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | 10.3k | 2026-05-29 | Research codebase for retrieval-augmented generation that indexes and searches web page screenshots rather than parsed text, accompanying the PixelRAG paper from Berkeley. |
| [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | 4.8k | 2026-04-04 | CLI that compiles raw documents into a structured LLM wiki following Google's Open Knowledge Format, with reasoning-based retrieval and no vector database. |
| [rahulnyk/knowledge_graph](https://github.com/rahulnyk/knowledge_graph) | 4.2k | 2023-10-22 | Notebook code that converts a text corpus into a knowledge graph, intended for graph-augmented generation and knowledge-graph-based QA. |
| [trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph) | 2.8k | 2024-07-10 | Platform pairing ontology-grounded context graphs with deterministic governance, enforcing business rules before agent actions and keeping decision evidence. |
| [raphaelmansuy/edgequake](https://github.com/raphaelmansuy/edgequake) | 2.3k | 2025-12-21 | Rust GraphRAG server inspired by LightRAG that turns documents into a knowledge graph and answers with sources; runs as one binary on Postgres with cloud or local LLMs. |
| [Kaelio/ktx](https://github.com/Kaelio/ktx) | 1.6k | 2026-05-10 | Context layer for data and analytics agents that builds approved metric definitions, joinable columns and business knowledge so Claude Code, Codex and others query a warehouse accurately. |
| [stair-lab/kg-gen](https://github.com/stair-lab/kg-gen) | 1.3k | 2024-10-30 | Python library, from a NeurIPS 2025 paper, that uses LLMs to extract knowledge graphs from any text, with an MCP server and experiments. |
| [lyon-industries/graphrag-workbench](https://github.com/lyon-industries/graphrag-workbench) | 738 | 2025-09-04 | Local desktop-style workbench wrapping Microsoft GraphRAG with document prep, indexing controls, project management and a Three.js 3D view of entities, relationships and communities. |
| [rahulnyk/graph_maker](https://github.com/rahulnyk/graph_maker) | 732 | 2024-05-01 | Python library, shown in notebooks, that converts text into a knowledge graph using an LLM and a user-supplied ontology. |
| [automataIA/graphrag-rs](https://github.com/automataIA/graphrag-rs) | 531 | 2025-09-21 | Modular Rust GraphRAG implementation that builds knowledge graphs from documents and answers natural-language queries, deployable server-only, WASM-only in the browser, or hybrid, with local LLM support. |

### Semantic & hybrid search

Local and hybrid search engines and CLIs, lexical, embedding or multi-vector, for finding things in code and documents.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [tobi/qmd](https://github.com/tobi/qmd) | 30.5k | 2025-12-08 | On-device CLI search engine for Markdown notes, transcripts and docs that combines BM25, vector search and local LLM re-ranking, aimed at agentic workflows. |
| [mixedbread-ai/mgrep](https://github.com/mixedbread-ai/mgrep) | 4.4k | 2025-11-06 | CLI for natural-language semantic search over code, images and PDFs, with built-in web search and integrations for coding agents. |
| [Ryandonofrio3/osgrep](https://github.com/Ryandonofrio3/osgrep) | 1.1k | 2025-11-21 | Local semantic search CLI for coding agents that answers natural-language queries like grep, with call-graph tracing via a trace command and role detection. |
| [lightonai/next-plaid](https://github.com/lightonai/next-plaid) | 594 | 2026-01-06 | NextPlaid multi-vector search engine plus ColGREP, a local semantic code search CLI for terminals and coding agents that combines regex filtering with semantic ranking. |
| [dropbox/witchcraft](https://github.com/dropbox/witchcraft) | 524 | 2026-03-24 | Dropbox's from-scratch safe-Rust reimplementation of Stanford's XTR-Warp multi-vector semantic search, backed by one SQLite file and able to run entirely on-device. |
| [Dicklesworthstone/frankensearch](https://github.com/Dicklesworthstone/frankensearch) | 87 | 2026-02-13 | Rust hybrid search library and fsfs CLI that returns fast first-pass results from a small embedding model, then refines them with MiniLM, fusing Tantivy BM25 and vector scores via Reciprocal Rank Fusion. |

### Token & context-window optimization

Tools that cut tokens sent to or from LLMs: output compressors, compact formats, token counters and tool-list routers.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 83.7k | 2026-01-22 | Single-binary Rust CLI proxy that filters and compresses output of common developer commands before it reaches the LLM, claiming 60-90% token reduction. |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 75.6k | 2026-01-07 | Library, proxy and MCP server that compresses tool outputs, logs, files, RAG chunks and conversation history before they reach the LLM, claiming 20% fewer tokens for coding agents and more for JSON. |
| [toon-format/toon](https://github.com/toon-format/toon) | 25.5k | 2025-10-22 | Token-Oriented Object Notation, a compact human-readable encoding of the JSON data model for LLM prompts, with a TypeScript SDK, CLI, spec and benchmarks. |
| [nicobailon/pi-boomerang](https://github.com/nicobailon/pi-boomerang) | 307 | 2026-03-02 | Extension for the pi coding agent that runs a task autonomously, then replaces its raw turn history in later context with a handoff summary to save tokens. |
| [Hmbown/aleph](https://github.com/Hmbown/aleph) | 218 | 2025-12-15 | MCP server and skill implementing Recursive Language Models by keeping search indexes, code execution and evidence in a Python process outside the prompt window. |
| [lirantal/tokenu](https://github.com/lirantal/tokenu) | 66 | 2026-03-09 | Unix du-style CLI that counts LLM tokens per file and directory to show which folders consume the most context window. |
| [fkiene/llmtrim-herdr](https://github.com/fkiene/llmtrim-herdr) | 55 | 2026-06-28 | herdr plugin that routes each agent pane's requests through the llmtrim compressing proxy and shows per-pane token savings in a badge. |
| [effortprogrammer/mcpflow-router](https://github.com/effortprogrammer/mcpflow-router) | 37 | 2026-02-10 | Gateway for OpenCode that sends the LLM only the MCP tools relevant to each query instead of every configured tool definition, saving context. |

## Agent tools & integrations

### MCP platforms & tool plumbing

Generic infrastructure for hosting, proxying and calling tools, including MCP managers and OpenAPI-to-agent bridges.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [openclaw/mcporter](https://github.com/openclaw/mcporter) | 5.1k | 2025-11-05 | TypeScript runtime and CLI for discovering and calling MCP servers, exposing them as a typed TypeScript API or packaging them as standalone CLIs. |
| [UsefulSoftwareCo/executor](https://github.com/UsefulSoftwareCo/executor) | 4.2k | 2026-02-07 | Open-source integration layer where MCP servers, OpenAPI specs and GraphQL APIs are configured once with auth and per-tool policies, then exposed as one catalog to any MCP-compatible agent. |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | 2.3k | 2025-03-12 | Platform for running and managing MCP servers in isolated containers, adding access policy, secrets handling and observability. |
| [hyper-mcp-rs/hyper-mcp](https://github.com/hyper-mcp-rs/hyper-mcp) | 883 | 2025-01-10 | Rust MCP server whose capabilities are extended through WebAssembly plugins distributed via OCI registries; works with Claude Desktop, Cursor and other MCP clients. |
| [awslabs/run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) | 380 | 2025-03-21 | AWS Labs library, with Python and npm packages, for running existing stdio-based MCP servers inside AWS Lambda functions. |
| [agoda-com/api-agent](https://github.com/agoda-com/api-agent) | 293 | 2026-01-11 | MCP server that wraps any GraphQL or REST API for natural-language queries, loading responses into DuckDB so SQL ranking, filtering and joins work even if the API lacks them. |
| [vercel-labs/specli](https://github.com/vercel-labs/specli) | 127 | 2026-01-18 | Turns any OpenAPI spec, from a URL or file, into a CLI or compiled executable that agents can call. |

### Service connectors (MCP servers, API CLIs & clients)

Connectors, MCP servers and agent-friendly CLIs that wrap one external service or API.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [better-auth/better-icons](https://github.com/better-auth/better-icons) | 1.4k | 2026-01-22 | CLI and MCP server, also installable as a skill, for searching and retrieving over 200,000 icons from 150+ collections. |
| [xdevplatform/xurl](https://github.com/xdevplatform/xurl) | 1.4k | 2024-12-14 | Official curl-like CLI for the X API supporting OAuth 1.0a and OAuth 2.0 PKCE, with multiple registered apps and tokens. |
| [kentcdodds/kody](https://github.com/kentcdodds/kody) | 806 | 2026-03-18 | Cloudflare Workers service speaking MCP that stores an agent's memory, keys, code and automations so they stay portable across MCP hosts. |
| [Infatoshi/x-cli](https://github.com/Infatoshi/x-cli) | 429 | 2026-02-14 | Python CLI that calls the X/Twitter API v2 directly to post, search, read timelines, like and bookmark; shares credentials with the author's x-mcp server. |
| [CrowdStrike/falcon-mcp](https://github.com/CrowdStrike/falcon-mcp) | 270 | 2025-06-10 | CrowdStrike MCP server that connects AI agents to Falcon detections, threat intel and hosts for security analysis and threat hunting. |
| [openclaw/goplaces](https://github.com/openclaw/goplaces) | 261 | 2026-01-02 | Go client library and CLI for the Google Places and Routes APIs. |
| [jaredpalmer/mogcli](https://github.com/jaredpalmer/mogcli) | 213 | 2026-02-12 | Unofficial Microsoft Graph CLI for personal and Entra ID accounts, covering mail, calendar, contacts, groups, tasks and OneDrive, with multiple profiles and an agent-friendly design. |
| [jeizzon/yarn-threads-cli](https://github.com/jeizzon/yarn-threads-cli) | 28 | 2026-01-29 | TypeScript CLI for Threads to post, reply, quote, read threads, search users and browse profiles from a terminal or an agent. |
| [code-yeongyu/agent-messenger](https://github.com/code-yeongyu/agent-messenger) | 22 | 2026-01-31 | CLI that lets agents read and send messages across Slack, Discord, Teams, Webex, Telegram, WhatsApp and other messengers. |
| [glassBead-tc/audius-mcp-atris](https://github.com/glassBead-tc/audius-mcp-atris) | 5 | 2025-02-01 | Effect-TS MCP server for the Audius music platform that replaces 100+ tools with two meta-tools, search and execute, running agent code in a QuickJS WASM sandbox. |

### Browser & computer-use automation

Browser, desktop and terminal-UI automation that lets agents drive real applications.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 44.1k | 2026-01-11 | Native Rust CLI for browser automation by AI agents, installable globally or as a pinned project dependency. |
| [alibaba/page-agent](https://github.com/alibaba/page-agent) | 29.5k | 2025-09-23 | In-page JavaScript GUI agent that you embed in a web page to control its interface from natural-language instructions, with no external browser driver. |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 23.1k | 2026-09-16 | Browser agent from Browser Use with a dynamic, indexed action space, where an LLM picks an operation and element to complete a goal quickly and cheaply. |
| [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | 18.5k | 2026-04-17 | Harness that lets Claude Code, Codex or Cursor drive your real logged-in Chrome over the DevTools Protocol, with the agent writing missing helpers as it works. |
| [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | 10.4k | 2026-02-15 | Standalone Go HTTP server, usually run as a user daemon, that gives agents control of multiple Chrome instances, with stealth injection and a real-time dashboard. |
| [hyperbrowserai/hyperbrowser-app-examples](https://github.com/hyperbrowserai/hyperbrowser-app-examples) | 1.9k | 2025-05-28 | Collection of complete example web apps built on the Hyperbrowser browser automation and scraping platform. |
| [kernel/kernel-images](https://github.com/kernel/kernel-images) | 1.1k | 2025-02-27 | Sandboxed Chrome browser images behind the Kernel hosted browsers-as-a-service platform, usable from DevTools-based frameworks such as Playwright and Puppeteer. |
| [0xSero/parchi](https://github.com/0xSero/parchi) | 550 | 2025-11-07 | Chrome and Firefox side-panel extension for chat-driven browser automation: navigate, read, click, type, extract and summarize. |
| [remorses/tuistory](https://github.com/remorses/tuistory) | 367 | 2025-12-04 | Wraps terminal commands and TUIs in named background sessions that agents can read, wait on, screenshot and type into, and that humans can attach to; Playwright-style control for terminal apps. |
| [RichardHruby/login-machine](https://github.com/RichardHruby/login-machine) | 293 | 2026-02-09 | Browser agent loop that logs into arbitrary websites by having Claude classify each screen while Playwright acts, with credentials flowing straight into the DOM rather than through the model. |
| [timpratim/macbrow](https://github.com/timpratim/macbrow) | 157 | 2026-09-18 | Experimental voice prototype that runs spoken commands as AppleScript on a Mac or drives Chrome for web tasks, using a small model that chooses a route rather than generating one. |
| [0xSero/sitegeist](https://github.com/0xSero/sitegeist) | 98 | 2026-03-16 | Browser sidebar AI assistant that automates web tasks, extracts data and fills forms under user guidance, plus a bridge that lets coding agents use the same browser. |
| [aduermael/wb](https://github.com/aduermael/wb) | 66 | 2026-06-20 | macOS 26+ command-line browser for agents built on system web views, with persistent sessions, compact JSON output, screenshots, clicks, forms and JS eval, without bundling Chromium or a driver server. |
| [supermemoryai/preprint](https://github.com/supermemoryai/preprint) | 22 | 2026-05-25 | Rust daemon that projects a live Chromium browser as a filesystem of markdown, actions, diffs, logs and artifacts, so agents drive the web by reading and writing files instead of using CDP. |

### Web crawling & scraping

Crawlers, scrapers and HTML-to-Markdown converters that turn web content into clean data for LLMs.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 192.4k | 2024-04-15 | Web crawling and scraping API that turns sites into LLM-ready Markdown and structured data, handling JavaScript-heavy pages; open source with a hosted service. |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 88.2k | 2024-10-13 | Adaptive Python scraping framework covering single requests to full crawls, with anti-bot fetchers, spiders, proxy rotation, a parser that adapts to site changes, a CLI and an MCP server. |
| [Y2Z/monolith](https://github.com/Y2Z/monolith) | 15.5k | 2017-02-20 | CLI, GUI and library in Rust that bundles a web page with its CSS, images and scripts into a single self-contained HTML file. |
| [watercrawl/WaterCrawl](https://github.com/watercrawl/WaterCrawl) | 2.2k | 2024-12-15 | Self-hostable web crawling application built on Django and Scrapy that turns web pages into LLM-ready data, with a hosted option and API. |
| [harlan-zw/mdream](https://github.com/harlan-zw/mdream) | 1k | 2025-04-16 | HTML-to-Markdown converter tuned for LLM input, with Rust and JavaScript engines and streaming support. |
| [paulpierre/markdown-crawler](https://github.com/paulpierre/markdown-crawler) | 476 | 2023-10-24 | Multithreaded Python crawler that recursively walks a website and writes one Markdown file per page, intended for chunking in RAG pipelines. |
| [needle-tools/md-browse](https://github.com/needle-tools/md-browse) | 256 | 2026-02-07 | Electrobun desktop browser that shows pages as Markdown, using Accept: text/markdown when a site supports it and converting HTML otherwise, to show the web as AI tools see it. |
| [mdowis/anansi](https://github.com/mdowis/anansi) | 117 | 2026-05-14 | Self-healing Python scraper that repairs broken selectors, falls back to browser rendering, and uses Chrome TLS fingerprints and personas against bot detection; ships an MCP server so an LLM can drive crawls. |
| [firecrawl/opencode-firecrawl](https://github.com/firecrawl/opencode-firecrawl) | 101 | 2026-02-10 | OpenCode plugin that adds Firecrawl web scraping, crawling and search plus lookups against the Firecrawl developer index and Alexandria providers. |

### Document parsing, OCR & extraction

PDF parsers, OCR models and extraction libraries that turn documents into LLM-ready text or structured data.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [google/langextract](https://github.com/google/langextract) | 39k | 2025-07-08 | Python library that uses LLMs to extract structured information from unstructured text with precise source grounding and interactive visualization. |
| [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | 29.7k | 2025-05-13 | Java-based open-source PDF parser that outputs Markdown, JSON with bounding boxes or HTML for AI pipelines, with a PDF accessibility automation angle. |
| [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | 19.7k | 2026-02-06 | Rust library, with npm and Python bindings, that classifies PDFs as text-based or scanned, extracts position-aware text and converts it to Markdown to support routing to OCR. |
| [datalab-to/chandra](https://github.com/datalab-to/chandra) | 12.5k | 2025-10-08 | OCR model from Datalab that converts images and PDFs into HTML, Markdown or JSON while preserving layout, covering complex tables, forms and handwriting. |
| [lumina-ai-inc/chunkr](https://github.com/lumina-ai-inc/chunkr) | 4.2k | 2024-08-24 | Document intelligence API that does layout analysis, OCR with bounding boxes and semantic chunking to turn PDFs, Office files and images into structured HTML or Markdown chunks; the open version is AGPL. |
| [shift-labs-ai/markit](https://github.com/shift-labs-ai/markit) | 1.3k | 2026-03-25 | Rust CLI and library that converts PDF, Office files, HTML, EPUB, Jupyter, RSS, images, audio and URLs to Markdown, using built-in Rust engines for several formats. |
| [datalab-to/lift](https://github.com/datalab-to/lift) | 1.2k | 2026-06-03 | 9B vision model that extracts JSON matching a caller-supplied schema from PDFs and images, using schema-constrained decoding to guarantee valid output. |

## Models, inference & LLM access

### LLM inference engines & serving

Engines and serving layers for running LLMs fast, from datacenter GPU servers to Apple Silicon, browsers and consumer hardware.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 94k | 2023-02-09 | Widely used LLM inference and serving engine focused on high throughput and memory efficiency, with an OpenAI-compatible server. |
| [JustVugg/colibri](https://github.com/JustVugg/colibri) | 42.5k | 2026-07-01 | Dependency-free C engine that runs very large mixture-of-experts models on modest hardware by keeping active experts in RAM and streaming the rest from disk. |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | 39.1k | 2023-06-12 | Python library that runs 70B-class LLMs on a single 4GB GPU by loading model layers on demand, without quantization, distillation or pruning. |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 37.2k | 2024-01-08 | Open-source serving framework for large language, vision-language and diffusion models, optimized for agentic workloads, large-scale serving and RL rollouts. |
| [antirez/ds4](https://github.com/antirez/ds4) | 23.9k | 2026-05-06 | Small native inference engine optimized for DeepSeek V4 Flash and a few other large models on consumer hardware, with Metal, CUDA and ROCm backends. |
| [mlc-ai/web-llm](https://github.com/mlc-ai/web-llm) | 19.3k | 2023-04-13 | In-browser LLM inference engine that runs models locally on WebGPU, exposing an OpenAI-style API from the MLC LLM project. |
| [LMCache/LMCache](https://github.com/LMCache/LMCache) | 12.1k | 2024-05-28 | KV-cache management layer for LLM serving that integrates with vLLM, reusing cached key/value state to reduce latency and compute in scalable inference. |
| [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | 7k | 2026-06-12 | Rust inference engine that autotunes its kernels for your hardware to run each model as fast as possible. Runs on Apple Silicon, NVIDIA, AMD or CPU and connects to coding agents. |
| [0xSojalSec/airllm](https://github.com/0xSojalSec/airllm) | 3.1k | 2025-09-26 | Fork of AirLLM, a Python library that runs very large LLMs on small GPUs by loading layers from disk during inference instead of keeping the whole model in VRAM. |
| [youssofal/MTPLX](https://github.com/youssofal/MTPLX) | 2.6k | 2026-05-02 | Mac app and CLI that serves local Qwen models on Apple Silicon using native multi-token-prediction speculative decoding, with OpenAI- and Anthropic-compatible local endpoints. |
| [vllm-project/vllm-metal](https://github.com/vllm-project/vllm-metal) | 1.9k | 2025-12-12 | Community-maintained vLLM hardware plugin that runs vLLM on Apple Silicon Macs, using MLX as the primary compute backend. |
| [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3) | 1.7k | 2025-04-06 | Inference and quantization library for running LLMs on consumer GPUs, introducing the EXL3 quantization format with flexible bitrates and parallel inference. |
| [naklecha/simple-llm](https://github.com/naklecha/simple-llm) | 489 | 2026-01-08 | Minimal 1,351-line Python inference engine for gpt-oss-20b and gpt-oss-120b on a single H100, with all GPU kernels written in Triton and MXFP4 checkpoints loaded directly. |
| [leyten/shard](https://github.com/leyten/shard) | 461 | 2026-06-15 | Pipeline-parallel LLM inference engine that splits a model across GPUs on separate machines over the internet, aiming at a peer-to-peer network that pools VRAM. |
| [beamivalice/sushi](https://github.com/beamivalice/sushi) | 270 | 2026-09-20 | Local AI server for Apple Silicon (M1+) that runs low-bit hybrid EXL3/affine quantized models. A detached fork of mlx-serve that also runs as a guest engine inside it. |
| [0xSero/glm-5.2-sm120](https://github.com/0xSero/glm-5.2-sm120) | 155 | 2026-06-18 | Docker and vLLM launch recipe for serving a REAP-pruned NVFP4 GLM-5.2 469B model on four RTX PRO 6000 Blackwell (SM120) GPUs with 250K context and MTP speculative decoding. |

### Local model runners & desktop AI

Launchers, runners and managers for picking, swapping and serving models on your own machines.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [exo-explore/exo](https://github.com/exo-explore/exo) | 47.9k | 2024-06-24 | Connects your devices into an AI cluster so models too large for one machine can run locally. Supports RDMA over Thunderbolt for faster inter-device communication. |
| [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | 38k | 2026-02-15 | Rust CLI and TUI that inspects your CPU, RAM, GPU and VRAM and recommends which open-source LLMs and quantizations will run comfortably on that hardware. |
| [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | 10.3k | 2025-07-22 | Eight SDKs over one C++ core for running LLMs, vision, speech, embeddings, RAG and image generation locally on phones, browsers, desktops and servers. |
| [pinokiocomputer/pinokio](https://github.com/pinokiocomputer/pinokio) | 8.3k | 2023-07-09 | Desktop launcher that installs and runs open-source AI projects through scripted one-click workflows. Works like a terminal app with a GUI, where scripts can run arbitrary commands. |
| [mostlygeek/llama-swap](https://github.com/mostlygeek/llama-swap) | 6k | 2024-10-04 | Zero-dependency Go proxy that hot-swaps between local models on demand in front of any OpenAI- or Anthropic-compatible server such as llama.cpp or vLLM. |
| [containers/ramalama](https://github.com/containers/ramalama) | 3.1k | 2024-07-24 | CLI that pulls and serves local AI models from any source inside OCI containers, applying familiar container workflows to local and production inference. |
| [Blaizzy/nativ](https://github.com/Blaizzy/nativ) | 1.5k | 2026-07-20 | Native macOS app for Apple silicon that bundles an mlx-vlm server, finds MLX models in your Hugging Face cache, and lets you chat with, serve and monitor them. |
| [Chen-zexi/vllm-cli](https://github.com/Chen-zexi/vllm-cli) | 506 | 2025-08-14 | Command-line tool for serving LLMs with vLLM, with an interactive interface, saved configuration profiles and GPU monitoring. |

### ML frameworks, training & fine-tuning

Array and ML frameworks, language bindings, fine-tuning libraries, training research and model conversion collections.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [ml-explore/mlx](https://github.com/ml-explore/mlx) | 28.8k | 2023-11-28 | Apple machine learning research's array framework for Apple silicon, with NumPy-like Python and C++ APIs. |
| [huggingface/peft](https://github.com/huggingface/peft) | 21.8k | 2022-11-25 | Hugging Face library of parameter-efficient fine-tuning methods such as LoRA, which adapt large pretrained models by training only a small number of extra parameters. |
| [huggingface/candle](https://github.com/huggingface/candle) | 21.2k | 2023-06-19 | Minimalist ML framework for Rust from Hugging Face, focused on performance including GPU support and easy deployment. |
| [maderix/ANE](https://github.com/maderix/ANE) | 7.3k | 2026-02-28 | Research project that trains neural networks, including backpropagation, directly on the Apple Neural Engine using reverse-engineered private APIs, without CoreML training, Metal or the GPU. |
| [InternScience/GraphGen](https://github.com/InternScience/GraphGen) | 1.2k | 2025-01-08 | Framework that generates synthetic supervised fine-tuning data for LLMs, guided by knowledge graphs. |
| [NVlabs/vibetensor](https://github.com/NVlabs/vibetensor) | 642 | 2026-01-05 | NVIDIA research artifact: a deep-learning system software stack, from Node.js and Python down to PTX assembly, generated entirely by LLM coding agents. |
| [john-rocky/coreai-model-zoo](https://github.com/john-rocky/coreai-model-zoo) | 460 | 2026-06-10 | Collection of converted models and conversion recipes for Apple's Core AI runtime on iPhone and Mac, covering chat, vision, speech and generative models, with Swift examples and per-model validation records. |
| [oxiglade/mlx-rs](https://github.com/oxiglade/mlx-rs) | 383 | 2023-12-23 | Unofficial Rust bindings for Apple's MLX machine learning library. |
| [razerofficial/aikit](https://github.com/razerofficial/aikit) | 209 | 2025-09-30 | Razer's preview toolkit for local LLM inference, fine-tuning and multi-GPU scaling, distributed with a Docker image. |

### Open model releases & research code

Released open model families and research code for language, multimodal and time-series tasks.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [google-research/timesfm](https://github.com/google-research/timesfm) | 34.6k | 2024-04-29 | Google Research's pretrained decoder-only foundation model for time-series forecasting, with PyTorch checkpoints including TimesFM 3.0. |
| [OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM) | 11.6k | 2024-01-29 | Repository for OpenBMB's MiniCPM family of small on-device language models, including MiniCPM5-1B and MiniCPM5-2B. |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 9.3k | 2026-09-17 | Family of small decision models (yes/no, choice, score) built on Qwen3.5 and Qwen3.8 in the style of Jev. Includes pretrained weights and training code for running or training your own. |
| [QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8) | 4.3k | 2025-09-11 | Repository for Alibaba's Qwen3.5, Qwen3.6 and Qwen3.8 open large language model series, linking to weights on Hugging Face and ModelScope. |
| [facebookresearch/tuna-2](https://github.com/facebookresearch/tuna-2) | 759 | 2026-04-22 | Official research code for Tuna-2, a unified multimodal model for understanding and generation that uses pixel embeddings instead of a vision encoder. |

### Speech, voice & dictation

Speech models and engines for TTS, speech recognition and VAD, plus voice and dictation apps built on them.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 57.8k | 2026-01-25 | Local, open-source voice studio for cloning voices, generating speech and dictating into any app, with an API for giving agents voices you own. |
| [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | 39.5k | 2025-09-16 | Tokenizer-free multilingual text-to-speech model (VoxCPM2) from OpenBMB that supports voice design and voice cloning. |
| [cjpais/Handy](https://github.com/cjpais/Handy) | 34k | 2025-02-13 | Free, open-source, offline cross-platform desktop speech-to-text app: press a shortcut, speak, and the transcription is typed into any text field. Written in Rust. |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | 27k | 2025-04-23 | Family of open-source text-to-speech models from Resemble AI, including a multilingual variant, with hosted demos and local install. |
| [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | 16.1k | 2025-08-05 | Open-source text-to-speech library with CPU-friendly models. Its flagship KittenTTS 2 is a 1.7B-parameter 1-bit speech language model with in-context voice cloning and expression control. |
| [supertone-oss-archive/supertonic](https://github.com/supertone-oss-archive/supertonic) (archived) | 13.8k | 2025-11-18 | Archived on-device multilingual text-to-speech project that runs natively through ONNX. Development and support have ended; code is kept for reference. |
| [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | 12.3k | 2025-09-21 | Open-source macOS voice-to-text dictation app that transcribes on-device and applies AI enhancement to the text. Installable via Homebrew, positioned as a local alternative to Wispr Flow. |
| [kyutai-labs/moshi](https://github.com/kyutai-labs/moshi) | 11.3k | 2024-08-07 | Kyutai's speech-text foundation model and framework for real-time, full-duplex spoken dialogue, built on the Mimi streaming neural audio codec. |
| [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | 9.9k | 2026-01-07 | Lightweight text-to-speech library from Kyutai designed to run on CPUs, installed with pip and called as a Python function. Requires PyTorch 2.5+. |
| [hexgrad/kokoro](https://github.com/hexgrad/kokoro) | 9.4k | 2025-01-10 | Python inference library for Kokoro-82M, an open-weight 82-million-parameter text-to-speech model, installable with pip. |
| [santinic/audiblez](https://github.com/santinic/audiblez) | 8.8k | 2025-01-14 | Python tool that converts EPUB e-books into .m4b audiobooks using Kokoro TTS, with a graphical interface, CUDA support and multiple languages. |
| [Blaizzy/mlx-audio](https://github.com/Blaizzy/mlx-audio) | 8.1k | 2024-11-27 | Library for text-to-speech, speech-to-text and speech-to-speech built on Apple's MLX framework for Apple Silicon. |
| [argmaxinc/argmax-oss-swift](https://github.com/argmaxinc/argmax-oss-swift) | 6.4k | 2024-01-26 | Open-source Swift SDK for on-device speech AI on Apple Silicon, covering speech recognition and speaker diarization. Home of WhisperKit with Core ML models. |
| [tmoroney/auto-subs](https://github.com/tmoroney/auto-subs) | 4.4k | 2023-03-15 | Local-first subtitle generator that turns audio or video into timestamped subtitles with selectable AI models. Runs standalone or connects to DaVinci Resolve, Premiere Pro and After Effects. |
| [MisoLabsAI/MisoTTS](https://github.com/MisoLabsAI/MisoTTS) | 3.2k | 2026-05-20 | Open 8-billion-parameter text-to-speech model aimed at emotive, expressive speech. Includes local quickstart instructions via uv and a hosted demo. |
| [kitlangton/Hex](https://github.com/kitlangton/Hex) (archived) | 2.9k | 2025-01-27 | Archived macOS hold-to-talk transcription app that pastes the transcribed text where you are typing. Development moved to anomalyco/hex; this repo preserves the legacy Swift app. |
| [amicalhq/amical](https://github.com/amicalhq/amical) | 1.6k | 2025-05-08 | Open-source, local-first desktop dictation and note-taking app that uses open-source speech models and works offline. Installable via Homebrew on macOS. |
| [Ampixa/sanoTTS](https://github.com/Ampixa/sanoTTS) | 797 | 2026-07-11 | Family of tiny neural text-to-speech voices of 294k to 2.3M parameters that need no cloud or NPU. They run in real time on an ESP32-S3 or in the browser via WASM. |
| [FireRedTeam/FireRedChat](https://github.com/FireRedTeam/FireRedChat) | 593 | 2025-09-09 | Self-hosted full-duplex voice interaction system with released pVAD, turn-detector, FireRedTTS and FireRedASR components for a cascaded pipeline. |
| [steipete/sag](https://github.com/steipete/sag) | 583 | 2025-12-07 | Go CLI that works like the macOS say command but speaks with ElevenLabs voices. Streams to speakers by default, can list voices or save audio files. |
| [freestyle-voice/freestyle](https://github.com/freestyle-voice/freestyle) | 488 | 2026-05-25 | Desktop voice app that dictates into any app via a hotkey, helps with writing, and can check in on a schedule with proactive reminders across connected apps. |
| [second-state/qwen3_asr_rs](https://github.com/second-state/qwen3_asr_rs) | 254 | 2026-02-20 | Pure Rust implementation of Qwen3-ASR speech recognition, shipped as a cross-platform CLI and an OpenAI-compatible transcription API server. |
| [second-state/qwen3_tts_rs](https://github.com/second-state/qwen3_tts_rs) | 234 | 2026-01-25 | Rust implementation of Qwen3 text-to-speech inference. Provides cross-platform CLI tools for speech generation and voice cloning, plus an OpenAI-compatible server. |
| [nyosegawa/speech.cpp](https://github.com/nyosegawa/speech.cpp) | 179 | 2026-09-29 | Speech engine in C++ on ggml covering TTS, speech recognition and VAD, with Metal, Vulkan and CPU backends. Ships one CLI and shared library behind a C API, plus an OpenAI-compatible server and live transcription. |
| [steipete/brabble](https://github.com/steipete/brabble) | 172 | 2025-12-03 | Always-on local voice daemon for macOS and Linux in Go that listens for a wake word, transcribes with whisper.cpp and then runs a configurable hook command. |
| [second-state/qwen3_audio_api](https://github.com/second-state/qwen3_audio_api) | 90 | 2026-01-26 | OpenAI-compatible API servers for Qwen3-TTS and Qwen3-ASR, in Python and Rust, serving /v1/audio/speech and /v1/audio/transcriptions for self-hosted text-to-speech and speech-to-text. |

### Vision, video & image models

Models and tools for computer vision, depth, pose, motion capture, and image and video generation.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [roboflow/supervision](https://github.com/roboflow/supervision) | 51.2k | 2022-11-28 | Python library of reusable computer-vision utilities for working with detection models, including annotators, object tracking, dataset handling and zones. |
| [CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) | 34.5k | 2017-04-24 | Real-time multi-person keypoint detection library from CMU that estimates body, face, hand and foot poses. Builds on Linux, macOS and Windows. |
| [freemocap/freemocap](https://github.com/freemocap/freemocap) | 10.5k | 2021-04-12 | Free markerless motion-capture system that reconstructs 3D human movement from ordinary cameras, with a Python server and a TypeScript front end. |
| [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) | 9.8k | 2026-01-03 | Official Python inference and LoRA training package for LTX-2, a DiT-based audio-video foundation model that generates synchronized video and audio. |
| [antirez/iris.c](https://github.com/antirez/iris.c) | 2k | 2026-01-18 | Text-to-image inference pipeline for Flux 2 diffusion-transformer models written entirely in C with no dependencies beyond the standard library; MPS and BLAS acceleration are optional. |
| [zapdos-labs/unblink](https://github.com/zapdos-labs/unblink) | 1.5k | 2025-11-05 | Camera monitoring application with a relay-node architecture that uses the Qwen3-VL vision-language model to summarize frames, with a natural-language chat interface over camera footage. |
| [localai-org/depth-anything.cpp](https://github.com/localai-org/depth-anything.cpp) | 1.1k | 2026-06-14 | From-scratch C++17 port of ByteDance's Depth Anything 2 and 3 on ggml, with GGUF weights, for monocular depth estimation and camera pose. Built by the LocalAI team. |
| [philipp-eisen/facestream](https://github.com/philipp-eisen/facestream) | 231 | 2025-01-27 | Web app for real-time face swapping that offloads processing so no powerful local machine is needed. Motivated by Deep Live Cam. |

### LLM gateways, routers & model catalogs

Gateways, routers and proxies that unify LLM providers and subscriptions, plus model catalogs, pricing data and API specs.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | 55.5k | 2025-07-01 | Go service that wraps CLI-based subscriptions (Codex, Claude Code, Gemini, Grok and others) as OpenAI, Gemini, Claude and Codex compatible API endpoints. |
| [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | 36.5k | 2026-04-21 | OpenAI-compatible proxy that aggregates the free tiers of 34 LLM providers behind one /v1 endpoint. Adds routing, automatic failover and encrypted key storage; intended for personal experimentation. |
| [decolua/9router](https://github.com/decolua/9router) | 31k | 2026-01-05 | Router that connects coding tools such as Claude Code, Cursor, Codex and Cline to 40+ free and low-cost LLM providers, with automatic fallback and token saving. |
| [maximhq/bifrost](https://github.com/maximhq/bifrost) | 8.9k | 2025-03-19 | Go AI gateway exposing one OpenAI-compatible API across many models, with failover, load balancing, semantic caching, virtual keys, budgets and an MCP gateway. |
| [anomalyco/models.dev](https://github.com/anomalyco/models.dev) | 7.3k | 2025-06-04 | Community-contributed open-source database and API of AI model specifications, pricing and capabilities, also used inside opencode. |
| [katanemo/plano](https://github.com/katanemo/plano) | 7.1k | 2024-07-09 | AI-native proxy server and data plane for agentic apps, handling LLM routing, agent orchestration, guardrails and tracing outside application code. Written in Rust. |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | 6.6k | 2026-02-03 | LLM router for autonomous agents that routes locally and lets agents pay per request with USDC wallets on Base and Solana via x402, instead of accounts and credit cards. |
| [nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio) | 4.9k | 2025-12-24 | Native macOS menu-bar app that tracks quota across Claude, Gemini, OpenAI, Qwen and Antigravity subscriptions and fails over between accounts. Manages CLIProxyAPI and wires up coding agents. |
| [openresponses/openresponses](https://github.com/openresponses/openresponses) | 1.1k | 2026-01-15 | Open specification for multi-provider LLM interfaces modeled on the OpenAI Responses API. Defines shared request/response shapes, streaming semantics and tool invocation patterns. |
| [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy) | 558 | 2025-06-10 | Self-hosted proxy and resilience library that exposes OpenAI- and Anthropic-compatible endpoints over many LLM providers, with multi-provider translation and load balancing across keys. |
| [ghuntley/underclass](https://github.com/ghuntley/underclass) | 237 | 2026-09-20 | Local OpenAI-compatible proxy that pools multiple ChatGPT/Codex and GitHub Copilot subscriptions. Pins sessions to one account to keep prompt caches warm and cools down accounts that exhaust quota. |
| [bitrouter/bitrouter](https://github.com/bitrouter/bitrouter) | 235 | 2026-03-06 | Local OpenAI-compatible model router written in Rust that learns from agent workflows which model to use for each request, with interpretable routing decisions. |
| [Portkey-AI/models](https://github.com/Portkey-AI/models) | 143 | 2025-12-26 | Open pricing and configuration dataset for 2,000+ LLMs across 40+ providers, served through a free no-auth API. It backs cost attribution in the Portkey AI Gateway. |
| [basetenlabs/baseten-switch](https://github.com/basetenlabs/baseten-switch) | 95 | 2026-07-27 | Beta macOS app and local Go gateway that routes supported AI coding harnesses between their native providers and models served on Baseten, with per-client model mappings. |
| [remorses/subrouter](https://github.com/remorses/subrouter) | 15 | 2026-08-26 | Proxy that cycles between your personal AI subscriptions (Claude, ChatGPT, Grok, opencode Go and others) so the next account takes over when one hits its rate limit. |

### LLM app utilities & typed AI functions

Small libraries and CLIs for using LLMs inside ordinary programs, shells and developer workflows.

| Project | Stars | Created | Description |
|---|--:|---|---|
| [vercel-labs/ai-cli](https://github.com/vercel-labs/ai-cli) | 825 | 2025-07-28 | Terminal CLI that generates text, images, video and audio and makes typed decisions through composable commands with stdin support. Built on the Vercel AI SDK and AI Gateway; requires Node.js 22+. |
| [junaid-mahmood/nlsh](https://github.com/junaid-mahmood/nlsh) | 473 | 2026-01-22 | Natural-language shell for macOS and Linux that translates plain-English requests into terminal commands. |
| [samwho/llmwalk](https://github.com/samwho/llmwalk) | 211 | 2025-12-14 | Python tool that explores the answer-space of an MLX model by branching on every token the sampler would consider and ranking completions by probability. |
| [wobsoriano/oxlint-plugin-jev](https://github.com/wobsoriano/oxlint-plugin-jev) | 88 | 2026-09-19 | Experimental Oxlint plugin whose lint rules are plain-English yes/no questions about a function, call, JSX element or file. Each match is sent to TypeSafe's Jev to be answered. |
| [BoundaryML/feelings](https://github.com/BoundaryML/feelings) | 24 | 2026-09-19 | Example language-style project that adds a typed .feels() method, an "AI if statement", to any value. Built on TypeSafe AI's Jev and BAML. |
| [Mechse/saft](https://github.com/Mechse/saft) | 20 | 2026-05-24 | CLI written in Odin that generates Git commit messages with Apple's on-device language model, needing no API keys or cloud access. |
