export function escapeHTML(str: string | undefined | null): string {
  if (!str) return '';
  return String(str).replace(/[&<>'"]/g, (tag) => {
    const chars: Record<string, string> = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    };
    return chars[tag] || tag;
  });
}
