let mix = require("laravel-mix");

mix.browserSync({
	proxy: "http://react-starter.local",
	files: ["**/*.html", "dist/css/**/*.css", "dist/js/**/*.js"],
	// injectChanges: true,
	// open: false,
});

mix.js("src/js/index.js", "dist/js")
	.react()
	.sass("src/sass/style.scss", "dist/css");
