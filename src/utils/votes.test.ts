import { describe, it, expect, beforeEach, vi } from 'vitest';
import { getMyVotes, saveMyVotes } from './votes';

describe('Votes Utils', () => {
  const recipeId = 'test-recipe';
  const VOTES_KEY = `pk-votes-${recipeId}`;

  beforeEach(() => {
    localStorage.clear();
    vi.restoreAllMocks();
  });

  describe('getMyVotes', () => {
    it('returns an empty set when no votes exist in localStorage', () => {
      expect(getMyVotes(recipeId)).toEqual(new Set());
    });

    it('returns a set with votes when valid JSON is in localStorage', () => {
      localStorage.setItem(VOTES_KEY, JSON.stringify(['fire', 'chef']));
      expect(getMyVotes(recipeId)).toEqual(new Set(['fire', 'chef']));
    });

    it('returns an empty set and does not throw when invalid JSON is in localStorage', () => {
      localStorage.setItem(VOTES_KEY, '{invalid json');
      expect(getMyVotes(recipeId)).toEqual(new Set());
    });
  });

  describe('saveMyVotes', () => {
    it('saves votes to localStorage correctly', () => {
      const votes = new Set(['fire', 'star']);
      saveMyVotes(recipeId, votes);
      expect(localStorage.getItem(VOTES_KEY)).toBe(JSON.stringify(['fire', 'star']));
    });
  });
});
