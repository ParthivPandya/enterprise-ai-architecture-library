# Agent Interoperability, Identity, and Delegated Authority

> **Document type:** Informative Guide  
> **Primary audience:** Enterprise Architects, Security Architects, Platform Engineers  
> **Use when:** Agents connect to tools, data, services, or other agents  
> **Scope:** Protocol-neutral architecture with MCP and agent-to-agent examples  
> **Last verified:** October 2026  
> **Authority:** Independent practitioner guidance  

---

## 1. Why Agent Connectivity Changes the Architecture

Traditional applications call APIs through code paths that developers can enumerate. Agents select tools dynamically, assemble context at runtime, and may delegate work to other agents. The architecture must therefore govern three separate questions:

1. **What capability is being advertised?**
2. **Which identity is requesting it?**
3. **Whose authority is being exercised?**

A protocol can standardise message exchange, but it does not establish trust. Connecting an agent through Model Context Protocol (MCP), an agent-to-agent protocol, or a proprietary tool interface does not make the remote capability safe, authorised, or accurate.

## 2. Interoperability Layers

| Layer | Concern | Required Architecture Evidence |
|---|---|---|
| Discovery | How tools, resources, prompts, and agents are found | Approved capability registry |
| Description | How input/output contracts and constraints are expressed | Versioned schema and semantic description |
| Transport | How messages are exchanged | Approved transport, encryption, endpoint identity |
| Identity | Which workload, agent, user, or service is acting | Authenticated non-human identity |
| Authority | What the caller may do and on whose behalf | Delegation token and policy decision |
| Execution | How the action is performed | Deterministic enforcement gateway |
| Evidence | What is recorded | Trace linking user intent, agent decision, tool call, and result |

## 3. Model Context Protocol Boundary

MCP can provide a common way for AI applications to discover and invoke tools or retrieve resources. Treat every MCP server as an integration boundary, not as a trusted extension of the model.

### 3.1 Minimum MCP server record

| Field | Example |
|---|---|
| Server ID and owner | `mcp-procurement-read-v2` |
| Trust zone | Internal restricted |
| Capabilities | Read approved supplier records |
| Prohibited capabilities | Contract approval, payment, supplier creation |
| Authentication | Workload identity with short-lived token |
| Authorisation policy | Attribute- and purpose-based |
| Data classification | Confidential |
| Output validation | Schema, size, classification, injection scanning |
| Review trigger | Capability, owner, schema, or trust-zone change |

### 3.2 MCP threat considerations

- A tool description can manipulate model selection or conceal side effects.
- Retrieved content can contain indirect prompt injection.
- A server can change behaviour without changing its advertised schema.
- An over-broad client token can convert a read tool into a privilege-escalation path.
- Tool output can leak secrets into subsequent context or memory.

Controls belong outside the model: allow-lists, schema validation, egress filtering, data-loss prevention, rate limits, transaction caps, and deterministic approval gates.

## 4. Agent-to-Agent Delegation

When one agent delegates to another, the receiving agent needs more than the caller's identity. It needs a bounded delegation envelope:

```text
Original human or service intent
        │
        ▼
Delegating agent identity
        │  signed task + purpose + limits + expiry
        ▼
Receiving agent identity
        │  policy decision
        ▼
Approved tool capability
```

The delegation envelope SHOULD contain:

- Original principal or business process
- Delegating and receiving workload identities
- Purpose and permitted actions
- Data classification and handling restrictions
- Maximum spend, duration, and number of steps
- Expiry and replay protection
- Human-approval requirements
- Correlation ID for end-to-end evidence

The receiving agent MUST NOT inherit every permission held by the delegating agent.

## 5. Non-Human Identity Architecture

An agent is a workload, not a person. Give each deployable agent, orchestrator, and tool gateway a separate non-human identity.

### 5.1 Identity principles

1. **No shared long-lived keys.**
2. **Use short-lived, audience-bound credentials.**
3. **Separate runtime identity from developer identity.**
4. **Bind authorisation to purpose and environment.**
5. **Record the original principal without impersonating them.**
6. **Rotate or revoke automatically when deployment state changes.**

### 5.2 Delegation patterns

| Pattern | Use | Risk |
|---|---|---|
| Service identity | Agent performs a system-owned task | Weak user-level accountability if context is not logged |
| On-behalf-of token | Agent acts for an authenticated user | Risk of over-delegation or token replay |
| Capability token | Narrow right to perform one action | Requires mature token issuance and validation |
| Approval token | Human approves a specific irreversible action | Must bind action parameters so approval cannot be reused |

## 6. Policy Enforcement Architecture

The model may propose an action. A deterministic policy enforcement point decides whether it may occur.

```text
Agent proposal
   │
   ▼
Schema validation ──▶ Identity verification ──▶ Policy decision
                                                  │
                                  deny ◀──────────┼──────────▶ allow
                                                  │
                                           Execution adapter
                                                  │
                                            Evidence record
```

Policy inputs SHOULD include identity, delegated purpose, tool, action parameters, data classification, risk tier, spend, jurisdiction, time, and prior steps.

## 7. Failure and Fallback

| Failure | Safe Response |
|---|---|
| Capability registry unavailable | Use cached signed metadata only within its validity window, otherwise stop |
| Remote agent identity cannot be verified | Reject delegation |
| Tool schema changes unexpectedly | Quarantine the tool version |
| Approval service unavailable | Queue reversible draft; do not execute irreversible action |
| Trace correlation breaks | Stop high-risk workflow and preserve partial evidence |
| Agent loop exceeds budget | Circuit-break and escalate |

## 8. Architecture Review Checklist

- [ ] Every agent and tool endpoint has a distinct workload identity
- [ ] Delegated authority is narrower than the delegator's total authority
- [ ] Credentials are short-lived and audience-bound
- [ ] Tool metadata and schemas are versioned and integrity-protected
- [ ] Untrusted tool/resource content is treated as injection-capable
- [ ] A deterministic gateway enforces permissions outside the model
- [ ] Irreversible actions use parameter-bound human approval
- [ ] End-to-end traces preserve original principal, delegation, decision, and result
- [ ] Revocation, expiry, circuit breaking, and manual fallback are tested

## 9. AI-ADM Mapping

| AI-ADM Phase | Agent Interoperability Output |
|---|---|
| B — Business | Delegation and accountability model |
| C — Data | Classification and context-sharing constraints |
| D — Application | Agent, MCP server, tool, and gateway interactions |
| E — Technology | Identity, transport, secrets, and policy infrastructure |
| F — Governance | Permission matrix, approval policy, and evidence requirements |
| I — Implementation Governance | Protocol conformance and abuse-case testing |

## References

1. Anthropic, [Model Context Protocol specification](https://modelcontextprotocol.io/specification/), verify the current protocol version before implementation.
2. Google, [Agent2Agent protocol](https://a2a-protocol.org/), verify the current specification and security guidance.
3. IETF, [OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700).
4. NIST, [Zero Trust Architecture (SP 800-207)](https://csrc.nist.gov/publications/detail/sp/800-207/final).
5. OWASP, [Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/).

