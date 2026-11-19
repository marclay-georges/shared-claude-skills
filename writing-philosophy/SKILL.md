---
name: writing-philosophy
description: >
  How to write anything a later session will act on: skills, agent and subagent prompts, session
  briefs, CLAUDE.md and memory edits, architecture documents, routine and scheduled-task prompts.
  Use whenever such a thing is being written, revised or reviewed, including a brief dashed off
  mid-task, and when Clay says "descriptive over prescriptive," "our philosophy," asks how to
  make a skill, prompt or CLAUDE.md better, or refers to "the skill-writing philosophy."
---

# Writing for a later reader

Much of what gets written in this workspace is not for Clay. It is for a Claude that has not
started yet: the skill a future session loads, the brief a subagent wakes up to, the line added to a
CLAUDE.md, the routine that fires at six in the morning. That reader has less context than the
writer, often cannot ask, and will act on the words. The test for whether a piece of writing falls
under this document is exactly that: will someone with less context than you act on it later?

The writer is usually Claude, mid-task, moving fast. A four-hundred-word agent prompt gets composed
in the gap between two tool calls, with no one invoking a skill first. So the craft here has to be
one you carry, not one you look up. The always-loaded block at the end of this file is what you
carry. This file is the reasoning behind it, for when you have time to think about the writing
itself.

Two outside sources recur below. "The context-engineering post" is Thariq Shihipar, "The new rules
of context engineering for Claude 5 generation models," claude.com/blog, 2026-07-24; the workspace
audit that applied it is `Projects/Career Cowork/.claude/CLAUDE-MD-AUDIT-2026-10-23.md`. "The
prompting reference" is Anthropic's prompting best-practices documentation.

Three kinds of reader show up most, and two things about them change how you write. The first is
whether a human is reachable. A session document is read with Clay present. A brief goes to a
subagent that should finish without asking. A routine runs with nobody there. The second is how
often the text is paid for. A CLAUDE.md line is read every session for months. A brief is read
once. A routine is read daily. Everything else in this document is the same for all three; the
section near the end says where they differ.


## Understanding over procedure, as a dial

The central idea has not changed. Explain what and why, then trust the reader to adapt. A reader who
understands why a procedure exists can handle the situation the procedure never anticipated. A
reader following a checklist cannot. This is the single most important idea here, and the rest
follows from it.

What has changed is the precision of the claim. It is not that documents should be descriptive. It
is that each passage sits somewhere on a dial between judgment and exact adherence, and the writer
chooses the setting passage by passage. Some things genuinely need exact adherence: a launch
command, a file path, a sequence where a skipped step breaks the ones after it, a boundary around
something irreversible, the way a fresh context window should begin before it has any state. For
those, be exact. Numbered steps are the right form when order matters. "Ask before deleting" is the
right form when deletion is the thing you cannot undo.

The dial has one rule regardless of setting: the purpose is on the page. An exact instruction with
its reason attached is something the reader can hold correctly, because they know what it protects
and can tell when a situation falls outside it. The same instruction without its reason is
something they can only obey or ignore. So the question for each passage is not "should this be a
rule or a principle" but "does the reader need exact adherence here, and do they know why."

An example of the difference, from this workspace. Insistence: "**NEVER** edit RESUME-SOURCE.md
directly. Always propose changes first." Purpose on the page: "RESUME-SOURCE.md is the only place
resume facts live, and every build selects from it verbatim, so one edit there changes every future
resume. Propose edits to it before making them." The boundary is just as firm in the second
version. The difference is that a reader can now tell what it protects, and so can recognize when a
situation falls outside it.


## What earns a line

Every line competes with every other line for the reader's attention, and in an always-loaded file
that competition is paid every session. The question of what to include matters as much as how to
say it.

