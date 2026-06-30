export function getMyVotes(recipeId: string): Set<string> {
  const VOTES_KEY = `pk-votes-${recipeId}`;
  try {
    return new Set(JSON.parse(localStorage.getItem(VOTES_KEY) ?? '[]'));
  } catch {
    return new Set();
  }
}

export function saveMyVotes(recipeId: string, votes: Set<string>): void {
  const VOTES_KEY = `pk-votes-${recipeId}`;
  localStorage.setItem(VOTES_KEY, JSON.stringify([...votes]));
}
