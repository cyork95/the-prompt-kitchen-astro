import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import pagefind from 'astro-pagefind';

export default defineConfig({
  site: 'https://thepromptkitchen.fyi',
  integrations: [
    mdx(),
    pagefind(),
  ],
  markdown: {
    shikiConfig: {
      theme: 'github-light',
      wrap: true,
    },
  },
  vite: {
    build: {
      rollupOptions: {
        // pagefind is only available after the build; don't resolve it at bundle time
        external: ['/pagefind/pagefind-ui.js', '/pagefind/pagefind.js'],
      },
    },
  },
});
