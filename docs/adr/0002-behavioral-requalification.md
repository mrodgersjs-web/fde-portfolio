# ADR 0002: Re-qualify routes with behavioral probes, never config readback

Status: accepted (2026-11-24)

Context: five agent clients, a gateway, and a hand-built registry silently
diverged. A client advertised 32,768 context against a server's 8,192; a
proxy's value was 4x off. One endpoint passed a tool cycle and failed
normal continuation days later. Config and catalog presence proved nothing.

Decision: every route is re-qualified by behavior: chat, streaming, tool
calls, multi-turn continuation with and without tools, embeddings by
dimension, vision by modality. Context values come from server readback, not
client config. Offline validation (43 roles, 31 fallback chains) runs before
any live slot is touched.

Consequences: a permanent rule, catalog presence proves nothing. Config
repairs keep parsing, file-mode, and hash checks with private backups and
exact diffs, and an overlay traced to one file is surgically removed rather
than reset. Costs: re-qualification is a scheduled loop, not a one-time
setup; the catalog is never trusted by reading alone.
