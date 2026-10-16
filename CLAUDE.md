# Working on the Wheel of Time study cards

This repo mirrors a set of linked Claude Docs ("cards") that study how *The Wheel of Time* is built, with craft lessons for writing. The Docs are the source of truth; the Markdown files here are exports of them. Read this file before touching either.

## What the user does, and what Claude does

- The user pastes a chapter's text, usually followed by close-reading notes and questions on a later turn.
- **Chapter text** → make a chapter card, checked against the pasted text, then link it from the previous chapter (Next) and the Story Map.
- **Reading notes** → add a "Reader's notes" table to that chapter card (Note | Reading), then answer the questions in chat. Notes often call for new world or character cards; make them when asked or clearly implied.
- **"Make X's card"** → a new card in the matching layout below, linked from the Story Map and the chapter cards where X appears.
- After any change, export the touched cards and push them to `main` (see Upload).

## Rules for content

- **Facts from the pasted text vs memory.** Everything the pasted chapters show is checked against them. Anything from later books is from memory and must be flagged in the card's Sources section, naming the details most worth confirming.
- **Never spoil beyond what's useful, never invent.** Mark uncertain readings as readings ("often read as", "the text never says").
- **Quotes stay short** (a few words to a sentence); everything else is paraphrase. The full chapter text is **not** stored in the repo or the cards (copyright); if exact wording is needed later, ask the user to paste the chapter again.
- **Style:** plain words, short sentences, a lead sentence that states the point, tables for anything compared across items. No emoji.

## Card layouts

**Chapter card** (title `EotW Ch. N — Title`, file `chapters/b01-eye-of-the-world/chNN-slug.md`):
links lines (Up: Story Map · Previous · Next · Shadow thread; Characters: …; World: …; Tales: …), lead, Setting (Place | What it shows | What it hides), Characters (Character | Mindset | Wants | Key moment) + "Named but not on stage", a chapter-specific section if the chapter calls for one, What the reader can't decode yet (Sign | What the village sees | What it means), Reader's notes (added later), Thread setup (Thread | What Chapter N seeds | Strength), Craft lessons (numbered), Sources.

**Character card** (title `WoT Character — Name`, file `characters/name.md`):
links line, lead (the arc in one paragraph, "This card is a first version…"), Starting point (what the chapters so far show), Arc (Book | Turning point | What shifts | Why), People (Person | Role in his/her change), Senses and surroundings (signature sense, Inner senses, Places table, Objects), Peoples and powers (Group or power | Relationship over time | Effect), Craft lessons, Sources.

**World card** (title `WoT — Name`, file `world/slug.md`): links line, lead + key bullets, a section on the entity across the series (table by book), Influence (Character or thread | Effect | Card), Sources. Add a row for it in the World Index.

**Thread card** (`threads/`) and **arc card** (`arcs/bNN-slug.md`) follow the existing Shadow and Road with Elyas cards.

## Satellite cards (places, people, songs, tales, history, peoples)

Satellite cards are created when a term becomes prominent, not on every mention. A mentions index makes sure nothing is lost in between.

- **Mentions index.** `world/mentions.md` is a repo-only file (no Docs card), one row per term: Term | Kind (place, person, song, tale, history, people, object) | Chapters | Card. After each new chapter card, add every newly named term and extend the Chapters column of terms named again, with a few words on how each appears. Passing names count: the chapter text is not stored, so a name left out of both the chapter card and the index is lost.
- **When a term gets its own card.** Any one of: it drives a scene, not just a mention; it appears in three or more chapters; the user asks for it; the user's notes clearly call for it. Otherwise it stays an index row.
- **Creating a card means backfilling.** Search the chapter cards and the index for the term and its variants (for Cairhien: Cairhien, Laman, Avendoraldera, Marath), and build the card's history from what they show. Fill the Card column in the index. Anything from later books is from memory and goes in Sources, as usual.
- **Updating an existing card.** Only when a chapter adds something real, such as a new row in its table, a new turn or a new fact. A plain repeat mention goes in the index only.
- **Batch it.** Do satellite work once per chapter, after the chapter card, in one pass, and name the touched cards in the chat summary.

## Card registry (Docs ids)

Project id (the doc) / tab id (needed for `export`). Body node ids come from `read` on the project.