Write what the reader cannot infer from the territory. These are the unknown knowns: the things so
obvious to the writer that they would never think to write them down, and that the reader would
never guess. In a codebase they are the gotchas, the one
place types live, the script that must run first. In a workflow they are Clay's actual preferences,
the ruling he gave once that overrides the sensible default, the failure that happened and should
not happen again. The context-engineering post says to spend most of a CLAUDE.md's tokens there,
and almost none on what a capable reader sees by looking.

Skip the obvious. A reader of this generation does not need to be told to read a file before
editing it, to verify after acting, or to use judgment. Telling them anyway is not harmless; it
dilutes the lines that matter and teaches the reader that the document does not trust them.

Prefer a reference to a description of one. When the thing you want is already embodied somewhere,
in code, a rendered artifact, a test suite, a rubric, a finished example of the output, point at it.
A description of a design is lossy; the HTML is not. A description of good output is an opinion;
a rubric a verifier can apply is a tool. The context-engineering post names this as a shift: simple specs gave way to
rich references because the reader can now handle them.


## The shapes prescription comes in

Prescription rarely announces itself. It arrives in ordinary forms: a bullet list of rules with no
reasoning attached, a bolded imperative, a parenthetical that quietly adds a constraint, a table of
what to do, a numbered protocol, a rule that says to always or never do something. None of these is
wrong on its own. A numbered protocol is right when order matters and a skipped step is a broken
one. "Always ask before X" is right when X is irreversible. The shape is not the problem; the shape
is where to look.

When a passage takes one of these forms, read it back and ask whether a reader could rebuild the
rule from its purpose. If the purpose is on the page, the shape is carrying a genuine requirement.
If the purpose is missing, the shape is carrying insistence, and the fix is to supply the reasoning
or to let the reader judge. The parenthetical deserves particular attention because it is the
quietest of these: a constraint slipped inside a clause reads as an aside and lands as a rule.

The deeper reason these shapes dominate is in the section on register below. Here the point is
only diagnostic: these are the forms to read back, every time, before the text leaves your hands.


## Teaching how to think, and the reader's mind

A document's job is to give the reader a mental model of the problem space. The test is whether a
reader who hits a situation the document never mentioned has enough understanding to reason
through it. If they would freeze, or follow the nearest-matching rule into the wrong outcome, the
document is missing a principle, not a rule.

Orient before instructing. Before saying what to do, help the reader see the landscape: what the
tools are and how they differ, what the trade-offs look like, what the problem space contains. A
reader who understands their tools can pick the right one for a situation you never drew.

Name the tensions. Real work involves competing priorities: speed against thoroughness, breadth
against depth, caution against momentum. Hide one behind a fixed choice and the reader will follow
your choice when the situation called for the other. Make the tension visible and say what should
govern it.

Surface the failure modes. If you know where things go wrong, say so and say why. A named failure
mode lets the reader recognize it in a form you did not anticipate. A rule guarding against it only
catches the form you did.

Then read the whole thing as the reader would. Could they start immediately? When something
unexpected happens, do they know the priorities well enough to make the call? Is there anything
they would follow literally that they should be adapting? That last question is the most
diagnostic; every yes marks a rule that needs its reason, or needs to become a principle.

Two things about the reader are easy to forget. A capable reader without a stated boundary will
helpfully expand into the adjacent territory: answering what should be escalated, reformatting what
should be left alone, analyzing where extraction was asked for. If scope matters, say what the scope
is and why, as context rather than constraint. And the reader rarely starts from nothing. There is
prior conversation, existing state, half-finished work. Good writing acknowledges that the world
already has state and teaches the reader to orient before acting.


## Structure carries meaning

Section order, narrative arc and hierarchy are load-bearing, not formatting.

Order follows dependency. The reader builds understanding top to bottom, so each section should be
able to assume what the ones above it established. When tempted to rearrange, ask what each section
assumes the reader already knows; that chain is the order.

The arc zooms in. Start at the widest frame, what this domain is and what tools exist, and narrow
toward specific action. Problem space, then principles, then patterns, then edge cases. This mirrors
how understanding builds; nobody can reason about element-level debugging before they understand the
page.

