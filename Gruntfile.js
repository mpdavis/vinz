module.exports = function(grunt) {

    var path = require('path');

    // USEFUL STUFF
    // ------------------------
    var frontendSrc = 'app/';
    var globs = {
        'frontend': {
            'js': frontendSrc + 'scripts/**/*.js',
            'css': frontendSrc + 'css/**/*.css',
            'templates': frontendSrc + '**/*.html',
            'views': frontendSrc + 'views/**/*.html'
        },
        'node': ['Gruntfile.js']
    };

    var bowerBase = 'app/bower_components/',
        buildBase = '.tmp/',
        frontendBase = 'app/',
        npmBase = 'node_modules/',
        staticBase = 'server/static/';

    var directories = {
        'bower': {
            'angular': bowerBase + 'angular/',
            'angularRoute': bowerBase + 'angular-route/',
            'angularResource': bowerBase + 'angular-resource/',
            'angularCookies': bowerBase + 'angular-cookies/',
            'angularSanitize': bowerBase + 'angular-sanitize/',
            'bootstrap': bowerBase + 'bootstrap/',
            'jquery': bowerBase + 'jquery/',
            'fontAwesome': bowerBase + 'font-awesome/',
            'chartjs': bowerBase + 'chartjs/'
        },
        'build': {
            'js': buildBase + 'js/'
        },
        'frontend': {
            'js': frontendBase + 'scripts/',
            'css': frontendBase + 'css/',
            'img': frontendBase + 'images/',
            'views': frontendBase + 'views/'
        },
        'npm': {
            'almond': npmBase + 'almond/'
        },
        'static': {
            'js': staticBase + 'js/',
            'css': staticBase + 'css/',
            'img': staticBase + 'images/',
            'fonts': staticBase + 'fonts/',
            'views': staticBase + 'views/'
        }
    };


    // GRUNT TASK CONFIGURATION
    // ------------------------
    grunt.config.init({
        'shell': {
            'options': {
                'stdout': true,
                'stderr': true
            },
            'install': {
                'command': [
                    './node_modules/bower/bin/bower install'
                ].join(' && ')
            },
            'bootstrap': {
                'command': [
                    'cd ' + directories.bower.bootstrap,
                    'npm install'
                ].join(' && ')
            }
        },

        'copy': {
            'bootstrap': {
                'files': [{
                    'expand': true,
                    'cwd': directories.bower.bootstrap + 'dist/',
                    'src': ['**'],
                    'dest': staticBase
                }]
            },
            'img': {
                'files': [{
                    'expand': true,
                    'cwd': directories.frontend.img,
                    'src': ['**'],
                    'dest': directories.static.img
                }]
            },
            'font': {
                'files': [{
                    'expand': true,
                    'cwd': directories.bower.fontAwesome + 'css/',
                    'src': ['font-awesome.min.css'],
                    'dest': directories.static.css
                }, {
                    'expand': true,
                    'cwd': directories.bower.fontAwesome + 'fonts/',
                    'src': ['**'],
                    'dest': directories.static.fonts
                }]
            },
            'app': {
                'files': [{
                    'expand': true,
                    'cwd': directories.build.js,
                    'src': ['app.js'],
                    'dest': directories.static.js
                }, {
                    'expand': true,
                    'cwd': directories.bower.jquery,
                    'src': ['jquery.js'],
                    'dest': directories.static.js
                }, {
                    'expand': true,
                    'cwd': directories.frontend.views,
                    'src': ['**'],
                    'dest': directories.static.views
                }]
            }
        },

        'jshint': {

        },

        concat: {
            css: {
                src: [
                    directories.frontend.css + 'main.css', 
                    directories.frontend.css + 'servers.css',
                    directories.frontend.css + 'animate.css',
                    directories.frontend.css + 'users.css'
                   ],
                dest: directories.static.css + 'styles.css'
            },
            js: {
                src: [
                    directories.bower.angular + 'angular.js',
                    directories.bower.angularResource + 'angular-resource.js',
                    directories.bower.angularRoute + 'angular-route.js',
                    directories.bower.angularCookies + 'angular-cookies.js',
                    directories.bower.angularSanitize + 'angular-sanitize.js',
                    directories.bower.chartjs + 'Chart.min.js',
                    directories.frontend.js + 'app.js',
                    directories.frontend.js + 'controllers/logs.js',
                    directories.frontend.js + 'controllers/servers.js',
                    directories.frontend.js + 'controllers/users.js',
                    directories.frontend.js + 'services/users.js',
                    directories.frontend.js + 'controllers/server_detail.js',
                    directories.frontend.js + 'services/logs.js',
                    directories.frontend.js + 'services/servers.js',
                    directories.frontend.js + 'controllers/public_key.js',
                    directories.frontend.js + 'services/public_key.js',
                    directories.frontend.js + 'controllers/server_groups.js',
                    directories.frontend.js + 'controllers/server_group_detail.js',
                    directories.frontend.js + 'controllers/user_groups.js',
                    directories.frontend.js + 'controllers/user_group_detail.js',
                    directories.frontend.js + 'services/user_groups.js',
                    directories.frontend.js + 'services/server_groups.js',
                    directories.frontend.js + 'controllers/dashboard.js'
                ],
                dest: directories.static.js + 'app.js'
            }
        },

        'watch': {
            'app': {
                'files': [globs.frontend.js, globs.frontend.css, globs.frontend.views],
                'tasks': ['dev-app']
            }
        },

        'clean': {
            'all': [staticBase, bowerBase, npmBase],
            'static': [staticBase]
        },

        browserSync: {
            dev: {
                bsFiles: {
                    src : [globs.frontend.js, globs.frontend.css, globs.frontend.views]
                }
            },
            options: {
                watchTask: true
            }
        }
    });


    // NPM GRUNT PLUGINS
    // ------------------------
    grunt.task.loadNpmTasks('grunt-contrib-clean');
    grunt.task.loadNpmTasks('grunt-contrib-copy');
    grunt.task.loadNpmTasks('grunt-contrib-concat');
    grunt.task.loadNpmTasks('grunt-contrib-jshint');
    grunt.task.loadNpmTasks('grunt-shell');
    grunt.task.loadNpmTasks('grunt-contrib-uglify');
    grunt.task.loadNpmTasks('grunt-contrib-watch');
    grunt.task.loadNpmTasks('grunt-browser-sync');


    // TASK ALIASES
    // ------------------------
    grunt.task.registerTask('install', [
        'shell:install'
    ]);
    grunt.task.registerTask('build-bootstrap', [
        'shell:bootstrap',
        'copy:bootstrap'
    ]);
    grunt.task.registerTask('build-frontend', [
        'copy:app',
        'copy:img',
        'copy:font',
        'copy:font',
        'concat'
    ]);
    grunt.task.registerTask('build-app', [
        'clean:static',
        'install',
        'build-bootstrap',
        'build-frontend'
    ]);
    grunt.task.registerTask('dev-app', [
        'build-frontend',
        'watch:app'
    ]);
    grunt.task.registerTask('reset', [
        'clean:all'
    ]);

    grunt.registerTask('default', ['browserSync', 'watch'])

};
