import { defineCollection, z } from 'astro:content';

// ── Recipe Book ─────────────────────────────────────────────────────────────
const recipes = defineCollection({
  type: 'content',
  schema: z.object({
    title:       z.string(),
    category:    z.string(),
    difficulty:  z.enum(['beginner', 'home-cook', 'sous-chef']).default('beginner'),
    tags:        z.array(z.string()).default([]),
    teaser:      z.string(),
    bestFor:     z.string().optional(),
    whenToUse:   z.string().optional(),
    featured:    z.boolean().default(false),
    community:   z.boolean().default(false),   // true = Grandma's Secret Recipe
    contributor: z.string().optional(),        // community submitter handle
    publishedAt: z.date().optional(),
  }),
});

// ── Cookbooks ────────────────────────────────────────────────────────────────
const cookbooks = defineCollection({
  type: 'content',
  schema: z.object({
    title:       z.string(),
    cookbook:    z.enum(['indie-hacker', 'student', 'creator', 'startup-founder', 'youtube-growth', 'indie-hacker-launch']),
    category:    z.string(),
    difficulty:  z.enum(['beginner', 'home-cook', 'sous-chef']).default('home-cook'),
    tags:        z.array(z.string()).default([]),
    teaser:      z.string().optional(),
    order:       z.number().default(0),        // display order within cookbook
  }),
});

// ── Meal Prep (System Prompts) ───────────────────────────────────────────────
const mealPrep = defineCollection({
  type: 'content',
  schema: z.object({
    title:    z.string(),
    tagline:  z.string(),
    category: z.enum(['writing', 'coding', 'learning', 'productivity', 'business']),
    bestOn:   z.array(z.string()).default([]),  // ['ChatGPT', 'Claude', ...]
    order:    z.number().default(0),
  }),
});

// ── Kitchen Guardrails ───────────────────────────────────────────────────────
const guardrails = defineCollection({
  type: 'content',
  schema: z.object({
    title:    z.string(),
    category: z.enum(['accuracy', 'trust', 'privacy', 'bias', 'safety']),
    analogy:  z.string(),                      // one-line kitchen metaphor
    order:    z.number().default(0),
  }),
});

// ── The Pantry ───────────────────────────────────────────────────────────────
const pantry = defineCollection({
  type: 'content',
  schema: z.object({
    title:    z.string(),
    shelf:    z.enum(['role', 'context', 'chain', 'format', 'tone', 'constraint']),
    whenToUse: z.string(),
    combineWith: z.array(z.string()).default([]),
    order:    z.number().default(0),
  }),
});

export const collections = { recipes, cookbooks, mealPrep, guardrails, pantry };
