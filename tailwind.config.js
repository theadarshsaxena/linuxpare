/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}", "./templates/*.html"],
  theme: {
    fontFamily: {
      'sans': ['Inter','poppins','ui-sans-serif', 'system-ui'],
      'serif': ['ui-serif', 'Georgia'],
      'mono': ['ui-monospace', 'SFMono-Regular']
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

