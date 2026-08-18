import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { getFavorites, saveFavorites, escapeHTML, STORAGE_KEY, type FavoriteItem } from './_favorites';

describe('Favorites utilities', () => {
  describe('escapeHTML', () => {
    it('returns the original string if no special characters are present', () => {
      expect(escapeHTML('hello world')).toBe('hello world');
      expect(escapeHTML('12345')).toBe('12345');
      expect(escapeHTML('')).toBe('');
    });

    it('escapes special HTML characters correctly', () => {
      expect(escapeHTML('&')).toBe('&amp;');
      expect(escapeHTML('<')).toBe('&lt;');
      expect(escapeHTML('>')).toBe('&gt;');
      expect(escapeHTML("'")).toBe('&#39;');
      expect(escapeHTML('"')).toBe('&quot;');
    });

    it('handles multiple occurrences and combinations of special characters', () => {
      const input = '<script>alert("XSS & \'hacks\'")</script>';
      const expected = '&lt;script&gt;alert(&quot;XSS &amp; &#39;hacks&#39;&quot;)&lt;/script&gt;';
      expect(escapeHTML(input)).toBe(expected);
    });

    it('does not escape other characters', () => {
      expect(escapeHTML('a/b+c-d=e')).toBe('a/b+c-d=e');
    });
  });

  beforeEach(() => {
    localStorage.clear();
    vi.restoreAllMocks();
  });

  afterEach(() => {
    localStorage.clear();
  });

  describe('getFavorites', () => {
    it('returns an empty object when localStorage is empty', () => {
      expect(getFavorites()).toEqual({});
    });

    it('returns parsed favorites when valid JSON is in localStorage', () => {
      const mockFavs: Record<string, FavoriteItem> = {
        '123': { title: 'Test Recipe', category: 'Testing', url: '/test' }
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(mockFavs));
      expect(getFavorites()).toEqual(mockFavs);
    });

    it('returns an empty object and does not throw when localStorage contains invalid JSON', () => {
      localStorage.setItem(STORAGE_KEY, 'invalid json {[');
      // It should catch the error and return {}
      expect(() => getFavorites()).not.toThrow();
      expect(getFavorites()).toEqual({});
    });

    it('returns an empty object and does not throw when localStorage is unavailable (throws on access)', () => {
      // Mock getItem to throw an error, simulating a scenario like strict privacy settings
      const getItemSpy = vi.spyOn(Storage.prototype, 'getItem').mockImplementation(() => {
        throw new Error('Access denied');
      });

      expect(() => getFavorites()).not.toThrow();
      expect(getFavorites()).toEqual({});

      getItemSpy.mockRestore();
    });
  });

  describe('saveFavorites', () => {
    it('saves favorites to localStorage as JSON string', () => {
      const mockFavs: Record<string, FavoriteItem> = {
        '456': { title: 'Another Recipe', category: 'Baking', url: '/bake' }
      };
      saveFavorites(mockFavs);

      const stored = localStorage.getItem(STORAGE_KEY);
      expect(stored).toBe(JSON.stringify(mockFavs));
    });
  });
});
