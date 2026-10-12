# Wheel of Time — Study Notes

Cards for studying how *The Wheel of Time* is built: its threads, characters, world and chapters, with craft lessons for writing. Start with the [Story Map](story-map.md), the hub that links to everything else.

These files are exports of linked Claude Docs. An export turns links between cards into plain titles, so after adding or replacing a card, run `python3 tools/link_cards.py` to turn them back into relative links. A new card needs its title and path added to the list at the top of that script.

## Folders

| Folder | What it holds | Files |
| --- | --- | --- |
| [story-map.md](story-map.md) | The hub: threads, macro shape, how the map grows | — |
| [threads/](threads/) | One card per story thread, with satellite cards beside it | [Perrin](threads/perrin.md) · [Perrin — Senses and Surroundings](threads/perrin-senses-and-surroundings.md) · [Perrin — Peoples and Powers](threads/perrin-peoples-and-powers.md) · [The Shadow](threads/shadow.md) |
| [characters/](characters/) | Character cards | [Faile](characters/faile.md) |
| [arcs/](arcs/) | Arc and event cards, prefixed by book | [The Road with Elyas (Book 1)](arcs/b01-road-with-elyas.md) |
| [chapters/](chapters/) | Chapter cards, one folder per book, files in chapter order | [Book 1, Ch. 1 — An Empty Road](chapters/b01-eye-of-the-world/ch01-an-empty-road.md) · [Book 1, Ch. 2 — Strangers](chapters/b01-eye-of-the-world/ch02-strangers.md) |
| [world/](world/) | The World Index and world cards (places, peoples, history) | [World Index](world/index.md) · [Manetheren](world/manetheren.md) · [Stedding](world/stedding.md) |
| [images/](images/) | Diagrams exported from the cards | — |
| [tools/](tools/) | `link_cards.py`, which relinks card titles after an export | — |

## Naming

- Books are numbered `b01` to `b14` so folders and files sort in reading order.
- Chapters are numbered `ch01`, `ch02`, and so on within their book's folder.
- A thread's satellite cards share its prefix (`perrin-…`), so they sort next to it.
