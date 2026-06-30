export const STORAGE_KEY = 'pk-favorites';

export interface FavoriteItem {
  title: string;
  category: string;
  url: string;
}

export function getFavorites(): Record<string, FavoriteItem> {
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '{}'); }
  catch { return {}; }
}

export function saveFavorites(favs: Record<string, FavoriteItem>) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(favs));
}
