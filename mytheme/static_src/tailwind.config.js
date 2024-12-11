module.exports = {
    content: [
        // Correct paths to your Django templates relative to the `tailwind.config.js` file

        // Dashboard templates
        '../../dashboard/templates/dashboard/**/*.html',

        // Issues templates
        '../../issues/templates/issues/**/*.html',

        // Tasks templates
        '../../tasks/templates/tasks/**/*.html',

        // Base templates and other theme templates
        '../templates/**/*.html',

        // Optional: Include all .html files in the project
        '../../../**/templates/**/*.html',
    ],
    theme: {
        extend: {
            colors: {
                blue: {
                    500: '#007bff',
                },
                orange: {
                    500: '#f59e0b',
                },
                black: {
                    DEFAULT: '#000',
                },
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
};
