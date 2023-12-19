Think I've cracked it. If you concatenate, in sequence, each of the src mappings for a particular category, then do the same for the dest, you find that the dest list is a rotated version of the source list. Seems each of the src and dest mappings are contiguous. In the test data at least...

So once you know what the start and end ranges are, and the rotation value, it should become simpler to map the seed ranges forwards to produce location ranges, and so pick the lowest.
Now to turn it into code, as long as the assumption holds true for the main data. A task for another day however...

```commandline
seed-to-soil:
50 98 2
52 50 48

src: [50,51,...,96,97][98,99]
dst: [52,53,...,98,99][50,51]

dst = src.rotate(-2)

soil-to-fertiliser:
0 15 37
37 52 2
39 0 15

src: [00,01,...,13,14][15,16,...,50,51][52,53]
dst: [39,40,...,52,53][00,01,...,35,36][37,38]

dst = src.rotate(-39)
```