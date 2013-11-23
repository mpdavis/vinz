module.exports = function(grunt) {

    var path = require('path');

    // USEFUL STUFF
    // ------------------------
    var frontendSrc = 'frontend/';
    var globs = {
        'frontend': {
            'js': frontendSrc + 'js/**/*.js',
            'less': frontendSrc + 'less/**/*.less',
            'templates': frontendSrc + '**/*.html'
        },
        'node': ['Gruntfile.js']
    };

    var bowerBase = 'bower_components/',
        buildBase = '.build/',
        frontendBase = 'frontend/',
        npmBase = 'node_modules/',
        staticBase = 'app/static/';

    var directories = {
        'bower': {
            'angular': bowerBase + 'angular/',
            'angularRoute': bowerBase + 'angular-route/',
            'bootstrap': bowerBase + 'bootstrap/',
            'jquery': bowerBase + 'jquery/',
            'lodash': bowerBase + 'lodash/',
            'restangular': bowerBase + 'restangular/',
            'text': bowerBase + 'text/'
        },
        'build': {
            'js': buildBase + 'js/'
        },
        'frontend': {
            'js': frontendBase + 'js/',
            'less': frontendBase + 'less/',
            'img': frontendBase + 'img/'
        },
        'npm': {
            'almond': npmBase + 'almond/'
        },
        'static': {
            'js': staticBase + 'js/',
            'css': staticBase + 'css/',
            'img': staticBase + 'img/'
        }
    };

    var modules = {
        'almond': directories.npm.almond + 'almond',
        'angular': directories.bower.angular + 'angular',
        'angularRoute': directories.bower.angularRoute + 'angular-route',
        'jquery': directories.bower.jquery + 'jquery',
        'lodash': directories.bower.lodash + 'dist/lodash',
        'restangular': directories.bower.restangular + 'dist/restangular',
        'text': directories.bower.text + 'text'
    };

    var appRelativeRoot = path.relative(
            path.resolve(directories.frontend.js),
            path.resolve('.')
        ) + '/';

    var appRequireConfig = {
        'paths': {
            'almond': appRelativeRoot + modules.almond,
            'angular': appRelativeRoot + modules.angular,
            'angular-route': appRelativeRoot + modules.angularRoute,
            'jquery': appRelativeRoot + modules.jquery,
            'lodash': appRelativeRoot + modules.lodash,
            'restangular': appRelativeRoot + modules.restangular,
            'text': appRelativeRoot + modules.text
        },
        'shim': {
            'angular': {
                'deps': [],
                'exports': 'angular'
            },
            'angular-route': {
                'deps': ['angular']
            },
            'jquery': {
                'deps': [],
                'exports': '$'
            },
            'lodash': {
                'deps': [],
                'exports': '_'
            },
            'restangular': {
                'deps': ['lodash']
            }
        },
        'modules': [{
            'name': 'libs',
            'create': true,
            'include': ['jquery']
        }, {
            'name': 'app',
            'include': [appRelativeRoot + modules.almond],
            'exclude': ['libs']
        }]
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
                    'npm install',
                    'grunt'
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
                }]
            }
        },

        'jshint': {

        },

        'recess': {
            'options': {
                'compile': true
            },
            'app': {
                'files': {
                    'app/static/css/app.css': directories.frontend.less + 'app.less'
                }
            }
        },

        'less': {
            'app': {
                'options': {
                    'paths': [directories.bower.bootstrap + 'less/']
                },
                'files': {
                    'app/static/css/app.css': directories.frontend.less + 'app.less'
                }
            }
        },

        'requirejs': {
            'options': {
                'cjsTranslate': true,
                'optimize': 'none',
                'logLevel': 2
            },
            'app': {
                'options': {
                    'paths': appRequireConfig.paths,
                    'shim': appRequireConfig.shim,
                    'modules': appRequireConfig.modules,
                    'baseUrl': directories.frontend.js,
                    'dir': directories.build.js
                }
            }
        },

        'watch': {
            'options': {
                'livereload': true
            },
            'app': {
                'files': [globs.frontend.js, globs.frontend.less, globs.frontend.templates],
                'tasks': ['dev-app']
            }
        },

        'clean': {
            'all': [staticBase, bowerBase, npmBase]
        }
    });


    // NPM GRUNT PLUGINS
    // ------------------------
    grunt.task.loadNpmTasks('grunt-contrib-clean');
    grunt.task.loadNpmTasks('grunt-contrib-copy');
    grunt.task.loadNpmTasks('grunt-contrib-jshint');
    grunt.task.loadNpmTasks('grunt-contrib-less');
    grunt.task.loadNpmTasks('grunt-recess');
    grunt.task.loadNpmTasks('grunt-contrib-requirejs');
    grunt.task.loadNpmTasks('grunt-shell');
    grunt.task.loadNpmTasks('grunt-contrib-uglify');
    grunt.task.loadNpmTasks('grunt-contrib-watch');


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
        'requirejs:app',
        'copy:app',
        'copy:img',
        'less:app'
    ]);
    grunt.task.registerTask('build-app', [
        'install',
        'build-bootstrap',
        'build-frontend',
    ]);
    grunt.task.registerTask('dev-app', [
        'build-frontend',
        'watch:app'
    ]);
    grunt.task.registerTask('reset', [
        'clean:all'
    ]);

    grunt.task.registerTask('default', 'dev');

};
