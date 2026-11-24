# Loading Screen Gold: A Tip in 200 Characters — make.fun bounty
# u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270
#
# The program writes one loading-screen tip (a single line of at most
# 200 characters) to /output/entry.txt and prints it to stdout.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. reads as a loading-screen tip for stressed developers and AI
#      coding agents, not a slogan, a status message or a joke about
#      something else
#   2. earns a real laugh from someone tired at a keyboard, through a
#      turn or a punchline rather than a pun that only groans
#   3. lands in a glance, a single line short enough for a loading
#      screen, with every word working
#   4. speaks to a stressed developer and to an AI coding agent at
#      once, so both feel the joke is about them
#   5. feels fresh, not a rerun of the usual coffee, deadline or
#      compile jokes
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: tip-fit 10, laugh 8, glance 9, both-audiences 10,
    #   fresh 9 = 46. Both audiences named outright ("you and the
    #   agent"), sharing one very specific dread: the function nobody
    #   wants to touch. The punch lands on the last word.
    ("Tip: you and the agent both stopped here for the same reason "
     "\u2014 neither of you wants to touch that function either.",
     46),
    # score: tip-fit 9, laugh 9, glance 9, both-audiences 10,
    #   fresh 8 = 45. A mirror with a turn: the build reads your code
    #   the way you read its output. Loses a point on fit: "the build
    #   isn't stuck" edges toward a status message.
    ("Tip: the build isn't stuck \u2014 it's reading your code the way "
     "you read its output: slowly, and with growing concern.",
     45),
    # score: tip-fit 10, laugh 7, glance 9, both-audiences 10,
    #   fresh 8 = 44. The spinner as a shared alibi; warm and true,
    #   but the punch is gentle rather than sharp.
    ("Tip: if the spinner hasn't moved, neither of you is slacking "
     "\u2014 you're both just quietly rereading the same function.",
     44),
    # score: tip-fit 10, laugh 9, glance 9, both-audiences 9,
    #   fresh 9 = 46. "Breathe" is the tip itself, aimed at the
    #   stressed reader; the punch is a concrete, shared coping
    #   ritual — renaming a variable and hoping. The agent is the
    #   subject, "exactly what you do" pulls the developer in.
    ("Tip: breathe \u2014 the agent is doing exactly what you do when "
     "stuck: renaming a variable and hoping for the best.",
     46),
    # score: tip-fit 9, laugh 8, glance 9, both-audiences 9,
    #   fresh 8 = 43. The stalling agent mirrors the developer, but
    #   "has read this file three times" is setup the joke mostly
    #   repeats rather than turns.
    ("Tip: the agent has read this file three times now. It isn't "
     "confused \u2014 it's stalling, exactly like you would.",
     43),
    # score: tip-fit 9, laugh 8, glance 8, both-audiences 7,
    #   fresh 8 = 40. The honest progress bar is a good image, but the
    #   agent is barely in the joke and "your estimates" leans on
    #   deadline humour the brief calls worn.
    ("Tip: the progress bar is the only honest thing here \u2014 it "
     "admits it has no idea how long this takes, unlike your "
     "estimates.",
     40),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
MAX_CHARS = 200


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= MAX_CHARS, \
            f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be a single line"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


# The selected tip (deterministic pick: highest score, then shortest):
# "Tip: breathe — the agent is doing exactly what you do when stuck:
# renaming a variable and hoping for the best." (110 characters)


def main():
    import os
    import sys

    tip = pick(CANDIDATES)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(tip)
    os.chmod("/output/entry.txt", 0o644)
    # Verify the written output: read it back byte-for-byte and re-check
    # the gate (1-200 characters, single line, non-blank). A truncated or
    # altered file must fail loudly instead of shipping a bad entry.
    with open("/output/entry.txt", "rb") as f:
        written = f.read().decode("utf-8")
    if written != tip:
        print("error: /output/entry.txt does not match selected tip",
              file=sys.stderr)
        sys.exit(1)
    if not (1 <= len(written) <= MAX_CHARS and written.strip()
            and "\n" not in written):
        print("error: /output/entry.txt fails gate: "
              f"{len(written)} chars", file=sys.stderr)
        sys.exit(1)
    print(tip)


if __name__ == "__main__":
    main()
