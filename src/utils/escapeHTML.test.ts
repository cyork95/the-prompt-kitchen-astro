import { describe, it, expect } from 'vitest';
import { escapeHTML } from './escapeHTML';

describe('escapeHTML', () => {
  it('escapes standard HTML characters', () => {
    expect(escapeHTML('<div>')).toBe('&lt;div&gt;');
    expect(escapeHTML('&')).toBe('&amp;');
    expect(escapeHTML('"')).toBe('&quot;');
    expect(escapeHTML("'")).toBe('&#39;');
  });

  it('handles null and undefined', () => {
    expect(escapeHTML(null)).toBe('');
    expect(escapeHTML(undefined)).toBe('');
  });

  it('handles regular text without escaping', () => {
    expect(escapeHTML('hello world')).toBe('hello world');
  });
});