| Card | Project id | Tab id | Repo file |
| --- | --- | --- | --- |
| Wheel of Time — Story Map | 39c6027a-ad85-4a4a-8b9b-9c7af47546d2 | 8a2acc57-5afb | story-map.md |
| WoT — World Index | 5b2343ae-b46d-4ef0-8d13-ef16ffa35c00 | 2ed67aa7-5f97 | world/index.md |
| WoT Thread — The Shadow | 1c097efe-6a0a-437d-b7e6-35af9c2de4bb | 18b6d287-7995 | threads/shadow.md |
| WoT Arc — The Road with Elyas | d4f39380-5995-4fee-89a1-fa7fd471483d | c3a79596-1be6 | arcs/b01-road-with-elyas.md |
| EotW Ch. 1 — An Empty Road | 5dca8815-5775-4ff1-b47a-b3151f5fe2fb | 74b41172-ef2a | chapters/b01-eye-of-the-world/ch01-an-empty-road.md |
| EotW Ch. 2 — Strangers | 65155d34-2b1e-4a0a-a896-47af022ceb2e | 168826be-c3a2 | chapters/b01-eye-of-the-world/ch02-strangers.md |
| EotW Ch. 3 — The Peddler | 444d692b-1f2f-46bd-8118-59cda6d643b1 | c952e22e-bc99 | chapters/b01-eye-of-the-world/ch03-the-peddler.md |
| EotW Ch. 4 — The Gleeman | d1d3a376-c069-4076-9311-0621e38c479b | 82f83a62-598f | chapters/b01-eye-of-the-world/ch04-the-gleeman.md |
| EotW Ch. 5 — Winternight | 9004528d-7269-4c32-924c-9d40d183e819 | bd5f4698-95f7 | chapters/b01-eye-of-the-world/ch05-winternight.md |
| EotW Ch. 6 — The Westwood | 879f8a0d-3334-42d6-9064-b032ddc569f9 | 0fb53c69-5871 | chapters/b01-eye-of-the-world/ch06-the-westwood.md |
| WoT Character — Rand | 7cdd511c-0de1-4c69-bf0b-44cacc3ce25e | 165c3ba5-0a92 | characters/rand.md |
| WoT Character — Mat | 22ea6a69-5461-4268-a0fa-ce23935aed12 | 114b10cb-1e77 | characters/mat.md |
| WoT Character — Perrin | 25cf1688-25f1-429b-a6dd-1542184d0e8b | 747663dc-5dc0 | characters/perrin.md |
| WoT Character — Egwene | 025ef0fd-df8c-4aed-bfee-ebdc06238285 | 59a2417f-5134 | characters/egwene.md |
| WoT Character — Nynaeve | 7b9cc816-d9d2-43a4-81b1-872b67bc5c63 | dfe2a301-ab81 | characters/nynaeve.md |
| WoT Character — Moiraine | a71a9423-1a4f-4725-bafb-236b3158c19e | 96fe0e8a-c2cb | characters/moiraine.md |
| WoT Character — Lan | d20f9576-f2b0-457c-8b1a-9328eadbcbae | f577ca5f-4642 | characters/lan.md |
| WoT Character — Faile | 52d4e435-7f39-433c-b038-e8c9c3c98664 | 15ab2687-3143 | characters/faile.md |
| WoT Character — Padan Fain | b65e563d-050f-44f7-98e9-cdb0bc3050f2 | cd2f354a-6837 | characters/padan-fain.md |
| WoT Character — Thom | c0e01687-c497-400b-be60-ed03b667a911 | fa3e445e-fcab | characters/thom.md |
| WoT Character — Tam | 05616f06-108f-497f-aeab-332983360b52 | 9bd1b38e-7bd0 | characters/tam.md |
| WoT — The Two Rivers | 6dfbe6fd-aa16-4a33-a1fb-c7c32d3be632 | 95243809-6bec | world/two-rivers.md |
| WoT — Ghealdan | f9f6ffa7-06e3-422a-8fe7-a67a5c8fb72f | 74414696-58ff | world/ghealdan.md |
| WoT — Illian | 533be7ee-a15a-4e04-957b-eb4dc2d372b9 | a2933d87-f7ef | world/illian.md |
| WoT — Tar Valon and the White Tower | 2b19d530-4845-4606-b4f8-baa4e0730584 | 4b479aa7-e9c4 | world/tar-valon.md |
| WoT — Children of the Light | 66e823a9-f28f-4cd7-8c32-16936eafa99f | a2d27180-e695 | world/children-of-the-light.md |
| WoT — Tales and Legends | f7c54d38-b260-494a-9ff3-ad8bd1914c04 | 28ec65a6-3eaa | world/tales-and-legends.md |
| WoT — Manetheren | d1a3216a-5b67-439f-991f-e729a1016aae | 9b45e123-493c | world/manetheren.md |
| WoT — Stedding | abc0b220-0444-404b-aa8f-3cefa7dac606 | 18b411fe-00c9 | world/stedding.md |

Add a row here for every new card. The doc link is `https://claude.ai/code/artifact/<project id>`.

## Working with Claude Docs

- Load the docs skill / `guide topic.index` first in a new session. New card: one `batch` birth with a pending block per section, `Artifact open` the link, then fill one section per `update`.
- Links between cards are mention chips: `"blocks":{"k":{"type":"mention","ref":"project/<id>"}}`, placed in `with` (or `source`) **beside** `from` and `as`, never inside `from`.
- Whole-block `replace` needs `ifHash` + `ifRev`; `find` targets don't. Table rows are added with `insert` `"as":"blocks"` (see `topic.editing`).
- Mentions often come back without a label and then export as the word `Doc`. Note the order of chips you sent; fix each `Doc` in the repo file by hand after export (or via `UP_TARGETS` for "Up: Doc").

## Upload to GitHub

1. `export` each changed card (`format: markdown`, `file` = tab id).
2. `python3 tools/save_exports.py "<export name>.md=<repo path>" ...` writes them and checks byte counts.
3. Replace any `Doc` placeholder with the right card title. In `threads/shadow.md`, replace the `&#91;embedded content: …\]` placeholder with `![The Shadow has one master but many competing servants](../images/shadow-chain-of-command.png)`.
4. For a new card, add its title and path to `TITLES` in `tools/link_cards.py`, and a link in `README.md`.
5. `python3 tools/link_cards.py`, then check links:
   ```
   python3 -c "
   import os,re,glob
   for f in glob.glob('**/*.md',recursive=True):
       for m in re.finditer(r'\]\(([^)#]+\.(?:md|png))\)', open(f,encoding='utf-8').read()):
           if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f),m.group(1)))): print('BROKEN',f,m.group(1))
   "
   grep -rn '\bDoc\b' --include=*.md characters chapters world threads story-map.md
   ```
6. Commit to `main` and `git push origin main`.

## State of the study

- Book 1, Chapters 1–6 have cards. Next: Chapter 7 (Out of the Woods).
- Open ideas: cards for Baerlon and Caemlyn (rows exist in the World Index), Tinkers, Aes Sedai, Aiel; an arc card for Winternight; the Tales card grows with each chapter.
