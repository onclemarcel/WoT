# Wheel of Time — Study Notes

Cards for studying how *The Wheel of Time* is built: its threads, characters, world and chapters, with craft lessons for writing. Start with the [Story Map](story-map.md), the hub that links to everything else.

These files are exports of linked Claude Docs. [CLAUDE.md](CLAUDE.md) describes how the cards are made and updated. An export turns links between cards into plain titles, so after adding or replacing a card, run `python3 tools/link_cards.py` to turn them back into relative links. A new card needs its title and path added to the list at the top of that script.

## Folders

| Folder | What it holds | Files |
| --- | --- | --- |
| [story-map.md](story-map.md) | The hub: threads, macro shape, how the map grows | — |
| [threads/](threads/) | Threads that follow a force or theme across the series, not one person | [The Shadow](threads/shadow.md) |
| [characters/](characters/) | One card per character: arc, people, senses and surroundings, peoples and powers | [Rand](characters/rand.md) · [Mat](characters/mat.md) · [Perrin](characters/perrin.md) · [Egwene](characters/egwene.md) · [Nynaeve](characters/nynaeve.md) · [Moiraine](characters/moiraine.md) · [Lan](characters/lan.md) · [Faile](characters/faile.md) · [Padan Fain](characters/padan-fain.md) · [Thom](characters/thom.md) · [Tam](characters/tam.md) |
| [arcs/](arcs/) | Arc and event cards, prefixed by book | [The Road with Elyas (Book 1)](arcs/b01-road-with-elyas.md) |
| [chapters/](chapters/) | Chapter cards, one folder per book, files in chapter order | [Book 1, Ch. 1 — An Empty Road](chapters/b01-eye-of-the-world/ch01-an-empty-road.md) · [Book 1, Ch. 2 — Strangers](chapters/b01-eye-of-the-world/ch02-strangers.md) · [Book 1, Ch. 3 — The Peddler](chapters/b01-eye-of-the-world/ch03-the-peddler.md) · [Book 1, Ch. 4 — The Gleeman](chapters/b01-eye-of-the-world/ch04-the-gleeman.md) · [Book 1, Ch. 5 — Winternight](chapters/b01-eye-of-the-world/ch05-winternight.md) · [Book 1, Ch. 6 — The Westwood](chapters/b01-eye-of-the-world/ch06-the-westwood.md) |
| [world/](world/) | The World Index and world cards (places, peoples, history) | [World Index](world/index.md) · [The Two Rivers](world/two-rivers.md) · [Ghealdan](world/ghealdan.md) · [Illian](world/illian.md) · [Tar Valon and the White Tower](world/tar-valon.md) · [Children of the Light](world/children-of-the-light.md) · [Tales and Legends](world/tales-and-legends.md) · [Manetheren](world/manetheren.md) · [Stedding](world/stedding.md) |
| [images/](images/) | Diagrams exported from the cards | — |
| [tools/](tools/) | `save_exports.py`, which writes Docs exports into the repo, and `link_cards.py`, which relinks card titles | — |

## Naming

- Books are numbered `b01` to `b14` so folders and files sort in reading order.
- Chapters are numbered `ch01`, `ch02`, and so on within their book's folder.
- A character's whole study lives in one card, with sections for arc, people, senses and surroundings, and peoples and powers.
