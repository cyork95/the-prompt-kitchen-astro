export const STORAGE_KEY = 'pk-favorites';
export const SESSION_KEY = 'pk-session';

export type FavoriteItem = { title: string; category: string; url: string };
export type Favorites = Record<string, FavoriteItem>;

export function getFavorites(): Favorites {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '{}');
  } catch {
    return {};
  }
}

export function saveFavorites(favs: Favorites) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(favs));
}
