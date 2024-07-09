const { addDynamicIconSelectors } = require("@iconify/tailwind");

/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./src/templates/**/*.{html,js}"],
	theme: {
		extend: {
			fontFamily: {
				teko: "'Teko', sans-serif",
				heebo: "'Heebo', sans-serif",
			},
		},
	},
	plugins: [addDynamicIconSelectors()],
};