Depth lives in files loaded on demand. This is progressive disclosure in its structural sense, and
it is a different idea from "ship lean and observe" even though the two share a name. A skill that
has grown long should be a short core plus reference files the reader opens when the situation
calls for them. A CLAUDE.md that has grown long should point at skills and memory files rather than
carry everything. The context-engineering post's picture is a tree of files, each loaded at the
right time, in place of one central repository the reader has to carry whole.

The closing block is canonical. A document long enough to warrant one ends with its principles in
compressed form: a named phrase and a sentence or two each, short enough to scan, specific enough
to act on. It is not a summary. It is the form the reader carries when the longer text is gone.
Clay's CLAUDE.md carries a shorter paraphrase of it as always-loaded text, and points here for the
reasoning.


## Register is the fight

The model mirrors the register it reads. Write like a colleague briefing a colleague and the
reader works like one: thoughtful, adaptive, trusted. Write like a policy manual and the reader
behaves like something constrained by one.

This matters more than it sounds, because of what the reader has already read before they reach
your text. The harness prompt is prescriptive. Tool descriptions are prescriptive. Most CLAUDE.md
files, including the ones in this workspace, are bullets, bold and tables. A descriptive paragraph
inside that is one voice against many, and it loses by default. That is the real reason the shapes
above keep appearing in Claude-written text: they are the register of nearly everything Claude
reads, so they are the register it writes.

Two things follow. A document asking for judgment has to model judgment in its own prose; a
bulleted list of reasons to write in paragraphs undercuts itself. And a document added to an
existing file should match the file's voice, or the seam shows. The test is whether a reader could
tell where the original writing ends and the addition begins. When a document has established a
metaphor, extend it rather than introduce a competing one; shared vocabulary is shared reasoning.


## Examples and interfaces

Two pieces of current guidance pull against each other here. The prompting reference still says
that three to five examples are among the most reliable ways to steer format, tone and structure.
The context-engineering post says that for this generation of models, examples constrain the
exploration space, and that effort is better spent designing the interface: what parameters the
reader has, what an enumeration implies, what the tool's shape says about how to use it.

Both are right about different things. An example that fixes a format, the exact shape of a record
or a table, helps, because format is something the reader cannot infer and should not improvise.
An example that fixes an approach narrows, because the reader will reproduce the approach rather
than reason to a better one. So when you reach for an example, ask which kind it is. If it is
about the shape of the output, keep it. If it is about how to get there, consider whether a
well-designed interface, a reference, or a stated goal would serve better. The context-engineering post's own case is a todo
tool whose status enumeration teaches its use without a single example; that is the pattern.


## Where the three readers differ

A session document is paid for every session. CLAUDE.md, memory slots, Hot Context, the Brain
Queue: every line is read at the start of every session for as long as it stays. So the bar for
inclusion is highest here, and the content should be the gotchas and preferences a reader could not
infer. Keep durable rules and working state distinct; working state ages, and stale reads as
current. Point rather than copy. A second copy of anything canonical will drift from the first, and
the one that drifts will look equally official.

A brief's reader starts cold. A subagent or a new session knows only what the brief says. It cannot
see this conversation, and it should finish without asking. So a brief carries the goal, what has
already been ruled out and why, the files worth reading, the scope and the reason for its edges,
what done looks like, and which judgment calls are the reader's to make. Completeness beats brevity
here; a short brief does not save tokens, it moves the cost into the reader's guessing. And if you
want an independent read, hand over the material, not your conclusion. A reader given a hypothesis
tends to return it confirmed.

A routine has no one to ask. A scheduled prompt fires with nobody present, and it fires again
tomorrow. So it carries its own policy for the unexpected: what to do when an input is missing,
when the world has changed since it was written, when the task cannot complete. A good default for
deviations: pick the conservative option, log the deviation, keep going. Dates are absolute, because "this week" means something different every time it runs. The prompt is self-contained,
because memory and Hot Context may be stale by the time it fires. And it says where its output
lands and how Clay learns it ran, because a routine that finishes silently has not finished.


