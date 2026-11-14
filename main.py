#!/usr/bin/env python3
"""The Key (v1) - a poem about agency.

Writes one fixed poem to /output/entry.txt: a son watches his father
rent a shop on a handshake, no paper signed, and lose it all when the
real owner arrives. Pure Python 3.13 standard library; every run
writes the same bytes.
"""

import os

POEM = """The Key

My father rented the shop on a handshake.
His friend held out the key and said, take it.
My father said, I trust you.
I said, sign the paper. Sign it.
He said, he is my friend.

It was like buying a taco.
Here is the money. Here is the key.
No paper. No name. No date.
Two years, he said. Two years.

We had not been there a year
when the real owner came to the door.
The man we paid was only the middle.
The shop is sold, he said. It is sold.
We said, we paid. We have the key.
He said, show me the paper.

We had no paper.

My father went quiet that day
and stayed quiet. The sickness came
the way a debt comes, slowly,
then all at once. One mistake.
One paper he would not sign.

I still hear the key in his hand.
Here is the money. Here is the key."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Guardrail: the gate takes UTF-8 text of 1 to 1,000 characters,
    # not only white space, or the entry is refused.
    text = POEM.encode("utf-8")
    assert 1 <= len(POEM) <= 1000, "poem outside the 1-1000 character gate"
    assert POEM.strip(), "poem is only white space"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    print("wrote", path, len(text), "bytes")


if __name__ == "__main__":
    main()
