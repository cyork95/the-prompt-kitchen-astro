export type Favorite = { title: string; category: string; url: string };
export type Favorites = Record<string, Favorite>;

export const STORAGE_KEY = 'pk-favorites';

export function getFavorites(): Favorites {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '{}');
  } catch {
    return {};
  }
}

export function saveFavorites(favs: Favorites): void {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(favs));
}
