import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { getFavorites, saveFavorites, STORAGE_KEY, type FavoriteItem } from './_favorites';

describe('Favorites utilities', () => {
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