## Iterating on what you wrote

The first version is a hypothesis about what the reader needs. How the reader performs is the
test.

Read transcripts, not just outputs. Output says whether the reader succeeded. The transcript says
how: where it hesitated, what it reached for, where it spent effort it did not need to, what it
misread. A right answer reached wastefully is a writing problem as much as a wrong answer.

Resist the patch. When something goes wrong, the instinct is to add a rule for that case. Usually
the better move is to ask why the reader's understanding was not enough. Missing principle? Missing
context to apply a principle it had? Too many competing signals? The fix is usually clarifying,
adding one piece of context, or removing something that was confusing. A document that grows with
every iteration is being patched, not fixed.

Ship lean, then add from observation. This is the other sense of progressive disclosure, about
process rather than structure. Start with the smallest version that could work, watch how the
reader uses it, and add depth only where you saw it struggle. Do not add a section because it might
help. Add it because you watched its absence cost something.

Subtract before adding. When revising, look first for what can leave or merge; the work-hygiene
skill in this workspace says why. This iteration dropped the first version's standing section on
its relationship to the skill-creator tool (the mechanics of testing and packaging live there, this
file is about the writing, and one sentence says so), generalized the first version's
browser-skill anecdotes, merged two sections that said the same thing about the reader, and
retired its one named diagnostic, which had become a false all-clear once the thing it watched for
was trained away. The shapes section above is its replacement.


## Principles

**Someone with less context will act on this.** That is the test for whether this applies. If a
later session, a subagent, or a routine will read your words and do something, you are writing
guidance, however short it is.

**Understanding over procedure.** Explain what and why, then trust the reader to adapt. A reader who
knows why a procedure exists can handle the case it never anticipated.

**The dial is set per passage.** Exact commands, ordered sequences, irreversibility boundaries and
cold-start instructions need exact adherence, with their reason attached. Everything else needs
judgment, with the context to exercise it.

**Write what cannot be inferred.** Gotchas, preferences, rulings, the failure that happened. Skip
what a capable reader sees by looking. Point at a reference when one embodies what you mean.

**Shapes are where to look, not what to avoid.** A rule list without reasons, a bold imperative, a
constraining parenthetical, a table of what to do, a numbered protocol, an always or a never. Each
has its place. Read each one back and ask whether the reader could rebuild it from its purpose.

**Orient before instructing.** Describe the tools, their trade-offs, and the landscape. Name the
tensions and say what governs them. Surface the failure modes and why they happen.

**Every line competes.** Over-instruction degrades the result as much as under-instruction: it
buries the lines that matter and tells the reader it is not trusted. After drafting, read with
deletion in mind. The best version is the shortest one that still produces good work.

**Order follows dependency.** Later sections assume earlier ones. Zoom from the widest frame toward
specific action. Put depth in files loaded on demand.

**Model the register you ask for.** The reader mirrors what it reads, and most of what it reads is
prescriptive. A document asking for judgment is written in paragraphs that exercise it.

**A session file is paid for every session.** Gotchas over the obvious, durable rules apart from
working state, pointers instead of copies.

**A brief's reader starts cold.** Goal, what is ruled out and why, files worth reading, scope and
its reason, what done looks like, which calls are theirs. Material rather than conclusions if you
want an independent read.

**A routine has no one to ask.** Its own policy for missing inputs and a changed world, absolute
dates, self-contained, and explicit about where output lands and how anyone learns it ran.

**When it fails, resist the patch.** The instinct is a new rule for the case. Look first for the
missing principle, the missing context, or the clutter that caused the confusion. A document that
grows with every failure is being patched, not fixed.

**Read it through as the reader.** Could you start immediately? Do you know what must stay fixed and
why? Would you follow anything literally that you should adapt? Every yes to the last marks a
rule that needs its reason or needs to become a principle.

The reasoning behind each of these, and where the three readers differ in detail, is in the
`writing-philosophy` skill.
