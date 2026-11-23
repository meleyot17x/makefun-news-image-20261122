# THE SIGNAL TOWER — Final 3 (@meleyotcok) · NI22 Wave 7

One-page newspaper for Sunday 22 November 2026: 15 cards + 21 briefs = 36
stories, 7 regions. Lead trio COP31 → Ukraine → Iran; fog grey / blue;
Layout C (three leads beside a vertical THE DAY IN NUMBERS rail).

## Build

- `compose.py` — PIL renderer (W=3900; fonts x1.45 vs G6, structure x~1.3).
  Renders `variant_A.png` (matrix layout C, matrix palette), `variant_B.png`
  (alternate layout A, same palette), `variant_C.png` (layout C, gold accent).
  Duel in `duel.md`: winner **A (35,5/40)**.
- `ni22v7-finish.sh final3 A` — fits winner to `entry.png` (1024×1024),
  runs margin check with `--fresh ni22-fresh-g7.txt`, writes `preview-300.png`.
- `main.py` — stdlib-only copy-only carrier with the 1024×1024 dimension gate.

## Gates (verified)

- entry.png 1024×1024, 237.176 bytes, sha256
  `58d033a9fd5b64a6e9bbbe70ed9b414bacf1e14b8da3c7b982c998334c59c671`
- margin check 13/13 (fresh G7 pool; brief segar 9/21 = 43%)
- render aspect 0,950 (3900×4105)
- main.py 2× run byte-identical (see verification below)

## Verify

```
MAKEFUN_OUTPUT_DIR=/tmp/ni22v7-verify-final3 python3 main.py
```

Izin Brian (chat utama, 23 Nov 2026): "Ya — bangun G7, bedah Top 1 dulu".
