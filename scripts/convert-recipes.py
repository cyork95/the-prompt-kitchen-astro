#!/usr/bin/env python3
"""
Convert Recipe Book HTML recipes to Astro Content Collection Markdown files.
Run from ThePromptKitchenV2 directory.
"""

import os
import re
import html

OUTPUT_DIR = r"C:\Users\coyof\Documents\Claude\Claude Code\ThePromptKitchenV2\src\content\recipes"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def strip_tags(text):
    """Remove HTML tags and decode entities."""
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    return text.strip()

def clean_pre(text):
    """Extract text from pre block."""
    m = re.search(r'<pre>(.*?)</pre>', text, re.DOTALL)
    if m:
        return html.unescape(m.group(1)).strip()
    return strip_tags(text)

# Recipe data: (slug, title, category, difficulty, tags, teaser, bestFor, whenToUse, featured)
# Then body content is written manually as MDX

recipes = [
    {
        "slug": "research-plan-implement",
        "title": "Research → Plan → Implement",
        "category": "Planning",
        "difficulty": "beginner",
        "tags": ["planning", "projects", "getting-started"],
        "teaser": "A 3-stage approach that prevents you from jumping into execution before you understand the problem.",
        "bestFor": "Work tasks, home projects, learning goals",
        "whenToUse": "Before starting any complex project",
        "featured": True,
        "body": '''Use this pattern when you're facing something unfamiliar or complex and you don't want to jump straight into doing — you want to think it through first. AI is excellent at helping you map a problem before diving in.

## The Recipe

```
I want to [describe your goal]. I'm not sure of the best approach yet, so let's do this in stages.

First, help me understand the landscape. What are the key things I should know before starting? What are the most common mistakes people make with this?

Then, based on that, suggest a concrete plan for my specific situation. I am [brief description of your context — experience level, resources, constraints].

Finally, give me the first 3 actionable steps I can take this week.
```

## Example — Planning a vegetable garden

```
I want to start a vegetable garden in my backyard. I'm not sure of the best approach yet, so let's do this in stages.

First, help me understand the landscape. What are the key things I should know before starting? What are the most common mistakes beginners make?

Then, based on that, suggest a concrete plan for my situation. I have a 10x12 foot sunny patch, I'm a complete beginner, and I want to grow things my family will actually eat — mostly salads, tomatoes, and herbs.

Finally, give me the first 3 actionable steps I can take this week.
```

> **New to AI?** Copy the example above, open [claude.ai](https://claude.ai) or [chat.openai.com](https://chat.openai.com), paste it in the message box, and press Enter. Replace the garden details with your own goal.

## Tips for better results

- The more specific your context (your experience, constraints, resources), the more tailored the plan will be.
- If you want to go deeper on the research phase, ask: *"What are the top 3 resources you'd recommend for learning more about this?"*
- For work projects, add "I need to present this to [audience]" to get communication-ready output.

## 🔁 Leftover Remixes

**🌶️ Spicy:** After the 3-step plan, add: *"Now identify the two assumptions in this plan most likely to be wrong — and tell me the cheapest way to test each one before I commit."*

**🧊 Mild:** Skip the research phase. Just ask: *"What is the single most important first step I should take this week to make progress on [goal]?"*

**💰 Budget:** *"What free resources — communities, YouTube channels, or books — would you use to learn this without spending money?"*
''',
    },
    {
        "slug": "teach-me-like",
        "title": "Teach Me Like I'm [level]",
        "category": "Learning",
        "difficulty": "beginner",
        "tags": ["learning", "education", "understanding"],
        "teaser": "Get any concept explained at exactly the right level for you — from curious 10-year-old to domain expert.",
        "bestFor": "Understanding concepts, skill-building, curiosity",
        "whenToUse": "Any time you want to learn something new",
        "featured": True,
        "body": '''AI is the most patient teacher in the world. It will explain anything at exactly the level you ask for — from "explain it to a curious 10-year-old" to "assume I have a graduate degree in this field." The trick is being explicit about your starting point.

## The Recipe

```
Explain [topic] to me like I'm [your level].

I already know: [what you do know — even "nothing" is fine]
I want to understand: [what specific aspect you're curious about]
Please use [analogies / real-world examples / no math] to make it concrete.
```

## Example — Understanding compound interest

```
Explain compound interest to me like I'm someone who never really paid attention in math class.

I already know: money in a savings account earns some interest each year, but beyond that I'm fuzzy.
I want to understand: why people say it's so powerful for long-term saving, and what the actual difference is between compound and simple interest.
Please use real-world examples with actual numbers to make it concrete — no formulas needed.
```

> **New to AI?** After reading the response, type *"Now explain the part about [whatever confused you]"* — the AI remembers what it just said and will go deeper on that specific part. You can ask as many follow-up questions as you want.

## Level guide — what to say for each depth

- **"like I'm 10 years old"** — pure basics, lots of analogies, no technical terms
- **"like a curious adult with no background"** — explain terms as you go, conversational
- **"I have general interest but no formal training"** — can use some standard terms if you explain them
- **"I'm a professional in a related field"** — assume domain knowledge, focus on the new thing
- **"I'm an expert, give me the nuance"** — skip the basics, go straight to edge cases and depth

## 🔁 Leftover Remixes

**🌶️ Spicy:** After the explanation, ask: *"Now quiz me with 3 questions to check whether I actually understood this. Grade my answers and fill in any gaps."*

**🧊 Mild:** Strip it back: *"Give me just the one key insight about [topic] that most people miss. One sentence."*

**💰 Budget:** *"What's the single best free resource — one book, video, or website — to actually learn this properly?"*
''',
    },
    {
        "slug": "devils-advocate-steelman",
        "title": "Devil's Advocate / Steelman",
        "category": "Critical Thinking",
        "difficulty": "home-cook",
        "tags": ["decision-making", "critical-thinking", "analysis"],
        "teaser": "Break AI's agree-with-you tendency — get the strongest case against your idea before you commit to it.",
        "bestFor": "Business decisions, purchases, plans, arguments",
        "whenToUse": "Before committing to a decision",
        "featured": True,
        "body": '''AI can get stuck agreeing with you — it's trained to be helpful and pleasant. This recipe breaks that pattern. A **Devil's Advocate** challenges your idea to find its weaknesses. A **Steelman** builds the strongest possible version of the opposing view. Both make your thinking sharper.

## The Devil's Advocate Recipe

```
I've decided to [your decision or plan]. I want you to play devil's advocate — push back hard on this idea. What are the strongest arguments against it? What could go wrong? What am I probably not considering? Don't soften it.
```

## The Steelman Recipe

```
I believe [your position]. But I want to understand the other side as charitably as possible. Give me the strongest, most thoughtful version of the opposing argument — not a strawman, but the best case someone who disagrees could make. Then tell me where you think the strongest points of genuine disagreement lie.
```

## Example — Deciding whether to freelance

```
I've decided to quit my job and go freelance as a graphic designer. I want you to play devil's advocate — push back hard on this idea. What are the strongest arguments against it? What financial, professional, or personal risks am I probably underweighting? What do most people get wrong about freelancing? Don't soften it.
```

> **New to AI?** This recipe works best after you've already made a decision and want a gut-check. After reading the response, you can ask *"Now give me the best counter-arguments to your objections"* to stress-test the other side too.

## 🔁 Leftover Remixes

**🌶️ Spicy:** Run both at once: *"Steelman my idea AND devil's advocate it simultaneously. Show me the strongest case for and against, then tell me where the real crux of the disagreement lies."*

**🧊 Mild:** Just the headlines: *"Give me the top 3 objections, each in one sentence. No explanation needed."*

**💰 Budget:** *"What's the cheapest, lowest-risk experiment I could run this week to test whether the main objection is actually true?"*
''',
    },
    {
        "slug": "step-by-step-breakdown",
        "title": "Step-by-Step Breakdown",
        "category": "Productivity",
        "difficulty": "beginner",
        "tags": ["productivity", "planning", "projects", "how-to"],
        "teaser": "Turn any overwhelming task into a concrete numbered list where every step is specific enough to actually do.",
        "bestFor": "Projects, new processes, technical tasks",
        "whenToUse": "Any time a task feels overwhelming",
        "featured": False,
        "body": '''When something feels too big to start, a numbered list of concrete steps cuts through the overwhelm. The key is being specific enough that each step is actually actionable — not "figure out the finances" but "open a spreadsheet and list every monthly expense."

## The Recipe

```
I need to [accomplish this goal]. Break this down into a step-by-step plan for me.

My situation: [relevant context — tools/software you have, your skill level, time available, constraints]

Give me concrete, actionable steps — each step should be specific enough that I know exactly what to do. Flag any steps where I might need outside help or where most people get stuck.
```

## Example — Setting up a home budget

```
I need to create a household budget for the first time. Break this down into a step-by-step plan for me.

My situation: I have a regular monthly salary, some irregular freelance income, and I've never formally tracked my spending before. I have access to my bank's online statements and I'm comfortable with Google Sheets.

Give me concrete, actionable steps — each step should be specific enough that I know exactly what to do. Flag any steps where most beginners get stuck or where decisions get complicated.
```

> **New to AI?** After you get the step list, pick just the first step and ask: *"Help me do step 1 right now."* The AI will walk you through that single step in detail.

## 🔁 Leftover Remixes

**🌶️ Spicy:** After the steps: *"Now identify which two steps are the most likely failure points for most people, and give me a contingency for each one."*

**🧊 Mild:** Bite-sized: *"Give me just the first 3 steps. I'll ask for more once I've done those."*

**💰 Budget:** *"Do the full plan but with zero budget — what's the free or DIY version of each step?"*
''',
    },
    {
        "slug": "summarize-for-audience",
        "title": "Summarize for [Audience]",
        "category": "Communication",
        "difficulty": "beginner",
        "tags": ["summarizing", "communication", "documents", "writing"],
        "teaser": "Turn any long document into a crisp summary calibrated for exactly who needs to read it.",
        "bestFor": "Work documents, research papers, meeting notes, news",
        "whenToUse": "After reading a long document, article, or report",
        "featured": False,
        "body": '''Not all summaries are the same. A summary for your CEO should look different from one you'd send to a colleague, which should look different from what you'd explain to a friend. Specifying the audience unlocks much more useful output.

## The Recipe

```
Here's [a document / article / set of notes]:

[paste your content here]

Summarize this for [your audience]. They need to understand [specific aspect they care about]. Keep it to [length — e.g., "3 bullet points" or "a short paragraph" or "under 100 words"]. Use [plain language / technical terms are fine / bullet points / prose].
```

## Example — Summarizing a medical article

```
Here's an article about a medication my father's doctor has recommended:

[paste article text here]

Summarize this for a 70-year-old with no medical background. He needs to understand what the medication is for, the most common side effects to watch out for, and whether there's anything he should ask his doctor. Keep it to a short, plain-English paragraph and a brief bullet list. No medical jargon — if a technical term is necessary, explain it in brackets.
```

> **New to AI?** Copy the text you want summarized (from a website, PDF, or document), then paste it into the chat after the recipe text. Most AI tools can read quite large blocks of text.

## Audience variations

| Audience | What to say |
|---|---|
| Executive / Boss | "For a busy executive who will spend 30 seconds reading this" |
| Non-specialist | "For someone with no background in [field]" |
| Specialist | "For a [profession] — use appropriate terminology" |
| Child / Family | "For a [age]-year-old / my non-technical family" |
| Public / Social | "For a general audience — could appear in a tweet thread" |

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"After the summary, give me the 3 questions a smart, skeptical reader would ask after reading this."*

**🧊 Mild:** *"Give me the single most important sentence from this document."*

**💰 Budget:** *"What's the one action I should take based on this document? Just one."*
''',
    },
    {
        "slug": "draft-critique-revise",
        "title": "Draft → Critique → Revise Loop",
        "category": "Writing",
        "difficulty": "home-cook",
        "tags": ["writing", "editing", "email", "documents"],
        "teaser": "A 3-step loop that produces better writing than asking once — draft, get it critiqued, then revise.",
        "bestFor": "Emails, proposals, essays, cover letters",
        "whenToUse": "Any time the writing quality actually matters",
        "featured": True,
        "body": '''The first draft AI produces is almost never the final product — and that's fine. This recipe treats AI as a writing partner, not a vending machine. You get a draft, have it torn apart, and then produce something much better.

## The Recipe

**Step 1 — Draft**
```
Write a [type of writing] for [situation/audience/purpose].

Here's my context: [everything the AI needs to know]

Tone: [formal / conversational / persuasive / etc.]
Length: [rough target]
Key points to include: [bullet points]
```

**Step 2 — Critique**
```
Now critique what you just wrote. What's weak? What would a skeptical reader push back on? What's missing? What could be cut? Be honest — don't just validate it.
```

**Step 3 — Revise**
```
Now rewrite it based on your own critique, fixing the issues you identified. Also apply this additional feedback from me: [your own notes].
```

## Example — Cover letter

**Step 1 prompt:**
```
Write a cover letter for a Senior Product Manager role at a fintech startup. I'm transitioning from a traditional banking background. I want to show I understand both the established finance side and the startup agility they're looking for. Tone: confident but not arrogant. Around 300 words.
```

**Step 2 prompt:**
```
Now critique that cover letter. What would a hiring manager with 200 applications cringe at? What feels generic? What's the strongest part? What's the weakest?
```

**Step 3 prompt:**
```
Rewrite it based on your critique. Also: make the opening line less generic — it currently sounds like every other cover letter.
```

> **New to AI?** This is a conversation — each message builds on the last. Don't start a new chat between steps. The AI remembers everything in the current conversation.

## 🔁 Leftover Remixes

**🌶️ Spicy:** After Step 3, add a Step 4: *"Now read this as a hostile critic trying to find reasons to dismiss it. What's the last remaining weakness?"*

**🧊 Mild:** Skip the loop — just ask: *"Write [X], then tell me what you'd change if you had more space."*

**💰 Budget:** *"Give me just the opening paragraph. I'll write the rest myself."*
''',
    },
    {
        "slug": "act-as-expert",
        "title": "Act as [Expert]",
        "category": "Getting Advice",
        "difficulty": "beginner",
        "tags": ["role-playing", "expertise", "advice", "consulting"],
        "teaser": "Frame AI as a specific expert and get answers calibrated to that domain's real vocabulary and concerns.",
        "bestFor": "Getting domain-specific advice without paying consultant rates",
        "whenToUse": "When you need expertise you don't have",
        "featured": False,
        "body": '''Asking AI to "act as" a specific expert shifts both the vocabulary and the depth of the answer. A generic "help me with my business plan" gets a different response than "act as a venture capitalist who has seen 500 pitches — tear my business plan apart."

## The Recipe

```
Act as a [specific role — e.g., "senior UX designer", "experienced divorce lawyer", "startup CFO"].

Your task: [what you want them to do]

My situation: [all relevant context]

Please respond as that expert would — using the vocabulary, frameworks, and level of detail appropriate for that role. If there's something important I haven't told you that you'd need to know, ask me.
```

## Example — Getting UX feedback

```
Act as a senior UX designer with 15 years of experience and strong opinions about conversion optimization.

Your task: Review my landing page copy and layout description and tell me what you'd change.

My situation: I'm launching a B2B SaaS tool for small accounting firms. The page currently has: a headline saying "Accounting made simple", a 200-word feature list, one screenshot, and a "Book a Demo" CTA. Conversion rate is under 1%.

Please respond as that expert would — tell me the top 3 problems and how you'd fix each one. Don't be gentle.
```

## Good expert roles to try

| Goal | Expert role to use |
|---|---|
| Business decisions | "Experienced entrepreneur who has built and sold 3 companies" |
| Writing | "Editor at a major magazine who has a low tolerance for fluff" |
| Career | "Executive recruiter who has placed 500 candidates in your industry" |
| Technical | "Senior engineer who does thorough code reviews" |
| Legal (general info only) | "Experienced solicitor explaining this concept — not legal advice" |

> **Note:** AI isn't a licensed professional. For medical, legal, or financial decisions, use this for orientation and education — then consult a real expert.

## 🔁 Leftover Remixes

**🌶️ Spicy:** Use multiple experts: *"First respond as a [Expert A]. Then respond as a [Expert B] who would completely disagree. Then tell me where the truth probably lies."*

**🧊 Mild:** Just ask: *"What would a [expert type] think of [my situation/plan]?"*

**💰 Budget:** *"What's the one question a [expert] would immediately ask that I haven't thought about?"*
''',
    },
    {
        "slug": "rubber-duck-debugging",
        "title": "Rubber Duck Debugging",
        "category": "Coding",
        "difficulty": "home-cook",
        "tags": ["coding", "debugging", "problem-solving", "technical"],
        "teaser": "Explain your code or problem to AI like a patient rubber duck — the act of explaining often reveals the bug.",
        "bestFor": "Coding bugs, logical errors, any problem you've been staring at too long",
        "whenToUse": "When you're stuck and can't see what's wrong",
        "featured": False,
        "body": '''The classic rubber duck debugging technique — explain your code to a rubber duck until you spot the bug yourself — works even better with AI. The AI actually responds, asks questions, and spots things you've been staring past for an hour.

## The Recipe

```
I'm trying to [what the code/system is supposed to do].

Here's the problem: [describe what's actually happening vs. what you expect]

Here's the relevant code / setup:
[paste your code or describe your system]

Walk me through what this code is actually doing, step by step. Don't jump straight to a fix — first help me understand where the logic breaks down. Then suggest the fix.
```

## Example — A loop that's not working

```
I'm building a script that should send a reminder email to everyone on a list who hasn't responded in 3 days.

The problem: It's sending reminders to everyone, including people who have responded. I've checked the condition twice and it looks right to me.

Here's the relevant code:
[paste code]

Walk me through what this loop is actually doing, step by step. Don't jump straight to a fix — first help me understand where the logic breaks down.
```

> **Works for non-coders too.** Stuck on a spreadsheet formula? A logic puzzle? A process that isn't working? Use the same approach — describe what you expect vs. what's happening, then ask AI to walk through it step by step.

## 🔁 Leftover Remixes

**🌶️ Spicy:** After the fix: *"Now assume the fix introduces a new bug. What's the most likely unintended consequence of the change you just suggested?"*

**🧊 Mild:** Just paste the code and ask: *"Explain what this code does, line by line, in plain English."*

**💰 Budget:** *"Without fixing it, just tell me: what are the 3 most likely causes of this kind of bug?"*
''',
    },
    {
        "slug": "chain-of-thought",
        "title": "Chain of Thought",
        "category": "Problem Solving",
        "difficulty": "home-cook",
        "tags": ["reasoning", "problem-solving", "analysis", "thinking"],
        "teaser": "Make AI show its work — force step-by-step reasoning to get more accurate answers on complex problems.",
        "bestFor": "Math problems, logic puzzles, multi-step analysis, decisions with many variables",
        "whenToUse": "When you need accurate reasoning, not just a fast answer",
        "featured": False,
        "body": '''AI produces better answers when it reasons out loud. Without prompting, it often jumps straight to a conclusion — which can be wrong on complex problems. "Chain of thought" prompting forces it to think step by step, catching errors in its own reasoning.

## The Recipe

```
[Your question or problem]

Before giving me your answer, think through this step by step. Show your reasoning at each stage. Only give me your final answer after you've worked through it.
```

Or alternatively:

```
Let's think through this carefully. Walk me through each step of your reasoning before reaching a conclusion. If any step depends on assumptions, call them out.
```

## Example — A tricky word problem

```
A shop buys items for £8 each and sells them for £10. But 20% of items sold get returned, and returned items can't be resold. If they sell 100 items, what's their profit?

Before giving me your answer, think through this step by step. Show your reasoning at each stage.
```

## When to use chain of thought

- Math problems with multiple steps
- Logic puzzles
- Decisions with several variables (e.g., "should I take the job offer?")
- Anything where you've gotten a suspiciously fast confident answer
- Medical, financial, or legal explanations (forces it to be more careful)

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Now challenge your own reasoning. What's the weakest step in your chain of thought? What assumption is most likely to be wrong?"*

**🧊 Mild:** After getting a fast answer you're unsure about: *"Walk me through how you got that — I want to check the reasoning."*

**💰 Budget:** *"Just give me the key equation or logic principle this question turns on."*
''',
    },
    {
        "slug": "constraints-guardrails",
        "title": "Constraints & Guardrails",
        "category": "Writing",
        "difficulty": "beginner",
        "tags": ["constraints", "writing", "control", "format"],
        "teaser": "Tell AI what NOT to do — guardrails are just as powerful as instructions for getting usable output.",
        "bestFor": "Any writing task where AI tends to over-produce or miss the mark",
        "whenToUse": "When you keep getting outputs that are too long, too formal, or miss the point",
        "featured": False,
        "body": '''Most people tell AI what to do. Fewer people tell it what *not* to do — and that second part is where the real control lives. Guardrails constrain AI's natural tendencies (too long, too hedge-y, too formal) and steer it toward what you actually want.

## The Recipe

Add any of these constraint phrases to your existing prompts:

```
Constraints:
- Maximum [X] words / sentences / bullet points
- No [jargon / buzzwords / passive voice / clichés / filler phrases]
- Do not start with [a question / "Certainly!" / "Great question!"]
- Avoid [giving advice I didn't ask for / adding a disclaimer / moralizing]
- Write as [a human would / a friend would / a [specific style]]
- Do not use [headers / bullet points / numbered lists] — just prose
- Never say [specific phrase you hate]
```

## Example — Email that sounds human

```
Write a follow-up email to a client after our discovery call.

Context: We had a 45-minute call. They're interested but not committed. I want to remind them of the key value I can offer and suggest a next step.

Constraints:
- Maximum 150 words
- Conversational tone — like an email from a person, not a corporation
- No buzzwords ("synergies", "leverage", "value-add")
- Don't start with "I hope this email finds you well"
- No bullet points — just short paragraphs
- End with a specific, low-pressure next step
```

## Most useful constraints by situation

| Situation | Constraint to add |
|---|---|
| AI is too long | "Maximum [X] words" or "Give me just the key points, not a full essay" |
| AI sounds robotic | "Write like a human talking to a friend" |
| AI keeps adding disclaimers | "Skip the caveats — just answer the question" |
| AI starts with pleasantries | "Do not open with affirmations like 'Great question!'" |
| AI is too formal | "Casual tone, like a Slack message, not an email" |

## 🔁 Leftover Remixes

**🌶️ Spicy:** Ask AI to write its own constraints first: *"Before writing this, tell me what constraints you think I should apply given my goal. Then apply them."*

**🧊 Mild:** Single constraint: *"Same prompt, but this time: maximum 3 sentences."*

**💰 Budget:** *"Write this in the most minimal way possible. What's the single sentence version?"*
''',
    },
    {
        "slug": "compare-options",
        "title": "Compare My Options",
        "category": "Decision Making",
        "difficulty": "beginner",
        "tags": ["decision-making", "comparison", "analysis", "evaluation"],
        "teaser": "Get a structured comparison of your specific options — not a generic pros/cons list, but one built for your situation.",
        "bestFor": "Purchases, career moves, business decisions, tool choices",
        "whenToUse": "When you have 2–5 concrete options and need to choose",
        "featured": False,
        "body": '''Generic pros-and-cons lists are useless if they ignore your specific situation. This recipe gets AI to compare options based on what actually matters to *you* — your constraints, your priorities, your context.

## The Recipe

```
I'm deciding between: [list your options]

My situation: [who you are, what you need, what your constraints are]

Compare these options for my specific situation. For each one, tell me:
- How well it fits what I actually need
- The biggest advantages in my case
- The hidden costs or downsides I might not see
- Who it's actually best for (and whether that's me)

Then give me your recommendation, with a reason.
```

## Example — Choosing a project management tool

```
I'm deciding between: Notion, Linear, and Trello

My situation: I run a 4-person freelance agency. We need to track client projects, not internal product development. We're not technical. Budget is a concern — we need free or very cheap. We've tried and abandoned Asana.

Compare these options for my specific situation. For each one, tell me how well it fits, the biggest advantages for my use case, hidden costs or downsides, and who it's really built for. Then recommend which one I should try first.
```

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Now make the case for the option you recommended least. If someone disagreed with your recommendation, what would be their best argument?"*

**🧊 Mild:** *"Skip the full comparison — just tell me which you'd choose if you were in my situation, and why in 2 sentences."*

**💰 Budget:** *"Assuming I need to minimize cost to zero, which option is the best free version and what am I giving up?"*
''',
    },
    {
        "slug": "iterative-refinement",
        "title": "Iterative Refinement",
        "category": "Writing",
        "difficulty": "home-cook",
        "tags": ["writing", "editing", "iteration", "refinement"],
        "teaser": "Build toward exactly what you want through a series of directed refinements rather than one perfect prompt.",
        "bestFor": "Any creative or written output that needs to feel just right",
        "whenToUse": "When a single prompt isn't getting you there",
        "featured": False,
        "body": '''Trying to write the perfect single prompt is a trap. Professional writers know that great work comes from iteration — a rough draft, then shaping, then polishing. AI works the same way. The trick is being specific about each refinement rather than saying "make it better."

## The Pattern

Start broad, then refine with specific directions:

```
[Initial request — just get something on the page]
```

Then iteratively shape it:
```
That's close. Now change these specific things:
- [Change 1 — be very specific]
- [Change 2]

Keep everything else the same.
```

## Example — A product description

**First pass:**
```
Write a product description for a handmade leather wallet. It's made by a small artisan in Scotland, takes 3 weeks to make, and costs £180.
```

**Refinement 1:**
```
Good start. Now change:
- Shorter — cut it by half
- Less adjective-heavy ("beautiful", "stunning" etc)
- Add a specific detail about the leather or the maker that sounds real, not marketing-speak
Keep the structure the same.
```

**Refinement 2:**
```
Better. Now:
- The opening line is still too generic. Replace it with something specific that earns the reader's attention in the first 5 words
- The final sentence feels like a tagline. Make it feel more like a craftsperson talking
```

## Key refinement moves

| Problem | What to say |
|---|---|
| Too long | "Cut this to [X] words. Keep the best parts, cut the rest." |
| Sounds generic | "Find and replace every generic word with something specific." |
| Wrong tone | "Make it sound like [X] wrote this, not a copywriter." |
| Missing something | "Add [element]. Place it after [specific point]." |
| Too formal / informal | "Shift the register to [more conversational / more professional]. Everything else stays." |

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Show me 3 completely different versions of the opening sentence. I'll pick one and we'll build from there."*

**🧊 Mild:** *"What's the single most impactful change you could make to this piece? Just that one thing."*

**💰 Budget:** *"What's the shortest version that still works?"*
''',
    },
    {
        "slug": "meeting-notes-cleaner",
        "title": "Meeting Notes Cleaner",
        "category": "Productivity",
        "difficulty": "beginner",
        "tags": ["productivity", "meetings", "notes", "summarizing"],
        "teaser": "Turn chaotic raw meeting notes into structured summaries, action items, and follow-up emails in seconds.",
        "bestFor": "Work meetings, client calls, team discussions, project check-ins",
        "whenToUse": "After any meeting where something important was decided or assigned",
        "featured": False,
        "body": '''Raw meeting notes are usually a mess — half-finished thoughts, tangents, initials without context. This recipe turns them into something actually useful: a clean summary, a clear action list, and if needed, a ready-to-send follow-up.

## The Recipe

```
Here are my raw notes from a meeting:

[paste your raw notes]

Please:
1. Write a short summary of what was discussed and decided (3–5 sentences max)
2. List all action items in this format: [Who] will [what] by [when — if mentioned]
3. Flag any decisions that seem unclear or anything that probably needs to be confirmed with the group

Meeting context: [who attended, what the meeting was about — optional but helps]
```

## Example

```
Here are my raw notes from a meeting:

kicked off at 2pm. mark and sarah there plus me. talked about q4 launch. sarah said marketing budget approved but only 60% of what we asked for. mark wants to push launch to nov instead of oct - sarah not sure. action: mark to put together revised timeline by friday. i need to check with design team about asset delivery. no one mentioned legal review - is that still needed? sarah leaving for conference next week.

Please:
1. Summary of what was discussed and decided
2. All action items with owner and deadline
3. Anything unclear or needing follow-up confirmation

Meeting context: Q4 product launch planning call, 3 attendees.
```

## 🔁 Leftover Remixes

**🌶️ Spicy:** Add: *"Also write a follow-up email I can send to all attendees — summary + action items in a readable format."*

**🧊 Mild:** Just: *"What are the 3 most important things from these notes?"*

**💰 Budget:** *"List only the action items. Who does what by when."*
''',
    },
    {
        "slug": "code-review-partner",
        "title": "Code Review Partner",
        "category": "Coding",
        "difficulty": "sous-chef",
        "tags": ["coding", "code-review", "technical", "software"],
        "teaser": "Get a thorough code review that covers correctness, edge cases, security, and readability — not just style.",
        "bestFor": "Any code before it ships, solo projects without a reviewer",
        "whenToUse": "Before merging or deploying code",
        "featured": False,
        "body": '''Working solo means no one reviews your code before it goes out. This recipe fills that gap — give AI your code and specific context, and get the kind of feedback a senior developer would give in a thorough review.

## The Recipe

```
Please review this code as a senior [language] developer with a strong focus on [your priorities — e.g., security, performance, readability, maintainability].

Context:
- What this code does: [brief description]
- Where it runs: [production / prototype / internal tool / etc.]
- My experience level: [approximate]
- Languages/frameworks: [relevant stack]

Code:
[paste your code]

Review it for:
1. Correctness — will this actually do what I think it does?
2. Edge cases — what inputs or states could break it?
3. [Your priority — e.g., security vulnerabilities / performance / readability]
4. Anything I'll regret in 6 months

Be specific. For each issue, tell me the line or section and exactly what to change.
```

## Example priorities for the review

| Context | Priority to add |
|---|---|
| User-facing production | "Security vulnerabilities and input validation" |
| Performance-sensitive | "Inefficiencies and N+1 queries" |
| Long-term codebase | "Maintainability and what will be confusing to the next dev" |
| Prototype | "Correctness — are there any logic errors?" |

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"After the review, rewrite the worst part in a way that fixes all the issues you identified."*

**🧊 Mild:** *"Just tell me the single most serious issue in this code. One thing."*

**💰 Budget:** *"Read this code and tell me: what's the most likely bug that will show up in production?"*
''',
    },
    {
        "slug": "interview-prep-coach",
        "title": "Interview Prep Coach",
        "category": "Career",
        "difficulty": "home-cook",
        "tags": ["career", "interviews", "job-search", "preparation"],
        "teaser": "Practice real interview questions for your specific role and get honest feedback on your answers.",
        "bestFor": "Job interviews, promotions, university applications",
        "whenToUse": "The week before an interview",
        "featured": False,
        "body": '''Most people prepare for interviews by reading lists of "common questions." That's not preparation — it's memorization. This recipe simulates a real interview, forces you to answer out loud (by typing), and gives you honest feedback on what's weak.

## The Recipe

```
Act as a tough but fair interviewer for a [job title] role at a [type of company].

My background: [2–3 sentences about your experience and what you bring]
The role: [paste the job description or describe the key responsibilities]

Conduct a mock interview with me. Ask me one question at a time, wait for my answer, then give me brief feedback on that answer (what worked, what was weak, what a strong answer would have included). Then ask the next question.

Focus on: [behavioral questions / technical questions / case studies — pick your focus]

Start with the question.
```

## How to run it

1. Paste the prompt and let AI ask the first question
2. Answer as you would in a real interview — type it out fully
3. Read the feedback carefully — the criticism is the valuable part
4. Ask AI to follow up with a harder version of the same question
5. After 5–6 questions, ask: *"Based on my answers so far, what's my biggest gap?"*

## Follow-up moves

After any answer:
- *"Ask me a follow-up that probes where my answer was vague"*
- *"What would a great answer to that question have included that I missed?"*
- *"Now give me the same question but phrased in the hardest possible way"*

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Now ask me the question interviewers ask when they're trying to disqualify someone — the trap questions."*

**🧊 Mild:** *"Just give me the 5 questions you'd most expect in this interview. I'll prepare answers on my own."*

**💰 Budget:** *"What's the one answer I need to get right in this interview to get the job?"*
''',
    },
    {
        "slug": "reframe-problem",
        "title": "Reframe the Problem",
        "category": "Problem Solving",
        "difficulty": "home-cook",
        "tags": ["problem-solving", "creativity", "thinking", "innovation"],
        "teaser": "Escape the frame you're stuck in — let AI restate your problem in a way that opens up solutions you haven't considered.",
        "bestFor": "Any problem where you keep hitting the same wall",
        "whenToUse": "When you're stuck in a loop and all your solutions feel incremental",
        "featured": False,
        "body": '''The way a problem is framed largely determines what solutions seem possible. "How do I make my meetings shorter?" gives different answers than "How do I get the outcomes we currently use meetings for, without meetings?" Same underlying issue, very different solutions.

This recipe asks AI to take your problem and restate it several different ways — often unlocking solutions that were invisible in the original frame.

## The Recipe

```
Here's the problem I'm trying to solve: [your problem as you currently understand it]

Restate this problem in 4 completely different ways that might open up new solutions:
1. A version that focuses on a different root cause
2. A version that inverts it (what if we wanted the opposite outcome?)
3. A version that expands the scope (what's the bigger problem this is a symptom of?)
4. A version that narrows the scope (what's the smallest version of this problem I could solve first?)

For each restatement, suggest one possible solution that the reframing suggests.
```

## Example

```
Here's my problem: My SaaS tool has a 40% churn rate after the first 30 days.

Restate this problem in 4 different ways:
1. A version that focuses on a different root cause
2. An inverted version
3. An expanded scope version
4. A narrowed scope version

For each, suggest one possible solution.
```

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Give me the most counterintuitive reframe you can. What's the version of this problem that would make someone laugh or seem ridiculous — but might actually contain a real insight?"*

**🧊 Mild:** *"Restate my problem in one sentence that makes the solution more obvious."*

**💰 Budget:** *"What's the version of this problem I could solve today with what I already have?"*
''',
    },
    {
        "slug": "tone-shift",
        "title": "Tone Shift",
        "category": "Communication",
        "difficulty": "beginner",
        "tags": ["writing", "tone", "communication", "editing"],
        "teaser": "Rewrite the same content for a completely different register — from formal to casual, clinical to warm, or direct to diplomatic.",
        "bestFor": "Emails, social posts, reports, any content going to multiple audiences",
        "whenToUse": "When you've written something for one audience and need a version for another",
        "featured": False,
        "body": '''You've written a solid piece of content — but it's pitched at the wrong register for this audience. Rewriting from scratch wastes time. This recipe takes your existing content and shifts the tone while keeping the substance.

## The Recipe

```
Here's my original text:

[paste your text]

Rewrite this in a [target tone] tone for [audience].

Current tone: [describe what you have]
Target tone: [describe what you need]
What must stay the same: [key facts, key points, length constraints]
What can change: [tone, vocabulary, sentence structure, examples used]
```

## Tone pairs — what to ask for

| From | To | Say this |
|---|---|---|
| Corporate / formal | Human / conversational | "Rewrite for a Slack message from a colleague, not a corporate memo" |
| Casual | Professional | "Rewrite as a formal email to an executive — no contractions, proper structure" |
| Technical | Plain English | "Rewrite for someone with no technical background — no jargon" |
| Direct / blunt | Diplomatic | "Rewrite to soften the criticism — same message, less confrontational" |
| Cold | Warm | "Rewrite with more warmth and empathy — same content, different relationship" |
| Long | Punchy | "Rewrite in half the words. Every sentence should earn its place." |

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Now write 3 completely different tones side-by-side: professional, casual, and playful. Let me pick which one I actually want to send."*

**🧊 Mild:** *"Change just the first paragraph to feel more [tone]. Keep everything else."*

**💰 Budget:** *"What's the one word or phrase in this text that most kills the [target] tone? What should I change it to?"*
''',
    },
    {
        "slug": "gap-finder",
        "title": "Gap Finder",
        "category": "Critical Thinking",
        "difficulty": "sous-chef",
        "tags": ["analysis", "critical-thinking", "strategy", "evaluation"],
        "teaser": "Find what's missing from your plan, argument, or proposal before someone else does.",
        "bestFor": "Business plans, proposals, essays, strategic documents",
        "whenToUse": "After you've written something important and before it goes out",
        "featured": False,
        "body": '''You've written a solid plan. You can see what you've covered. What you can't easily see is what's missing. This recipe gives your document to AI with one specific job: find what's not there.

## The Recipe

```
Here's my [document / plan / proposal / argument]:

[paste your content]

Your job: find what's missing, not what's wrong with what's there.

Specifically:
1. What questions would a skeptical reader have that this doesn't answer?
2. What assumptions does this make that aren't stated or defended?
3. What scenarios or edge cases aren't accounted for?
4. What's the weakest section that needs more support?
5. What would you add if you were the author?
```

## Example — A business plan review

```
Here's my business plan for a local meal prep delivery service:

[paste plan]

Find what's missing:
1. What questions would a potential investor have that this doesn't address?
2. What assumptions am I making that I haven't defended?
3. What scenarios haven't I considered?
4. What section is weakest?
5. What critical section is missing entirely?
```

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Imagine you're trying to poke holes in this to get out of a contract. What are the 3 gaps you'd exploit?"*

**🧊 Mild:** *"What's the single most important thing missing from this? Just one."*

**💰 Budget:** *"What one question does this leave unanswered that the reader will absolutely ask?"*
''',
    },
    {
        "slug": "cold-email-that-gets-replies",
        "title": "Cold Email That Gets Replies ✨",
        "category": "Communication",
        "difficulty": "home-cook",
        "tags": ["email", "outreach", "sales", "networking"],
        "teaser": "Write cold emails that get real responses — short, specific, and built around what matters to the recipient.",
        "bestFor": "Job outreach, sales emails, partnership requests, journalist pitches",
        "whenToUse": "When you need to reach someone who doesn't know you",
        "featured": True,
        "body": '''Most cold emails fail because they're about the sender. The ones that work are about the recipient — what they care about, what problem they have, why this email is worth 30 seconds of their time. This recipe is designed around that principle.

## The Recipe

```
Write a cold email to [who you're contacting and their role].

Purpose: [what you want — a reply, a call, an introduction, etc.]

About them: [what you know about this person or their company — be specific]

About me: [who you are and why you're relevant — brief]

The value for them: [what's in it for them — why should they respond?]

Constraints:
- Maximum 150 words
- No "I hope this email finds you well" or similar openers
- Lead with something specific about them, not about me
- Clear, single ask at the end
- Conversational tone — like a human, not a pitch deck
```

## What makes a cold email work

| Element | Bad version | Good version |
|---|---|---|
| Opening | "I hope you're well..." | "I read your thread about [specific thing] and..." |
| Who you are | "I'm the founder of [startup]..." | One sentence, only what's relevant to them |
| The ask | "I'd love to connect sometime" | "Would a 15-minute call next week work?" |
| Length | 3 paragraphs | 4–6 sentences |

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Write 3 completely different opening lines for this email. I'll pick the strongest one."*

**🧊 Mild:** *"Critique the cold email I've already written and tell me the one thing most likely to get it deleted."*

**💰 Budget:** *"What's the single most important sentence I need to get right in this cold email?"*
''',
    },
    {
        "slug": "learn-any-skill-30-days",
        "title": "Learn Any Skill in 30 Days ✨",
        "category": "Learning",
        "difficulty": "beginner",
        "tags": ["learning", "skills", "self-improvement", "study"],
        "teaser": "Get a realistic, structured 30-day learning plan for any skill — with daily habits, milestones, and resources.",
        "bestFor": "Languages, technical skills, instruments, professional skills, hobbies",
        "whenToUse": "When you're serious about learning something new",
        "featured": False,
        "body": '''Most people learn new skills inefficiently — watching tutorials without practicing, or practicing without structure. A good learning plan alternates input (learning) with output (doing) and has clear milestones so you know if you're on track. This recipe builds one for you.

## The Recipe

```
I want to learn [skill] in the next 30 days. I can commit [X hours per week].

My current level: [complete beginner / some basics / intermediate]
My goal: [what "success" looks like at the end of 30 days — be specific]
I learn best by: [videos / reading / doing / being taught / a mix]
Resources I have: [tools, subscriptions, equipment you already have]

Build me a realistic 30-day learning plan with:
1. Week-by-week milestones (what I should be able to do by the end of each week)
2. A daily habit I can do in [your time limit] that compounds over 30 days
3. The 3 most important things to focus on (and what most beginners waste time on)
4. Free resources you'd use if you were learning this from scratch
```

## After the plan — how to use it well

- Ask: *"What's the one thing that separates people who successfully learn this from those who give up?"*
- After week 1: *"I've been doing [what you've been doing]. What should I adjust for week 2?"*
- If stuck: *"I'm struggling with [specific thing]. What exercise would help me break through this?"*

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Give me the aggressive version — what would the plan look like if I had 2 hours a day and wanted to reach [ambitious milestone] in 30 days?"*

**🧊 Mild:** *"Just tell me the single most important thing to practice in the first week."*

**💰 Budget:** *"What's the free version of this learning plan? No paid courses, apps, or subscriptions."*
''',
    },
    {
        "slug": "content-repurposing-machine",
        "title": "Content Repurposing Machine ✨",
        "category": "Content Creation",
        "difficulty": "home-cook",
        "tags": ["content", "social-media", "writing", "marketing"],
        "teaser": "Turn one piece of content into many — a single blog post becomes a thread, a newsletter, a LinkedIn post, and more.",
        "bestFor": "Bloggers, creators, marketers, anyone building an audience",
        "whenToUse": "After creating any long-form content",
        "featured": False,
        "body": '''Creating original content is hard. Distributing what you've already created is not — but most people don't do it systematically. This recipe takes one piece of content and extracts everything useful from it into other formats.

## The Recipe

```
Here's my original [blog post / newsletter / video transcript / podcast notes]:

[paste your content]

Repurpose this into:
1. A Twitter/X thread (8–10 tweets, hook tweet first, actionable throughout)
2. A LinkedIn post (professional tone, 150–200 words, end with a question)
3. A 3-sentence email newsletter teaser (with a "read more" call to action)
4. A TikTok / short video script (60 seconds, hook in first 3 seconds)
5. 5 standalone quotes or takeaways I could post individually

Keep the core ideas from the original — don't add things I didn't say. Adapt the format and tone for each platform.
```

## Which formats to request

| Goal | Format to request |
|---|---|
| Grow on X/Twitter | "A 10-tweet thread, numbered, with a strong hook" |
| LinkedIn engagement | "A personal story format — insight through experience" |
| Email list | "A conversational newsletter teaser with curiosity gap" |
| SEO / blog | "A companion FAQ post answering 5 questions this raises" |
| Slides | "5 slides: title, problem, solution, evidence, call to action" |

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Which 3 ideas in my original are most underexplored? Turn each into a full new piece."*

**🧊 Mild:** *"Just give me the best tweet from this content. One tweet."*

**💰 Budget:** *"What are the 5 most quotable lines from this? I'll schedule them over the next week."*
''',
    },
    {
        "slug": "post-meeting-followup-email",
        "title": "Post-Meeting Follow-Up Email ✨",
        "category": "Communication",
        "difficulty": "beginner",
        "tags": ["email", "meetings", "productivity", "communication"],
        "teaser": "Turn rough meeting notes into a professional follow-up email that confirms decisions and assigns accountability.",
        "bestFor": "Client calls, sales meetings, project check-ins, interviews",
        "whenToUse": "Within an hour of any important meeting",
        "featured": False,
        "body": '''The follow-up email is where meetings become real. It's where decisions get confirmed, accountability gets assigned, and misunderstandings get caught before they become problems. Most people either don't send them or send generic ones. This recipe fixes that.

## The Recipe

```
Write a post-meeting follow-up email based on these notes:

Meeting: [who attended and what it was about]
Date: [today's date]
Key discussion points: [what was talked about]
Decisions made: [what was agreed]
Action items: [who does what by when]
Next meeting / next step: [if applicable]

Tone: [professional / warm-professional / formal]
Send to: [recipient — affects how formal it should be]

Format:
- Brief opening that references the meeting positively
- Summary of what was decided (bullet points)
- Clear action items with owners and deadlines
- Next step or follow-up
- Friendly but professional close
```

## Example input

```
Meeting: Discovery call with Sarah Chen, Head of Marketing at Brightfield Co
Date: Today
Discussion: They're looking for a brand identity refresh. Current brand feels dated. Budget is around £15k. Timeline: needs to be done by Q1.
Decisions: They want to see initial concepts. No decision on whether to proceed yet.
Action items: I'll send a proposal by Friday. They'll confirm budget internally by end of week.
Next step: Follow-up call in 2 weeks.

Tone: warm-professional (we got on well)
```

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Also write a separate internal note to myself about what I should research before the next meeting."*

**🧊 Mild:** *"Just write the action items section — I'll write the rest myself."*

**💰 Budget:** *"What's the minimum I need to include in a follow-up for it to be useful?"*
''',
    },
    {
        "slug": "scene-starter-fiction",
        "title": "Scene Starter for Fiction ✨",
        "category": "Creative Writing",
        "difficulty": "home-cook",
        "tags": ["creative-writing", "fiction", "storytelling", "writing"],
        "teaser": "Beat the blank page — get a compelling scene opening you can take and make your own.",
        "bestFor": "Short stories, novels, screenplays, creative writing practice",
        "whenToUse": "When you know roughly what needs to happen but can't find the first sentence",
        "featured": False,
        "body": '''The hardest part of fiction isn't the plot — it's the first sentence. Once you have something down, you can shape it. The blank page is the enemy. This recipe gives you something to react to: a scene that you can accept, modify, or strongly disagree with, but either way it breaks the paralysis.

## The Recipe

```
Write the opening of a scene with these elements:

Characters: [who's in it]
Setting: [where and when]
What needs to happen: [the purpose of the scene — what must change by the end]
Tone: [tense, quiet, absurd, melancholic — the emotional register you want]
POV: [first person / third limited / third omniscient]
Style preference: [literary / genre / lean / atmospheric — optional]

Don't resolve the scene — just open it. I'll take it from there.
```

## Example

```
Write the opening of a scene:

Characters: A woman in her 50s returning to her childhood home for the first time in 20 years. She doesn't know her estranged sister will be there.
Setting: A cluttered house in rural Ireland, late afternoon, winter.
What needs to happen: The sister needs to appear. The tension between them needs to be established without anyone saying it directly.
Tone: Loaded silence, restrained — things unsaid
POV: Third limited, following the returning woman
Style: Literary, sensory details

Don't resolve it. Stop after the moment they see each other.
```

## After getting the scene

- *"Change the pacing — slow it down / speed it up in [section]"*
- *"Rewrite this but with [character] withholding something specific"*
- *"Give me 3 alternative first lines. Different approaches."*
- *"Make this feel more like [author whose style you want to study]"*

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Write the scene twice — once from Character A's POV and once from Character B's. Same events, completely different experience."*

**🧊 Mild:** *"Give me 5 possible first sentences for this scene. I'll pick the one that feels right."*

**💰 Budget:** *"What's the one specific sensory detail that would make this scene feel most real?"*
''',
    },
    {
        "slug": "10-10-10-decision-test",
        "title": "10-10-10 Decision Test ✨",
        "category": "Decision Making",
        "difficulty": "beginner",
        "tags": ["decision-making", "perspective", "thinking", "clarity"],
        "teaser": "Test a decision across three time horizons — 10 minutes, 10 months, 10 years — to see what really matters.",
        "bestFor": "Any significant life or work decision",
        "whenToUse": "When you're torn between two options and can't get perspective",
        "featured": False,
        "body": '''The 10-10-10 framework (from Suzy Welch) cuts through short-term noise by asking how you'll feel about a decision across three very different time horizons. AI makes this much more useful by doing the analysis for you, not just prompting you to think about it.

## The Recipe

```
I'm deciding whether to [your decision].

Apply the 10-10-10 test to this specific decision. For each time horizon, give me a specific, honest analysis — not generic advice:

1. In 10 minutes: How will I feel right after making this decision? What's the immediate emotional reaction for each option?
2. In 10 months: What will the practical consequences look like? What will I wish I had or hadn't done?
3. In 10 years: What's the likely long-term trajectory? What will I regret if I don't do this? What might I regret if I do?

Then: Given this analysis, which option does the 10-10-10 test favour, and is there anything it misses about my situation?

My context: [add relevant details — your values, your situation, what's holding you back]
```

## Example

```
I'm deciding whether to leave my secure job to join an early-stage startup as employee #6.

Apply the 10-10-10 test:
1. In 10 minutes: How will I feel about each choice immediately?
2. In 10 months: What are the practical consequences?
3. In 10 years: What's the long-term picture and regret risk?

My context: I'm 31, no dependents, have 8 months emergency savings, the startup is in a space I care about, and I've been comfortable but bored for 2 years.
```

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Now add a 10-decades horizon — imagine you're 90 and looking back. What would that version of you say about this decision?"*

**🧊 Mild:** *"Skip the framework — just tell me: what's the main thing I'll regret if I don't do this?"*

**💰 Budget:** *"What's the lowest-cost way to test this decision before fully committing?"*
''',
    },
    {
        "slug": "weekly-review-reset",
        "title": "Weekly Review & Reset ✨",
        "category": "Productivity",
        "difficulty": "beginner",
        "tags": ["productivity", "reflection", "habits", "planning"],
        "teaser": "Use AI to run a structured weekly review — what worked, what didn't, and what to focus on next week.",
        "bestFor": "Anyone who wants to improve week-over-week, not just stay busy",
        "whenToUse": "Every Friday or Sunday evening",
        "featured": False,
        "body": '''The weekly review is one of the highest-leverage productivity habits — but most people skip it because it feels vague. This recipe gives you a structured way to run it with AI as your thinking partner, not just a blank journal page.

## The Recipe

```
I'm doing my weekly review. Help me think through it.

This week I worked on: [quick summary — projects, tasks, what occupied your time]
Wins this week: [what went well, even small things]
What didn't happen: [what you planned but didn't do]
What felt hard or draining: [optional — what took more energy than expected]
What I learned: [any insight, mistake, or new information]

Based on this, help me:
1. Identify the pattern — what does this week reveal about how I work?
2. Identify the one thing I should do differently next week
3. Help me set 3 focused priorities for next week (not a to-do list — big outcomes)
4. Ask me 2 questions I should be asking myself that I haven't thought to ask
```

## How to make it a habit

- Keep a simple running document where you drop notes throughout the week
- On Friday, paste those notes into this prompt
- The AI's questions (point 4) become the journaling prompts for the following week
- After 4 weeks, ask: *"Here are my last 4 weekly reviews. What pattern do you see that I'm probably not seeing?"*

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Be honest with me: based on this week, what am I probably telling myself that isn't true about my productivity?"*

**🧊 Mild:** *"Skip the analysis — just help me pick my 3 priorities for next week."*

**💰 Budget:** *"What's the one question I should ask myself every Sunday night to prepare for the week?"*
''',
    },
    {
        "slug": "reverse-brainstorm",
        "title": "Reverse Brainstorm ✨",
        "category": "Creativity",
        "difficulty": "home-cook",
        "tags": ["brainstorming", "creativity", "problem-solving", "innovation"],
        "teaser": "Generate your best ideas by first brainstorming the worst ones — reverse engineering failure often reveals the path to success.",
        "bestFor": "Creative problems, marketing ideas, product features, any brainstorm that feels stuck",
        "whenToUse": "When regular brainstorming keeps producing the same ideas",
        "featured": False,
        "body": '''When forward brainstorming gets stuck, go backwards. Instead of asking "how do we succeed at X?", ask "how would we guarantee failure at X?" The answers are often darkly funny — and when you flip them, you get genuinely non-obvious ideas.

## The Recipe

**Step 1 — The Reverse**
```
I'm trying to [your goal or challenge].

First, help me brainstorm the opposite: how would I guarantee failure at this? What are all the ways this could go terribly wrong? What would I do if I *wanted* this to fail? Be creative — the more specific the failure modes, the better.

Give me 10–15 ways to guarantee failure.
```

**Step 2 — The Flip**
```
Now flip each of those failure modes into a positive action or insight. Some of these flips will be obvious. Some will be surprisingly useful. Some won't make sense when inverted — that's fine, just note it.
```

## Example — Marketing a new course

**Step 1 — Reverse:**
```
I'm launching an online course on sourdough baking. How would I guarantee it fails? What are all the ways to make sure no one buys it and everyone who does regrets it?
```

**Step 2 — Flip:**
*"The failure: 'Price it so it feels too cheap to be credible'"*
→ *Flip: "Test a price point that signals expertise — £197 instead of £29"*

*"The failure: 'Make the title sound like every other baking course'"*
→ *Flip: "Name it specifically — 'Sourdough for people who've failed three times already'"*

## 🔁 Leftover Remixes

**🌶️ Spicy:** *"Now pick the 3 most interesting flips. For each one, give me a specific, actionable version I could test this week."*

**🧊 Mild:** *"Skip the flipping — just give me the 5 most surprising failure modes. I'll do my own flipping."*

**💰 Budget:** *"What's the one failure mode that, if I avoid it, gives me the best chance of success?"*
''',
    },
]

def write_recipe(recipe):
    slug = recipe["slug"]
    path = os.path.join(OUTPUT_DIR, f"{slug}.md")

    tags_yaml = ', '.join(f'"{t}"' for t in recipe["tags"])
    featured_str = "true" if recipe.get("featured") else "false"

    lines = [
        "---",
        f'title: "{recipe["title"]}"',
        f'category: "{recipe["category"]}"',
        f'difficulty: "{recipe["difficulty"]}"',
        f'tags: [{tags_yaml}]',
        f'teaser: "{recipe["teaser"]}"',
    ]
    if recipe.get("bestFor"):
        lines.append(f'bestFor: "{recipe["bestFor"]}"')
    if recipe.get("whenToUse"):
        lines.append(f'whenToUse: "{recipe["whenToUse"]}"')
    lines.append(f'featured: {featured_str}')
    lines.append("---")
    lines.append("")
    lines.append(recipe["body"].strip())
    lines.append("")

    content = "\n".join(lines)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  OK {slug}.md")

print(f"Writing {len(recipes)} recipes to {OUTPUT_DIR}...")
for r in recipes:
    write_recipe(r)
print(f"\nDone! {len(recipes)} recipes created.")
