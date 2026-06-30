import { describe, it, expect, beforeEach, vi, afterEach } from 'vitest';
import { getFavorites, saveFavorites, STORAGE_KEY } from './favorites';

describe('favorites utility', () => {
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

    it('returns an empty object when localStorage returns null', () => {
      vi.spyOn(Storage.prototype, 'getItem').mockReturnValue(null);
      expect(getFavorites()).toEqual({});
    });

    it('returns parsed favorites when valid JSON is in localStorage', () => {
      const mockFavs = {
        'recipe-1': { title: 'Recipe 1', category: 'Cat 1', url: '/1' },
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(mockFavs));
      expect(getFavorites()).toEqual(mockFavs);
    });

    it('returns an empty object and does not throw when localStorage contains invalid JSON', () => {
      localStorage.setItem(STORAGE_KEY, 'invalid json {[');
      expect(() => getFavorites()).not.toThrow();
      expect(getFavorites()).toEqual({});
    });

    it('returns an empty object and does not throw when localStorage access throws', () => {
      vi.spyOn(Storage.prototype, 'getItem').mockImplementation(() => {
        throw new Error('Storage access error');
      });
      expect(() => getFavorites()).not.toThrow();
      expect(getFavorites()).toEqual({});
    });
  });

  describe('saveFavorites', () => {
    it('saves favorites to localStorage as JSON string', () => {
      const mockFavs = {
        'recipe-2': { title: 'Recipe 2', category: 'Cat 2', url: '/2' },
      };
      saveFavorites(mockFavs);
      const stored = localStorage.getItem(STORAGE_KEY);
      expect(stored).toEqual(JSON.stringify(mockFavs));
    });
  });
});
