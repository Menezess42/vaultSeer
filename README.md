# VaultSeer

**VaultSeer** is a local-first semantic search tool designed to navigate through a user's personal knowledge base — such as markdown notes and PDF documents — without relying on any online APIs or cloud services.

This tool is ideal for individuals who value privacy, control over their data, and the ability to search abstract or concrete information across curated directories.

---

## 🧠 Project Philosophy

VaultSeer works as a librarian in a dwarven fortress: it does not provide final answers, but rather points to the most relevant documents from your knowledge vaults, helping reinforce understanding through active retrieval.

Initially, VaultSeer will:

- Index and monitor local directories (e.g., Obsidian vaults, curated PDF folders).
- Use semantic similarity to return a list of documents most likely to contain relevant information.
- Operate purely via terminal and entirely offline.
- Rely on metadata such as file names, directory structures, and markdown headers.

---

## 📁 Project Structure (suggested)

```text
vaultseer/
├── flake/                   # Nix flake files
│   ├── flake.nix
│   └── flake.lock
├── .envrc                   # direnv environment loader
├── README.md                # Project description and instructions
├── vaultseer/               # Main Python package (to be developed)
│   ├── __init__.py
│   ├── core/                # Pure logic: domain, indexers, similarity algorithms
│   ├── interface/           # CLI and/or GUI interactions
│   ├── infra/               # Persistence and storage (e.g., FAISS, SQLite, etc.)
│   └── config.py
├── tests/                   # Unit and integration tests
│   └── __init__.py
├── data/                    # Temporary folder for ingested documents (git-ignored)
├── notebooks/               # Prototypes, scratchpads, embeddings experiments
├── requirements.txt         # Python dependencies for pip
└── pyproject.toml           # Optional Python build metadata
```
---
### ⚠️Note:
- This is a proposed layout based on scalable software architecture principles and typical RAG-based workflows. It is subject to change as the project matures.
---
### ✅ Current Status
- [X] Initial project skeleton established
- [ ] Evaluate local embedding libraries (e.g., sentence-transformers, gtr, all-MiniLM)
- [ ] Evaluate vector index options (e.g., faiss, annoy, chroma, hnswlib)
- [ ] Implement document ingestion and metadata extraction
- [ ] Implement semantic search prototype
- [ ] Integrate with terminal CLI
---
### 📜 License
- To be defined.
---
### 🛠️ Developed by
- This project is maintained and built by DwarfSoftware, a company that values modularity, reliability, and well-crafted software rooted in the engineering spirit of the dwarves.

