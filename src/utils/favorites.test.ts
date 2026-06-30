import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { getFavorites, saveFavorites, STORAGE_KEY, Favorites } from './favorites';

describe('favorites utility', () => {
  let localStorageMock: Record<string, string>;

  beforeEach(() => {
    localStorageMock = {};

    vi.stubGlobal('localStorage', {
      getItem: vi.fn((key: string) => localStorageMock[key] ?? null),
      setItem: vi.fn((key: string, value: string) => {
        localStorageMock[key] = value;
      }),
      removeItem: vi.fn((key: string) => {
        delete localStorageMock[key];
      }),
      clear: vi.fn(() => {
        localStorageMock = {};
      }),
    });
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  describe('getFavorites', () => {
    it('returns an empty object when localStorage is empty', () => {
      const result = getFavorites();
      expect(result).toEqual({});
      expect(localStorage.getItem).toHaveBeenCalledWith(STORAGE_KEY);
    });

    it('returns an empty object when localStorage data is corrupt/invalid JSON', () => {
      localStorageMock[STORAGE_KEY] = 'invalid-json-{';
      const result = getFavorites();
      expect(result).toEqual({});
    });

    it('returns parsed object when localStorage data is valid JSON', () => {
      const mockData: Favorites = {
        'prompt-1': { title: 'Prompt 1', category: 'Testing', url: '/prompts/prompt-1/' },
      };
      localStorageMock[STORAGE_KEY] = JSON.stringify(mockData);

      const result = getFavorites();
      expect(result).toEqual(mockData);
    });
  });

  describe('saveFavorites', () => {
    it('saves data correctly to localStorage', () => {
      const mockData: Favorites = {
        'prompt-2': { title: 'Prompt 2', category: 'Dev', url: '/prompts/prompt-2/' },
      };
      saveFavorites(mockData);
      expect(localStorage.setItem).toHaveBeenCalledWith(STORAGE_KEY, JSON.stringify(mockData));
      expect(localStorageMock[STORAGE_KEY]).toBe(JSON.stringify(mockData));
    });
  });
});
